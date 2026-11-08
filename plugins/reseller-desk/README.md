# Reseller Desk plugin

For people who buy at carboots, charity shops, Marketplace or auctions and resell on eBay, Vinted and the rest.

## What it does
- **The app** (say "open reseller desk"): your own Reseller Desk app inside Claude. Home screen with profit and stock, New item, Sold, Expenses, Messages and the group chat, all tap-to-use.
- **Send photos and a note** ("£5, bought Sunday, working"): writes the full listing and adds the item to your tracker.
- **Send a sold screenshot**: marks it Sold and offers a thank-you card or message.
- **Mention a cost**: adds it to your expenses.
- **Returns and refunds**: updates the row.
- **Miles**: "drove 12 miles to the carboot" adds it to a Mileage tab that works out the HMRC claim (55p a mile from April 2026) and adds it to your expenses.
- **Your sheet keeps up**: "from now on I buy at the market too", "add a column for weight" changes the app settings and your spreadsheet together.
- **Make your own**: in the app, More › Make your own. Describe a feature in your words; it runs on your own sheet only and shows you every change before making it.
- **Chat**: replies to messages and who's online.
- **Entry fees worked out for you**: it learns which days you go to each place from what you buy, and asks what you paid to get in once per day. It never asks how often you go.

## Works with your own spreadsheet
Say "set up reseller desk". It opens the app, and the app walks you through linking your sheet with proper buttons: it matches your columns and checks with you before writing anything. No sheet? It makes one. The chat skills then use the same settings.

## Needs
Google Drive and Google Sheets connected in Claude.

## Skills
| Skill | Use it when |
|---|---|
| open-app | Get the app, or open it |
| reseller-setup | First time: opens the app to set up |
| new-listing | Photos of something to sell |
| log-sale | Something sold |
| log-expense | You paid for something |
| return-or-refund | It came back or you refunded |
| log-miles | You drove somewhere for the business |

Made with Claude.
