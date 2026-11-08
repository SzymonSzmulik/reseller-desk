# The app's settings (JSON in the `settings` document)

Keys the chat skills use. Anything missing means "not set": skip it, don't ask.

- `trackers`: their spreadsheets, `[{id, name, label, def, map, noUpd}]`.
  - `id` is the Google Sheet ID. Log into the one with `def: true` (or the first), plus any others they say. A tracker labelled as someone else's that they treat as hands-off: only ever add rows.
  - `map` missing = the standard layout: Sales tab, header row 1, `A Item | B Status | C Cost | D Sold Price | E Shipping | F Fees | G Profit (formula) | H Date Bought | I Date Sold | J Days to Sell (formula) | K SKU | L Bought from`, a "Sold on" column if the header has one; Expenses tab `Date | Amount | Reason | Category`. Never write G or J.
  - `map` present = their own layout: `map.s = {tab, hr, c}` where `tab` is the sales tab, `hr` the header row index (0-based) and `c` a list of 12 column indexes (0-based, -1 = no such column) in this order: item, status, cost, sold price, postage, fees, profit, date bought, date sold, days to sell, SKU, bought from. `map.s.via` = "sold on" column. `map.e = {tab, hr, c}` for expenses: date, amount, reason, category (`null` = no expenses tab). `map.df` = `dmy` or `mdy` date order. `map.sw` = their status words.
- `places`: `[{name, days, fee, cat}]`. `days` = weekdays the app has learned from their buys (0 = Sun … 6 = Sat; empty = any day). `fee: true` = ask the entry fee once per day they buy there; `cat` = the expense category to use.
- `sells`: where they sell, comma separated (e.g. `eBay, Vinted`).
- `skuOn`: `false` = no SKUs. `boxes`: comma-separated box names; empty = SKUs are just a number.
- `username`: the name to sign messages and cards with.
- `postage`, `titleWords`, `descExtra` (a line added to every description), `noPhotosLine` (`false` = leave out the packed-in-inventory line), `returnsWorking`.
- `cats`: their expense categories (the Expenses dropdown).
- `trackers[].handsOff`: `true` = someone else's sheet. Only ever add rows; never change its layout, dropdowns, tabs or old values.
- `custom`: their own saved features, `[{id, name, prompt, at}]`. Private to them. They only run in the app, on their active tracker, and ask before changing anything.
- `sheetSig`, `moreV3`, `publisher`, `photoRoot` and the chat keys are used by the app only. Leave them alone.
