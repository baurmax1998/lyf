from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).parent
RAW = ROOT / "raw"

PAGES = [
    {
        "slug": "training",
        "source": RAW / "training-plan.md",
        "title": "lyf – Trainingsplan Klettern",
        "description": "Vollständiger Trainingsplan für Klettern mit Kraft, Hangboard, Mobility und Progression.",
        "badge": "Trainingsplan Klettern",
        "hero_title": "Trainingsplan Klettern – Wochenplan",
        "hero_text": "Die vollständigen Inhalte aus dem Markdown-Plan, überführt in eine navigierbare HTML-Seite.",
    },
    {
        "slug": "mental",
        "source": RAW / "mental-training-plan.md",
        "title": "lyf – Mentaler Trainingsplan",
        "description": "Vollständiger mentaler Trainingsplan für Klettern mit Fokus, Atmung, Commitment und Reflexion.",
        "badge": "Mentales Training",
        "hero_title": "Mentaler Trainingsplan – ergänzend zum Wochenplan",
        "hero_text": "Die vollständigen Inhalte aus dem Markdown-Plan, überführt in eine navigierbare HTML-Seite.",
    },
    {
        "slug": "alltag",
        "source": RAW / "alltags-mental-plan.md",
        "title": "lyf – Mentaler Alltagsplan",
        "description": "Vollständiger mentaler Alltagsplan mit Wochenstruktur, Abendroutine und Tagesplanung.",
        "badge": "Mentaler Alltagsplan",
        "hero_title": "Mentaler Alltagsplan – Wochenstruktur + Tagesplanung",
        "hero_text": "Die vollständigen Inhalte aus dem Markdown-Plan, überführt in eine navigierbare HTML-Seite.",
    },
    {
        "slug": "haushalt",
        "source": RAW / "haushalt-selfcare-plan.md",
        "title": "lyf – Haushalt und Selfcare",
        "description": "Vollständiger Haushalts- und Selfcare-Plan über 4 Wochen mit Triggern und Wiederholungen.",
        "badge": "Haushalt & Selfcare",
        "hero_title": "Haushalts- und Selfcare-Plan – 4 Wochen",
        "hero_text": "Die vollständigen Inhalte aus dem Markdown-Plan, überführt in eine navigierbare HTML-Seite.",
    },
]

NAV = [
    ("index.html", "Start", "index"),
    ("training.html", "Training", "training"),
    ("mental.html", "Mental", "mental"),
    ("alltag.html", "Alltag", "alltag"),
    ("haushalt.html", "Haushalt &amp; Selfcare", "haushalt"),
]


def inline_format(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped


def markdown_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()

        if not stripped:
            close_lists()
            i += 1
            continue

        if stripped == "---":
            close_lists()
            out.append("<hr />")
            i += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            close_lists()
            level = len(heading.group(1))
            text = inline_format(heading.group(2).strip())
            anchor = re.sub(r"[^a-z0-9äöüß]+", "-", heading.group(2).strip().lower()).strip("-")
            out.append(f'<h{level} id="{anchor}">{text}</h{level}>')
            i += 1
            continue

        ul = re.match(r"^-\s+(.*)$", stripped)
        if ul:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_format(ul.group(1))}</li>")
            i += 1
            continue

        ol = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if ol:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_format(ol.group(2))}</li>")
            i += 1
            continue

        close_lists()
        paragraph = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt == "---" or re.match(r"^(#{1,6})\s+", nxt) or re.match(r"^-\s+", nxt) or re.match(r"^\d+\.\s+", nxt):
                break
            paragraph.append(nxt)
            i += 1
        out.append(f"<p>{inline_format(' '.join(paragraph))}</p>")

    close_lists()
    return "\n        ".join(out)


def render_nav(active: str) -> str:
    links = []
    for href, label, key in NAV:
        cls = ' class="active"' if key == active else ""
        links.append(f'<a{cls} href="{href}">{label}</a>')
    return "\n          ".join(links)


def render_page(page: dict[str, str], body: str) -> str:
    nav = render_nav(page["slug"])
    return f'''<!doctype html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{page["title"]}</title>
    <meta name="description" content="{page["description"]}" />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <header class="site-header">
      <nav class="nav">
        <a class="brand" href="index.html">lyf</a>
        <div class="nav-links">
          {nav}
        </div>
      </nav>
    </header>

    <main class="content">
      <section class="hero">
        <span class="badge">{page["badge"]}</span>
        <h1>{page["hero_title"]}</h1>
        <p class="lead">{page["hero_text"]}</p>
      </section>

      <section class="section markdown panel">
        {body}
      </section>
    </main>

    <footer class="footer">
      <p><a href="index.html">← Zurück zur Startseite</a></p>
    </footer>
  </body>
</html>
'''


def main() -> None:
    for page in PAGES:
        md = page["source"].read_text(encoding="utf-8")
        body = markdown_to_html(md)
        output = ROOT / f'{page["slug"]}.html'
        output.write_text(render_page(page, body), encoding="utf-8")
        print(f"generated {output.name}")


if __name__ == "__main__":
    main()
