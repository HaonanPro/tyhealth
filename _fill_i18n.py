# -*- coding: utf-8 -*-
from pathlib import Path
import re
import json
import html as html_lib

products = Path(__file__).resolve().parent / "products"
for p in products.glob("*.html"):
    text = p.read_text(encoding="utf-8")
    m = re.search(r"window\.PAGE_TRANSLATIONS = (\{.*?\});\s*</script>", text, re.S)
    if not m:
        print("no i18n", p.name)
        continue
    data = json.loads(m.group(1))
    zh = data["zh"]

    def fill(match):
        key = match.group(1)
        val = zh.get(key, "")
        return f'data-i18n="{key}">{html_lib.escape(val)}'

    # empty content between tags
    new_html = re.sub(r'data-i18n="([^"]+)">\s*<', lambda m: fill(m) + "<", text)
    new_html = re.sub(r'data-i18n="([^"]+)"></', lambda m: fill(m) + "</", new_html)
    p.write_text(new_html, encoding="utf-8")
    print("filled", p.name)
