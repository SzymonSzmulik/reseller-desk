---
name: new-listing
description: Use when someone sends photos of an item to sell, with a note like "£5, bought Sunday, working" or "list this". Writes the full listing (eBay, Vinted or other sites) and adds the item to their tracker as Listed, in one go.
---

# New listing

Do everything in one go. Only stop to ask for what's missing.

## First
Read their Reseller Desk settings the way the reseller-setup skill describes (from the app). No app or no settings yet: run reseller-setup, which opens the app to set up. Never run setup as questions in chat. Follow the settings' tracker layout, date order and SKU setting exactly.

## Ask only if missing (AskUserQuestion, tappable, one round)
- **Cost** (never guess). Options from their usual buy prices.
- **Date bought.** "Today", "Sunday" and so on mean the real date.
- **Working, tested, untested or faulty.** Never guess this from the photos.
- **Where from**, only if their sheet has a bought-from column and it isn't obvious. Options from their places.
- **Box**, only when SKUs use boxes. If they don't say, use the box of that type used most recently in their SKU column and say which.

## 1. Work out the item
From the photos. The exact model counts only when they said it or it's clearly readable in a photo. Otherwise give your best guess, tell them where the label usually is, and leave the model out of the title until they confirm.

## 2. Write the listing
Follow `references/listing.md`. Write for the first site in `sells` unless they name one.

## 3. SKU
If SKUs are on: pick a random 4-digit number never used before in the SKU column of any tracker in the settings (any box, sold or not). When all 4-digit numbers are used, use 5. With boxes: `<BOX> - <number>`. Without: just the number. SKUs off: leave it empty.

## 4. Add it to the tracker
For their main tracker (and any other tracker they always log into):
1. Read the sales tab and find the first empty row after the last item. Check the item isn't already there as Listed.
2. Write only: item = the listing title, status = the listed word, cost, postage 0, fees 0, date bought (in their date style), SKU, bought from. Leave sold fields and formula columns alone. If a formula column doesn't reach the new row, copy it down from the row above.
3. Copy the format of the row above onto the new row.
4. Read the row back and check the title is on the row you wrote. Fix it at once if not.
5. Then handle the place: date fix and entry fee, per the reseller-setup skill's `references/places.md`. Ask nothing about how often they go.

## 5. Optional: draft on eBay
Only if a browser tool is available and they sell on eBay: fill in Sell an item and click Save as draft. Never click List. They add the photos and price.

## Reply
The listing fields, then one line per tracker: row, title, cost, date, SKU. Keep it short.

## Never
Put buyer details anywhere. Change existing rows. Reuse a SKU number.
