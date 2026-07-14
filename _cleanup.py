# -*- coding: utf-8 -*-
from pathlib import Path

root = Path(__file__).resolve().parent
for p in (root / "products").glob("*.html"):
    t = p.read_text(encoding="utf-8")
    t2 = t.replace('class="" ', "")
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
        print("cleaned", p.name)

robots = root / "robots.txt"
if not robots.exists():
    robots.write_text(
        "User-agent: *\nAllow: /\nSitemap: https://www.tyhealthtech.com/sitemap.xml\n",
        encoding="utf-8",
    )
    print("wrote robots.txt")
else:
    print("robots exists:", robots.read_text(encoding="utf-8")[:200])
