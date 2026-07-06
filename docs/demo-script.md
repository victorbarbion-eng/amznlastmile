# Demo Script — ShipSense

**Total: ~4 min for jury, ~2 min for Loom.** Demo path is chosen for maximum impact: show the messy input, then the instant, grounded, honest output.

---

## Step 1 — The problem, live (20s)
Open the Pink Papaya discovery pack (the folder of CRM notes + 5 contradictory emails).
> "This is what a real opportunity looks like — no clean form, just notes and emails that disagree about volume and geography. A BD spends days on this. Watch ShipSense do it in seconds."

## Step 2 — Ingest (20s)
Paste the pack into the Intake screen → click **Analyse opportunity**.
> "It parses the RFQ or the free text into a single structured opportunity — and it flags where the sources contradict each other."

## Step 3 — Decision Overview (45s)
Point to the animated **Opportunity Score ring** and **band pill**.
> "Score 61 — Pursue with conditions. Win probability 44%."
Point to the serviceable-vs-declared bar.
> "They declared ~3,800 parcels a day, but only about 76% is serviceable — because France, 18% of their volume, is outside Amazon Shipping's coverage."

## Step 4 — Service-Fit Breakdown (40s)
Show the waterfall: declared → minus France → minus Italy → minus Portugal.
> "This is the whole game. 58% of Amazon Shipping's historical losses were service or geographic gaps. ShipSense sizes the *real* deal first, so we never over-promise."
Open the contradiction flag.
> "It even caught that the COO said 'three quarters Spain' but the co-founder treats France as a second home market — so it tells the BD exactly what to confirm."

## Step 5 — Pricing scenarios (40s)
Show the three glass columns.
> "Three scenarios, all checked against our margin guardrails: Aggressive at 14%, Balanced at 21% — recommended — and Conservative at 28%. The Aggressive one is flagged amber: below 13% would need VP approval."

## Step 6 — Win probability + why (30s)
Show the top-3 drivers.
> "44%, and it tells you why: the France requirement drags it down — internationally-dependent deals historically win 35% versus 62% — but their pain is peak collapse and slow claims, which are exactly Amazon Shipping's strengths, so those pull it back up."

## Step 7 — Client proposal + automation (30s)
Open the generated proposal; show the Session-18 automation.
> "It writes a client-ready proposal tailored to their three pains, and the automation sends it: paste → Supabase → Gemini writes the proposal and email → Gmail → a human approves. No black box — every number links to its source."

## Step 8 — Generalisation + close (20s)
Paste a random historical opportunity to prove it's not hard-coded.
> "Same engine, any deal. ShipSense turns days of manual analysis into a minute — grounded in data, always explainable. From opportunity to recommendation, in minutes."

---

## Anticipated jury questions

**"Is this really AI or just a formula?"**
> "The scoring and pricing are deliberately rule-based — transparent and auditable, which is what a compliance-sensitive B2B pricing decision requires. The AI is where it belongs: reading messy, contradictory documents into structured data, and writing the summary, risk assessment and client proposal. It's the right tool for each job."

**"Why would Amazon use this?"**
> "Amazon Shipping is scaling Enterprise BD in Spain, a €4B market, and BDs lose 30–40% of their time to manual reconciliation. This compresses that to minutes and makes decisions consistent — while keeping a human in the loop."

**"What's the riskiest assumption, and how did you test it?"**
> "That the copilot sizes serviceable volume correctly. We validated it against hand-calculations for both live deals — Tecnomania comes out at ~2.45M/yr, within a few percent of the manual figure."

**"How do you handle the contradictions in the data?"**
> "We don't hide them. ShipSense surfaces every inconsistency, takes a reasoned position, and lists the exact questions the BD must send the client before committing — which is what a good BD actually does."

**"Does it generalise beyond these two cases?"**
> "Yes — the engine takes a generic opportunity schema. We just proved it on a random historical row live."
