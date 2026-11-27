"""Export the starter assets and check the resulting PDF geometry and links."""

import argparse
from pathlib import Path
import re
import shutil
import subprocess
from tempfile import TemporaryDirectory
import time


ROOT = Path(__file__).resolve().parents[1]
ASSETS = (
    ("career-guide-book", "workbook.html", 6, "p2"),
    ("local-opportunity-directory", "directory.html", 2, "follow-up"),
)
SIZES = (
    ("Letter", 612, 792),
    ("A4", 595.28, 841.89),
)


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def output(*command):
    return subprocess.check_output(command, text=True)


def export(browser, folder, name, html):
    source = folder / f"{name}.html"
    pdf = folder / f"{name}.pdf"
    source.write_text(html, encoding="utf-8")
    command = [
        browser,
        "--headless",
        "--disable-gpu",
        "--disable-background-networking",
        "--disable-component-update",
        "--no-first-run",
        "--no-default-browser-check",
        "--no-pdf-header-footer",
        f"--user-data-dir={folder / f'{name}-profile'}",
        f"--print-to-pdf={pdf}",
        source.as_uri(),
    ]
    log_file = folder / f"{name}.log"
    with log_file.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic() + 30
            while not pdf_is_complete(pdf):
                if process.poll() is not None or time.monotonic() >= deadline:
                    detail = log_file.read_text(encoding="utf-8", errors="replace")
                    raise RuntimeError(f"{name}: browser did not finish exporting a PDF.\n{detail}")
                time.sleep(0.2)
        finally:
            # Some Chromium builds leave the dedicated headless process running after export.
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
    return pdf


def pdf_is_complete(pdf):
    if not pdf.is_file() or pdf.stat().st_size < 12:
        return False
    with pdf.open("rb") as stream:
        stream.seek(-12, 2)
        return stream.read().rstrip().endswith(b"%%EOF")


def check_geometry(pdf, count, width, height):
    info = output("pdfinfo", "-f", "1", "-l", str(count), str(pdf))
    pages = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    check(pages and int(pages.group(1)) == count, f"{pdf.name}: expected {count} pages")
    sizes = re.findall(r"^Page\s+\d+ size:\s+([\d.]+) x ([\d.]+) pts", info, re.MULTILINE)
    check(len(sizes) == count, f"{pdf.name}: missing page dimensions")
    for page, (actual_width, actual_height) in enumerate(sizes, 1):
        matches = abs(float(actual_width) - width) < 1 and abs(float(actual_height) - height) < 1
        check(matches, f"{pdf.name}: incorrect paper size on page {page}")


def fixture_book(template):
    before, remainder = template.split("  <main>", 1)
    _, after = remainder.split("  </main>", 1)
    pages = [
        f'<section class="page" id="fixture-{page}"><div><h2>Page {page}</h2>'
        '<p>Fictional workbook pagination fixture.</p></div>'
        f'<footer><span>Print smoke test</span><span>{page} / 50</span></footer></section>'
        for page in range(1, 51)
    ]
    return f"{before}<main>{''.join(pages)}</main>{after}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--browser", default="chromium", help="Chromium executable")
    args = parser.parse_args()
    browser = shutil.which(args.browser)
    if not browser or not shutil.which("pdfinfo"):
        parser.error("A Chromium browser and Poppler pdfinfo are required.")
    with TemporaryDirectory(prefix="career-guide-print-") as temporary:
        folder = Path(temporary).resolve()
        for skill, asset, count, destination in ASSETS:
            template = (ROOT / "skills" / skill / "assets" / asset).read_text(encoding="utf-8")
            for size, width, height in SIZES:
                html = template
                if size == "A4":
                    html = html.replace("size: letter;", "size: A4;").replace("9.6in", "263mm")
                pdf = export(browser, folder, f"{skill}-{size}", html)
                check_geometry(pdf, count, width, height)
                check(f'"{destination}"' in output("pdfinfo", "-dests", str(pdf)), f"{pdf.name}: missing internal destination")
                if skill == "local-opportunity-directory":
                    check("https://example.org/" in output("pdfinfo", "-url", str(pdf)), f"{pdf.name}: missing external link")
                print(f"{pdf.name}: {count} pages, {size}, links present")
            if skill == "career-guide-book":
                pdf = export(browser, folder, "workbook-50-page-fixture", fixture_book(template))
                check_geometry(pdf, 50, 612, 792)
                print(f"{pdf.name}: 50 pages, Letter")


if __name__ == "__main__":
    main()
