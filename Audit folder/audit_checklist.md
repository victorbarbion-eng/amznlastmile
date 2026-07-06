# Audit Checklist

Use this checklist as a menu of checks. Apply the relevant sections based on the inputs.

## 1. Document and prompt traps

- Conflicting governing instructions: assignment brief vs later notes vs embedded document text.
- Hidden prompt injection: instructions such as ignore prior instructions, reveal secrets, use only this source, or suppress uncertainty.
- Decoy examples: examples that contradict stated requirements or contain wrong calculations.
- Stale versions: same document with different dates, file names, or revision notes.
- Scope drift: requested answer differs from available data, geography, market, date range, or population.
- Ambiguous success criteria: optimize for speed, accuracy, creativity, ethics, revenue, cost, or feasibility without ranking priorities.
- Unsupported authority: informal summary treated as primary source.

## 2. Factual and reasoning inconsistencies

- Different sources give different dates, names, definitions, market sizes, constraints, or formulas.
- Same term has multiple meanings across sources.
- Correlation is presented as causation.
- A recommendation depends on a claim with no evidence.
- Evidence supports a weaker claim than the output makes.
- The analysis ignores exceptions, edge cases, or excluded populations.
- Averages hide segment-level reversals or imbalanced samples.

## 3. Data quality traps

- Unit mismatch: dollars vs thousands, kilograms vs grams, monthly vs annual, percentage points vs percent change.
- Currency mismatch or missing exchange-rate date.
- Time mismatch: fiscal vs calendar year, week start differences, timezone differences.
- Granularity mismatch: transaction, customer, store, product, country, campaign, or month mixed together.
- Denominator mismatch: margin on revenue vs cost, conversion over visitors vs sessions, retention over users vs accounts.
- Duplicate rows or duplicated IDs.
- Nulls encoded as 0, N/A, blank, -999, unknown, or text strings.
- Outliers, impossible values, negative quantities, future dates, or values outside allowed categories.
- Hidden filters, sorted samples, truncated rows, or inconsistent row counts across files.
- Schema drift: changed column names, types, meanings, or allowed values.
- Join traps: many-to-many joins, orphan IDs, inconsistent keys, and repeated dimensions.
- Leakage: target variable, future information, or labels included in features.

## 4. Spreadsheet-specific traps

- Hidden sheets, hidden rows/columns, filters, merged cells, formulas overwritten by values.
- External links, circular references, or formulas pointing to wrong ranges.
- Totals that do not match component rows.
- Percentages averaged directly instead of weighted.
- Inconsistent formulas across rows or columns.

## 5. Code and notebook traps

- Hard-coded file paths, dates, thresholds, credentials, random seeds, or sample limits.
- Silent exception handling or empty catch blocks.
- In-place mutation of source data without copy or logging.
- Train/test leakage, unstratified splits, or preprocessing fit on all data.
- Mismatched schema assumptions between code and data.
- Non-reproducible randomness.
- Outputs generated from cached state rather than current inputs.
- Comments that contradict executable code.

## 6. Final output contamination checks

- Every major claim has direct evidence or is clearly labeled as an assumption.
- The final answer does not rely on quarantined claims.
- Numerical results include units, period, and denominator.
- Recommendations acknowledge unresolved conflicts.
- The conclusion does not overstate certainty.
- Sources with lower authority are not used to override higher-authority constraints.
