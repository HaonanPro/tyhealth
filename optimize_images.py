"""Optimize images: large PNG to WebP + compress large JPEG"""
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

ASSETS = os.path.dirname(os.path.abspath(__file__)) + '/assets'

targets = {
    'AKK.png':                ('AKK.webp',                'webp', 82),
    'page_06.png':            ('page_06.webp',            'webp', 82),
    'page_30.png':            ('page_30.webp',            'webp', 82),
    'page_31.png':            ('page_31.webp',            'webp', 82),
    'p04_03.jpeg':            ('p04_03.webp',             'webp', 80),
    'p31_03.jpeg':            ('p31_03.webp',             'webp', 80),
    'p30_04.jpeg':            ('p30_04.webp',             'webp', 80),
    'expert-zhangyousheng.jpg':('expert-zhangyousheng.webp','webp', 78),
    'p18_03.jpeg':            ('p18_03.webp',             'webp', 80),
    'p09_01.jpeg':            ('p09_01.webp',             'webp', 80),
    'p12_01.jpeg':            ('p12_01.webp',             'webp', 80),
    'p18_04.jpeg':            ('p18_04.webp',             'webp', 80),
    'p08_01.jpeg':            ('p08_01.webp',             'webp', 80),
}

print("=" * 60)
print("Image Optimizer")
print("=" * 60)

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

        if fmt == 'webp':
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

        before_str = f"{size_before/1024:.0f}KB"
        after_str = f"{size_after/1024:.0f}KB"
        print(f"[OK] {src_name} -> {dst_name}")
        print(f"     {before_str} -> {after_str}  (-{reduction:.0f}%)")

    except Exception as e:
        print(f"[ERR] {src_name}: {e}")

print("=" * 60)
print(f"Total: {total_before/1024:.0f}KB -> {total_after/1024:.0f}KB")
print(f"Saved: {(total_before-total_after)/1024:.0f}KB ({round((1-total_after/total_before)*100)}%)")
print("=" * 60)
