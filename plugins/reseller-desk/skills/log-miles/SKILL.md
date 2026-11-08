---
name: log-miles
description: Use when someone mentions a trip they drove for the business ("drove 12 miles to the carboot", "40 mile round trip to the auction", "log my miles") so it can be claimed back. Adds it to the Mileage tab of their tracker.
---

# Log miles

## First
Read their Reseller Desk settings the way the reseller-setup skill describes (from the app). No app or no settings yet: run reseller-setup. Never run setup as questions in chat.

## Steps
1. Get: date (today if not said; "Sunday" means the real date), from, to, reason in their words, and miles. Ask only for the miles if missing (never guess a distance). "There and back" / "round trip" = double a one-way figure, and say so.
2. Find the Mileage tab in their main tracker (`Date | From | To | Reason | Miles | Claim (£)`).
   - No Mileage tab: tell them in one line to open the app › More › Miles, which adds it (a backup is made first). Don't build it by hand in chat. On a tracker they treat as hands-off (someone else's), never add the tab.
3. Check there isn't already a row with the same date, from, to and miles. Write A to E on the first empty row, date in their date style, miles as a plain number. Never write column F (the claim is a formula) or the rate cells in H:I.
4. Read the row back and give the claim from column F.

## The rate (UK, HMRC simplified mileage)
55p a mile for the first 10,000 business miles in the tax year (6 April to 5 April) from 6 April 2026, 45p before that, 25p a mile after 10,000. The tab's formula works it out. It goes in Box 18 (car, van and travel) and is added to their expense totals.

Claiming miles means they can't also claim real fuel or car costs for that vehicle. If they log petrol as an expense and also log miles, tell them once, in one line.

## Reply
One line: date, from → to, miles, claim, row.
