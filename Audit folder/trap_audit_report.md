# Trap Audit Report

## Executive Summary
- Overall risk level: High
- Main finding: The source pack is usable, but not safe for blind ingestion. The major traps are serviceability gaps, ambiguous pricing/currency handling, Tecnomania weight percentages summing to 110%, and leakage fields in the historical dataset.
- Safe-to-use inputs: Project Brief, Industry Challenge README, Service Description, one copy of the P&L workbook, Historical Opportunities, Opportunity Pink Papaya, and Opportunity Tecnomania, with caveats below.
- Inputs requiring caution: Amazon Shipping AI Copilot.pptx and Class Summary Document.epub are image-only for practical purposes; the MP4 has no embedded transcript or caption text available from local inspection; PL Industry Challenge (1).xlsx is a byte-identical duplicate of PL Industry Challenge.xlsx.

## Source Inventory
| ID | Source | Type | Authority | Notes |
|---|---|---|---|---|
| S10 | Project Brief.docx | Brief | Highest - governing assignment | Defines deliverables, submission rules, rubric, and "read first" role. |
| S05 | Industry Challenge README.docx | Challenge brief | Highest - governing task spec | Defines expected outputs and explicitly says Service Description is source of truth for capabilities. |
| S11 | Service Description.pptx | Service capability deck | High - capability source of truth | Supports Spain peninsula and Balearics, home delivery only, no Portugal/Canary/Ceuta/Melilla, no PUDO, no international, no B2B palletized, no returns. |
| S09 | PL Industry Challenge.xlsx | Pricing workbook | High - cost/guardrail source | Unique canonical copy. Contains cost tables, premium fees, FX note, and margin guardrails. |
| S08 | PL Industry Challenge (1).xlsx | Pricing workbook duplicate | Duplicate | Same SHA-256 as S09: d51947fc... Treat as duplicate, not separate evidence. |
| S04 | Historical Opportunities.xlsx | Dataset | High - benchmarking dataset | 360 rows; no duplicate opportunity IDs; outcome labels internally consistent. Beware leakage fields. |
| S07 | Opportunity Tecnomania.docx | Primary case/RFQ | High - opportunity evidence | Formal RFQ. Contains several requirements outside Amazon Shipping service capabilities. |
| S06 | Opportunity Pink Papaya.docx | Primary case/discovery pack | High - opportunity evidence | Fragmentary notes/emails by design. France, bulky items, and exact serviceable volume remain unresolved. |
| S01 | Amazon Shipping AI Copilot.pptx | Visual guide/deck | Medium - instructor/guide artifact | Image-only slides. Visual inspection confirms mission, required outputs, test cases, guardrails, deadlines. Not text-searchable. |
| S02 | Amazon Shipping Industry Challenge 2026 Hackathon Guide.mp4 | Video | Unresolved | No embedded transcript/caption text found locally. Spoken-only instructions could not be audited. |
| S03 | Class Summary Document.epub | Class summary | Low - general class context | Image-only class recap. Useful for AI workflow guidance, not case facts. Contains Blackboard link labeled UNSAFE_HTML, but no prompt injection observed. |

## Found Inconsistencies and Traps
| ID | Severity | Category | Issue | Flagged Evidence | Why It Matters | Recommended Handling |
|---|---|---|---|---|---|---|
| T01 | High | Service fit | Tecnomania requests large amounts of volume outside current Amazon Shipping coverage. | S11 slide 3: Portugal, Canary Islands, Ceuta and Melilla not supported; S07 Table 5: 2% Canary/Ceuta/Melilla, 12% Portugal mainland, 2% Madeira/Azores. | A solution that prices all 2.92M parcels as serviceable will overstate revenue and feasibility. | Treat only Spain peninsula plus Balearics as geo-serviceable before other filters: 84% of volume. Flag the remaining 16% as unsupported unless subcontracting/alternative carrier is proposed. |
| T02 | High | Service fit | Tecnomania requires services Amazon Shipping says it does not currently provide: returns, PUDO/locker fallback, B2B/palletized/business-address deliveries. | S11 slide 3 says home delivery only, no PUDO/international/B2B palletized, no client returns. S07 paragraphs 121-126 require pickup-point fallback with consent; paragraphs 137-141 require returns; paragraph 62/Table 8 show 6% B2B. | These are not minor pricing add-ons; they affect go/no-go and client-facing proposal credibility. | Explicitly mark these as gaps. Do not present full compliance. Offer phased scope, exclusions, or partner/subcontractor options. |
| T03 | High | Product limits | Tecnomania includes overweight/oversize demand, but Amazon Shipping max is 15kg and 80x80x60cm. | S11 slide 6: max weight 15kg, max dimensions 80x80x60cm. S07 Table 6 includes 15-20kg and 20-30kg bands. S07 Table 7 has XL/XXL up to 110x80x30cm. | Pricing unsupported parcels as deliverable creates a false feasible opportunity. | Exclude or quarantine over-15kg and dimension-exceeding parcels. Ask for overlap between weight and dimension bands before exact sizing. |
| T04 | High | Data quality | Tecnomania weight distribution sums to 110%, not 100%. | S07 Table 6 values: 8 + 12 + 25 + 28 + 17 + 10 + 6 + 4 = 110. | Weighted-average pricing, serviceability, and capacity calculations will be inflated or distorted. | Quarantine exact weight mix. Either ask for corrected table or normalize explicitly and label the assumption. |
| T05 | High | Pricing/currency | P&L has mixed currency/sign formatting. Fixed costs use "$0,17" while the workbook provides an EUR/USD FX rate and RFQ requires EUR pricing. | S09 Read Me: "EUR/USD FX rate -> 1,16"; S09 Other Fix Costs rows use "$0,17"; S07 paragraph 205 requires EUR excluding VAT. | A pricing engine may parse "$0,17" incorrectly or fail to convert USD to EUR, changing contribution margin. | Define a deterministic parsing rule before margin calculations. If treating fixed cost as USD 0.17, convert using the workbook FX rate. |
| T06 | High | Model leakage | Historical dataset includes post-outcome fields that must not be predictive inputs. | S04 Data Dictionary: Outcome, Lost Reason, Final Margin %. Deep scan: 191 won, 169 lost; labels internally clean. | Using Lost Reason or Final Margin to estimate win probability leaks the answer and inflates model quality. | For win probability, exclude Outcome, Lost Reason, and Final Margin from features. Use Outcome only as training label/evaluation target. |
| T07 | Medium | Pricing/service trap | Pricing workbook includes cost bands up to 30kg, but service capability stops at 15kg. | S09 cost-sheet headers include up to 30kg; S11 slide 6 max weight is 15kg. | The presence of cost bands can falsely imply Amazon can serve 15-30kg parcels. | Treat 15-30kg workbook rows as non-authoritative for service capability. Service Description overrides workbook coverage. |
| T08 | Medium | Volume inconsistency | Tecnomania annual volume is internally ambiguous. | S07 paragraph 103 says forecast based on FY2025 actuals plus 27% growth; S07 Table 3 says total forecast is 2,920,000; S07 Table 1 also says annual parcels shipped approx. 2.92M FY2025 expected. FY2025 plus 27% would be 3,708,400. | This can materially change revenue and pricing volume. | Use the explicit Table 3 forecast of 2,920,000 as the challenge input, but quarantine the "plus 27%" derivation unless clarified. |
| T09 | Medium | Peak arithmetic | Tecnomania peak statements do not align cleanly. | S07 paragraph 150 says Black Friday week is about 6% of annual volume; S07 Table 11 says Black Friday week is approx. 5.0x baseline. With 2.92M annual volume and Q1-Q3 monthly distribution, 6% annual implies about 3.66x Q1-Q3 daily baseline. | Peak capacity and cost stress tests may be overstated or understated depending which claim is used. | Present both and avoid a single precise peak daily number unless you choose and document a conservative assumption. |
| T10 | Medium | Claims metric mismatch | Amazon claims timing and Tecnomania's claims KPI use different clocks. | S11 slide 8: funds credited within approx. 7 calendar days of claim approval. S07 Table 10: claim resolution <=20 days from submission to financial resolution; paragraph 147 expects <=15 days for most claims. | "7 days" does not prove compliance if approval takes time. | State Amazon likely improves claims speed, but confirm total submission-to-resolution SLA before promising compliance. |
| T11 | High | Opportunity ambiguity | Pink Papaya France requirement is unresolved and commercially important. | S06 paragraph 88: Spain 76%, France 18%, Italy 5%, Portugal 1%. Paragraph 89 says Spain-first could work if France plan is real. Paragraph 100 says France is not "maybe later" and needs a real timeline. S11 says international/France not supported. | A Spain-only proposal may lose despite strong Spain home-delivery fit. | Do not call France optional. Recommend Spain launch only with explicit France gap, roadmap caveat, or partner path. |
| T12 | Medium | Opportunity ambiguity | Pink Papaya PUDO appears to be a workaround, not a hard requirement. | S06 paragraph 60 says pickup points were used because home delivery failed; paragraph 90 says pickup points are a workaround and "I won't die on that hill." | Over-penalizing Pink Papaya for PUDO need would understate fit. | Mark PUDO as non-required unless client reconfirms. Emphasize reliable home delivery. |
| T13 | Medium | Opportunity ambiguity | Pink Papaya bulky/home-goods volume is unquantified. | S06 paragraph 91 says heavy/awkward items exist and can be ordered with clothes; paragraph 77 asks for anything over 15kg or larger than 80x80x60cm. | Exact serviceable volume and operational risk cannot be finalized. | Price/core-score apparel flow separately. Add follow-up for SKU-level weights/dimensions and basket mixing. |
| T14 | Low | Versioning | Pink Papaya cover says last updated 11 June 2026 but includes 12-13 June emails. | S06 paragraph 14 says last updated 11 June 2026; tables 4-6 include emails dated 12 and 13 June 2026. | Could mislead chronological authority if a system relies on cover metadata. | Treat the 13 June Marta email as latest evidence despite cover date. |
| T15 | Medium | Source completeness | MP4 guide could not be audited for spoken content. | S02 extraction found no embedded strings/caption text; local mdls/strings inspection did not recover transcript. | If the video contains unique rules, they are missing from the audit. | Get a transcript or manually confirm whether it adds any requirements not in S01/S05/S10. |
| T16 | Medium | Machine-readability | S01 and S03 are image-only for the relevant content. | S01 PowerPoint slides contain one picture per slide and no selectable text. S03 EPUB contains index.html plus image0.png; the visible class recap is an image. | A RAG pipeline that extracts only text will miss guide/deadline/rubric/class guidance. | OCR or manually encode the relevant rules before using these in the copilot knowledge base. |
| T17 | Low | Duplicate source | Two P&L workbooks are exact duplicates. | S08 and S09 have identical SHA-256 d51947fc627b180eb2b419097fe7546647f9839957f024688b9d582309815f77. | Duplicate ingestion can double-weight or confuse source inventory. | Keep S09 as canonical and ignore S08. |
| T18 | Low | Metadata | Several Office files have placeholder or generator metadata. | S01 core properties show created 2006 and modified 2011 despite file download in 2026; S10 has 2013 dates; several docs list python-docx/openpyxl. | Embedded dates are not reliable for document recency. | Use visible document dates and filesystem/download times for version control. |

## Quarantined Claims
| Claim | Reason | Needed Evidence |
|---|---|---|
| Amazon Shipping can fully serve Tecnomania's requested scope. | Contradicted by service capability source of truth. | Explicit approved subcontracting/alternative arrangement or updated Service Description. |
| Tecnomania serviceable volume can be calculated exactly from provided tables. | Geo, B2B, returns, overweight, and dimension filters may overlap; weight percentages sum to 110%. | Corrected weight table and overlap between region, weight, dimension, B2B, and returns volumes. |
| Tecnomania 2027 volume should be FY2025 2.92M plus 27%. | RFQ table also states 2.92M as the 2027 forecast. | Clarification from challenge owner or consolidated Q&A. |
| Pink Papaya France is optional. | COO softens timing, but co-founder makes France timeline material. | Client confirmation of acceptable Spain-first launch and concrete France timeline requirement. |
| Pink Papaya requires PUDO/lockers. | Later email says pickup points are a workaround. | Direct client answer confirming whether PUDO should remain in scope. |
| Pink Papaya chunky home-goods volume is negligible. | Low-volume claim lacks weights, dimensions, and basket-mixing data. | SKU/order extract or warehouse estimate for >15kg and >80x80x60cm items. |
| P&L fixed cost values are EUR 0.17. | Cells show "$0,17" while the workbook gives EUR/USD FX. | Workbook owner confirmation of source currency and conversion rule. |
| Historical win probability can use Lost Reason or Final Margin as features. | These are post-outcome fields and leak the target. | Feature list that excludes post-outcome variables. |
| MP4 contains no additional rules. | No transcript/captions were recoverable locally. | Transcript or manual review notes. |

## Safe Assumptions for Solution Generation
| Assumption | Basis | Confidence |
|---|---|---|
| Service Description is the source of truth for capabilities. | S05 paragraph 81 explicitly says so. | High |
| Amazon Shipping supports home delivery in Spanish Peninsula and Balearic Islands only for this challenge. | S11 slide 3 and S01 slide 9 align. | High |
| Amazon Shipping does not currently support Portugal, Canary Islands, Ceuta/Melilla, France/Italy/international, PUDO, B2B palletized, or client returns. | S11 slide 3 and S01 slide 9 align. | High |
| Max parcel capability is 15kg and 80x80x60cm. | S11 slide 6 and S01 slide 9 align. | High |
| Weekend delivery is included at no extra charge. | S11 slide 4 and S06 email framing. | High |
| OTP costs EUR 0.35 per package and SOD costs EUR 0.10 per package. | S11 slide 5 and S09 Read Me align. | High |
| Financial guardrails are minimum contribution margin 13%, target 21%, VP approval below 13%, automatic no-go below 9%. | S09 Read Me. | High |
| Use only one P&L workbook copy. | S08 and S09 hashes identical. | High |
| Historical dataset has 360 opportunities with clean IDs and clean outcome/lost-reason/final-margin label consistency. | Deep workbook scan. | High |
| Historical serviceable volume follows an implicit formula close to total * geo_fit * (1 - oversized_pct / 2), rounded. | Deep scan max absolute difference <=1. | Medium |
| Pink Papaya latest quantified geography split is Spain 76%, France 18%, Italy 5%, Portugal 1%, but it is rough and unvalidated. | S06 paragraph 88. | Medium |
| Tecnomania geographic distribution sums to 100%, and initially serviceable geography is Spain peninsula plus Balearics = 84%. | S07 Table 5 and S11 coverage. | High |

## Post-Solution Review
| Output Claim / Decision | Supported? | Evidence | Risk / Fix |
|---|---|---|---|
| No final generated solution was supplied for review. | Not applicable | User asked for source-pack trap audit. | Run a post-solution review after the MVP/deck/recommendations are drafted. |
| Amazon Shipping AI Copilot.pptx can be used as source text. | Partly | S01 is image-only; visual review confirms guide content, but text extraction returns no slide text. | OCR/manual transcription before RAG ingestion. |
| A final solution may recommend pursuing Tecnomania without caveats. | Not supported | S07 requirements conflict with S11 capabilities. | Must include service exclusions, unserviceable volume, and go/no-go caveats. |
| A final solution may recommend pursuing Pink Papaya as a strong Spain-first fit. | Supported with caveats | S06 shows strong pain-fit in Spain, but France is material and unsupported. | Proposal must be transparent about France gap and ask for timeline/acceptance of phased approach. |
| A final solution may present exact weighted pricing for Tecnomania. | Not supported until fixed | S07 weight table sums to 110%; S09 currency ambiguity. | Normalize or seek corrected data; define FX/fixed-cost rule. |

## Final Go / No-Go
Safe with caveats. The pack can support the hackathon output if the solution explicitly quarantines unsupported scope, fixes/labels pricing assumptions, avoids historical target leakage, and surfaces unresolved client questions. It is not safe for blind RAG ingestion or fully automated pricing without preprocessing and guardrails.
