"""Builds responsive AVIF + WebP variants of every photo in photos/ (the source JPEGs).

Run after adding or replacing a photo:  python3 scripts/images.py
Writes public/img/opt/<name>-<width>.{avif,webp} and src/lib/images.json
(the widths available per image, read by the <Pic> component).
"""
import json, pathlib
from PIL import Image

SRC = pathlib.Path('photos')
OUT = pathlib.Path('public/img/opt')
OUT.mkdir(exist_ok=True)
WIDTHS = [400, 800, 1200]
manifest = {}
for f in sorted(SRC.glob('*.jpg')):
    name = f.stem
    if name.endswith('-sm'):
        base = name[:-3]
        if (SRC / f'{base}.jpg').exists():
            continue  # the full-size original covers this image
        name = base
    if name == 'logo-circle':
        continue
    im = Image.open(f).convert('RGB')
    widths = [w for w in WIDTHS if w <= im.width] or [im.width]
    if im.width > widths[-1] and len(widths) < len(WIDTHS):
        widths.append(im.width)
    for w in widths:
        v = im.copy()
        v.thumbnail((w, 10_000), Image.LANCZOS)
        v.save(OUT / f'{name}-{w}.avif', quality=42, speed=4)
        v.save(OUT / f'{name}-{w}.webp', quality=55, method=6)
    manifest[name] = {'w': widths, 'ratio': round(im.width / im.height, 4)}
pathlib.Path('src/lib/images.json').write_text(json.dumps(manifest, indent=1))
print(len(manifest), 'images')
