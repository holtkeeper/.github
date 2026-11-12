#!/usr/bin/env python3
import functools
import math
import pathlib
import subprocess
import tempfile

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "profile" / "assets"
FONTS = ROOT / "scripts" / "fonts"

BG = "#0b0b0c"
PANEL = "#111113"
RAISE = "#18181b"
FG = "#ededef"
SOFT = "#c9c9cf"
MUTED = "#93939b"
ACCENT = "#f0a63a"
INK = "#0b0b0c"

HEAD = (
    "M32 9C47 9 57 19 58 32C58.5 37 60 41 62.5 44C59.5 44.5 58 45.5 57.5 47C60 48.5 61 50 61 51.5"
    "C57 51 55 52 52.5 54C47 58.5 40 60 32 60C24 60 17 58.5 11.5 54C9 52 7 51 3 51.5"
    "C3 50 4 48.5 6.5 47C6 45.5 4.5 44.5 1.5 44C4 41 5.5 37 6 32C7 19 17 9 32 9Z"
)


def shade(color, amount):
    r, g, b = (int(color[i : i + 2], 16) for i in (1, 3, 5))
    return "#" + "".join(f"{round(c * (1 - amount)):02x}" for c in (r, g, b))


def head(color, inner, ink=INK, nose_opacity=1.0):
    ears = "".join(
        f'<circle cx="{x}" cy="16.5" r="8" fill="{shade(color, 0.2)}"/><circle cx="{x}" cy="16.5" r="3.8" fill="{color}"/>'
        f'<circle cx="{x}" cy="16.5" r="3.8" fill="#fff" fill-opacity=".3"/>'
        for x in (12.5, 51.5)
    )
    return (
        f'<g fill="none">{ears}<path d="{HEAD}" fill="{color}"/>'
        f'<ellipse cx="32" cy="50" rx="15" ry="8.5" fill="#fff" fill-opacity=".22"/>'
        f'<ellipse cx="32" cy="45.2" rx="3.4" ry="2.3" fill="{ink}" fill-opacity="{nose_opacity}"/>{inner}</g>'
    )


def mascot():
    face = (
        f'<circle cx="22.5" cy="32" r="3.7" fill="{INK}"/><circle cx="23.8" cy="30.7" r="1.25" fill="#fff"/>'
        f'<circle cx="41.5" cy="32" r="3.7" fill="{INK}"/><circle cx="42.8" cy="30.7" r="1.25" fill="#fff"/>'
        f'<path d="M28.6 48.6q1.7 1.9 3.4 0q1.7 1.9 3.4 0" stroke="{INK}" stroke-width="1.3" stroke-linecap="round"/>'
    )
    return head(ACCENT, face)


CAPABILITIES = [
    (
        "review",
        "Review",
        "#9d8cff",
        '<path d="M26.5 21.5h11a3 3 0 0 1 3 3v6a3 3 0 0 1-3 3h-5.5l-4 3.5v-3.5h-1.5a3 3 0 0 1-3-3v-6a3 3 0 0 1 3-3z" fill="#fff"/>'
        '<circle cx="28" cy="27.5" r="1.4" fill="{c}"/><circle cx="32" cy="27.5" r="1.4" fill="{c}"/><circle cx="36" cy="27.5" r="1.4" fill="{c}"/>',
    ),
    (
        "updates",
        "Updates",
        "#6aa2ff",
        '<path d="M32 37V21.5M25.5 28 32 21.5l6.5 6.5" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>',
    ),
    (
        "audit",
        "Audit",
        "#f2665f",
        '<path d="M32 20l8 3.2v5.8c0 5.3-3.4 9.1-8 10.8-4.6-1.7-8-5.5-8-10.8v-5.8z" fill="#fff"/>'
        '<path d="M28.4 29.4l2.5 2.5 4.7-4.9" stroke="{c}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
    ),
    (
        "browserslist",
        "Browserslist",
        "#2dd4bf",
        '<circle cx="32" cy="29" r="8.5" stroke="#fff" stroke-width="2.4"/>'
        '<path d="M32 20.5c-3 2.6-4.3 5.3-4.3 8.5s1.3 5.9 4.3 8.5c3-2.6 4.3-5.3 4.3-8.5s-1.3-5.9-4.3-8.5zM23.5 29h17" stroke="#fff" stroke-width="1.8"/>',
    ),
    (
        "release",
        "Release",
        "#f472b6",
        '<path d="M23.5 21.5h9l7.5 7.5-9 9-7.5-7.5z" fill="#fff" stroke="#fff" stroke-width="1.6" stroke-linejoin="round"/>'
        '<circle cx="27.8" cy="25.8" r="2" fill="{c}"/>',
    ),
    (
        "quality",
        "Quality",
        "#3ecf8e",
        '<path d="M32 19.5l2.4 7.1 7.1 2.4-7.1 2.4-2.4 7.1-2.4-7.1-7.1-2.4 7.1-2.4z" fill="#fff" stroke="#fff" stroke-width="1.2" stroke-linejoin="round"/>',
    ),
]


def capability(name):
    _, _, color, glyph = next(c for c in CAPABILITIES if c[0] == name)
    return head(color, glyph.replace("{c}", color), nose_opacity=0.8)


@functools.cache
def font(name):
    path = FONTS / f"{name}.ttf"
    blob = hb.Blob.from_file_path(str(path))
    return TTFont(path), hb.Font(hb.Face(blob))


def text(s, x, y, name, size, fill, anchor="start", tracking=0.0):
    tt, hbfont = font(name)
    upem = tt["head"].unitsPerEm
    buf = hb.Buffer()
    buf.add_str(s)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf, {"kern": True, "liga": True})
    glyphs = tt.getGlyphSet()
    order = tt.getGlyphOrder()
    scale = size / upem
    pen_x, parts = 0.0, []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        pen = SVGPathPen(glyphs)
        glyphs[order[info.codepoint]].draw(pen)
        d = pen.getCommands()
        if d:
            parts.append(f'<path transform="translate({pen_x + pos.x_offset:.1f} 0)" d="{d}"/>')
        pen_x += pos.x_advance + tracking * upem
    width = (pen_x - tracking * upem) * scale
    start = {"start": x, "middle": x - width / 2, "end": x - width}[anchor]
    return f'<g fill="{fill}" transform="translate({start:.2f} {y}) scale({scale:.5f} {-scale:.5f})">{"".join(parts)}</g>', width


def label(*args, **kwargs):
    return text(*args, **kwargs)[0]


def background(w, h, cx, cy, r, glow=0.18, grid=True, rounded=0):
    shape = f'rx="{rounded}"' if rounded else ""
    lines = (
        f'<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#fff" stroke-opacity=".035"/></pattern>'
        if grid
        else ""
    )
    return f"""<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{PANEL}"/><stop offset="1" stop-color="{BG}"/></linearGradient>
  <radialGradient id="glow" cx="{cx}" cy="{cy}" r="{r}" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="{ACCENT}" stop-opacity="{glow}"/><stop offset="1" stop-color="{ACCENT}" stop-opacity="0"/>
  </radialGradient>
  {lines}
</defs>
<rect width="{w}" height="{h}" {shape} fill="url(#bg)"/>
{f'<rect width="{w}" height="{h}" {shape} fill="url(#grid)"/>' if grid else ""}
<rect width="{w}" height="{h}" {shape} fill="url(#glow)"/>"""


def place(svg_inner, cx, cy, size):
    k = size / 64
    return f'<g transform="translate({cx - 32 * k:.2f} {cy - 34.25 * k:.2f}) scale({k:.4f})">{svg_inner}</g>'


def chips(x, y, items):
    out, cx = [], x
    for c in items:
        body, width = text(c, 0, 0, "geist-mono-500", 20, SOFT)
        pill = width + 36
        out.append(
            f'<rect x="{cx}" y="{y}" width="{pill:.1f}" height="42" rx="21" fill="{RAISE}" stroke="#fff" stroke-opacity=".13"/>'
            + label(c, cx + 18, y + 28, "geist-mono-500", 20, SOFT)
        )
        cx += pill + 10
    return "".join(out)


def social():
    w, h = 1280, 640
    lines = ["Keeps a fleet of Git repositories in order:", "AI review, dependency updates, audits", "and releases on GitLab and GitHub."]
    body = "".join(label(l, 520, 330 + i * 46, "geist-400", 32, SOFT) for i, l in enumerate(lines))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{background(w, h, 260, 330, 420)}
{place(mascot(), 270, 330, 330)}
{label("holtkeeper/holtkeeper", 520, 180, "geist-mono-500", 26, ACCENT)}
{label("Holtkeeper", 516, 268, "geist-700", 84, FG, tracking=-0.025)}
{body}
{chips(520, 490, ["TypeScript", "Bun", "GitLab", "GitHub", "MIT"])}
{label("github.com/holtkeeper", 1220, 594, "geist-mono-500", 20, MUTED, anchor="end")}
</svg>"""


def profile_banner():
    w, h = 1280, 420
    row = "".join(place(capability(c[0]), 572 + i * 76, 336, 60) for i, c in enumerate(CAPABILITIES))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{background(w, h, 270, 215, 330)}
{place(mascot(), 270, 210, 290)}
{label("holtkeeper/holtkeeper", 540, 96, "geist-mono-500", 22, ACCENT)}
{label("Holtkeeper", 536, 178, "geist-700", 86, FG, tracking=-0.025)}
{label("The keeper of your repository holt.", 540, 228, "geist-400", 30, SOFT)}
{label("Review, updates, audits and releases for a fleet of Git repos.", 540, 266, "geist-400", 22, MUTED)}
{row}
</svg>"""


def avatar(w=512):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{w}" viewBox="0 0 512 512">
{background(512, 512, 256, 280, 330, glow=0.22, grid=False)}
{place(mascot(), 256, 262, 400)}
</svg>"""


PANDORA = f"""<g fill="none">
<circle cx="32" cy="24" r="20" fill="{ACCENT}" opacity=".16"/>
<circle cx="32" cy="26" r="11" fill="{ACCENT}" opacity=".22"/>
<path d="M12 34h40v18a4 4 0 0 1-4 4H16a4 4 0 0 1-4-4z" fill="#27272a"/>
<path d="M12 40h40v4H12z" fill="#1c1c20"/>
<rect x="28.5" y="41" width="7" height="8" rx="1.5" fill="{ACCENT}"/>
<path d="M10 31.5 45.5 17l2.4 5.6L12.4 37z" fill="#3f3f46"/>
<path d="M10 31.5 45.5 17" stroke="#52525b" stroke-width="1.4" stroke-linecap="round"/>
<circle cx="24" cy="14" r="1.8" fill="{ACCENT}"/>
<circle cx="34" cy="7" r="1.4" fill="#ffd591"/>
<circle cx="40" cy="27" r="1.6" fill="{ACCENT}"/>
<circle cx="29" cy="21" r="1.2" fill="#ffd591"/>
<circle cx="19" cy="24" r="1" fill="{ACCENT}"/>
<path d="M44 9l1 2.4 2.4 1-2.4 1-1 2.4-1-2.4-2.4-1 2.4-1z" fill="#ffd591"/>
</g>"""


def disclaimer():
    w, h = 1280, 260
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{background(w, h, 160, 130, 260, glow=0.2, rounded=24)}
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="24" fill="none" stroke="{ACCENT}" stroke-opacity=".4"/>
<g transform="translate(62 34) scale(3)">{PANDORA}</g>
{label("DISCLAIMER · PANDORA'S BOX", 330, 74, "geist-mono-500", 20, ACCENT, tracking=0.12)}
{label("Fully AI-generated. Use at your own risk.", 328, 128, "geist-700", 42, FG, tracking=-0.015)}
{label("Not a single line of code was written or reviewed by a human.", 330, 172, "geist-400", 24, SOFT)}
{label("Written by Claude through Claude Code. Open with care.", 330, 208, "geist-400", 24, SOFT)}
</svg>"""


def write(name, svg, width):
    path = OUT / f"{name}.svg"
    path.write_text(svg)
    subprocess.run(["rsvg-convert", "-w", str(width), "-o", str(OUT / f"{name}.png"), str(path)], check=True)


def icon_svg(inner):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 64 64">{inner}</svg>'


EMOJI_OUT = ROOT / "slack" / "emoji"
EMOJI_INK = "#1a120c"
EMOJI_STATUS = {
    "reviewing": ("#8b6cff", "#6a4fe0", "#fff"),
    "clean": ("#1f9d55", "#157a41", "#fff"),
    "minor": ("#fbbf24", "#d99a06", EMOJI_INK),
    "changes": ("#e5484d", "#bf2f34", "#fff"),
    "skipped": ("#7c8491", "#5d6470", "#fff"),
}


def emoji_glyph(status, ink, cx, cy, size):
    k = size / 10
    w = 2.4 * k
    return {
        "reviewing": f'<circle cx="{cx - k}" cy="{cy - k}" r="{3.6 * k}" stroke="{ink}" stroke-width="{w}"/>'
        f'<path d="M{cx + 1.8 * k} {cy + 1.8 * k}l{3 * k} {3 * k}" stroke="{ink}" stroke-width="{w * 1.1}" stroke-linecap="round"/>',
        "clean": f'<path d="M{cx - 4.6 * k} {cy + 0.2 * k}l{3.2 * k} {3.2 * k} {6.2 * k}-{6.6 * k}" stroke="{ink}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>',
        "minor": f'<path d="M{cx} 22.5V37.5" stroke="{ink}" stroke-width="{w * 1.05}" stroke-linecap="round"/>',
        "changes": f'<path d="M{cx - 3.8 * k} {cy - 3.8 * k}l{7.6 * k} {7.6 * k}M{cx + 3.8 * k} {cy - 3.8 * k}l-{7.6 * k} {7.6 * k}" stroke="{ink}" stroke-width="{w}" stroke-linecap="round"/>',
        "skipped": f'<path d="M{cx - 4.5 * k} {cy}h{9 * k}" stroke="{ink}" stroke-width="{w * 1.05}" stroke-linecap="round"/>',
    }[status]


def emoji(status, t=0.0):
    color, dark, ink = EMOJI_STATUS[status]
    dx, dy = (1.4 * math.cos(t), 1.4 * math.sin(t)) if status == "reviewing" else (0.0, 0.0)
    tint = '<circle cx="{x}" cy="16.5" r="3.8" fill="#fff" fill-opacity=".3"/>'
    ears = "".join(
        f'<circle cx="{x}" cy="16.5" r="8" fill="{dark}"/><circle cx="{x}" cy="16.5" r="3.8" fill="{color}"/>{tint.format(x=x)}'
        for x in (12.5, 51.5)
    )
    nose = 'fill-opacity="1"' if status == "minor" else 'fill-opacity=".8"'
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128" viewBox="0 0 64 64">
<g fill="none">{ears}<path d="{HEAD}" fill="{color}"/>
<ellipse cx="32" cy="50" rx="15" ry="8.5" fill="#fff" fill-opacity=".22"/>
<ellipse cx="32" cy="45.2" rx="3.4" ry="2.3" fill="{EMOJI_INK}" {nose}/>
<g transform="translate({dx} {dy})">{emoji_glyph(status, ink, 32, 29.5, 17)}</g></g>
</svg>"""


def write_emoji(status):
    EMOJI_OUT.mkdir(parents=True, exist_ok=True)
    svg = EMOJI_OUT / f"hk-{status}.svg"
    svg.write_text(emoji(status))
    subprocess.run(["rsvg-convert", "-w", "128", "-o", str(EMOJI_OUT / f"hk-{status}.png"), str(svg)], check=True)


def write_animated(status, frames=16, ms=90):
    from PIL import Image

    images = []
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(frames):
            src = pathlib.Path(tmp) / f"{i}.svg"
            src.write_text(emoji(status, 2 * math.pi * i / frames))
            png = src.with_suffix(".png")
            subprocess.run(["rsvg-convert", "-w", "128", "-o", str(png), str(src)], check=True)
            rgba = Image.open(png).convert("RGBA")
            frame = rgba.convert("RGB").quantize(colors=255, method=Image.Quantize.MEDIANCUT)
            frame.paste(255, mask=rgba.getchannel("A").point(lambda a: 255 if a < 128 else 0))
            images.append(frame)
    images[0].save(
        EMOJI_OUT / f"hk-{status}.gif", save_all=True, append_images=images[1:], duration=ms, loop=0, transparency=255, disposal=2
    )


OUT.mkdir(parents=True, exist_ok=True)
write("banner", profile_banner(), 1280)
write("avatar", avatar(), 512)
write("slack-bot", avatar(1024), 1024)
write("ai-disclaimer", disclaimer(), 1280)
write("social-holtkeeper", social(), 1280)
write("icon-holtkeeper", icon_svg(mascot()), 128)
for name, *_ in CAPABILITIES:
    write(f"icon-{name}", icon_svg(capability(name)), 128)
for status in EMOJI_STATUS:
    write_emoji(status)
write_animated("reviewing")
