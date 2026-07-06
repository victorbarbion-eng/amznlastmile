# TASKS.md — ShipSense

Executable task list. Work top to bottom. Mark `[x]` when done and note the decision in `decisions/` if it changes the product.

---

## Phase 1 — Data & rules (M1)
- [ ] Import pricing workbook (First/Middle/Last/Other cost tabs) into `data/` as clean CSVs (rate card by volume band × weight band).
- [ ] Import the 360-deal historical dataset into `data/`.
- [ ] Write `research/service_fit.md` — the ES-only, home-delivery-only, B2C-only, ≤15 kg rules.
- [ ] Write `research/guardrails.md` — CM 21% target / 13% min / VP <13% / no-go <9%; Balearic 1.35×; SOD €0.10; OTP €0.35; EUR/USD 1.16.
- [ ] Write `research/win_rate_analysis.md` — the historical patterns (intl 62%→35%, pain-type win rates, geo-fit, margins).

## Phase 2 — Engines (M2)
- [ ] `sizing`: Declared → Serviceable (geo, oversized, PUDO, B2B, intl). Validate Tecnomania ≈ 2.45M/yr.
- [ ] `scoring`: 0–100 across the 5 dimensions (PRD §5) with explainability strings.
- [ ] `pricing`: cost build per parcel (4 layers, volume×weight lookup, Balearic 1.35×, $→€ at 1.16) → 3 scenarios with CM + guardrail status.
- [ ] `win_probability`: baseline 53% adjusted by evidence factors; output % + top-3 drivers.
- [ ] Unit-check all four on Tecnomania and Pink Papaya; hand-calc in `research/`.

## Phase 3 — Copilot + UI (M3, M4)
- [ ] LLM ingestion: parse RFQ + free-text notes/emails into the opportunity schema (handle contradictions → flag them).
- [ ] Generate the 9 outputs (summary, score, risks, pricing, strategy, follow-ups, proposal, win prob, sources).
- [ ] Build glass screens from `docs/design.md`: Intake · Decision Overview · Service-Fit · Risk · Pricing · Win Probability · Proposal · Sources.
- [ ] Wire engines → UI; run both live deals end-to-end.
- [ ] Prove generalisation: score a random historical row live.

## Phase 4 — Persist, automate, deploy (M5, M6)
- [ ] Supabase: tables for opportunities, scores, pricing, decisions, audit trail; RLS on.
- [ ] Automation (Session 18): Form/paste → Supabase/Sheets → Gemini writes proposal + client email → Gmail sends → human approves.
- [ ] Deploy (Streamlit Cloud / hosted); confirm the link works.
- [ ] Security audit (Codex): no secrets/keys committed before push.
- [ ] Screenshots → Blackboard.

## Phase 5 — Pitch & submission (M7)
- [ ] Write/refine the 30s script (`docs/oral-pitch.md`); rehearse.
- [ ] Record Loom (max 2 attempts).
- [ ] Complete submission: value prop, Amazon problem, description, AI solution + stack, MVP link, **group # + all member full names**. One submission per team.

## Backlog / roadmap (say "roadmap," don't fake)
- [ ] Live SP-API / Amazon Shipping API integration.
- [ ] Multi-language proposal generation.
- [ ] CRM sync (auto-pull discovery packs).
