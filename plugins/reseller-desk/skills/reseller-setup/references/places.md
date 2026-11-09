# Places and entry fees: worked out, not asked

Never ask how often they go anywhere, or which days. The app learns each place's days from their buys and saves them in `places[].days`.

- Date fix: if they bought somewhere on a day it doesn't happen (by `days`), use the latest of its days on or before that date and say so. Places with no `days` keep the exact date.
- Entry fees: after logging a buy from a place with `fee: true`, check their expenses for a row on that date with reason `Entry fee: <place>`. If there's none, ask once for that day: "What did you pay to get in at <place> on <day date>?", with their usual past fees as options plus "Didn't pay". Write it as an expense with category `cat` (or the closest one they use). Several items from the same day: ask once.
- Template trackers with a Carboot_entry tab add carboot fees themselves: there, write the fee to that tab's Fee change date and Fee columns (I:J) if they exist, never to Expenses.
  - Ask for the price on the FIRST item they list as bought from Carboot on each date, not on later items from that same date. Check I:J for that date first; if it's already there, don't ask. Ask "What did you pay to get in on <day date>?" with Free, £2, £4 and their usual fees as options.
  - Write the date to column I and the price to column J of the first empty row. If they skip, the usual fee stays (Saturday £2, Sunday £4) and you ask again with the next Carboot item for that date.
  - Only on trackers that aren't hands-off. A hands-off tracker (like Dad's) is never written to for this.
- A place not in `places`: ask once "Do you pay to get in at <place>?" and tell them they can add it in the app (More › Settings › Buying).
