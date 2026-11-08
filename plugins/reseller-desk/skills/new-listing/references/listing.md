# Listing layout

Every field the person pastes goes in its own code block, with its label on the line above, outside the block. UK spelling unless the settings say otherwise. Plain and honest, no hype.

## Status wording
- Tested working: `TESTED WORKING`, condition "Used". No spares, parts or no-returns wording.
- Faulty: `FAULTY SPARES`, condition "For parts or not working", no-returns line.
- Untested: `UNTESTED`, condition "For parts or not working", no-returns line.

## eBay
1. **Title**, max 80 characters: Brand + model + key spec + colour + extras + status in caps. Use their own title exactly if they give one.
2. **Custom label (SKU)**, if there is one.
3. **Item specifics** as a small table: Brand, Model, Type, Colour, key specs. Only facts from the photos or their note.
4. **Condition**: from the status.
5. **Condition description**, max 1000 characters, 2 to 4 sentences: status, faults, cosmetic condition, what's not included. End with: "Item packed and stored in inventory, so no further photos can be provided."
6. **Description** as HTML in a ```html block (tell them to switch eBay's description box to HTML):
   - `<p><b>` intro: what it is, key specs, colour.
   - Status as `<h2>`.
   - `<p><b>Condition:</b></p>` + `<ul>`: their faults first, in caps if serious, then cosmetic condition. Never invent faults or say it works unless they did.
   - `<p><b>What's included:</b></p>` + `<ul>`, and `<p><b>Not included:</b></p>` + `<ul>`.
   - Closing `<p>` with `<b>This item has been packed and stored in inventory, so no further photos can be provided.</b>` and "Please see the photos, as they form part of the description". No-returns line only for faulty or untested.
   - Plain HTML only.
7. **Photos**: which of the sent photos go with it.

## Vinted, Depop, Facebook
Title (short, no caps status shouting), then a plain-text description of 3 to 6 short lines: what it is, condition and faults, what's included, the packed-in-inventory line. Suggested category. No HTML.
