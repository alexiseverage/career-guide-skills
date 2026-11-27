# Print and delivery

Use the requested paper size or the usual size at the intended print location. When the location or preferred size is unknown, use US Letter. Use portrait pages by default and keep a wider binding margin on the inside of facing pages. Design for true-size duplex printing with long-edge flip. Include these settings in the book and note any worksheet pages worth copying.

## Build

- Start from [the editable HTML template](../assets/workbook.html), or use a renderer that can reproduce the structure. Replace the example material. In HTML, assign stable page IDs, use one section per planned page, and update headings, page numbers, contents links, return links, and source references as the structure changes.
- Set the CSS page size and the printable content minimum height together. The template starts at US Letter with a 9.6 inch content minimum. For A4, use `size: A4` and `--page-content-height: 263mm` with the supplied vertical margins. If those margins change, leave a little tolerance below the resulting printable height.
- Use readable body type at about 11–12 pt, clear heading levels, spare decoration, and dark text on light paper. Keep source notes legible at actual size. Leave generous handwriting room and make labels, checkbox outlines, and rules visible in grayscale. Keep explanations with their examples and labels with the writing space they describe.
- Keep the editable HTML self-contained with embedded styles, local or embedded graphics if used, and no scripts needed to view or print it. Keep semantic headings, searchable text, and useful link labels. Use system or appropriately licensed fonts and embed fonts when the chosen PDF renderer supports it.

## Verify

1. Export with the requested paper size, 100% scale, and browser headers and footers turned off when printing from HTML. Keep PDF link annotations if the exporter supports them.
2. Check the actual PDF page count and size. Compare the planned and rendered page sequence and check for unexpectedly blank pages or overflow. Resolve mismatches by rebalancing or splitting content and updating the page plan. Keep body type and writing space usable.
3. Inspect the cover, contents, longest lesson, densest action page, a worksheet, and the source pages at print size. Check both sides of a facing-page spread for the gutter, test internal and source links, and check grayscale contrast. Check the PDF text layer for missing or clipped content where tooling allows.
4. Provide the verified PDF and editable source with the total PDF page count and paper size. Offer a truthful fallback when a renderer is unavailable. Include the HTML or a page-numbered manuscript with export instructions, and describe the target count as planned until it can be measured.
