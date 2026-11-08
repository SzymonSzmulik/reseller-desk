---
name: reseller-setup
description: First-time setup and settings for Reseller Desk. Use when someone says "set up reseller desk", "link my tracker", "use my spreadsheet", "change my settings", or when another Reseller Desk skill can't find their settings. Setup is done in the app, not in chat.
---

# Reseller Desk setup

**Setup happens in the app, never as questions in chat.** The app's own screens ask everything (their spreadsheet, matching its columns, where they buy and sell, SKUs, their name) with proper buttons, and check with them before changing their sheet.

## Steps
1. Run the open-app skill: open their Reseller Desk app, or make it if they don't have it yet.
2. Reply in one or two lines: "Reseller Desk is open. Its first screen walks you through linking your spreadsheet. Come back here when you're done and send photos of something to list."
3. Ask nothing else in chat. Don't search Drive, read sheets or make a tracker here; the app does all of that.

To change a setting later ("from now on I buy at the market too", "add a column for weight", "new expense type"): do it straight away from chat, in both the settings and their spreadsheet, following `references/sheet-changes.md`. In the app the same things live in More › Settings and More › Your spreadsheet.

## How the chat skills read the settings
The app saves their settings in its own database. Every other Reseller Desk skill reads them like this, before doing anything:
1. Find their Reseller Desk artifact (Artifact tool, `action: "list"`, title Reseller Desk).
2. Read the settings with the ArtifactData tool on that artifact's url: list the collection under `data/users`, then get the document `settings`. Its `settings` field is JSON. What each key means is in `references/settings.md`.
3. If there's no app, or no settings yet (they haven't finished the app's setup), run this skill instead of asking questions in chat.
4. If ArtifactData isn't available, fall back to reading their tracker's header row and matching columns by name, and ask nothing that the sheet already answers.
