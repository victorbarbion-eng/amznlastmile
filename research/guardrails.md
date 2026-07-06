# Financial Guardrails & Cost Model

From the Pricing Workbook (P&L). Every pricing recommendation must respect these.

## Contribution-margin guardrails (per deal)
| Rule | Value | Action |
|---|---|---|
| Target CM | **21%** | Aim here (Balanced scenario) |
| Minimum CM | **13%** | Floor for a normal approval |
| VP approval required | **< 13%** | Escalate; flag amber |
| Automatic No-Go | **< 9%** | Do not recommend; flag red |

## Cost model (four layers, per parcel)
Each is a rate card indexed by **daily-volume band × weight band**:
1. **First Mile** — pickup (truck).
2. **Middle Mile** — sortation & linehaul.
3. **Last Mile** — home-delivery van.
4. **Other Fixed** — corporate/support/claims, flat **$0.17/parcel** → convert at **EUR/USD 1.16** ≈ **€0.147**.

Higher daily volume → lower per-parcel cost (economies of scale). Heavier parcels → higher cost.

## Modifiers
- **Balearic Islands: ×1.35** on affected volume.
- Premium add-ons (optional, on top): **SOD €0.10**, **OTP €0.35** per parcel.

## Pricing math
```
cost_per_parcel = first + middle + last + other(€0.147)   [by vol×weight band]
cost_per_parcel × region_multiplier (Balearic 1.35)
+ add_ons (SOD/OTP if requested)
price = cost / (1 − target_CM)
CM% = (price − cost) / price
```
Blend across the weight-band and region mix to get the deal-level price and CM.
