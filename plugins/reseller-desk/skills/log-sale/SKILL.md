---
name: log-sale
description: Use when someone sends an order or sold screenshot (eBay, Vinted, Depop, Facebook), or says "this sold", "log a sale". Marks the item Sold in their tracker and offers a thank-you card or message.
---

# Log a sale

## First
Read their Reseller Desk settings the way the reseller-setup skill describes (from the app). No app or no settings yet: run reseller-setup, which opens the app to set up. Never run setup as questions in chat. Follow the settings' tracker layout, date order and SKU setting exactly.

## Read the screenshot
Item title, SKU / custom label, sold date, item price, and only the costs the seller pays (selling fees, ad fees, a postage label they bought). Never count what the buyer paid on top (buyer protection, postage the buyer paid, VAT). Anything not shown stays blank. Never guess a figure. Work out which site it sold on from the screenshot.

## For the main tracker and each extra tracker
1. Read the sales tab.
2. Find the row: SKU first, then the title on a Listed row (ignore case and small differences). Several matches: the oldest unsold one, and say which row. Already Sold: say so, change nothing. No match: say so and offer to add a new row.
3. Write only: status = sold word, sold price, date sold (their date style), fees and postage if the seller paid any, sold on (if that column exists), SKU only if blank.
4. Their own columns (any other heading they added, e.g. "Buyer postcode area" or "Courier"): fill one only when the screenshot or their message clearly gives it, and never with buyer names or addresses. Never write formula columns. Read the row back; check profit and days to sell work and the date shows as a date.

## Thank-you card or message
Then offer, as one tappable question: a printable thank-you card (Google Doc), a message to the buyer, or neither.
- **Card**: a Google Doc with a short warm note, the item name, the order date and their signature. The buyer's first name may go on the card, never in the sheet.
- **Message**: "Hi <name>," when they give the buyer's first name, otherwise just "Hi,". Never leave a placeholder like {buyer} in the text.

## Never
Put the buyer's name, address, email or phone in any sheet. Change cost, date bought or bought from.

## Reply
One line per tracker: row, sold price, date, fees, and anything left blank.
