#!/usr/bin/env python3
"""Regenerate the PDF handouts from the Jupyter notebooks.

Requirements:
    pip install nbconvert
    Google Chrome (or Chromium) installed locally

Usage:
    python scripts/build_pdf.py                # build all lectures
    python scripts/build_pdf.py 第3讲-Python数据类型  # build one lecture
    CHROME=/path/to/chrome python scripts/build_pdf.py

The script renders each notebook to HTML with nbconvert, rewrites the
relative image paths to local file URLs, then prints the page to A4 PDF
with headless Chrome. Keeping the pipeline in one place makes the PDFs
reproducible when a notebook changes.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_DIR = ROOT / "notebooks"
PDF_DIR = ROOT / "pdf"

PRINT_CSS = """
<style>
@page { size: A4; margin: 15mm 14mm 15mm 14mm; }
html, body { margin: 0 !important; padding: 0 !important; max-width: none !important;
  font-family: -apple-system, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif !important;
  font-size: 15px !important; line-height: 1.75 !important; color: #222; }
.container { width: auto !important; max-width: none !important; }
.cell { border: none !important; padding: 0 !important; margin: 0 0 14px 0 !important;
  break-inside: auto !important; }
h1 { font-size: 22px !important; margin: 0 0 12px !important; line-height: 1.45 !important; }
h2 { font-size: 21px !important; margin: 22px 0 10px !important; break-after: avoid; }
h3, h4 { font-size: 17px !important; margin: 16px 0 8px !important; break-after: avoid; }
p { margin: 6px 0 !important; orphans: 2; widows: 2; }
pre { font-size: 12.5px !important; line-height: 1.55 !important; white-space: pre-wrap !important;
  word-break: break-word; background: #f7f7f7 !important; border: 1px solid #e5e5e5; border-radius: 4px;
  padding: 8px 10px !important; break-inside: auto !important; }
.output pre { background: #fff !important; border: none; padding: 4px 0 !important; }
img { max-width: 100% !important; height: auto !important; }
blockquote { margin: 8px 0 !important; padding: 8px 14px !important; font-size: 14px;
  break-inside: auto !important; }
hr { margin: 14px 0; }
a[href]::after { content: none !important; }
</style>
</head>"""


def find_chrome() -> str:
    candidates = [
        os.environ.get("CHROME"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    sys.exit(
        "Could not find Chrome/Chromium. Install it, or set CHROME=/path/to/chrome."
    )


def build_one(notebook: Path, out_dir: Path, chrome: str) -> tuple[Path, int]:
    html_path = out_dir / (notebook.stem + ".html")
    pdf_path = out_dir / (notebook.stem + ".pdf")

    subprocess.run(
        [
            sys.executable, "-m", "nbconvert", "--to", "html",
            "--template", "classic",
            "--output-dir", str(out_dir), str(notebook),
            "--output", notebook.stem,
        ],
        check=True,
        capture_output=True,
    )

    html = html_path.read_text(encoding="utf-8")
    if "</head>" not in html:
        sys.exit(f"Unexpected nbconvert output: {html_path}")

    # nbconvert's --embed-images rewrites inline <font> tags and drops their
    # text, which would erase every highlighted sentence. Instead keep the
    # original HTML and point relative image paths at the real files.
    img_base = (NOTEBOOK_DIR / "img").resolve().as_uri()
    html, replaced = re.subn(
        r'src="img/([^"]+)"', lambda m: f'src="{img_base}/{quote(m.group(1))}"', html
    )
    html = html.replace("</head>", PRINT_CSS, 1)
    html_path.write_text(html, encoding="utf-8")

    subprocess.run(
        [
            chrome, "--headless=new", "--disable-gpu", "--no-sandbox",
            "--no-pdf-header-footer", f"--user-data-dir={out_dir / 'chrome-profile'}",
            "--virtual-time-budget=10000", "--allow-file-access-from-files",
            f"--print-to-pdf={pdf_path}", html_path.as_uri(),
        ],
        check=True,
        capture_output=True,
    )

    if not pdf_path.exists() or pdf_path.stat().st_size < 10_000:
        sys.exit(f"PDF generation failed: {pdf_path}")
    return pdf_path, replaced


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate lecture PDFs from notebooks.")
    parser.add_argument(
        "lectures", nargs="*",
        help="Notebook stems to build (default: all). Example: 第1讲-Python介绍",
    )
    args = parser.parse_args()

    notebooks = sorted(NOTEBOOK_DIR.glob("*.ipynb"))
    if args.lectures:
        wanted = set(args.lectures)
        notebooks = [n for n in notebooks if n.stem in wanted]
        missing = wanted - {n.stem for n in notebooks}
        if missing:
            sys.exit(f"Notebook not found: {', '.join(sorted(missing))}")
    if not notebooks:
        sys.exit(f"No notebooks found in {NOTEBOOK_DIR}")

    chrome = find_chrome()
    PDF_DIR.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="python-beginner-pdf-") as tmp:
        for notebook in notebooks:
            pdf, replaced = build_one(notebook, Path(tmp), chrome)
            target = PDF_DIR / pdf.name
            shutil.copy2(pdf, target)
            print(f"built {target.relative_to(ROOT)}  ({target.stat().st_size / 1024:.0f} KB, {replaced} images)")


if __name__ == "__main__":
    main()
