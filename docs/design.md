# design.md — ShipSense Visual System

Premium, Apple-inspired glass UI. The copilot should feel like an executive decision console an Amazon Shipping BD would trust — calm, credible, decision-oriented. Not industrial logistics, not generic SaaS, not "AI dashboard."

---

## 1. Design principles
- **Clarity over decoration.** The score, the go/no-go and the pricing are the heroes.
- **Layered glass.** Translucent panels floating over a soft, bright background.
- **Restraint.** One accent colour (system blue). Colour is used to mean something (status), not to fill space.
- **Breathing room.** Generous spacing; strong hierarchy between summary → risks → pricing → proposal.

## 2. Palette

```css
/* Surfaces */
--bg:            #eef2f8;   /* mist / cloud background */
--glass:         rgba(255,255,255,0.62);
--glass-strong:  rgba(255,255,255,0.78);
--glass-border:  rgba(255,255,255,0.7);
--silver:        #dfe6ef;

/* Text */
--ink:           #1d1f24;   /* graphite, never pure black */
--ink-soft:      #5b6472;
--ink-faint:     #8a93a3;

/* Accent + status */
--blue:          #0a84ff;   /* Apple system blue — single accent */
--blue-soft:     rgba(10,132,255,0.12);
--green:         #34c759;   /* pursue / within guardrail */
--amber:         #ff9f0a;   /* clarify / VP approval / warning */
--red:           #ff3b30;   /* decline / no-go / hard gap */
```

Dark mode (optional): background `#0e1116`, glass `rgba(30,34,42,0.55)`, same blue accent, text `#eef1f6`.

## 3. Materials
- **Glass panel:** `background: var(--glass); backdrop-filter: blur(24px) saturate(140%); border: 1px solid var(--glass-border); border-radius: 20px; box-shadow: 0 10px 40px rgba(31,45,74,0.10);`
- **KPI tile:** smaller glass tile, radius 16px, large number in `--ink`, label in `--ink-soft`.
- **Status pill:** translucent tinted background (`--blue-soft` etc.), 999px radius, 12px text, medium weight.
- **Primary CTA:** solid `--blue`, white text, pill, subtle depth. Only one strong CTA per view.
- **Secondary:** glass button, `--ink` text, hairline border.

## 4. Typography
- Family: **SF Pro / Inter** (`-apple-system, "SF Pro Display", Inter, system-ui, sans-serif`).
- Scale: Display 34/40 · H1 24/30 · H2 18/24 · Body 15/22 · Caption 13/18.
- Weights: 600 for headings & numbers, 400–500 for body. Tighten letter-spacing on large numbers (`-0.01em`).

## 5. Layout & spacing
- 12-column grid, 24px gutters, max content width ~1200px.
- Spacing scale: 4 / 8 / 12 / 16 / 24 / 32 / 48.
- Left sidebar (frosted glass) · floating top bar (glass strip) · content area of stacked glass cards.
- Motion: 200–300ms ease-out on hover/reveal; panels slide + fade in; score ring animates on load. No bouncy/gimmicky motion.

## 6. Key screens (what to build)

1. **Opportunity Intake** — paste RFQ/notes or upload; large rounded input; "Analyse opportunity" primary CTA.
2. **Decision Overview** — the money screen: animated **Opportunity Score ring (0–100)**, **band pill** (Pursue/Conditions/Clarify/Decline), **Win Probability**, and a serviceable-vs-declared volume bar. KPI tiles: serviceable volume, annual revenue, recommended CM, top risk.
3. **Service-Fit Breakdown** — declared → serviceable waterfall (geo, oversized, PUDO, B2B, intl each shaved off), each as a soft chip with the % removed and why.
4. **Risk Assessment** — cards grouped operational / commercial / financial; severity as tinted pills; each with a one-line mitigation.
5. **Pricing Scenarios** — three glass columns (Aggressive / Balanced / Conservative), each with price/parcel, annual revenue, CM %, guardrail status pill (green within / amber VP / red no-go), rationale.
6. **Win Probability** — % with the top-3 drivers as horizontal bars, benchmarked against the 360-deal baseline.
7. **Client Proposal** — clean, exportable, Amazon-Shipping-branded proposal preview.
8. **Sources** — evidence list linking every figure to its document/dataset.

## 7. Data viz
- Charts embedded inside glass cards, not pasted widgets. Thin strokes, soft fills, `--blue` primary series.
- Score ring: 12px stroke, rounded caps, colour by band (green/amber/red), grey track.
- Waterfall + horizontal bars for service-fit and win drivers — muted, legible, no heavy gridlines.

## 8. Hard rules
- ❌ No black/yellow. ❌ No industrial logistics styling. ❌ No generic SaaS template. ❌ No cheap gradients or over-decoration.
- ✅ Translucent, layered, bright, refined. ✅ One restrained blue accent. ✅ Status colour used meaningfully. ✅ Jury-ready and premium.

## 9. Copy tone
Confident, plain, decision-oriented. Say "Serviceable volume," "Recommended margin," "Top risk: France outside coverage." Avoid hype. The interface should read like an experienced BD wrote it.
