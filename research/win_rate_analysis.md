# Win-Rate Analysis (360 historical opportunities)

Computed from `data/historical_opportunities.csv`. These are the evidence-based factors behind the win-probability model. **Never invent — use these.**

## Baseline
- **Win rate: 53%** (191 won / 360). Lost: 169.

## Why deals are lost
| Lost reason | Count | Share of losses |
|---|---|---|
| Service gap | 50 | 30% |
| Geographic gap | 48 | 28% |
| Price | 45 | 27% |
| Lost to competitor | 25 | 15% |
| Timing / no decision | 1 | <1% |

➡️ **Service gap + Geographic gap = 58% of losses.** Coverage fit is the #1 predictor. Size serviceable volume first.

## International demand is the biggest killer
- **Requires Intl = Yes → win rate 35%** (42/119).
- **Requires Intl = No → win rate 62%** (149/241).
➡️ Any international requirement (Pink Papaya's France) is a strong negative signal.

## We win on service, not price
Win rate by main pain point:
| Pain point | Win rate |
|---|---|
| Low delivery quality | 72% |
| Poor customer service | 64% |
| Slow claims | 59% |
| Poor tracking / visibility | 56% |
| Peak collapse | 54% |
| Lack of weekend delivery | 53% |
| International expansion | 40% |
| Price / cost | 24% |

➡️ Service-driven pains win; price-driven pains lose. We run **~+8% vs incumbent** whether we win or lose — price is not our lever.

## Secondary signals
- **Geo fit:** won avg **91%** vs lost **83%**.
- **Pain severity:** won avg **2.98** vs lost **2.75** (more acute pain → more likely to switch).
- **Won margins:** 10.3%–34.0%, **mean ~21%** (matches the 21% target CM guardrail).

## Model shape (transparent)
```
win_prob = 53%
  + service_fit_adjustment      (high serviceable/geo-fit → +, gaps → −)
  + intl_penalty                (Requires Intl → strong −)
  + pain_match_adjustment       (service-pain → +, price-pain → −) × severity
  + competition_adjustment      (higher competitive intensity → −)
→ clamp 0–100, output with top-3 drivers.
```
