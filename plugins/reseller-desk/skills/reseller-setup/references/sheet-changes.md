# Changes said in chat ("from now on…", "also track…")

Their spreadsheet should always match what they tell you. When they say something that changes how they work, update BOTH the app settings and the sheet, then read both back.

## What to change
| They say | Settings (the `settings` doc) | Sheet |
|---|---|---|
| "I buy at X too" / "I don't go to Y any more" | add or remove in `places` | the Bought from dropdown (Sales, bought-from column, rows 2–997) lists every place |
| "I sell on Vinted too" | `sells` | a Sold on dropdown, if the sheet has that column |
| "new expense type: storage" | add to `cats` | the Expenses category dropdown (Category column, rows 2–300) |
| "add a column for X" / "track the weight" | none | add the column header after the last used column on that tab; never inside the formula columns. The app then shows it in New item and Edit details, and the chat skills fill it when the info is given |
| "add a tab for X" | none | add the tab with the headers they want |
| "use boxes WOR 3" / "no SKUs" | `boxes` / `skuOn` | none |
| "log miles" / "I want to claim mileage" | none | the Mileage tab, added by the app (More › Miles) |

Dropdowns are "show a warning", never "reject", so old rows with other words stay valid.

## How
1. Read the settings with ArtifactData (`get` the settings doc) and keep its version.
2. Change only the keys you need in the JSON, then `update` the doc, pinned to that version (`if_version`). If it was changed meanwhile, read it again and redo the change. Never drop other keys.
3. Change the sheet only on trackers that aren't hands-off (`handsOff: true`, or a tracker that's someone else's, like "Dad's"). On those, change only the settings and say the sheet was left alone.
4. Never touch formula columns (profit, days to sell, claim), existing values, or rows already written. Adding a column or tab never moves existing ones.
5. Read the settings and the sheet back. Reply in one line with what changed.

If ArtifactData isn't available: change the sheet only and tell them to set it in the app too (More › Settings).
