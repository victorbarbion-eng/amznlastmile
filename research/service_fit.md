# Service-Fit Rules (source of truth for serviceability)

Derived from the Service Description and the Historical Opportunities data dictionary.

## What Amazon Shipping serves
- **Geography:** Spain peninsula + **Balearic Islands** (Balearic carries a **1.35× cost multiplier**).
- **Delivery:** **home delivery only (B2C)**. Weekend delivery **included, no surcharge**.
- **Size/weight:** parcels **≤ 15 kg and ≤ 80×80×60 cm**.

## What it does NOT serve (strip before pricing)
- **International**: France, Italy, Portugal — and by extension **Canary Islands, Ceuta, Melilla, Madeira, Azores** (outside ES peninsula + Balearic).
- **PUDO / pickup points / lockers** — home delivery only.
- **B2B / business addresses** — B2C only.
- **Oversized**: > 15 kg or > 80×80×60 cm.

## Serviceable volume formula
```
Serviceable = Declared
            × Geo-fit%              (share inside ES peninsula + Balearic)
            × (1 − oversized%)      (>15kg or oversized dims)
            × (1 − PUDO share)
            × (1 − B2B share)
            × (1 − intl share)
```
Always report the **gap** between declared and serviceable — identifying it is half the challenge.

## Premium add-ons (optional, priced on top)
- **Signature on Delivery (SOD): €0.10 / parcel**
- **One-Time Password (OTP): €0.35 / parcel**
- FX: **EUR/USD = 1.16** (the "Other Fix Costs" tab is quoted in $ at $0.17/parcel → ÷1.16 ≈ €0.147).
