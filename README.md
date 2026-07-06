# ShipSense — Enterprise Opportunity Copilot for Amazon Shipping

> IE University · **Amazon Shipping Industry Challenge 2026**
> A working AI MVP that helps Amazon Shipping Enterprise Business Developers **evaluate, size, price and win** complex enterprise shipping opportunities in Spain & Portugal.

---

## The problem

Amazon Shipping is the last-mile arm of Amazon Supply Chain Services — internally seen as a candidate to become "the AWS of logistics." In Spain (>€4B last-mile market, ~1.3–1.5B parcels/yr) the Enterprise BD team must assess large, messy opportunities that arrive as **RFQs, discovery packs, CRM notes, emails and spreadsheets** — often incomplete and contradictory.

Today it's manual. BDs spend **30–40% of their time** reconciling data across Sales, Pricing, Ops and Finance before a recommendation reaches leadership. One opportunity takes days; the deal cycle runs months.

## The solution

**ShipSense ingests any opportunity and returns an explainable decision package in minutes:**

1. **Executive Summary** · 2. **Opportunity Score (0–100)** · 3. **Risk Assessment** · 4. **Pricing (3 guardrail-compliant scenarios)** · 5. **Commercial Strategy** · 6. **Follow-Up Questions** · 7. **Client-ready Proposal** · 8. **Win Probability** (benchmarked to 360 historical deals) · 9. **Sources / evidence trail**.

Rule-based scoring and pricing keep it **transparent and auditable**; an LLM layer writes the summaries, risks, strategy and client proposal. A human always reviews before "final."

## Why it wins deals (grounded in the historical data)

- **Service/geographic fit is the #1 predictor** — 58% of past losses were service or geographic gaps. ShipSense sizes the *real serviceable* volume first.
- **International demand kills deals** — win rate drops **62% → 35%** when a prospect needs international. ShipSense flags it loudly (the Pink Papaya France problem).
- **We win on service, not price** — win rate is 54–72% for service-driven pains (peak, claims, CX, quality) vs **24%** for price-driven pains. ShipSense matches the client's pain to Amazon Shipping's strengths.

## Service-fit rules (the decision core)

| | Serviceable | Not serviceable |
|---|---|---|
| Geography | Spain peninsula + Balearic | International (FR/IT/PT), Canary/Ceuta/Melilla, Madeira/Azores |
| Delivery | Home (B2C), weekend included | PUDO/lockers; B2B addresses |
| Size | ≤15 kg, ≤80×80×60 cm | Oversized |

**Guardrails:** Target CM **21%**, min **13%**, VP approval <13%, auto no-go <9%.

## The two live opportunities

- **Tecnomania (RFQ)** — electronics retailer, 2.92M parcels/yr. ShipSense strips ~16% unserviceable volume → **serviceable ≈ 2.45M/yr**, leads on peak resilience + PoD security + fast claims.
- **Pink Papaya (Discovery Pack)** — D2C fashion, ~3,800/day. ShipSense reconciles contradictory notes and **surfaces France (~18%, a hard co-founder requirement) as the #1 risk**, then wins Spain now with an honest France roadmap.

## Repository structure

```
opportunity-copilot/
├── CLAUDE.md            # session memory — read first
├── README.md            # this file
├── PLANNING.md          # milestones, sprints, jury checklist
├── TASKS.md             # executable task list
├── .gitignore
├── docs/
│   ├── PRD.md           # product requirements — source of truth
│   ├── design.md        # Apple-glass visual system
│   ├── oral-pitch.md    # 30-second pitch script
│   └── demo-script.md   # live demo walkthrough
├── prototype/
│   └── shipsense.html   # interactive MVP prototype (glass UI)
├── prompts/             # reusable Claude/Gemini prompt pack
├── data/                # pricing workbook + historical dataset (source of truth for numbers)
├── research/            # service-fit rules, win-rate analysis, sizing notes
├── decisions/           # architecture & product decision log
└── assets/              # exported screens, logos, screenshots
```

## Tool stack (as taught, Sessions 11–18)

Claude/Codex (build + security audit) → Stitch / Google AI Studio (screens from PRD + design.md) → **GitHub** (push only after audit) → **Supabase** (persistence, auth, RLS) → automation **Google Forms → Sheets → Gemini → Gmail** → **Streamlit Cloud** (deploy) → **Loom** (30s video).

## Deliverables (challenge)

1. A **working MVP** (deployed, not slides). 2. This **GitHub repo** (organised + documented). 3. A **30-second pitch video** (submission page, 2 attempts).

## Getting started with Claude

Paste into any fresh Claude/Codex session:

> Read CLAUDE.md and docs/PRD.md first. This is ShipSense — an Enterprise Opportunity Copilot for Amazon Shipping (IE Industry Challenge 2026). Continue from TASKS.md. Ground all numbers in the class data; never invent figures.

---

*Academic project. All companies, volumes, prices and outcomes in the challenge materials are fictional and anonymised (per the challenge disclaimer).*
