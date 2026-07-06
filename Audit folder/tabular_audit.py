#!/usr/bin/env python3
"""Lightweight tabular data audit for CSV, JSON, and simple XLSX files.

Outputs JSON with schema, missingness, duplicates, suspicious values, and basic stats.
This script intentionally avoids heavy dependencies. XLSX support uses Python's zip/xml
modules and reads raw sheet cell values from workbook XML.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import os
import re
import statistics
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from typing import Any, Dict, Iterable, List, Tuple

NULL_TOKENS = {"", "na", "n/a", "null", "none", "nan", "unknown", "-999", "999999", "?"}
DATE_PATTERNS = [
    "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y", "%m-%d-%Y",
    "%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M:%S", "%m/%d/%Y %H:%M:%S",
]


def load_csv(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample)
        except csv.Error:
            dialect = csv.excel
        return list(csv.DictReader(f, dialect=dialect))


def load_json(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        obj = json.load(f)
    if isinstance(obj, list):
        rows = obj
    elif isinstance(obj, dict):
        # Prefer the first list of dicts if present; otherwise audit the dict as one row.
        rows = next((v for v in obj.values() if isinstance(v, list) and all(isinstance(x, dict) for x in v)), [obj])
    else:
        rows = [{"value": obj}]
    return [r if isinstance(r, dict) else {"value": r} for r in rows]


def xlsx_shared_strings(z: zipfile.ZipFile) -> List[str]:
    try:
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    strings = []
    for si in root.findall("a:si", ns):
        parts = [t.text or "" for t in si.findall(".//a:t", ns)]
        strings.append("".join(parts))
    return strings


def col_index(cell_ref: str) -> int:
    letters = re.sub(r"[^A-Z]", "", cell_ref.upper())
    idx = 0
    for ch in letters:
        idx = idx * 26 + ord(ch) - ord("A") + 1
    return idx - 1


def load_xlsx(path: str) -> List[Dict[str, Any]]:
    with zipfile.ZipFile(path) as z:
        shared = xlsx_shared_strings(z)
        sheet_names = [n for n in z.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")]
        if not sheet_names:
            return []
        root = ET.fromstring(z.read(sheet_names[0]))
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    rows_raw: List[List[Any]] = []
    for row in root.findall(".//a:sheetData/a:row", ns):
        values: Dict[int, Any] = {}
        for c in row.findall("a:c", ns):
            ref = c.attrib.get("r", "A1")
            idx = col_index(ref)
            t = c.attrib.get("t")
            v = c.find("a:v", ns)
            value = "" if v is None or v.text is None else v.text
            if t == "s" and value.isdigit() and int(value) < len(shared):
                value = shared[int(value)]
            values[idx] = value
        if values:
            rows_raw.append([values.get(i, "") for i in range(max(values) + 1)])
    if not rows_raw:
        return []
    headers = [str(x).strip() or f"column_{i+1}" for i, x in enumerate(rows_raw[0])]
    return [{headers[i] if i < len(headers) else f"column_{i+1}": row[i] if i < len(row) else "" for i in range(max(len(headers), len(row)))} for row in rows_raw[1:]]


def is_null(v: Any) -> bool:
    if v is None:
        return True
    return str(v).strip().lower() in NULL_TOKENS


def to_float(v: Any) -> float | None:
    if is_null(v):
        return None
    s = str(v).strip().replace(",", "")
    if s.endswith("%"):
        s = s[:-1]
    try:
        x = float(s)
        return x if math.isfinite(x) else None
    except ValueError:
        return None


def parse_date(v: Any) -> datetime | None:
    if is_null(v):
        return None
    s = str(v).strip()
    for pat in DATE_PATTERNS:
        try:
            return datetime.strptime(s, pat)
        except ValueError:
            pass
    return None


def infer_type(values: List[Any]) -> str:
    non_null = [v for v in values if not is_null(v)]
    if not non_null:
        return "empty"
    nums = sum(to_float(v) is not None for v in non_null)
    dates = sum(parse_date(v) is not None for v in non_null)
    if nums / len(non_null) >= 0.9:
        return "numeric"
    if dates / len(non_null) >= 0.8:
        return "date"
    return "text"


def audit(rows: List[Dict[str, Any]], path: str) -> Dict[str, Any]:
    columns = sorted({k for row in rows for k in row.keys()})
    result: Dict[str, Any] = {
        "file": os.path.basename(path),
        "row_count": len(rows),
        "column_count": len(columns),
        "columns": {},
        "duplicate_rows": 0,
        "warnings": [],
    }
    row_keys = [json.dumps(row, sort_keys=True, default=str) for row in rows]
    result["duplicate_rows"] = sum(c - 1 for c in Counter(row_keys).values() if c > 1)
    if result["duplicate_rows"]:
        result["warnings"].append(f"found {result['duplicate_rows']} duplicate row(s)")
    duplicate_cols = [c for c, count in Counter([c.strip().lower() for c in columns]).items() if count > 1]
    if duplicate_cols:
        result["warnings"].append(f"possible duplicate columns by case/spacing: {duplicate_cols}")

    for col in columns:
        vals = [row.get(col) for row in rows]
        nulls = sum(is_null(v) for v in vals)
        non_null_vals = [v for v in vals if not is_null(v)]
        typ = infer_type(vals)
        info: Dict[str, Any] = {
            "inferred_type": typ,
            "missing_count": nulls,
            "missing_pct": round(nulls / len(rows), 4) if rows else 0,
            "distinct_count": len(set(map(str, non_null_vals))),
            "sample_values": list(dict.fromkeys(map(str, non_null_vals[:10])))[:5],
        }
        if typ == "numeric":
            nums = [to_float(v) for v in vals]
            nums = [x for x in nums if x is not None]
            if nums:
                info.update({"min": min(nums), "max": max(nums), "mean": statistics.fmean(nums)})
                if len(nums) >= 4:
                    mean = statistics.fmean(nums)
                    stdev = statistics.pstdev(nums)
                    if stdev:
                        outliers = sum(abs((x - mean) / stdev) > 4 for x in nums)
                        if outliers:
                            info["possible_outliers_z_gt_4"] = outliers
                if any(x < 0 for x in nums) and re.search(r"qty|quantity|sales|revenue|price|cost|amount|count|units", col, re.I):
                    info["warning"] = "negative values in a normally non-negative metric"
        if typ == "date":
            dates = [parse_date(v) for v in vals]
            dates = [d for d in dates if d is not None]
            if dates:
                info.update({"min_date": min(dates).isoformat(), "max_date": max(dates).isoformat()})
                future = sum(d.year > datetime.now().year + 1 for d in dates)
                if future:
                    info["warning"] = f"{future} date(s) far in the future"
        if nulls and len(rows) and nulls / len(rows) > 0.25:
            info["warning_high_missingness"] = True
        result["columns"][col] = info
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit tabular files for common data-quality traps.")
    parser.add_argument("path")
    parser.add_argument("--out", help="Write JSON output to this path")
    args = parser.parse_args()

    ext = os.path.splitext(args.path)[1].lower()
    try:
        if ext == ".csv":
            rows = load_csv(args.path)
        elif ext == ".json":
            rows = load_json(args.path)
        elif ext == ".xlsx":
            rows = load_xlsx(args.path)
        else:
            raise ValueError("supported extensions: .csv, .json, .xlsx")
        report = audit(rows, args.path)
    except Exception as exc:
        report = {"file": os.path.basename(args.path), "error": str(exc)}
        print(json.dumps(report, indent=2), file=sys.stderr)
        return 2

    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
