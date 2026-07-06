# CLAUDE.md — Project Memory

> Paste-and-go context file. Read this first at the start of every Claude/Codex session, then read `docs/PRD.md`. This file is the single source of truth for what we are building and why.

---

## 1. What this project is

**ShipSense** — an AI-powered **Enterprise Opportunity Copilot** for Amazon Shipping Business Developers in Spain & Portugal.

It ingests a messy enterprise opportunity (a formal RFQ, a discovery pack of CRM notes + emails, spreadsheets, call notes) and produces a structured, explainable decision package: an executive summary, a **serviceable-volume sizing**, an **opportunity score**, a **risk assessment**, **three pricing scenarios** that respect the financial guardrails, a **commercial strategy**, **follow-up questions**, a **win-probability estimate** benchmarked against 360 historical deals, a **client-ready proposal**, and a full **sources / evidence trail**.

This is the IE University **Amazon Shipping Industry Challenge 2026**. The deliverable is a **working MVP**, a **GitHub repo**, and a **30-second pitch video** — not slides.

## 2. The Amazon problem we solve

Enterprise BDs spend **30–40% of their time** gathering and reconciling information across Sales, Pricing, Operations and Finance before a recommendation can even reach leadership. A single opportunity takes days to analyse; deal cycles run months to years. ShipSense compresses the "read → size → risk → price → recommend" cycle from days to minutes, with transparency and traceability so a human can trust and defend the output.

## 3. Non-negotiable ground truths (from the class materials)

### Amazon Shipping can / cannot (service fit — this drives everything)
- ✅ Serves: **Spain peninsula + Balearic Islands** home delivery (B2C). Weekend delivery included at no extra cost.
- ❌ Does **NOT** serve: **International** (France / Italy / Portugal), **PUDO / pickup points / lockers** (home delivery only), **B2B / business addresses** (B2C only).
- ❌ Out of size/weight: parcels **>15 kg or >80×80×60 cm** are oversized/unserviceable.
- Region cost multiplier: **Balearic 1.35×**. Premium add-ons: **Signature on Delivery (SOD) €0.10**, **One-Time Password (OTP) €0.35**. FX **EUR/USD 1.16** (the "Other Fix Costs" tab is quoted in $ at $0.17/parcel → convert).

### Financial guardrails (per deal, on contribution margin)
- **Target CM 21%** · **Minimum CM 13%** · **VP approval required below 13%** · **Automatic No-Go below 9%**.
- Cost model has four layers: First Mile (pickup) + Middle Mile (sortation & linehaul) + Last Mile (home delivery van) + Other Fixed (support/claims ~$0.17). All are per-parcel rate cards **by daily-volume band × weight band**.

### What the historical data proves (360 deals — use these, do not invent)
- Overall win rate **53%**. **Service gap + Geographic gap = 58% of all losses.** Coverage fit is the #1 predictor.
- **Requires Intl = Yes → win rate drops 62% → 35%.** International demand is the biggest risk flag.
- Win rate is **high when the pain is service-driven** (Low delivery quality 72%, Poor CS 64%, Slow claims 59%, Peak collapse 54%) and **low when the pain is price** (Price/cost 24%). We win on service, not on being cheap (we run ~+8% vs incumbent whether we win or lose).
- Won deals land **10–34% margin, mean ~21%** — exactly the target guardrail.

## 4. The two live opportunities

- **Opportunity 1 — Tecnomania (RFQ):** clean electronics retailer, 2.92M parcels/yr, ES+PT. Trap: ~16% of volume is unserviceable (Canary/Ceuta/Melilla 2%, Portugal 12%+Madeira/Azores 2% intl, B2B 6% overlap, ~10% >15 kg, XL/XXL 10%). **Serviceable ≈ 2.45M/yr (ES peninsula + Balearic).** Their #1 issue is **peak collapse** (incumbent dumped 23% of parcels at PUDO in Nov 2025) → our sweet spot.
- **Opportunity 2 — Pink Papaya (Discovery Pack):** D2C fashion, ~3,800 parcels/day, fast growth. Contradictions in the notes (volume, geography). Spain ~76%, **France ~18% and treated as a "second home market" by the co-founder (hard requirement)**, Italy 5%, Portugal 1%. France is our biggest deal-breaker risk. Pains: peak, slow claims, poor CX — all our strengths. The copilot must **surface the France gap, take a position, and list the exact questions to resolve.**

## 5. The nine required outputs (the copilot MUST produce all)

1. Executive Summary · 2. Opportunity Score · 3. Risk Assessment · 4. Pricing Recommendation (3 scenarios, guardrail-compliant, with rationale + trade-offs + negotiation strategy) · 5. Commercial Strategy · 6. Required Follow-Up Actions · 7. Client Proposal / Pitch Deck · 8. Win Probability Score (benchmarked to history) · 9. Sources Used.

**The logic must generalise** — it cannot be hard-coded to these two deals. Any future opportunity (new volumes, geography, pains) must score with the same engine.

## 6. Grading rubric (100 pts) — optimise for this
Amazon Challenge Relevance **20** · MVP Functionality **20** · AI Solution Quality **20** · Business Problem Understanding **15** · Innovation **15** · Pitch Clarity **10**.

## 7. Tool stack (as taught — Sessions 11–18)
Claude/Codex (build + memory + security audit before push) → Stitch / Google AI Studio (screens from PRD + design.md) → GitHub (only push after security audit) → Supabase (persistence, auth, RLS) → automation: **Google Forms → Sheets → Gemini → Gmail** (or Zapier) → Streamlit Cloud (deploy) → Loom (30s video). Project **folder is the source of truth**, not any one tool.

## 8. Visual language
Premium Apple-inspired glass UI. Frosted translucent panels, soft whites / icy blues / silver-grey, restrained system-blue accent, rounded corners, subtle atmospheric shadows, SF Pro / Inter typography. No black/yellow, no industrial logistics look, no generic SaaS template. See `docs/design.md`.

## 9. How Claude should work each session
1. Read this file, then `docs/PRD.md`, then check `TASKS.md` for the current task.
2. When new code/design files enter the repo, scan the folder and update understanding (source-of-truth habit).
3. Ground every number in the class data (`data/` + `research/`). Never invent volumes, costs or win rates.
4. Run a **security audit** (no secrets, no keys) before proposing a GitHub push.
5. Update `TASKS.md` and `decisions/` when a decision is made.

## 10. One-line session primer (paste into a fresh Claude chat)
> Read CLAUDE.md and docs/PRD.md first. This is ShipSense — an Enterprise Opportunity Copilot for Amazon Shipping (IE Industry Challenge 2026). Continue from TASKS.md. Ground all numbers in the class data; never invent figures.
