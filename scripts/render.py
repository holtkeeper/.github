#!/usr/bin/env python3
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "profile" / "assets"

ORANGE = "#ff7a1a"
EMBER = "#d95a0b"
AMBER = "#ffb547"
CREAM = "#ffe6cc"
INK = "#1a120c"

HEAD = "M8 42c0-14 10.7-25 24-25s24 11 24 25v6H8z"
EARS = (
    f'<circle cx="13.5" cy="25.5" r="4.6" fill="{EMBER}"/><circle cx="50.5" cy="25.5" r="4.6" fill="{EMBER}"/>'
    f'<circle cx="13.5" cy="25.5" r="2" fill="{AMBER}"/><circle cx="50.5" cy="25.5" r="2" fill="{AMBER}"/>'
)
LEFT_EYE = f'<circle cx="23" cy="32" r="3.4" fill="{INK}"/><circle cx="24.2" cy="30.8" r="1.1" fill="#fff"/>'
RIGHT_EYE = f'<circle cx="41" cy="32" r="3.4" fill="{INK}"/><circle cx="42.2" cy="30.8" r="1.1" fill="#fff"/>'
MUZZLE = (
    f'<ellipse cx="32" cy="41.5" rx="12" ry="6.5" fill="{CREAM}"/>'
    f'<path d="M21 39.5l-8.5-1.8M21 42.5l-8.5 1M43 39.5l8.5-1.8M43 42.5l8.5 1" stroke="{CREAM}" stroke-opacity=".85" stroke-width="1.2" stroke-linecap="round"/>'
    f'<ellipse cx="32" cy="38.2" rx="3.3" ry="2.3" fill="{INK}"/>'
    f'<path d="M28.6 41.6q1.7 2 3.4 0q1.7 2 3.4 0" stroke="{INK}" stroke-width="1.4" stroke-linecap="round"/>'
)
KEY = (
    f'<circle cx="11" cy="52.5" r="5" stroke="{AMBER}" stroke-width="3.4"/>'
    f'<rect x="15.5" y="50.8" width="42.5" height="3.4" rx="1.7" fill="{AMBER}"/>'
    f'<rect x="45" y="52" width="3.4" height="6.5" rx="1.2" fill="{AMBER}"/>'
    f'<rect x="51" y="52" width="3.4" height="4.8" rx="1.2" fill="{AMBER}"/>'
)

GLYPHS = {
    "review": '<path d="M40 22h12a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-6l-4 3.5V34h-2a3 3 0 0 1-3-3v-6a3 3 0 0 1 3-3z" fill="#fff"/>'
    '<circle cx="41.5" cy="28" r="1.3" fill="#8b6cff"/><circle cx="46" cy="28" r="1.3" fill="#8b6cff"/><circle cx="50.5" cy="28" r="1.3" fill="#8b6cff"/>',
    "updates": '<path d="M46 35V21M40.5 26.5 46 21l5.5 5.5" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
    "audit": '<path d="M46 19.5l7.5 3v5.5c0 5-3.2 8.6-7.5 10.2-4.3-1.6-7.5-5.2-7.5-10.2v-5.5z" fill="#fff"/>'
    '<path d="M42.6 28.6l2.4 2.4 4.4-4.6" stroke="#e5484d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
    "browserslist": '<circle cx="46" cy="28" r="8" stroke="#fff" stroke-width="2"/>'
    '<path d="M46 20c-2.8 2.4-4 5-4 8s1.2 5.6 4 8c2.8-2.4 4-5 4-8s-1.2-5.6-4-8zM38 28h16" stroke="#fff" stroke-opacity=".75" stroke-width="1.6"/>',
    "release": '<path d="M38.5 21.5h8.5l7 7-8.5 8.5-7-7z" fill="#fff"/><circle cx="42.5" cy="25.5" r="1.8" fill="#e0a800"/>',
    "quality": '<path d="M46 19l2.2 6.8L55 28l-6.8 2.2L46 37l-2.2-6.8L37 28l6.8-2.2z" fill="#fff"/>',
    "knowledge": '<path d="M46 22.6c-2.4-1.7-5.2-2.4-8.5-2.4v14.6c3.3 0 6.1.7 8.5 2.4 2.4-1.7 5.2-2.4 8.5-2.4V20.2c-3.3 0-6.1.7-8.5 2.4z" fill="#fff"/>'
    '<path d="M46 22.6v14.6M40.2 25.2c1.4 0 2.6.3 3.6.8M40.2 28.7c1.4 0 2.6.3 3.6.8M51.8 25.2c-1.4 0-2.6.3-3.6.8M51.8 28.7c-1.4 0-2.6.3-3.6.8" stroke="#1f9d55" stroke-width="1.3" stroke-linecap="round"/>',
    "bundles": '<path d="M46 19l8.5 4.6v9.6L46 37.8l-8.5-4.6v-9.6z" fill="#fff"/>'
    '<path d="M37.9 23.8 46 28.2l8.1-4.4M46 28.2v9.2" stroke="#0ea5e9" stroke-width="1.7" stroke-linejoin="round"/>',
    "repos": '<path d="M41 22.5v11M41 30c0-3 1.6-4.4 4.6-4.6l1.4-.1c2.6-.2 4-1.5 4-4" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    '<circle cx="41" cy="21.5" r="2.6" fill="#fff"/><circle cx="41" cy="34.5" r="2.6" fill="#fff"/><circle cx="51" cy="21.5" r="2.6" fill="#fff"/>',
    "credentials": '<path d="M41.5 26.5v-2.5a4.5 4.5 0 0 1 9 0v2.5" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    '<rect x="38.5" y="26" width="15" height="11.5" rx="2.4" fill="#fff"/>'
    '<circle cx="46" cy="30.8" r="1.6" fill="#64748b"/><rect x="45.2" y="31" width="1.6" height="3.6" rx=".8" fill="#64748b"/>',
    "coverage": '<circle cx="46" cy="28" r="7.5" stroke="#fff" stroke-opacity=".4" stroke-width="3.2"/>'
    '<path d="M46 20.5a7.5 7.5 0 1 1-7.5 7.5" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>',
    "testids": '<path d="M40.5 19.5 52.5 28l-5.4 1.1 3.2 5.9-2.6 1.4-3.2-5.9-4 3.7z" fill="#fff" stroke="#fff" stroke-width="1.2" stroke-linejoin="round"/>',
    "branches": '<path d="M41 22.5v11M41 24.5c0 3.6 2.6 5.5 7 5.5" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
    '<circle cx="41" cy="21.5" r="2.6" fill="#fff"/><circle cx="41" cy="34.5" r="2.6" fill="#fff"/><circle cx="51" cy="30" r="2.6" fill="#fff"/>',
    "ci": '<circle cx="46" cy="29.5" r="7" stroke="#fff" stroke-width="2.4"/><rect x="44.2" y="18.5" width="3.6" height="2.6" rx="1" fill="#fff"/>'
    '<path d="M46 29.5v-4M46 29.5l2.6 1.8" stroke="#fff" stroke-width="2" stroke-linecap="round"/>',
    "licenses": '<path d="M46 20v15.5M39 23.5h14M42 36h8M39 23.5l-2.8 6.5M39 23.5l2.8 6.5M53 23.5l-2.8 6.5M53 23.5l2.8 6.5" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/>'
    '<path d="M36.2 30h5.6a2.8 2.8 0 0 1-5.6 0zM50.2 30h5.6a2.8 2.8 0 0 1-5.6 0z" fill="#fff"/><circle cx="46" cy="20" r="1.6" fill="#fff"/>',
    "api": '<path d="M42 20.5c-2 0-3 .8-3 2.6v2.6c0 1.4-.8 2.3-2.3 2.3 1.5 0 2.3.9 2.3 2.3v2.6c0 1.8 1 2.6 3 2.6M50 20.5c2 0 3 .8 3 2.6v2.6c0 1.4.8 2.3 2.3 2.3-1.5 0-2.3.9-2.3 2.3v2.6c0 1.8-1 2.6-3 2.6" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="46" cy="28" r="1.8" fill="#fff"/>',
    "fleet": '<path d="M37.5 30.5h17l-3.2 5.5H40.7z" fill="#fff"/><path d="M46 19v11.5" stroke="#fff" stroke-width="1.8" stroke-linecap="round"/>'
    '<path d="M47.4 20.5l6.4 8.5h-6.4zM44.6 22.5l-4.6 6.5h4.6z" fill="#fff"/>',
    "stack": '<path d="M46 19.5l8.5 4.5-8.5 4.5-8.5-4.5z" fill="#fff"/>'
    '<path d="M37.5 28.5l8.5 4.5 8.5-4.5M37.5 33l8.5 4.5 8.5-4.5" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
    "activity": '<path d="M37 28.5h4l2.6-6.5 4.8 13 2.6-6.5h4" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    "ai": '<path d="M44 22l1.9 6.1L52 30l-6.1 1.9L44 38l-1.9-6.1L36 30l6.1-1.9z" fill="#fff"/>'
    '<path d="M51.5 17.5l1 2.8 2.8 1-2.8 1-1 2.8-1-2.8-2.8-1 2.8-1z" fill="#fff"/>',
    "storage": '<path d="M39 22.5c0-1.7 3.1-3 7-3s7 1.3 7 3v11c0 1.7-3.1 3-7 3s-7-1.3-7-3z" fill="#fff"/>'
    '<path d="M39 22.5c0 1.7 3.1 3 7 3s7-1.3 7-3M39 28c0 1.7 3.1 3 7 3s7-1.3 7-3" stroke="#a16207" stroke-width="1.4"/>',
    "auditlog": '<rect x="39.5" y="19.5" width="13" height="17" rx="2.2" fill="#fff"/>'
    '<path d="M42.5 24h7M42.5 28h7M42.5 32h4.5" stroke="#9f1239" stroke-width="1.6" stroke-linecap="round"/>',
    "users": '<circle cx="50.8" cy="23.2" r="2.7" fill="#fff" fill-opacity=".6"/><path d="M47 34c.3-3.4 1.8-5.6 4-5.6 2.8 0 4.8 2.4 4.8 5.6z" fill="#fff" fill-opacity=".6"/>'
    '<circle cx="44" cy="24.2" r="3.3" fill="#fff"/><path d="M37.2 36c0-4 2.9-6.8 6.8-6.8s6.8 2.8 6.8 6.8z" fill="#fff"/>',
    "automation": '<path d="M48 19l-8.5 10.8h5.6L43.6 37l8.6-11.2h-5.6z" fill="#fff" stroke="#fff" stroke-width="1" stroke-linejoin="round"/>',
    "jobs": '<path d="M37.5 22.2l1.7 1.7 3.1-3.3M37.5 28.2l1.7 1.7 3.1-3.3M37.5 34.2l1.7 1.7 3.1-3.3" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'
    '<path d="M45.5 22.5h9M45.5 28.5h9M45.5 34.5h6" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/>',
    "settings": '<circle cx="46" cy="28" r="7.2" stroke="#fff" stroke-width="3" stroke-dasharray="2.9 2.755"/>'
    '<circle cx="46" cy="28" r="4.6" stroke="#fff" stroke-width="2.6"/>',
    "warmup": '<path d="M46 19c.5 3.5 3 5 4.6 7.6 1.4 2.2 1.9 4 1.9 5.4 0 3.6-2.9 6-6.5 6s-6.5-2.4-6.5-6c0-2.6 1.4-4.6 3-5.8.1 1.6.8 2.8 2 3.4-.6-3.7.3-7.5 1.5-10.6z" fill="#fff"/>'
    '<path d="M46 30.5c1.6 1.4 2.6 2.7 2.6 4 0 1.6-1.2 2.5-2.6 2.5s-2.6-.9-2.6-2.5c0-1.3 1-2.6 2.6-4z" fill="#dc2626"/>',
}

VARIANTS = {
    "review": "#8b6cff",
    "updates": "#3b82f6",
    "audit": "#e5484d",
    "browserslist": "#14b8a6",
    "release": "#e0a800",
    "quality": "#ec4899",
    "knowledge": "#1f9d55",
    "bundles": "#0ea5e9",
    "repos": "#4f46e5",
    "credentials": "#64748b",
    "coverage": "#65a30d",
    "testids": "#c026d3",
    "branches": "#7c3aed",
    "ci": "#0891b2",
    "licenses": "#b45309",
    "api": "#0f766e",
    "fleet": "#1d4ed8",
    "stack": "#be123c",
    "activity": "#059669",
    "ai": "#9333ea",
    "storage": "#a16207",
    "auditlog": "#9f1239",
    "users": "#db2777",
    "automation": "#0369a1",
    "jobs": "#1e293b",
    "settings": "#52525b",
    "warmup": "#dc2626",
}


def icon(name="holtkeeper"):
    if name == "holtkeeper":
        head = f'<path d="{HEAD}" fill="{ORANGE}"/>{LEFT_EYE}{RIGHT_EYE}'
    else:
        clip = f"head-{name}"
        head = (
            f'<clipPath id="{clip}"><path d="{HEAD}"/></clipPath>'
            f'<path d="{HEAD}" fill="{ORANGE}"/>{LEFT_EYE}'
            f'<g clip-path="url(#{clip})"><rect x="32" width="32" height="64" fill="{VARIANTS[name]}"/>'
            f'<g transform="translate(44.5 30.5) scale(.74) translate(-46 -28)">{GLYPHS[name]}</g></g>'
        )
    return f'<g fill="none">{EARS}{head}{MUZZLE}{KEY}</g>'


CAPABILITIES = [
    ("review", "Review", "AI review of merge requests: line threads with suggestions, replies, incremental re-review."),
    ("updates", "Updates", "Package updates across the fleet through Renovate; the agent fixes code when a pipeline breaks."),
    ("audit", "Audit", "Vulnerabilities from lockfiles of any ecosystem, fixed per package manager, with an expiring allowlist."),
    ("browserslist", "Browserslist", "Scheduled <code>update-browserslist-db</code> with a before/after diff of the resolved browsers."),
    ("release", "Release", "Changelog, readiness checks, tags, release notes and manual deploy jobs."),
    ("quality", "Quality", "Lint, dead code, duplication, secrets, licenses, bundle size and config drift across repositories."),
]

FONT = "Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "Menlo, SF Mono, monospace"


def background(w, h, accent, cx=0.2, cy=0.55, strip=True):
    bar = (
        f'<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{ORANGE}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>'
        if strip
        else ""
    )
    return f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#120c08"/><stop offset="1" stop-color="#1e140d"/>
  </linearGradient>
  <radialGradient id="glow" cx="{w * cx}" cy="{h * cy}" r="{h * 0.75}" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{accent}" stop-opacity=".24"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="dots" width="32" height="32" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.4" fill="#fff" fill-opacity=".05"/>
  </pattern>
  {bar}
</defs>
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect width="{w}" height="{h}" fill="url(#dots)"/>
<rect width="{w}" height="{h}" fill="url(#glow)"/>
{f'<rect y="{h - 10}" width="{w}" height="10" fill="url(#bar)"/>' if strip else ""}"""


def chips(x, y, items, accent):
    out, cx = [], x
    for c in items:
        width = 26 + len(c) * 14.5
        out.append(
            f'<rect x="{cx}" y="{y}" width="{width}" height="44" rx="22" fill="{accent}" fill-opacity=".14" stroke="{accent}" stroke-opacity=".5"/>'
            f'<text x="{cx + width / 2}" y="{y + 29}" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="500" fill="#f1e6dc">{c}</text>'
        )
        cx += width + 12
    return "".join(out)


def social():
    w, h = 1280, 640
    lines = ["Keeps a fleet of Git repositories in order:", "AI review, dependency updates, audits", "and releases on GitLab and GitHub."]
    text = "".join(
        f'<text x="520" y="{318 + i * 46}" font-family="{FONT}" font-size="34" fill="#cdbcad">{l}</text>' for i, l in enumerate(lines)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{background(w, h, ORANGE)}
<g transform="translate(96 150) scale(5.4)">{icon()}</g>
<text x="520" y="188" font-family="{MONO}" font-size="30" fill="{ORANGE}">holtkeeper/<tspan fill="#a8907d">holtkeeper</tspan></text>
<text x="520" y="268" font-family="{FONT}" font-size="80" font-weight="700" fill="#fbf5ef">Holtkeeper</text>
{text}
{chips(520, 488, ["TypeScript", "Bun", "GitLab", "GitHub", "MIT"], ORANGE)}
<text x="1220" y="590" text-anchor="end" font-family="{MONO}" font-size="22" fill="#8a7464">github.com/holtkeeper</text>
</svg>"""


def profile_banner():
    w, h = 1280, 420
    row = "".join(
        f'<g transform="translate({540 + i * 102} 282) scale(1.35)">{icon(name)}</g>'
        for i, name in enumerate(["holtkeeper", *(c[0] for c in CAPABILITIES)])
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{background(w, h, ORANGE)}
<g transform="translate(110 62) scale(4.4)">{icon()}</g>
<text x="540" y="150" font-family="{FONT}" font-size="92" font-weight="700" fill="#fbf5ef">Holtkeeper</text>
<text x="544" y="208" font-family="{FONT}" font-size="34" fill="#cdbcad">The keeper of your repository holt.</text>
<text x="544" y="252" font-family="{FONT}" font-size="24" fill="#9c8574">Review, updates, audits and releases for a fleet of Git repos.</text>
{row}
</svg>"""


def avatar():
    w = 512
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{w}" viewBox="0 0 {w} {w}">
{background(w, w, ORANGE, 0.5, 0.5, strip=False)}
<g transform="translate(65 28) scale(6)">{icon()}</g>
</svg>"""


PANDORA = f"""<g fill="none">
<circle cx="32" cy="24" r="20" fill="{AMBER}" opacity=".18"/>
<circle cx="32" cy="26" r="11" fill="{AMBER}" opacity=".22"/>
<path d="M12 34h40v18a4 4 0 0 1-4 4H16a4 4 0 0 1-4-4z" fill="#8a4a24"/>
<path d="M12 40h40v4H12z" fill="#6b3518"/>
<rect x="28.5" y="41" width="7" height="8" rx="1.5" fill="{AMBER}"/>
<path d="M10 31.5 45.5 17l2.4 5.6L12.4 37z" fill="#a85a2c"/>
<path d="M10 31.5 45.5 17" stroke="#d07a42" stroke-width="1.4" stroke-linecap="round"/>
<circle cx="24" cy="14" r="1.8" fill="{AMBER}"/>
<circle cx="34" cy="7" r="1.4" fill="#ffe08a"/>
<circle cx="40" cy="27" r="1.6" fill="{ORANGE}"/>
<circle cx="29" cy="21" r="1.2" fill="#ffe08a"/>
<circle cx="19" cy="24" r="1" fill="{ORANGE}"/>
<path d="M44 9l1 2.4 2.4 1-2.4 1-1 2.4-1-2.4-2.4-1 2.4-1z" fill="#ffe08a"/>
</g>"""


def disclaimer():
    w, h = 1280, 260
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <linearGradient id="dbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#160e08"/><stop offset="1" stop-color="#0d0b09"/>
  </linearGradient>
  <radialGradient id="dglow" cx="150" cy="130" r="260" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{AMBER}" stop-opacity=".28"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="ddots" width="28" height="28" patternUnits="userSpaceOnUse">
    <circle cx="2" cy="2" r="1.3" fill="#fff" fill-opacity=".05"/>
  </pattern>
</defs>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="28" fill="url(#dbg)" stroke="{AMBER}" stroke-opacity=".45" stroke-width="2"/>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="28" fill="url(#ddots)"/>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="28" fill="url(#dglow)"/>
<g transform="translate(62 34) scale(3)">{PANDORA}</g>
<text x="330" y="74" font-family="{MONO}" font-size="22" letter-spacing="3" fill="{AMBER}">⚠ DISCLAIMER · PANDORA'S BOX</text>
<text x="330" y="128" font-family="{FONT}" font-size="44" font-weight="700" fill="#f7f1ea">Fully AI-generated. Use at your own risk.</text>
<text x="330" y="172" font-family="{FONT}" font-size="25" fill="#cbbfb2">Not a single line of code was written or reviewed by a human.</text>
<text x="330" y="208" font-family="{FONT}" font-size="25" fill="#cbbfb2">Written by Claude through Claude Code. Open with care.</text>
</svg>"""


def write(name, svg, width):
    path = OUT / f"{name}.svg"
    path.write_text(svg)
    subprocess.run(["rsvg-convert", "-w", str(width), "-o", str(OUT / f"{name}.png"), str(path)], check=True)


def icon_svg(name):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 64 64">{icon(name)}</svg>'


OUT.mkdir(parents=True, exist_ok=True)
write("banner", profile_banner(), 1280)
write("avatar", avatar(), 512)
write("ai-disclaimer", disclaimer(), 1280)
write("social-holtkeeper", social(), 1280)
write("icon-holtkeeper", icon_svg("holtkeeper"), 128)
for name in VARIANTS:
    write(f"icon-{name}", icon_svg(name), 128)
