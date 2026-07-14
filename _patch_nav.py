# -*- coding: utf-8 -*-
"""Add product dropdown to product detail page navbars."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent / "products"

OLD = """    <nav class="nav">
      <a href="../index.html#about" data-i18n="pp.nav.about">企业介绍</a>
      <a href="../index.html#products" data-i18n="pp.nav.products">产品矩阵</a>
      <a href="../index.html#platform" data-i18n="pp.nav.platform">技术平台</a>
      <a href="#contact" data-i18n="pp.nav.contact">商务合作</a>
    </nav>"""

NEW = """    <nav class="nav">
      <a href="../index.html#about" data-i18n="pp.nav.about">企业介绍</a>
      <div class="nav-item has-dropdown">
        <a href="../index.html#products" data-i18n="pp.nav.products" class="nav-parent" aria-haspopup="true">产品矩阵</a>
        <div class="nav-dropdown" role="menu">
          <a href="akk.html" role="menuitem" data-i18n="nav.p.akk">AKM Lab-01 AKK 菌</a>
          <a href="tengcha.html" role="menuitem" data-i18n="nav.p.tengcha">藤茶提取物</a>
          <a href="enzyme.html" role="menuitem" data-i18n="nav.p.enzyme">高性能酶开发</a>
          <a href="wujitai.html" role="menuitem" data-i18n="nav.p.wujitai">乌鸡肽</a>
          <a href="qingqianliu.html" role="menuitem" data-i18n="nav.p.qingqianliu">青钱柳叶多酚</a>
          <a href="jinhuahongcha.html" role="menuitem" data-i18n="nav.p.jinhua">金花黑茶提取物</a>
        </div>
      </div>
      <a href="../index.html#platform" data-i18n="pp.nav.platform">技术平台</a>
      <a href="#contact" data-i18n="pp.nav.contact">商务合作</a>
    </nav>"""

for p in ROOT.glob("*.html"):
    t = p.read_text(encoding="utf-8")
    if "has-dropdown" in t:
        print("skip", p.name)
        continue
    if OLD not in t:
        print("pattern miss", p.name)
        continue
    t = t.replace(OLD, NEW)
    t = t.replace("styles.css?v=20260714", "styles.css?v=20260714b")
    t = t.replace("script.js?v=20260714", "script.js?v=20260714b")
    p.write_text(t, encoding="utf-8")
    print("patched", p.name)
