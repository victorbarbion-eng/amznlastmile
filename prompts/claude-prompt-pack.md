# Claude / Gemini Prompt Pack — ShipSense

Copy-paste prompts for building and running the copilot. All assume `CLAUDE.md` + `docs/PRD.md` are in context.

---

## 0. Session primer (start every chat)
> Read CLAUDE.md and docs/PRD.md first. This is ShipSense — an Enterprise Opportunity Copilot for Amazon Shipping (IE Industry Challenge 2026). Continue from TASKS.md. Ground all numbers in the class data; never invent figures.

## 1. Parse an opportunity (ingestion)
> You are an Amazon Shipping opportunity analyst. Read the opportunity below (it may be a formal RFQ or messy CRM notes + emails). Extract into JSON with fields: company, industry, declared_daily_volume, declared_annual_volume, geo_split (region→%), weight_bands, oversized_share, requires_intl, intl_share, requires_pudo, requires_b2b, weekend_need, main_pain_points[], pain_severity, competitive_intensity, contract_length, growth_rate, notes. Where sources contradict, add a `contradictions[]` list with the conflicting values and their source. Do not guess missing values — mark them `null` and add to `open_questions[]`.
> Opportunity: """{PASTE}"""

## 2. Size serviceable volume
> Using research/service_fit.md, compute serviceable volume from the parsed opportunity. Strip international, Canary/Ceuta/Melilla/Madeira/Azores, PUDO, B2B, and oversized (>15kg or >80×80×60cm). Show the waterfall (each deduction + reason) and the final serviceable annual + daily volume. State the declared→serviceable gap in % and parcels.

## 3. Score the opportunity
> Apply the PRD §5 scoring engine (service fit 30, financial 20, pain-match 20, strategic 15, friction 15). Return the 0–100 score, the band, a one-line explainability per dimension, and the overall band rationale.

## 4. Price it (3 scenarios)
> Using data/pricing_workbook and research/guardrails.md, build cost per parcel (First+Middle+Last+Other, by volume band × weight band; Balearic ×1.35; convert Other from $0.17 at EUR/USD 1.16; add SOD/OTP only if the client needs PoD/security). Produce Aggressive (~14% CM), Balanced (~21%), Conservative (~28%) scenarios: price/parcel, blended annual revenue, resulting CM, guardrail status (green ≥13 / amber VP <13 / red no-go <9), rationale, negotiation posture.

## 5. Win probability
> Using research/win_rate_analysis.md, estimate win probability from a 53% baseline, adjusting for service/geo fit, international requirement, pain-type match × severity, and competitive intensity. Output a % and the top-3 drivers with direction and magnitude.

## 6. Risks + strategy + follow-ups
> Produce (a) a risk assessment grouped operational/commercial/financial, each rated with a one-line mitigation; (b) a commercial strategy (positioning + negotiation approach) that leads with the client's service-driven pains; (c) the exact follow-up questions to send the client to resolve every open question and contradiction.

## 7. Client proposal
> Write a client-ready proposal for {COMPANY}, tailored to their top pains. Sections: executive value proposition, serviceable coverage (honest about gaps), how we fix each pain (peak resilience, fast claims, weekend included, PoD security), recommended pricing approach, implementation plan, why Amazon Shipping. Executive tone, no hype.

## 8. Security audit (before GitHub push)
> Scan the whole project folder. List any secrets, API keys, tokens or credentials in tracked files. Confirm .gitignore covers .env and keys. Do not approve a push until clean.

## 9. Prove generalisation (jury)
> Take this random historical opportunity row and run the full pipeline (parse→size→score→price→win-prob) to show the engine is not hard-coded to Tecnomania or Pink Papaya.
> Row: """{PASTE ROW}"""
