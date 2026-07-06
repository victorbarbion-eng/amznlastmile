# Decision 0001 — Product is an Enterprise Opportunity Copilot (not a partner-approval tool)

**Date:** 2026-07-06
**Status:** Accepted

## Context
An earlier draft framed the product as "RouteIQ," a last-mile *partner/operator approval* system (approving delivery companies to join Amazon's service). After reading the actual challenge materials (Project_Brief, README_Industry_Challenge, the P&L workbook, the 360-deal dataset, and the two opportunities), that framing was wrong.

## The real challenge
Build an **AI-powered Enterprise Opportunity Copilot** that helps Amazon Shipping **Business Developers** evaluate, size, price and win **enterprise shipping opportunities** (RFQs, discovery packs). The subject being scored is the **commercial opportunity/customer**, not a delivery contractor. Required outputs are fixed by the brief (9 of them). Deliverables: working MVP, GitHub repo, 30s pitch video. Rubric is 100 points.

## Decision
Rebuild everything around the Opportunity Copilot: rename to **ShipSense**, ground all logic in the Service Description (service-fit), the P&L (pricing + guardrails) and the historical dataset (win probability). Keep the taught tool stack (Claude/Codex, Stitch/AI Studio, GitHub+audit, Supabase, Session-18 automation, Streamlit, Loom) and the Apple-glass visual language.

## Consequences
- All Markdown files (CLAUDE, PRD, README, design, PLANNING, TASKS, pitch, demo) rewritten to the real brief.
- Numbers are now grounded: 53% baseline win rate, intl 62%→35%, service-gap = 58% of losses, Tecnomania serviceable ≈ 2.45M/yr, guardrails 21/13/9%.
- The prototype must present the 9 outputs, not an approval queue.
