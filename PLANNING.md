# PLANNING.md — ShipSense

Milestones, sprint plan and the jury-readiness checklist for the Amazon Shipping Industry Challenge 2026.

---

## North star
Ship a **working MVP** that ingests any opportunity and returns all **9 required outputs**, grounded in the class data, defensible in front of an Amazon evaluator. Optimise for the rubric: Relevance 20 · MVP Functionality 20 · AI Quality 20 · Problem Understanding 15 · Innovation 15 · Pitch 10.

## Milestones

| # | Milestone | Definition of done |
|---|---|---|
| M1 | **Foundations** | Class data extracted into `data/`; service-fit rules + guardrails documented in `research/`; repo scaffolded; CLAUDE.md + PRD.md final. |
| M2 | **Engines** | Serviceable-sizing, scoring, pricing (3 scenarios) and win-probability logic implemented and unit-checked against hand-calcs for both live deals. |
| M3 | **Copilot core** | LLM ingestion parses RFQ + free-text notes into the opportunity schema; generates summary, risks, strategy, follow-ups, proposal. All 9 outputs produced end-to-end. |
| M4 | **UI** | Apple-glass prototype (design.md) wired to the engines; Decision Overview, Service-Fit, Pricing, Win Probability, Proposal, Sources screens working. |
| M5 | **Persistence + automation** | Supabase stores opportunities/scores/decisions; Session-18 automation (Form/paste → Sheets/Supabase → Gemini proposal + email → Gmail). |
| M6 | **Deploy + evidence** | Deployed (Streamlit Cloud / hosted). Security audit passed, no secrets. Screenshots to Blackboard. |
| M7 | **Pitch** | 30-second Loom recorded (2 attempts). Submission form completed: value prop, Amazon problem, description, AI solution + stack, MVP link, group # + all member names. |

## Sprint plan (compressed)

**Sprint 1 — Data & rules.** Load pricing workbook + 360-deal dataset; codify service-fit and guardrails; validate Tecnomania serviceable ≈ 2.45M and win-rate factors.

**Sprint 2 — Engines.** Build sizing → scoring → pricing → win-probability as pure, testable functions that take the opportunity schema. Confirm both live deals produce sensible, guardrail-compliant output.

**Sprint 3 — Copilot + UI.** LLM parse + generation for the 9 outputs; build the glass screens from design.md; connect engines to UI; demo both deals live.

**Sprint 4 — Persist, deploy, pitch.** Supabase + automation; deploy; security audit; screenshots; record the 30s pitch; finalise submission.

## Risks & mitigations
- **Scope creep** → the 9 outputs are the contract; anything else is roadmap, not MVP.
- **Faking integrations** → never claim SP-API is live; show it as roadmap. Judges reward honesty.
- **Hard-coding the two deals** → engines take a generic schema; prove generalisation by scoring a random historical row live.
- **Numbers that don't tie out** → every figure traces to `data/`; keep a hand-calc in `research/`.

## Jury-readiness checklist
- [ ] All 9 outputs generated live from a single pasted opportunity.
- [ ] Serviceable sizing matches hand-calc (±3%).
- [ ] All 3 pricing scenarios respect guardrails (green/amber/red shown).
- [ ] Win probability shows top-3 drivers, tied to historical data.
- [ ] France gap (Pink Papaya) and unserviceable volume (Tecnomania) surfaced clearly.
- [ ] Engine generalises — demonstrated on a third/unseen opportunity.
- [ ] Deployed link works; repo is clean; no secrets committed.
- [ ] 30s pitch: problem → solution → impact, crystal clear.
- [ ] Submission: group #, all member names, MVP link.
