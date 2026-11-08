---
name: open-app
description: Use when someone says "open reseller desk", "open reseller desk and pin it", "open the app", "set up the app", "show me my numbers", or installs this plugin and wants the Reseller Desk app. Puts the Reseller Desk app (home screen, new item, stock, sold, expenses, miles, chat) into their Claude as their own private page and opens it.
---

# Open the Reseller Desk app

The app is the screen part of this plugin: tap-to-use pages for adding items, logging sales, stock, profit, expenses and the group chat. It lives in this skill's folder as `assets/reseller-desk.html`.

## 1. Already have it? Open it
List their artifacts (Artifact tool, `action: "list"`) and look for one titled **Reseller Desk**. If there is one, open it (`action: "open"`). If they asked for it to be pinned, try to pin it (`action: "pin"`). If pinning isn't possible here, say in one line: "Tap the pin option at the top of the page to add it to your sidebar." Then stop. Never make a second copy; their settings are tied to the first one. The app updates itself when a new version comes out.

## 2. Otherwise, make their copy
1. Check Google Sheets and Google Drive are connected. If not, say in one line that the app needs both, and offer to connect them.
2. Copy `assets/reseller-desk.html` from this skill's folder into the working directory as `reseller-desk.html`. Copy the file exactly, byte for byte (with `cp`). Never retype, shorten or "tidy" it.
3. It's a complete page starting with `<!doctype html>`; publish it as it is. Read it first if your publishing rules require that.
4. Publish it with the Artifact tool:
   - `file_path`: the copied `reseller-desk.html`
   - `icon`: `store`
   - `description`: `Your reseller app: add items, log sales, see stock and profit, linked to your Google Sheet.`
   - `files`: `{"reseller-desk.html": "reseller-desk.html"}` (the same file again, at that path; the app reads it for updates)
   - `capabilities`, exactly:
```json
{"artifact":{},"db":{"rules":[{"path":"owner","read":"admin","write":"admin"}]},"downloads":{},"mcp":{"servers":[{"server":"Google Sheets","tools":["get_values","update_spreadsheet","get_spreadsheet"]},{"server":"Google Drive","tools":["create_file","share_file","search_files","download_file_content","copy_file"]}]},"sample":{"images":true},"user":{}}
```
5. Pinning, so it sits in their Claude sidebar under its own name, one tap away:
   - If they asked to pin it ("open reseller desk and pin it", "pin it to my sidebar"), pass `pin: true` on this publish.
   - Otherwise ask once with AskUserQuestion: "Pin Reseller Desk to your Claude sidebar so it's one tap away?" (Yes, pin it (Recommended) / No thanks). On yes, pin it (`action: "pin"`).

## 3. Tell them
Two lines: the app is ready and only they can see it, and the first screen walks them through linking their spreadsheet (or making one). After that, the chat skills (new listing, log sale and so on) and the app use the same sheet.

## Never
Change the app's code, publish it to someone else's artifact, or share it publicly.
