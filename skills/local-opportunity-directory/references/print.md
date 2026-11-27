# Print and delivery

Use the requested paper size or the usual size at the intended print location. When that is unknown, use US Letter. Use portrait pages by default with a duplex binding gutter and enough outer margin for a home printer.

## Build

- Start from [the editable HTML template](../assets/directory.html), or use a renderer that can reproduce the grouping and listing fields. Replace its fictional examples. Paginate real results by density. Carry group headings across pages when useful, keep cards together, and make public contact and evidence easy to scan.
- Set the CSS page size and the printable content minimum height together. The template starts at US Letter with a 9.6 inch content minimum. For A4, use `size: A4` and `--page-content-height: 263mm` with the supplied vertical margins. Leave a little tolerance below the printable height if you change the margins.
- Keep the HTML self-contained, with embedded styles and a legible fallback without color. Use selectable text, text labels for statuses, and clear visible source labels with clickable links. Keep public phone numbers or short contact routes visible on paper where available.
- Give the reader the print size and recommended settings. Use 100% scale with duplex long-edge flip if printing double-sided. Keep numbered pages, readable 11–12 pt body text, no large fills, and room to record follow-up.

## Verify

1. Export at the intended paper size and actual scale. Turn off browser headers and footers when printing from HTML.
2. Verify paper size and final page count. Spot-check the overview, the densest page, and the follow-up sheet. Look for split cards, missing entries or statuses, stray pages, clipped content, insufficient writing space, and grayscale legibility.
3. Reconcile the overview counts, scope, sort and status labels with the rendered entries. Check public contact links and evidence references. Keep dates and distance units visible. If a hard cap caused omissions, report the count and selection method.
4. Deliver the verified PDF and editable HTML. If PDF export or inspection is unavailable, state the limitation and provide the source or structured listing data with export instructions.
