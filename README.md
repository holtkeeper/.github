# .github

The [Holtkeeper organization profile](https://github.com/holtkeeper): `profile/README.md`, its
banner, the avatar, capability icons and the social preview image of the repository. Text is set
in Geist (`scripts/fonts/`, SIL OFL) and converted to outlines, so the SVGs need no fonts.
`slack/` holds the Slack app's texts, colors and review status emoji.

```sh
pip install fonttools uharfbuzz pillow
python3 scripts/render.py   # also needs rsvg-convert
```
