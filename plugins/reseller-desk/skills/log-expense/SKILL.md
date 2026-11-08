---
name: log-expense
description: Use when someone mentions a business cost ("bought tape £3.50", "petrol £20", a receipt photo) or an entry fee for a carboot or market. Adds it to the expenses tab of their tracker.
---

# Log an expense

## First
Read their Reseller Desk settings the way the reseller-setup skill describes (from the app). No app or no settings yet: run reseller-setup, which opens the app to set up. Never run setup as questions in chat. Follow the settings' tracker layout, date order and SKU setting exactly.

## Steps
1. Date (today if not said), the amount paid (ask if missing, never guess), and a short reason in their words.
2. Category: reuse the wording already in their expenses tab for the same kind of thing. If the tab is empty, use: tape/labels/bubble wrap → `Postage & packaging`; boxes, storage, office → `Phone, stationery & office costs`; fuel and travel → `Car, van & travel`; entry fees → `Entry fees`.
3. Miles driven ("12 miles to the carboot") are not an expense row: use the log-miles skill.
4. Several items on one receipt: one row each.
5. Check there isn't already a row with the same date, amount and reason. Then write to the first empty row, in their date style, amount as a plain number. Read it back.
6. Do it for each extra tracker too, unless they say "mine only".

## Entry fees
Never ask how often they go anywhere. Entry fees are picked up when they log buys (see reseller-setup `references/places.md`). If they mention one directly, add it as `Entry fee: <place>` on that date, unless their tracker has a Carboot_entry tab that adds carboot fees itself (see reseller-setup `references/places.md`).

## Reply
One line: date, amount, reason, category, row.
