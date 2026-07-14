"""Convert remaining hero/small images to WebP"""
import os, sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
ASSETS = os.path.dirname(os.path.abspath(__file__)) + '/assets'

targets = {
    'hero-wujitai.jpg':           ('hero-wujitai.webp',           'webp', 80),
    'hero-tengcha-product.jpg':   ('hero-tengcha-product.webp',   'webp', 82),
    'hero-tengcha-raw.jpg':       ('hero-tengcha-raw.webp',       'webp', 80),
    'hero-slide-p04.jpg':         ('hero-slide-p04.webp',         'webp', 80),
    'hero-slide-p31.jpg':         ('hero-slide-p31.webp',         'webp', 80),
    'hero-original.jpg':          ('hero-original.webp',          'webp', 80),
    'hero-qingqianliu-product.jpg':('hero-qingqianliu-product.webp','webp', 80),
    'p13_01.jpeg':                ('p13_01.webp',                 'webp', 80),
    'p30_03.jpeg':                ('p30_03.webp',                 'webp', 80),
    'expert-liusuchun.jpg':       ('expert-liusuchun.webp',       'webp', 80),
    'p25_01.jpeg':                ('p25_01.webp',                 'webp', 80),
    'p23_03.jpeg':                ('p23_03.webp',                 'webp', 80),
}

total_before = 0
total_after = 0

for src_name, (dst_name, fmt, quality) in targets.items():
    src_path = os.path.join(ASSETS, src_name)
    dst_path = os.path.join(ASSETS, dst_name)
    if not os.path.exists(src_path):
        print(f"[SKIP] Not found: {src_name}")
        continue
    size_before = os.path.getsize(src_path)
    total_before += size_before
    try:
        img = Image.open(src_path)
        w, h = img.size
        max_dim = 1920
        if w > max_dim or h > max_dim:
            ratio = min(max_dim / w, max_dim / h)
            new_w, new_h = int(w * ratio), int(h * ratio)
            img = img.resize((new_w, new_h), Image.LANCZOS)
            print(f"  -> Resize: {w}x{h} -> {new_w}x{new_h}")
        if img.mode in ('RGBA', 'LA', 'P'):
            if img.mode == 'RGBA' and src_name.endswith('.png'):
                img.save(dst_path, 'WEBP', quality=quality, lossless=False)
            else:
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    rgb_img.paste(img, mask=img.split()[3])
                else:
                    rgb_img.paste(img)
                rgb_img.save(dst_path, 'WEBP', quality=quality)
        else:
            img.save(dst_path, 'WEBP', quality=quality)
        size_after = os.path.getsize(dst_path)
        total_after += size_after
        reduction = (1 - size_after / size_before) * 100
        print(f"[OK] {src_name} -> {dst_name}  {size_before/1024:.0f}KB -> {size_after/1024:.0f}KB  (-{reduction:.0f}%)")
    except Exception as e:
        print(f"[ERR] {src_name}: {e}")

print(f"\nTotal: {total_before/1024:.0f}KB -> {total_after/1024:.0f}KB  (-{round((1-total_after/total_before)*100)}%)")
