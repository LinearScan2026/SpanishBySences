"""
Build script: converts cheatsheet markdown files + style.css into a
self-contained index.html with EN/ES language switcher.

Usage:  python build.py
Output: index.html in the same directory
"""

import re
import pathlib

ROOT = pathlib.Path(__file__).parent
CSS_FILE = ROOT / "style.css"
OUTPUT_FILE = ROOT / "index.html"

LANG_DIRS = {
    "es": ROOT / "cheatsheets",
    "en": ROOT / "cheatsheets-en",
}

AREA_ORDER = [
    ("01-bano.md",            "bano",       "🚿 Baño — 卫生间",                    "🚿 Bathroom — 卫生间"),
    ("02-sala.md",            "sala",       "🛋️ Sala — 客厅",                      "🛋️ Living Room — 客厅"),
    ("03-mesa-comedor.md",    "comedor",    "🍽️ Mesa / Comedor — 餐桌",            "🍽️ Dining Table — 餐桌"),
    ("04-puerta-entrada.md",  "puerta",     "🚪 Puerta / Entrada — 大门玄关",       "🚪 Front Door — 大门玄关"),
    ("05-dormitorio.md",      "dormitorio", "🛏️ Dormitorio — 卧室",                "🛏️ Bedroom — 卧室"),
    ("06-cocina.md",          "cocina",     "🍳 Cocina — 厨房（安全优先）",          "🍳 Kitchen — 厨房（安全优先）"),
    ("07-ascensor.md",        "ascensor",   "🛗 Ascensor — 电梯",                   "🛗 Elevator — 电梯"),
    ("08-garaje.md",          "garaje",     "🅿️ Garaje — 地下车库",                "🅿️ Garage — 地下车库"),
    ("09-coche.md",           "coche",      "🚗 Coche — 汽车内",                    "🚗 Car — 汽车内"),
    ("10-guarderia.md",       "guarderia",  "🏫 Guardería — 幼儿园门口",             "🏫 Kindergarten — 幼儿园门口"),
]

NAV_ICONS = ["🚿", "🛋️", "🍽️", "🚪", "🛏️", "🍳", "🛗", "🅿️", "🚗", "🏫"]
NAV_LABELS = ["卫生间", "客厅", "餐桌", "玄关", "卧室", "厨房", "电梯", "车库", "汽车", "幼儿园"]

PHASE_RE = re.compile(r"^##\s*阶段\s*(\d+)（.*?）[：:]\s*(.+)$")
TIPS_RE = re.compile(r"^##\s*💡\s*小贴士")
TABLE_ROW_RE = re.compile(r"^\|(.+)\|$")
TABLE_SEP_RE = re.compile(r"^\|[-| ]+\|$")

PHASE_TITLES = {
    1: "阶段 1（第 1-2 月）：听懂并执行",
    2: "阶段 2（第 3-4 月）：短句输出",
    3: "阶段 3（第 5-6 月）：简单对话",
    4: "阶段 4（第 7-8 月）：描述与叙述",
    5: "阶段 5（第 9-10 月）：感受与想法",
    6: "阶段 6（第 11-12 月）：自主表达",
}


def parse_md(filepath: pathlib.Path):
    """Parse a cheatsheet markdown file into phases and tips."""
    phases = []
    tips_lines = []
    current_phase = None
    in_tips = False

    for raw_line in filepath.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()

        if TIPS_RE.match(line):
            in_tips = True
            continue

        if in_tips:
            if line.startswith("- "):
                tips_lines.append(line[2:])
            continue

        m = PHASE_RE.match(line)
        if m:
            phase_num = int(m.group(1))
            current_phase = {"num": phase_num, "rows": []}
            phases.append(current_phase)
            continue

        if current_phase is None:
            continue
        if TABLE_SEP_RE.match(line):
            continue

        row_m = TABLE_ROW_RE.match(line)
        if row_m:
            cols = [c.strip() for c in row_m.group(1).split("|")]
            if len(cols) >= 3:
                header_words = {"家长说", "中文", "期望孩子反应", "引导孩子说"}
                if cols[0] in header_words:
                    continue
                current_phase["rows"].append(
                    {"es": cols[0], "zh": cols[1], "resp": cols[2]}
                )

    return phases, tips_lines


def h(s: str) -> str:
    """HTML-escape a string."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build_area_html(area_id, area_title, phases, tips, is_first, lang):
    open_cls = " open" if is_first else ""
    full_id = f"{area_id}-{lang}"
    lines = [f'<div class="area lang-{lang}" id="{full_id}">']
    lines.append(f'  <div class="area-header" onclick="toggleArea(this)">')
    lines.append(f"    <h2>{h(area_title)}</h2>")
    lines.append(f'    <span class="toggle{open_cls}">&#9654;</span>')
    lines.append(f"  </div>")
    lines.append(f'  <div class="area-body{open_cls}">')

    for phase in phases:
        n = phase["num"]
        title = PHASE_TITLES.get(n, f"阶段 {n}")
        lines.append(f'    <div class="phase phase-{n}" data-phase="{n}">')
        lines.append(f'      <div class="phase-title">{h(title)}</div>')
        lines.append(f'      <div class="phrase-list">')
        for row in phase["rows"]:
            lines.append(
                f'        <div class="phrase">'
                f'<div class="es">{h(row["es"])}</div>'
                f'<div class="zh">{h(row["zh"])}</div>'
                f'<div class="resp">{h(row["resp"])}</div>'
                f"</div>"
            )
        lines.append(f"      </div>")
        lines.append(f"    </div>")

    if tips:
        lines.append(f'    <div class="tips">')
        lines.append(f"      <h3>💡 小贴士</h3>")
        lines.append(f"      <ul>")
        for tip in tips:
            lines.append(f"        <li>{h(tip)}</li>")
        lines.append(f"      </ul>")
        lines.append(f"    </div>")

    lines.append(f"  </div>")
    lines.append(f"</div>")
    return "\n".join(lines)


def build_nav_html():
    parts = []
    for i, (_, area_id, _, _) in enumerate(AREA_ORDER):
        parts.append(f'  <a href="#{area_id}" class="nav-link" data-area="{area_id}">{NAV_ICONS[i]} {NAV_LABELS[i]}</a>')
    return "\n".join(parts)


def build_filter_html():
    buttons = ['  <button class="active" onclick="filterPhase(\'all\')">全部</button>']
    for n in PHASE_TITLES:
        buttons.append(f"  <button onclick=\"filterPhase('{n}')\">阶段{n}</button>")
    return "\n".join(buttons)


def build_full_html(css, areas_html, nav_html, filter_html):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>家庭场景语言启蒙小抄 EN/ES</title>
  <style>
{css}

.lang-switch {{
  display: flex;
  justify-content: center;
  gap: 0;
  padding: 0.5rem 1rem;
  background: #fff;
  border-bottom: 1px solid #ddd;
}}

.lang-switch button {{
  padding: 0.4rem 1.2rem;
  font-size: 0.85rem;
  border: 1px solid #2c5f2d;
  background: #fff;
  color: #2c5f2d;
  cursor: pointer;
  font-family: inherit;
  font-weight: 600;
}}

.lang-switch button:first-child {{
  border-radius: 4px 0 0 4px;
}}

.lang-switch button:last-child {{
  border-radius: 0 4px 4px 0;
  border-left: none;
}}

.lang-switch button.active {{
  background: #2c5f2d;
  color: white;
}}

.lang-es, .lang-en {{ display: none; }}
.lang-es.visible, .lang-en.visible {{ display: block; }}

@media print {{
  .lang-switch {{ display: none !important; }}
}}
  </style>
</head>
<body>

<div class="header">
  <h1>家庭场景语言启蒙小抄</h1>
  <p>Mommy/Mam&aacute; &middot; Daddy/Pap&aacute; &middot; Baby &middot; Grandpa/Abuelo &middot; Grandma/Abuela</p>
</div>

<div class="lang-switch">
  <button class="active" onclick="switchLang('es')">Espa&ntilde;ol 🇪🇸</button>
  <button onclick="switchLang('en')">English 🇬🇧</button>
</div>

<nav class="nav" id="nav">
{nav_html}
</nav>

<div class="phase-filter">
{filter_html}
</div>

{areas_html}

<div class="footer">
  家庭场景语言启蒙小抄 &middot; Mommy, Daddy, Baby, Grandpa, Grandma
</div>

<script>
var currentLang = 'es';

function switchLang(lang) {{
  currentLang = lang;
  var buttons = document.querySelectorAll('.lang-switch button');
  buttons.forEach(function(btn) {{ btn.classList.remove('active'); }});
  if (lang === 'es') buttons[0].classList.add('active');
  else buttons[1].classList.add('active');

  document.querySelectorAll('.area').forEach(function(el) {{
    el.classList.remove('visible');
  }});
  document.querySelectorAll('.lang-' + lang).forEach(function(el) {{
    el.classList.add('visible');
  }});

  document.querySelectorAll('.nav-link').forEach(function(a) {{
    a.href = '#' + a.getAttribute('data-area') + '-' + lang;
  }});
}}

function toggleArea(header) {{
  var body = header.nextElementSibling;
  var toggle = header.querySelector('.toggle');
  body.classList.toggle('open');
  toggle.classList.toggle('open');
}}

function filterPhase(phase) {{
  var buttons = document.querySelectorAll('.phase-filter button');
  buttons.forEach(function(btn) {{ btn.classList.remove('active'); }});
  event.target.classList.add('active');

  document.querySelectorAll('.phase').forEach(function(p) {{
    if (phase === 'all' || p.getAttribute('data-phase') === phase) {{
      p.style.display = '';
    }} else {{
      p.style.display = 'none';
    }}
  }});
}}

document.addEventListener('DOMContentLoaded', function() {{
  switchLang('es');
  // Open first visible area
  var first = document.querySelector('.lang-es .area-body');
  var firstToggle = document.querySelector('.lang-es .toggle');
  if (first) first.classList.add('open');
  if (firstToggle) firstToggle.classList.add('open');
}});
</script>

</body>
</html>'''


def main():
    css = CSS_FILE.read_text(encoding="utf-8")

    all_areas_html = []
    for lang, lang_dir in LANG_DIRS.items():
        lang_label = "ES" if lang == "es" else "EN"
        print(f"[{lang_label}] Building from {lang_dir.name}/")
        for i, (filename, area_id, title_es, title_en) in enumerate(AREA_ORDER):
            md_path = lang_dir / filename
            if not md_path.exists():
                print(f"  SKIP {filename} (not found)")
                continue
            title = title_es if lang == "es" else title_en
            phases, tips = parse_md(md_path)
            html = build_area_html(area_id, title, phases, tips, is_first=(i == 0), lang=lang)
            all_areas_html.append(html)
            total = sum(len(p["rows"]) for p in phases)
            print(f"  OK {filename}: {len(phases)} phases, {total} phrases")

    areas_html = "\n\n".join(all_areas_html)
    nav_html = build_nav_html()
    filter_html = build_filter_html()
    full_html = build_full_html(css, areas_html, nav_html, filter_html)

    OUTPUT_FILE.write_text(full_html, encoding="utf-8")
    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"\nDone: {OUTPUT_FILE.name} ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
