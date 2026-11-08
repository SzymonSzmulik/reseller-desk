---
name: return-or-refund
description: Use when a sold item comes back or the buyer gets a partial refund ("it was returned", "refunded £5", a return screenshot). Updates the matching row in their tracker.
---

# Return or refund

## First
Read their Reseller Desk settings the way the reseller-setup skill describes (from the app). No app or no settings yet: run reseller-setup, which opens the app to set up. Never run setup as questions in chat. Follow the settings' tracker layout, date order and SKU setting exactly.

## Find the row
SKU first, then title, on a Sold row. Not found or not sold yet: say so and stop.

## Full return
- Set status to the returned word (from settings; `Returned` by default). Leave the sold price and dates as they are so the history stays.
- If a return postage label cost them money, add it to fees.
- Ask once: relist it? If yes, add a new Listed row with the same title and cost, today's date, and a **new** SKU (never reuse the old number).

## Partial refund
Add the refund to fees (fees = old fees + refund). Status stays Sold.

## For each tracker
Same changes on each extra tracker, by SKU or title. Only touch the cells above. Read the row back.

## Reply
One line per tracker: row, what changed.
