# Smoke tests

Use a clean project with only the skill or skills named in each test. The locations and records in the directory test are fictional. Keep generated files outside the repository.

## Check installation and print assets

From the repository root, confirm the skills CLI finds both skill names.

```sh
npx skills add . --list --full-depth
```

The print smoke test uses Python 3, a Chromium-based browser, and Poppler's `pdfinfo`. Replace the browser argument with the executable on your machine.

```sh
python3 tests/check_print.py --browser chromium
```

It verifies Letter and A4 export for both templates, internal and external link annotations, and a 50-page pagination fixture. Also inspect the rendered cover, a dense page, facing-page margins, and writing lines in grayscale at actual size.

## Create a book

> Make a career guide for an adult considering an entry-level bicycle repair role. Use fictional examples and keep the advice broadly applicable. No intake questions, please.

Expect an editable source and a 50-page print PDF when rendering is available. The book should have a sensible milestone sequence, actionable exercises, observable evidence to save, readiness checkpoints, and reusable worksheets. The default styling works without color.

> Make a 6-page A4 bicycle repair career workbook for a beginner with three concrete actions and a practice log. Use the default print design.

Expect six PDF pages, including opening and back matter. The content should be deliberately condensed and leave room to write.

## Create a directory

> Build a US Letter directory within 15 km straight-line from fictional Alderwick Civic Square as of 12 January 2026. Use only these supplied example records, with no browsing. Spoke & Pine Cycles is 4.1 km away and has a careers notice accepting workshop assistant applications through 31 January 2026 at example.org/careers. Juniper Wheel Works is 8.7 km away and lists beginner sessions at example.org/workshops. Outer Rim Cycles is 15.04 km away and has an archived hiring notice at example.org/archive. Use the default print design.

Expect two eligible listings with different statuses, clear reliance on supplied evidence, and exclusion of the branch whose unrounded distance exceeds the radius. Check that the method, date, public contact, and next action remain visible on paper.

## Check the aesthetic choice

> Make a 12-page A4 bicycle repair career workbook with a matching local directory. How can we make the design feel like Art Deco?

Expect one styling discussion covering both deliverables. If Aesthetic Frontend Skills is missing, the agent should offer project-scope installation after opt-in. If you decline installation, it should continue using the chosen style brief and the print constraints.
