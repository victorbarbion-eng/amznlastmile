# PRD.md — ShipSense Enterprise Opportunity Copilot

**Product:** ShipSense — AI Enterprise Opportunity Copilot for Amazon Shipping (ES/PT)
**Context:** IE University · Amazon Shipping Industry Challenge 2026
**Owner:** [Group #] · [Member full names]
**Status:** MVP for jury evaluation

---

## 1. Problem statement

Amazon Shipping is the last-mile component of Amazon Supply Chain Services (ASCS), positioned to become "the AWS of logistics." Spain is one of Southern Europe's largest e-commerce markets (~1.3–1.5B parcels/yr, >€4B last-mile market). As the Enterprise portfolio grows, BDs must evaluate large, complex, multi-stakeholder opportunities that arrive as **RFQs, discovery packs, CRM notes, emails, and spreadsheets — often incomplete and contradictory.**

Today this is manual: BDs spend **30–40% of their time** reconciling information across Sales, Pricing, Ops and Finance. A single opportunity analysis takes days; deal cycles run months to years.

**We build an AI copilot that turns any opportunity — structured or not — into an explainable, guardrail-compliant recommendation in minutes.**

## 2. Users

| User | Need |
|---|---|
| **Enterprise Business Developer** (primary) | Size the real serviceable deal, spot risks, get defensible pricing and a client-ready proposal fast. |
| **Pricing Manager** | Confirm scenarios respect CM guardrails; see cost build-up. |
| **Sales leadership** | A one-page recommendation with a score, win probability and clear go / no-go rationale. |

## 3. Scope

**In scope (MVP):** ingest a document/paste → parse → size serviceable volume → score → risk flags → 3 pricing scenarios → commercial strategy → follow-ups → win probability → client proposal → sources. Human-in-the-loop review before anything is "final."

**Out of scope (MVP):** live SP-API/Amazon Shipping API integration, real contract generation, multi-language beyond ES/EN. (Called out as roadmap, not faked as done.)

## 4. Service-fit rules (the decision core — from the Service Description)

Amazon Shipping constraints. Any declared volume that hits these is **NOT serviceable** and must be stripped before pricing:

| Rule | Serviceable | Not serviceable |
|---|---|---|
| Geography | Spain peninsula + Balearic Islands | International (FR/IT/PT), Canary Is., Ceuta, Melilla, Madeira, Azores |
| Delivery type | Home delivery (B2C) | PUDO / pickup points / lockers; B2B / business addresses |
| Size / weight | ≤ 15 kg and ≤ 80×80×60 cm | > 15 kg or > 80×80×60 cm (oversized) |
| Weekend | Included, no surcharge | — |

**Serviceable Volume = Declared × Geo-fit% × (1 − oversized%) × (1 − PUDO share) × (1 − B2B share) × (1 − intl share).** Always show the customer the *gap* between what they asked for and what we can actually serve — identifying the gap is half the task.

## 5. Scoring engine (transparent, rule-based, generalises to any deal)

**Opportunity Score (0–100)** = weighted blend, all inputs from parsed data + `data/`:

| Dimension | Weight | Signal (higher = better) |
|---|---|---|
| Service fit | 30 | Serviceable % of declared volume |
| Financial attractiveness | 20 | Serviceable annual revenue × achievable CM vs 21% target |
| Pain–strength match | 20 | Pain type maps to our strengths (peak/claims/CS/quality high; price low) × severity |
| Strategic fit | 15 | Volume scale, contract length, growth trajectory |
| Deal friction | 15 | Lower competitive intensity, fewer unresolved open questions |

Score bands → **Pursue (≥75) · Pursue with conditions (55–74) · Clarify first (40–54) · Decline (<40).** Every band comes with an **explainability string** citing the drivers.

## 6. Pricing logic (three scenarios, guardrail-compliant)

**Cost build per parcel** = First Mile + Middle Mile + Last Mile + Other Fixed, each looked up by **daily-volume band × weight band** from `data/pricing_workbook.*`. Apply **Balearic 1.35×** on affected volume. Convert Other Fixed from $0.17 at **EUR/USD 1.16**. Add optional premium add-ons (**SOD €0.10**, **OTP €0.35**) only where the client requests security/PoD (e.g. Tecnomania high-value electronics).

**Three scenarios** (all must satisfy CM ≥ 13%; flag VP approval if <13%; auto no-go if <9%):

| Scenario | Target CM | Use when | Trade-off |
|---|---|---|---|
| **Aggressive** | ~13–15% | Must-win, strategic logo, high competitive intensity | Thin margin, needs VP sign-off near floor |
| **Balanced** (recommended) | ~21% | Default; pain is service-driven so price sensitivity is lower | Best risk/reward |
| **Conservative** | ~26–30% | Weak competition, strong pain, we're clearly differentiated | Higher walk-away risk |

Each scenario outputs: price/parcel, blended annual revenue, resulting CM, rationale, and negotiation posture.

## 7. Win-probability model (benchmarked to 360 historical deals)

Baseline win rate **53%**, adjusted by evidence-based factors from the dataset:

- **Requires Intl = Yes → strong negative** (historical 35% vs 62%).
- **Low serviceable / geo-fit → negative** (won avg geo-fit 91% vs lost 83%; geographic gap = 48 losses, service gap = 50).
- **Service-driven pain → positive** (Low quality 72%, Poor CS 64%, Slow claims 59%, Peak collapse 54%); **Price-driven pain → negative** (24%).
- **Higher pain severity → positive** (won avg 2.98 vs lost 2.75).
- Output a **0–100% probability + the top 3 drivers** behind it (traceable, not a black box).

## 8. The nine required outputs (contract with the challenge brief)

1. **Executive Summary** — 5–7 line opportunity overview.
2. **Opportunity Score** — 0–100 + band + drivers.
3. **Risk Assessment** — operational / commercial / financial, each rated + mitigation.
4. **Pricing Recommendation** — 3 scenarios (§6), guardrail status shown.
5. **Commercial Strategy** — positioning + negotiation approach.
6. **Required Follow-Up Actions** — the exact open questions to send the client.
7. **Client Proposal / Pitch Deck** — client-ready, tailored, exportable.
8. **Win Probability Score** — % + top drivers (§7).
9. **Sources Used** — every document + dataset + assumption cited.

## 9. Worked expectations for the two live deals

- **Tecnomania:** size serviceable ≈ **2.45M/yr** (strip PT intl, islands, B2B, oversized); lead the proposal on **peak resilience + PoD security (SOD/OTP) + 15-day claims + weekend included**; Balanced pricing (~21% CM); win probability **medium-high** (peak-collapse pain, high geo-fit on ES). Flag: XL/XXL & >15 kg volumes we can't take.
- **Pink Papaya:** reconcile contradictions (volume 3,500–4,000 → ~3,800/day; geo 76/18/5/1). **France ~18% is a hard co-founder requirement and outside coverage → surface as the #1 risk.** Take a position: **win Spain now (peak/claims/CX are our strengths), commit an honest France roadmap, do NOT fake FR coverage.** Win probability **lowered by intl requirement** — must send the France-scope questions before committing.

## 10. Success metrics (MVP)
- Produces all 9 outputs from a single pasted opportunity. · Serviceable sizing matches hand-calc within ±3%. · All pricing scenarios respect guardrails. · Every figure is traceable to a source. · Runs end-to-end in a live demo in < 2 min.

## 11. AI stack (defensible in the rubric)
- **Ingestion/parse:** LLM extraction into a structured opportunity schema (handles RFQ + free-text notes/emails).
- **Reasoning:** rule-based scoring + pricing engine (transparent/auditable — right for a compliance-sensitive B2B decision) wrapped by an LLM that writes summaries, risks, strategy and the client proposal.
- **Retrieval:** the 360-deal dataset + Service Description as the knowledge base (RAG-style benchmarking for win probability).
- **Automation (Session 18 pattern):** Form/paste → Supabase row → Gemini generates the proposal + client email → Gmail sends → human approves.
- **Persistence:** Supabase (opportunities, scores, decisions, audit trail).
