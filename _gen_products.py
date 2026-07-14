# -*- coding: utf-8 -*-
"""Generate product detail pages for tianyi-tech-green."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "products"
OUT.mkdir(exist_ok=True)

# Shared product list for related links
PRODUCTS = [
    ("akk", "AKM Lab-01 AKK 菌", "AKM Lab-01 AKK", "assets/AKK.webp"),
    ("tengcha", "藤茶提取物", "Vine Tea Extract", "assets/hero-tengcha-product.webp"),
    ("enzyme", "高性能酶开发", "High-Performance Enzyme", "assets/p04_03.webp"),
    ("wujitai", "乌鸡肽", "Black-Bone Chicken Peptide", "assets/hero-wujitai.webp"),
    ("qingqianliu", "青钱柳叶多酚", "Cyclocarya Polyphenols", "assets/p31_03.webp"),
    ("jinhuahongcha", "金花黑茶提取物", "Golden Dark Tea Extract", "assets/p13_01.webp"),
]

COMMON_PAGE_KEYS_ZH = {
    "pp.home": "首页",
    "pp.products": "产品矩阵",
    "pp.cta": "商务合作",
    "pp.cta.back": "返回产品矩阵",
    "pp.related": "相关产品",
    "pp.disclaimer": "研究与临床数据仅供研发与商务参考，不构成产品功效承诺或医疗建议。具体规格、法规与应用方案请以商务对接确认为准。",
    "pp.nav.about": "企业介绍",
    "pp.nav.products": "产品矩阵",
    "pp.nav.platform": "技术平台",
    "pp.nav.contact": "商务合作",
    "pp.metrics": "关键指标",
    "pp.science": "科学背景",
    "pp.mechanism": "核心成分与机制",
    "pp.benefits": "功效与证据",
    "pp.process": "工艺与规格",
    "pp.apps": "应用与复配",
    "pp.proof": "资质与背书",
    "pp.cases": "案例与数据",
    "pp.pain": "产业痛点",
    "pp.platform": "技术平台",
}

COMMON_PAGE_KEYS_EN = {
    "pp.home": "Home",
    "pp.products": "Products",
    "pp.cta": "Contact Sales",
    "pp.cta.back": "Back to Products",
    "pp.related": "Related Products",
    "pp.disclaimer": "Research and clinical data are for R&D and B2B reference only, and do not constitute efficacy claims or medical advice. Final specifications, regulatory status, and applications are subject to commercial confirmation.",
    "pp.nav.about": "About",
    "pp.nav.products": "Products",
    "pp.nav.platform": "Platform",
    "pp.nav.contact": "Contact",
    "pp.metrics": "Key Metrics",
    "pp.science": "Scientific Background",
    "pp.mechanism": "Actives & Mechanism",
    "pp.benefits": "Benefits & Evidence",
    "pp.process": "Process & Specs",
    "pp.apps": "Applications",
    "pp.proof": "Credentials",
    "pp.cases": "Cases & Data",
    "pp.pain": "Industry Pain Points",
    "pp.platform": "Technology Platform",
}

# Product definitions: content blocks
# metrics: list of {num, label_zh, label_en}
# sections with structured content

def page_shell(slug, title_zh, title_en, desc_zh, desc_en, image, tag_zh, tag_en, lead_zh, lead_en, body_html, page_i18n_zh, page_i18n_en):
    related = []
    for s, nz, ne, img in PRODUCTS:
        if s == slug:
            continue
        related.append(f'''
        <a class="related-card" href="{s}.html">
          <img src="../{img}?v=20260714" alt="{nz}" loading="lazy" width="320" height="200">
          <h3 data-i18n="rel.{s}">{nz}</h3>
        </a>''')
    related_html = "\n".join(related)

    # related product names in i18n
    for s, nz, ne, _ in PRODUCTS:
        page_i18n_zh[f"rel.{s}"] = nz
        page_i18n_en[f"rel.{s}"] = ne

    # merge common
    zh = {**COMMON_PAGE_KEYS_ZH, **page_i18n_zh}
    en = {**COMMON_PAGE_KEYS_EN, **page_i18n_en}
    zh["p.title"] = title_zh
    en["p.title"] = title_en
    zh["p.tag"] = tag_zh
    en["p.tag"] = tag_en
    zh["p.lead"] = lead_zh
    en["p.lead"] = lead_en
    zh["p.meta"] = desc_zh
    en["p.meta"] = desc_en

    i18n_json = json.dumps({"zh": zh, "en": en}, ensure_ascii=False, indent=2)

    contain = " contain-image" if slug == "enzyme" else ""

    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title data-i18n="doc.title">{title_zh} - 天颐健康科技</title>
  <meta name="description" data-i18n-content="doc.desc" content="{desc_zh}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://www.tyhealthtech.com/products/{slug}.html">
  <meta property="og:title" content="{title_zh} - 天颐健康科技">
  <meta property="og:description" content="{desc_zh}">
  <meta property="og:url" content="https://www.tyhealthtech.com/products/{slug}.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="天颐健康科技">
  <link rel="icon" type="image/x-icon" href="/favicon.ico?v=20260531">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=DM+Sans:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css?v=20260714">
</head>
<body data-lang="zh" class="product-page">
  <header class="site-header">
    <a class="brand" href="../index.html" aria-label="天颐健康科技">
      <img class="brand-logo" src="../assets/tianyi-logo-full.png?v=20260526" alt="天颐健康科技 Logo">
      <span class="brand-name" data-i18n="brand.name">天颐健康科技</span>
    </a>
    <nav class="nav">
      <a href="../index.html#about" data-i18n="pp.nav.about">企业介绍</a>
      <a href="../index.html#products" data-i18n="pp.nav.products">产品矩阵</a>
      <a href="../index.html#platform" data-i18n="pp.nav.platform">技术平台</a>
      <a href="#contact" data-i18n="pp.nav.contact">商务合作</a>
    </nav>
    <div class="header-actions">
      <button class="lang-toggle" type="button" aria-label="Switch language" data-lang-toggle>EN</button>
    </div>
  </header>

  <main>
    <section class="pp-hero">
      <div class="pp-hero-copy">
        <nav class="breadcrumb" aria-label="breadcrumb">
          <a href="../index.html" data-i18n="pp.home">首页</a>
          <span>/</span>
          <a href="../index.html#products" data-i18n="pp.products">产品矩阵</a>
          <span>/</span>
          <span data-i18n="p.title">{title_zh}</span>
        </nav>
        <p class="tag" data-i18n="p.tag">{tag_zh}</p>
        <h1 data-i18n="p.title">{title_zh}</h1>
        <p class="lead" data-i18n="p.lead">{lead_zh}</p>
        <div class="hero-actions">
          <a class="primary-btn" href="#contact" data-i18n="pp.cta">商务合作</a>
          <a class="ghost-btn" href="../index.html#products" data-i18n="pp.cta.back">返回产品矩阵</a>
        </div>
      </div>
      <div class="pp-hero-media">
        <img class="{contain.strip()}" src="../{image}?v=20260714" alt="{title_zh}" width="720" height="480" fetchpriority="high">
      </div>
    </section>

{body_html}

    <section class="pp-related">
      <div class="section-head">
        <div>
          <p class="section-kicker">More</p>
          <h2 data-i18n="pp.related">相关产品</h2>
        </div>
      </div>
      <div class="related-grid">
{related_html}
      </div>
    </section>

    <section class="pp-disclaimer">
      <p data-i18n="pp.disclaimer">{COMMON_PAGE_KEYS_ZH["pp.disclaimer"]}</p>
    </section>
  </main>

  <footer class="site-footer" id="contact">
    <div class="footer-inner">
      <div class="footer-brand">
        <img class="footer-logo" src="../assets/tianyi-logo-full.png?v=20260526" alt="天颐健康科技">
        <p class="footer-tagline" data-i18n="footer.tagline">科技功能食品与生物制造解决方案平台</p>
        <p class="footer-desc" data-i18n="footer.desc">以药食同源功能原料为根基，融合高性能酶开发、微生态技术与应用验证能力，助力健康产品与生物制造项目落地。</p>
      </div>
      <div class="footer-contact">
        <h3 data-i18n="footer.title">商务合作</h3>
        <div class="contact-list">
          <div class="contact-item">
            <span class="contact-role" data-i18n="footer.role1">国内负责人</span>
            <span class="contact-name" data-i18n="footer.name1">王先生</span>
            <a class="contact-phone" href="tel:18665617521">186 6561 7521</a>
          </div>
          <div class="contact-item">
            <span class="contact-role" data-i18n="footer.role2">国外负责人</span>
            <span class="contact-name" data-i18n="footer.name2">胡先生</span>
            <a class="contact-phone" href="tel:13794376845">137 9437 6845</a>
          </div>
          <div class="contact-item contact-item--landline">
            <span class="contact-role" data-i18n="footer.role3">公司总机</span>
            <a class="contact-phone" href="tel:+862038828529" data-i18n="footer.name3">020-38828529</a>
          </div>
          <div class="contact-item contact-item--address">
            <span class="contact-role" data-i18n="footer.address">地址</span>
            <span class="contact-address">广东省广州市海珠区新港东路1166号<br>环汇商业广场-南塔6楼</span>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p data-i18n="footer.copyright">© 2026 广州天颐健康科技有限公司. 保留所有权利.</p>
    </div>
  </footer>

  <script>
    window.PAGE_TRANSLATIONS = {i18n_json};
  </script>
  <script src="../script.js?v=20260714"></script>
</body>
</html>
'''


def metrics_html(items):
    # items: (num, key_label)
    cards = []
    for num, key in items:
        cards.append(f'''        <article class="metric-card">
          <strong>{num}</strong>
          <span data-i18n="{key}"></span>
        </article>''')
    return f'''    <section class="pp-metrics">
      <div class="section-head"><div><p class="section-kicker">Metrics</p><h2 data-i18n="pp.metrics">关键指标</h2></div></div>
      <div class="metric-grid">
{chr(10).join(cards)}
      </div>
    </section>
'''


def text_section(kicker, title_key, body_key, extra=""):
    return f'''    <section class="pp-section">
      <div class="section-head"><div><p class="section-kicker">{kicker}</p><h2 data-i18n="{title_key}"></h2></div></div>
      <p class="pp-prose" data-i18n="{body_key}"></p>
      {extra}
    </section>
'''


def cards_section(kicker, title_key, card_keys):
    # card_keys: list of (title_key, text_key)
    arts = []
    for ti, te in card_keys:
        arts.append(f'''        <article>
          <h3 data-i18n="{ti}"></h3>
          <p data-i18n="{te}"></p>
        </article>''')
    return f'''    <section class="pp-section">
      <div class="section-head"><div><p class="section-kicker">{kicker}</p><h2 data-i18n="{title_key}"></h2></div></div>
      <div class="pp-card-grid">
{chr(10).join(arts)}
      </div>
    </section>
'''


def list_section(kicker, title_key, items_keys):
    lis = "\n".join(f'          <li data-i18n="{k}"></li>' for k in items_keys)
    return f'''    <section class="pp-section">
      <div class="section-head"><div><p class="section-kicker">{kicker}</p><h2 data-i18n="{title_key}"></h2></div></div>
      <ul class="pp-list">
{lis}
      </ul>
    </section>
'''


def table_section(kicker, title_key, headers, rows):
    # headers: list of i18n keys or plain
    # rows: list of list of (text or data-i18n key with prefix i:)
    ths = "".join(f'<th data-i18n="{h}"></th>' if h.startswith("t.") else f'<th>{h}</th>' for h in headers)
    trs = []
    for row in rows:
        tds = []
        for cell in row:
            if isinstance(cell, str) and cell.startswith("i:"):
                tds.append(f'<td data-i18n="{cell[2:]}"></td>')
            else:
                tds.append(f'<td>{cell}</td>')
        trs.append("<tr>" + "".join(tds) + "</tr>")
    return f'''    <section class="pp-section">
      <div class="section-head"><div><p class="section-kicker">{kicker}</p><h2 data-i18n="{title_key}"></h2></div></div>
      <div class="pp-table-wrap">
        <table class="pp-table">
          <thead><tr>{ths}</tr></thead>
          <tbody>
            {"".join(trs)}
          </tbody>
        </table>
      </div>
    </section>
'''


# ─────────────────── AKK ───────────────────
def build_akk():
    zh = {
        "doc.title": "AKM Lab-01 AKK 菌 - 天颐健康科技",
        "doc.desc": "AKM Lab-01 嗜黏蛋白阿克曼菌（AKK）：新一代益生菌标杆原料，覆盖减重、糖脂代谢、睡眠与免疫方向，含 Amuc_1100 / P9 / Amuc_1409 核心蛋白与临床备案支持。",
        "m1": "海内外专利布局",
        "m2": "规格量级（TFU 级）",
        "m3": "已备案临床方向",
        "m4": "核心功效蛋白检测",
        "s1.title": "科学背景",
        "s1.body": "嗜黏蛋白阿克曼菌（Akkermansia muciniphila，AKK）是新一代益生菌（NGPs）代表。2004 年被发现后，相关研究快速增长；2019 年 Nature Medicine 等研究推动其产业化。EFSA 等地区已对巴氏灭活 AKK 形成安全评估路径。天颐联合慕恩生物，以 AKM Lab-01 菌株服务功能食品与健康管理产品开发。",
        "s2.title": "核心成分与机制",
        "c1.t": "Amuc_1100",
        "c1.d": "核心膜蛋白，与肠道屏障、代谢与免疫调节密切相关，是国际研究共识中的关键功效物质之一。",
        "c2.t": "P9（Amuc_1631）",
        "c2.d": "代谢调节相关蛋白，可参与 GLP-1 通路相关调控逻辑，面向糖脂代谢与体重管理配方。",
        "c3.t": "Amuc_1409",
        "c3.d": "双重修复方向蛋白：支持免疫稳态相关调节，并与肠道干细胞/屏障修复研究相关。",
        "c4.t": "巴氏灭活优势",
        "c4.d": "多项研究与内部验证显示，巴氏灭活形式在部分代谢指标与稳定性上具备产业化优势，更适配食品与补充剂供应链。",
        "s3.title": "功效方向与证据",
        "b1.t": "减重与糖脂代谢",
        "b1.d": "临床前数据显示对体重、血糖 AUC、胆固醇与内脏脂肪等指标的改善潜力；已布局减重相关临床备案 NCT07331974。",
        "b2.t": "抗高血脂方向临床",
        "b2.d": "抗高血脂症相关临床试验备案 NCT06974266，以高等级证据路径服务代谢健康产品。",
        "b3.t": "睡眠与情绪",
        "b3.d": "通过肠-脑轴相关机制研究，AKM Lab-01 在降低觉醒时间与活动水平等指标上展示促眠/镇静相关潜力（研究数据）。",
        "b4.t": "肠道屏障与免疫",
        "b4.d": "通过 SCFA、Amuc 蛋白等路径支持黏液层与屏障功能，并参与免疫平衡调节相关讨论。",
        "s4.title": "工艺、规格与稳定性",
        "s4.body": "提供高纯度灭活冻干粉等规格，支持万亿级 TFU 量级原料开发；冻干粉与液体制剂均有稳定性考察数据。原料纯度可达 99.99% 以上量级表述（以批次 COA 为准）。国际保藏号 DSM 35743 等提供可追溯性支持。",
        "s5.title": "应用与复配建议",
        "a1": "剂型：粉剂、胶囊、片剂、软糖、液体等",
        "a2": "场景：体重管理、糖脂代谢、睡眠脑健康、免疫协同",
        "a3": "复配：可与植提物、维矿、胶原、鱼油/磷虾油等协同",
        "a4": "协同案例方向：AKK + 金花黑茶提取物用于代谢与体重管理",
        "s6.title": "资质与背书",
        "p1": "慕恩生物合作菌株 AKM Lab-01，多国/地区专利与保藏编号支持",
        "p2": "FSSC22000、ISO、FDA 注册、HALAL 等生产与体系认证（以合作方资质为准）",
        "p3": "美国 Self-GRAS 等安全性路径（以最新法规文件为准）",
        "p4": "核心蛋白检测方法专利与工艺专利矩阵",
    }
    en = {
        "doc.title": "AKM Lab-01 AKK - Tianyi Health Tech",
        "doc.desc": "AKM Lab-01 Akkermansia muciniphila (AKK): next-gen probiotic ingredient for weight, metabolic, sleep and immune formulations, with key proteins Amuc_1100 / P9 / Amuc_1409 and clinical registrations.",
        "m1": "Patent portfolio",
        "m2": "TFU-scale potency",
        "m3": "Clinical tracks filed",
        "m4": "Core protein assays",
        "s1.title": "Scientific Background",
        "s1.body": "Akkermansia muciniphila (AKK) is a flagship next-generation probiotic (NGP). Since its discovery in 2004 and high-impact publications such as Nature Medicine (2019), industrial interest has accelerated. Pasteurized AKK has clear safety assessment pathways in regions such as the EU. Tianyi partners with Moon (慕恩) Bio to bring strain AKM Lab-01 to functional food and wellness brands.",
        "s2.title": "Actives & Mechanism",
        "c1.t": "Amuc_1100",
        "c1.d": "A key outer-membrane protein linked to barrier, metabolic and immune pathways — a widely cited functional marker of AKK.",
        "c2.t": "P9 (Amuc_1631)",
        "c2.d": "Metabolism-related protein associated with GLP-1 pathway discussion for glucose-lipid and weight management formulas.",
        "c3.t": "Amuc_1409",
        "c3.d": "Repair-oriented protein discussed for immune homeostasis and intestinal stem-cell / barrier support.",
        "c4.t": "Pasteurized format",
        "c4.d": "Pasteurized AKK can offer application and stability advantages for food/supplement supply chains versus live formats in certain use cases.",
        "s3.title": "Benefits & Evidence",
        "b1.t": "Weight & metabolic health",
        "b1.d": "Preclinical signals on body weight, glucose AUC, cholesterol and visceral fat; weight-management clinical registration NCT07331974.",
        "b2.t": "Dyslipidemia clinical track",
        "b2.d": "Anti-hyperlipidemia clinical registration NCT06974266 to support higher-level evidence for metabolic products.",
        "b3.t": "Sleep & mood",
        "b3.d": "Gut–brain axis research shows potential to reduce wake time and activity levels (research data, not a medical claim).",
        "b4.t": "Barrier & immunity",
        "b4.d": "SCFA and Amuc proteins support mucus/barrier discussion and immune balance narratives for formulation design.",
        "s4.title": "Process, Specs & Stability",
        "s4.body": "High-purity pasteurized freeze-dried powder and other formats at trillion-level TFU scale (batch COA prevails). Stability data available for powder and liquid systems. Traceability supported by deposit numbers such as DSM 35743.",
        "s5.title": "Applications",
        "a1": "Formats: powder, capsules, tablets, gummies, liquids",
        "a2": "Use cases: weight, metabolic balance, sleep/brain, immune synergy",
        "a3": "Synergies: botanicals, vitamins/minerals, collagen, fish/krill oil",
        "a4": "Example stack: AKK + golden dark tea extract for metabolic/weight programs",
        "s6.title": "Credentials",
        "p1": "Moon Bio strain AKM Lab-01 with multi-region patents and culture deposits",
        "p2": "Manufacturing systems such as FSSC22000 / ISO / FDA registration / HALAL (partner certificates)",
        "p3": "Self-GRAS and other safety pathways (subject to current dossiers)",
        "p4": "Patent matrix covering protein assays and process innovations",
    }
    body = metrics_html([("18+", "m1"), ("10¹²", "m2"), ("2", "m3"), ("3", "m4")])
    body += text_section("Science", "s1.title", "s1.body")
    body += cards_section("Mechanism", "s2.title", [("c1.t", "c1.d"), ("c2.t", "c2.d"), ("c3.t", "c3.d"), ("c4.t", "c4.d")])
    body += cards_section("Evidence", "s3.title", [("b1.t", "b1.d"), ("b2.t", "b2.d"), ("b3.t", "b3.d"), ("b4.t", "b4.d")])
    body += text_section("Quality", "s4.title", "s4.body")
    body += list_section("Applications", "s5.title", ["a1", "a2", "a3", "a4"])
    body += list_section("Proof", "s6.title", ["p1", "p2", "p3", "p4"])
    return page_shell(
        "akk", "AKM Lab-01 AKK 菌", "AKM Lab-01 AKK",
        zh["doc.desc"], en["doc.desc"],
        "assets/AKK.webp", "二代益生菌标杆", "Next-Gen Probiotic Benchmark",
        "来源于慕恩生物的嗜黏蛋白阿克曼菌 AKM Lab-01，聚焦代谢、睡眠与免疫，以高含量核心蛋白与临床备案路径服务全球健康品牌。",
        "Moon Bio strain AKM Lab-01 for metabolic, sleep and immune formulas — high functional proteins with clinical registration pathways.",
        body, zh, en,
    )


# ─────────────────── Enzyme ───────────────────
def build_enzyme():
    zh = {
        "doc.title": "高性能酶开发 - 天颐健康科技",
        "doc.desc": "天颐联合智演生合，以 SMALT+AI 定向进化加速平台，提供从候选酶筛选、分子优化、表达制备到应用验证的一站式高性能酶开发服务。",
        "m1": "优化周期可缩短至",
        "m2": "高通量筛选量级",
        "m3": "可公开案例方向",
        "m4": "核心场景覆盖",
        "s1.title": "平台定位",
        "s1.body": "客户需要的往往不是单一酶产品，而是在真实配方、工艺与成本约束下可验证的应用结果。天颐联合智演生合（Avolution），基于 SMALT 高频靶向突变系统与 AI 模型闭环，构建「进化加速器」SSA 智能合成生物平台，解决突变低效、筛选慢、干湿实验脱节等产业化痛点。",
        "s2.title": "产业痛点与方案",
        "x1.t": "突变低效",
        "x1.d": "传统体外单点突变深度有限、区域不可精准定制。→ 体内多蛋白高频靶向突变，功能探索更深。",
        "x2.t": "筛选缓慢",
        "x2.d": "通量低、优化周期常需 4–6 个月、有效数据不足。→ 液滴微流控/单细胞等筛选，通量可达 ≥10⁹，周期可压至 1–2 月。",
        "x3.t": "AI 脱节",
        "x3.d": "缺乏高质量基因型—表型数据闭环。→ AI 多性能协同优化与持续自学习，提升命中率。",
        "s3.title": "技术闭环",
        "s3.body": "平台耦合 SMALT 高频靶向突变、高通量筛选（单细胞拉曼、液滴微流控等）与人工智能模型，产出表型与基因型高度一致的数据，驱动干湿实验高速迭代。知识产权覆盖 SMALT 系统与 AI 蛋白质设计优化方法；背景 IP 来自中山大学独家商业化授权路径。",
        "s4.title": "可量化案例",
        "c1.t": "PET 塑料降解酶",
        "c1.d": "两轮优化后酶活较成熟工业酶提升约 3 倍，超过既有商用酶水平，持续优化稳定性与工艺适配。",
        "c2.t": "PlHpaB（圣草酚路径）",
        "c2.d": "模型预测突变体命中率约 77%，单轮即可获得活性提升约 5 倍的高效突变体。",
        "c3.t": "甲基转移酶",
        "c3.d": "三轮迭代 34 个突变，29 个活性提升；相对活性约 4.4 倍，kcat/Km 约提升 7 倍。",
        "c4.t": "甲酸脱氢酶 FDH",
        "c4.d": "两轮推荐各 10 个突变体，最高活性提升约 3 倍，服务辅酶再生与绿色催化。",
        "s5.title": "应用场景",
        "a1": "食品：加工用酶、功能蛋白改造、发酵菌株优化、安全与保鲜",
        "a2": "工业：工业酶工程、生物燃料与绿色能源、生物材料与化学品、环境与塑料循环",
        "a3": "医药：纳米抗体与生物药、药物中间体绿色合成、细胞治疗模块优化",
        "a4": "交付：候选筛选 → 分子优化 → 表达制备 → 制剂与应用验证",
        "s6.title": "团队与合作",
        "s6.body": "智演生合团队汇聚束文圣教授、杨跃东教授、刘建忠教授等合成生物学与 AI 交叉力量，并与美格基因等产业化伙伴协同。天颐以应用场景与客户网络对接酶工程能力，服务食品、健康与工业客户的真实痛点。",
    }
    en = {
        "doc.title": "High-Performance Enzyme Development - Tianyi Health Tech",
        "doc.desc": "Tianyi partners with Avolution (智演生合) on the SMALT+AI directed evolution platform for end-to-end enzyme screening, optimization, expression and application validation.",
        "m1": "Optimization cycle",
        "m2": "Screening throughput",
        "m3": "Public case tracks",
        "m4": "Core industries",
        "s1.title": "Platform Positioning",
        "s1.body": "Clients need validated outcomes under real formulation, process and cost constraints—not just a catalog enzyme. With Avolution, Tianyi leverages SMALT targeted mutagenesis and AI closed loops (SSA evolutionary accelerator) to fix low mutation efficiency, slow screening and wet–dry disconnects.",
        "s2.title": "Pain Points & Solutions",
        "x1.t": "Inefficient mutation",
        "x1.d": "Classic in vitro single-site mutation is shallow. → In vivo multi-protein high-frequency targeted mutagenesis for deeper exploration.",
        "x2.t": "Slow screening",
        "x2.d": "Low throughput and 4–6 month cycles. → Microfluidics/single-cell screening at ≥10⁹ scale; cycles can compress to 1–2 months.",
        "x3.t": "AI disconnect",
        "x3.d": "Missing genotype–phenotype data loops. → Multi-objective AI optimization with continuous learning to raise hit rates.",
        "s3.title": "Closed-Loop Technology",
        "s3.body": "SMALT mutagenesis, high-throughput screening and AI models produce consistent genotype–phenotype data for rapid iteration. IP covers SMALT and AI protein design methods, with background IP under exclusive commercialization pathways from Sun Yat-sen University.",
        "s4.title": "Quantified Cases",
        "c1.t": "PETase",
        "c1.d": "After two rounds, activity ~3× mature industrial enzymes, surpassing certain commercial benchmarks; further stability work ongoing.",
        "c2.t": "PlHpaB (eriodictyol path)",
        "c2.d": "~77% hit rate on predicted mutants; ~5× activity gain in a single round.",
        "c3.t": "Methyltransferase",
        "c3.d": "34 mutants / 3 rounds; 29 improved; ~4.4× relative activity and ~7× kcat/Km.",
        "c4.t": "Formate dehydrogenase",
        "c4.d": "Two rounds of 10 mutants each; peak activity ~3× for cofactor regeneration and green catalysis.",
        "s5.title": "Applications",
        "a1": "Food: processing enzymes, protein engineering, fermentation strains, safety & preservation",
        "a2": "Industry: industrial enzymes, biofuels, biomaterials/chemicals, plastics recycling",
        "a3": "Pharma: nanobodies, green intermediate synthesis, cell-therapy modules",
        "a4": "Delivery: screen → optimize → express → formulate & validate",
        "s6.title": "Team & Partnership",
        "s6.body": "Avolution brings leading SYSU and AI talent (Profs. Shu, Yang, Liu et al.) with Magigene industrialization links. Tianyi connects real customer scenarios in food, health and industry to enzyme engineering capacity.",
    }
    body = metrics_html([("1–2 月", "m1"), ("≥10⁹", "m2"), ("4+", "m3"), ("食品/工业/医药", "m4")])
    # fix m4 en
    en["m4"] = "Food / industry / pharma"
    body += text_section("Positioning", "s1.title", "s1.body")
    body += cards_section("Pain Points", "s2.title", [("x1.t", "x1.d"), ("x2.t", "x2.d"), ("x3.t", "x3.d")])
    body += text_section("Platform", "s3.title", "s3.body")
    body += cards_section("Cases", "s4.title", [("c1.t", "c1.d"), ("c2.t", "c2.d"), ("c3.t", "c3.d"), ("c4.t", "c4.d")])
    body += list_section("Applications", "s5.title", ["a1", "a2", "a3", "a4"])
    body += text_section("Team", "s6.title", "s6.body")
    return page_shell(
        "enzyme", "高性能酶开发", "High-Performance Enzyme Development",
        zh["doc.desc"], en["doc.desc"],
        "assets/p04_03.webp", "SMALT + AI 进化加速器", "SMALT + AI Evolution Accelerator",
        "联合智演生合，把酶开发从「碰运气」变成可计算、可迭代、可放大的工程化服务。",
        "With Avolution, enzyme development becomes computable, iterable and scalable engineering—not trial-and-error.",
        body, zh, en,
    )


# ─────────────────── Tengcha ───────────────────
def build_tengcha():
    zh = {
        "doc.title": "藤茶提取物 - 天颐健康科技",
        "doc.desc": "显齿蛇葡萄叶（藤茶）提取物，核心成分二氢杨梅素 DMY，高黄酮含量，面向护肝解酒、抗氧化与尿酸管理等功能食品开发。",
        "m1": "黄酮含量量级",
        "m2": "核心活性",
        "m3": "原料资质方向",
        "m4": "研究积淀",
        "s1.title": "科学背景",
        "s1.body": "藤茶来源于显齿蛇葡萄（Ampelopsis grossedentata）叶，被誉为「黄酮之王」。核心成分二氢杨梅素（DMY）在护肝、解酒、抗氧化与代谢相关方向具备扎实研究基础。天颐藤茶首席科学家张友胜博士长期深耕藤茶现代化研究，为原料开发提供关键技术支撑。",
        "s2.title": "核心成分与机制",
        "c1.t": "二氢杨梅素 DMY",
        "c1.d": "二氢黄酮醇类代表成分，支持抗氧化与肝脏保护相关机制研究。",
        "c2.t": "总黄酮复合体系",
        "c2.d": "多酚黄酮协同，服务口服美容、抗炎舒适与代谢配方设计。",
        "c3.t": "酒精代谢相关",
        "c3.d": "研究提示可增强 ADH/ALDH 活性逻辑，加速乙醇代谢讨论，适配应酬与护肝场景。",
        "c4.t": "尿酸与神经保护",
        "c4.d": "在尿酸管理与神经保护方向有研究探索，可与其他代谢原料协同。",
        "s3.title": "功效方向与证据",
        "b1.t": "护肝解酒",
        "b1.d": "功能食品与特膳开发中的经典方向，强调酒精代谢与氧化应激管理。",
        "b2.t": "抗氧化 / 口服美容",
        "b2.d": "高黄酮特征适合抗氧与美丽营养配方。",
        "b3.t": "药品路径参考（分栏）",
        "b3.d": "显齿蛇葡萄总黄酮含片曾完成口腔溃疡相关临床试验路径（药品逻辑与食品原料严格区分，仅作科研背景）。",
        "b4.t": "产区与品质",
        "b4.d": "精选湖南张家界及湘西永顺等核心产区原料，从源头控制品质。",
        "s4.title": "工艺与规格",
        "s4.body": "标准化提取与纯化路径，黄酮含量可达约 45% 量级（以规格书为准）；可提供不同 DMY/总黄酮规格以匹配终端成本与宣称策略。支持固体饮料、压片、胶囊等剂型。",
        "s5.title": "应用与复配",
        "a1": "解酒护肝固体饮料、口服液、压片糖果",
        "a2": "抗氧化/抗疲劳营养补充剂",
        "a3": "与金花黑茶、青钱柳等代谢原料复配",
        "a4": "出口方案示例：黑茶 + 藤茶（高 DMY）地域风味与代谢定位",
        "s6.title": "资质与背书",
        "p1": "新食品原料相关资质路径（以现行法规与批件为准）",
        "p2": "张友胜博士藤茶现代化研究与专著背书",
        "p3": "产区溯源与质量体系支持",
        "p4": "可提供检测报告与规格定制沟通",
    }
    en = {
        "doc.title": "Vine Tea Extract - Tianyi Health Tech",
        "doc.desc": "Ampelopsis grossedentata (vine tea) leaf extract rich in dihydromyricetin (DMY) for liver support, antioxidant and uric-acid management formulations.",
        "m1": "Flavonoid level",
        "m2": "Key active",
        "m3": "Novel food pathway",
        "m4": "Research depth",
        "s1.title": "Scientific Background",
        "s1.body": "Vine tea from Ampelopsis grossedentata leaves is known as a flavonoid powerhouse. Dihydromyricetin (DMY) underpins liver, alcohol-metabolism and antioxidant research. Chief scientist Dr. Zhang Yousheng provides deep modernization expertise for this ingredient line.",
        "s2.title": "Actives & Mechanism",
        "c1.t": "Dihydromyricetin (DMY)",
        "c1.d": "Signature dihydroflavonol linked to antioxidant and hepatoprotective research.",
        "c2.t": "Total flavonoid complex",
        "c2.d": "Multi-phenol synergy for beauty-from-within and comfort formulas.",
        "c3.t": "Alcohol metabolism",
        "c3.d": "Discussed for ADH/ALDH support narratives in social/liver-care products.",
        "c4.t": "Uric acid & neuro",
        "c4.d": "Exploratory directions for uric acid and neuroprotection stacks.",
        "s3.title": "Benefits & Evidence",
        "b1.t": "Liver & alcohol care",
        "b1.d": "A classic functional-food positioning around ethanol metabolism and oxidative stress.",
        "b2.t": "Antioxidant / beauty",
        "b2.d": "High-flavonoid profile for beauty nutrition and daily defense.",
        "b3.t": "Pharma reference (separate)",
        "b3.d": "Total-flavonoid lozenge clinical history exists in pharma context—kept strictly separate from food-ingredient claims.",
        "b4.t": "Origin quality",
        "b4.d": "Sourced from core Hunan origins such as Zhangjiajie and Yongshun.",
        "s4.title": "Process & Specs",
        "s4.body": "Standardized extraction/purification; flavonoid content around 45% class (COA prevails). Multiple DMY/total-flavonoid grades available for cost and claim strategies.",
        "s5.title": "Applications",
        "a1": "Liver-care RTD powders, liquids, compressed candies",
        "a2": "Antioxidant / anti-fatigue supplements",
        "a3": "Stacks with golden dark tea and Cyclocarya polyphenols",
        "a4": "Export concept: dark tea + high-DMY vine tea regional flavors",
        "s6.title": "Credentials",
        "p1": "Novel food-related pathways (subject to current regulation)",
        "p2": "Scientific leadership from Dr. Zhang Yousheng",
        "p3": "Origin traceability and quality systems",
        "p4": "COA and custom-spec discussions available",
    }
    body = metrics_html([("~45%", "m1"), ("DMY", "m2"), ("新食品原料", "m3"), ("20+ 年", "m4")])
    en["m3"] = "Novel food"
    # m4 number is bilingual via separate keys if regenerated carefully
    body += text_section("Science", "s1.title", "s1.body")
    body += cards_section("Mechanism", "s2.title", [("c1.t", "c1.d"), ("c2.t", "c2.d"), ("c3.t", "c3.d"), ("c4.t", "c4.d")])
    body += cards_section("Evidence", "s3.title", [("b1.t", "b1.d"), ("b2.t", "b2.d"), ("b3.t", "b3.d"), ("b4.t", "b4.d")])
    body += text_section("Quality", "s4.title", "s4.body")
    body += list_section("Applications", "s5.title", ["a1", "a2", "a3", "a4"])
    body += list_section("Proof", "s6.title", ["p1", "p2", "p3", "p4"])
    return page_shell(
        "tengcha", "藤茶提取物", "Vine Tea Extract",
        zh["doc.desc"], en["doc.desc"],
        "assets/hero-tengcha-product.webp", "黄酮之王", "King of Flavonoids",
        "显齿蛇葡萄叶来源，以二氢杨梅素 DMY 为核心，服务护肝解酒、抗氧化与代谢舒适类产品创新。",
        "DMY-rich Ampelopsis leaf extract for liver care, antioxidant and metabolic comfort innovation.",
        body, zh, en,
    )


# ─────────────────── Wujitai ───────────────────
def build_wujitai():
    zh = {
        "doc.title": "乌鸡肽 - 天颐健康科技",
        "doc.desc": "泰和乌鸡来源小分子活性肽，生物酶解工艺，面向滋补焕新、营养支持与口服美容类功能食品与营养补充剂。",
        "m1": "原料品种",
        "m2": "工艺路径",
        "m3": "形态",
        "m4": "应用方向",
        "s1.title": "产品起源",
        "s1.body": "乌鸡是中国传统滋补食材代表。天颐乌鸡肽以泰和乌鸡为原料，通过现代生物酶解将大分子蛋白转化为更易吸收的小分子活性肽，让传统滋补走向标准化、规格化与配方友好的工业原料。",
        "s2.title": "核心价值",
        "c1.t": "小分子肽",
        "c1.d": "酶解工艺控制肽段分布，提升溶解性与消化吸收友好度。",
        "c2.t": "全面营养基底",
        "c2.d": "保留乌鸡蛋白来源的氨基酸与肽营养特征，服务日常滋补与术后/运动营养讨论（按终端法规设计）。",
        "c3.t": "口服美容协同",
        "c3.d": "可与胶原、弹性蛋白肽、抗氧化植提等复配，构建「内服滋养」组合。",
        "c4.t": "配方友好",
        "c4.d": "适合粉剂、饮品、膏方现代化剂型与礼品滋补场景。",
        "s3.title": "功效与应用方向",
        "b1.t": "滋补焕新",
        "b1.d": "面向气虚疲劳、四季进补、女性调养等传统滋补现代化产品。",
        "b2.t": "营养支持",
        "b2.d": "作为优质蛋白肽原料，服务特医备选讨论、老年营养与运动恢复类产品设计。",
        "b3.t": "口服美容",
        "b3.d": "与美容营养赛道结合，强调由内而外的蛋白肽补充。",
        "b4.t": "证据说明",
        "b4.d": "详细人体数据与规格参数以产品规格书与第三方检测为准；欢迎索取完整资料包。",
        "s4.title": "工艺与规格",
        "s4.body": "生物酶解 → 分离纯化 → 干燥制粉的标准化路径，强调分子量可控、风味优化与重金属/微生物限量达标。具体肽含量、分子量分布、溶解性等指标可按客户应用定制沟通。",
        "s5.title": "应用建议",
        "a1": "滋补固体饮料、小分子肽饮",
        "a2": "膏滋现代化：浓缩液/粉剂",
        "a3": "女性/职场抗疲劳营养包",
        "a4": "与乌鸡传统食养 IP 联名礼盒原料",
        "s6.title": "背书方向",
        "p1": "道地乌鸡原料叙事 + 现代酶解科技",
        "p2": "可配套企业标准与检测报告",
        "p3": "适配国潮滋补与跨境食养表达",
        "p4": "商务侧提供样品与配方建议",
    }
    en = {
        "doc.title": "Black-Bone Chicken Peptide - Tianyi Health Tech",
        "doc.desc": "Taihe black-bone chicken peptides via enzymatic hydrolysis for nourishing, nutritional support and beauty-from-within products.",
        "m1": "Heritage breed",
        "m2": "Process",
        "m3": "Format",
        "m4": "Use cases",
        "s1.title": "Origin",
        "s1.body": "Black-bone chicken is a classic Chinese tonic food. Tianyi converts Taihe black-bone chicken protein into small bioactive peptides through modern enzymatic hydrolysis—standardized, formulatable and supply-chain ready.",
        "s2.title": "Core Value",
        "c1.t": "Small peptides",
        "c1.d": "Controlled hydrolysis for solubility and absorption-friendly peptide profiles.",
        "c2.t": "Nutrient base",
        "c2.d": "Amino acid/peptide nutrition from chicken protein for daily tonic concepts (design per local rules).",
        "c3.t": "Beauty synergy",
        "c3.d": "Stacks with collagen and antioxidant botanicals for beauty-from-within kits.",
        "c4.t": "Formulation-ready",
        "c4.d": "Works in powders, drinks and modernized tonic formats.",
        "s3.title": "Directions",
        "b1.t": "Nourishing renewal",
        "b1.d": "Modern tonic products for fatigue, seasonal care and women’s wellness narratives.",
        "b2.t": "Nutritional support",
        "b2.d": "Protein-peptide base for senior nutrition and recovery concepts.",
        "b3.t": "Oral beauty",
        "b3.d": "Beauty nutrition positioning with peptide supplementation stories.",
        "b4.t": "Evidence note",
        "b4.d": "Detailed human data and specs via COA/dossier on request.",
        "s4.title": "Process & Specs",
        "s4.body": "Enzymatic hydrolysis → separation → drying. Molecular-weight windows, flavor and safety limits per specification; custom grades available.",
        "s5.title": "Applications",
        "a1": "Tonic RTD powders and peptide drinks",
        "a2": "Modern paste/concentrate formats",
        "a3": "Women’s / workplace fatigue kits",
        "a4": "Heritage IP gift sets",
        "s6.title": "Credentials",
        "p1": "Heritage raw material + modern bio-process story",
        "p2": "Enterprise standards and test reports",
        "p3": "Fits China-chic tonic and cross-border wellness",
        "p4": "Samples and formula advice via sales",
    }
    body = metrics_html([("泰和乌鸡", "m1"), ("生物酶解", "m2"), ("肽粉", "m3"), ("滋补/美容", "m4")])
    en["m1"] = "Taihe chicken"
    en["m2"] = "Enzymatic"
    en["m3"] = "Peptide powder"
    en["m4"] = "Tonic / beauty"
    body += text_section("Origin", "s1.title", "s1.body")
    body += cards_section("Value", "s2.title", [("c1.t", "c1.d"), ("c2.t", "c2.d"), ("c3.t", "c3.d"), ("c4.t", "c4.d")])
    body += cards_section("Directions", "s3.title", [("b1.t", "b1.d"), ("b2.t", "b2.d"), ("b3.t", "b3.d"), ("b4.t", "b4.d")])
    body += text_section("Quality", "s4.title", "s4.body")
    body += list_section("Applications", "s5.title", ["a1", "a2", "a3", "a4"])
    body += list_section("Proof", "s6.title", ["p1", "p2", "p3", "p4"])
    return page_shell(
        "wujitai", "乌鸡肽", "Black-Bone Chicken Peptide",
        zh["doc.desc"], en["doc.desc"],
        "assets/hero-wujitai.webp", "滋补焕新", "Nourishing Renewal",
        "以泰和乌鸡为原料，生物酶解小分子肽，让传统滋补变成可规格化的现代营养原料。",
        "Enzymatically hydrolyzed Taihe black-bone chicken peptides—heritage tonic, modern specs.",
        body, zh, en,
    )


# ─────────────────── Qingqianliu ───────────────────
def build_qingqianliu():
    zh = {
        "doc.title": "青钱柳叶多酚 - 天颐健康科技",
        "doc.desc": "青钱柳叶多酚（植物胰岛素方向），服务血糖管理、血脂调节与代谢综合征相关功能食品开发，含人群研究与动物实验证据参考。",
        "m1": "多酚含量量级",
        "m2": "人群研究参考",
        "m3": "干预周期示例",
        "m4": "核心场景",
        "s1.title": "科学背景",
        "s1.body": "青钱柳（Cyclocarya paliurus）叶富含多糖、黄酮、三萜与多酚类成分，民间与现代研究均关注其代谢调节潜力，有「植物胰岛素」方向的科普表达。天颐青钱柳叶多酚面向三高调理与糖脂管理原料市场，可与金花黑茶等协同构建方案。",
        "s2.title": "核心成分与机制",
        "c1.t": "叶多酚复合",
        "c1.d": "多酚含量可达约 25% 量级（规格书为准），支持抗氧化与代谢酶调节相关讨论。",
        "c2.t": "糖代谢路径",
        "c2.d": "研究涉及改善胰岛素敏感性、调节肝糖原与糖异生相关通路（如 AMPK 等讨论）。",
        "c3.t": "脂代谢路径",
        "c3.d": "动物与人群研究提示对 TG、TC、LDL-c、HDL-c 等血脂谱的潜在改善。",
        "c4.t": "菌群与代谢物",
        "c4.d": "临床研究讨论其通过调节肠道菌群与代谢物改善代谢表型的可能性。",
        "s3.title": "功效与临床/人群证据",
        "b1.t": "84 天人群干预参考",
        "b1.d": "公开研究中，青钱柳叶提取物干预 84 天，受试者 HbA1c 可从约 7.9% 降至约 6.9%，与格列齐特组降幅无显著差异（研究数据，非产品宣称）。",
        "b2.t": "糖脂与菌群临床",
        "b2.d": "Open-label 与 RCT 研究观察 FBG、2hPBG、OGTT AUC 及 TG、HDL-c 等指标，并报告有益菌富集相关发现。",
        "b3.t": "痛风相关探索",
        "b3.d": "颗粒剂研究在急性痛风抗炎镇痛与预防发作频次方面有临床探索，为延伸场景提供科学线索。",
        "b4.t": "动物与体外",
        "b4.d": "高脂高糖/STZ 等模型中显示降糖、调脂、抗氧化与胰岛保护相关结果；酚类提取物 DPPH 清除等抗氧化数据突出。",
        "s4.title": "工艺与规格",
        "s4.body": "叶原料热水提取、浓缩、干燥制粉等路径；可提供多酚含量规格与有机硒相关叙事（以实际检测为准）。适合固体饮料、压片、乳粉添加等。",
        "s5.title": "应用与复配",
        "a1": "血糖管理草本固体饮料 / 茶珍",
        "a2": "成人乳粉与特膳中的植物代谢模块",
        "a3": "与金花黑茶提取物组成糖脂双降方案",
        "a4": "与黄精等传统食材复配的国潮代谢产品",
        "s6.title": "资质与说明",
        "p1": "研究文献与临床试验信息用于研发参考",
        "p2": "终端宣称须符合目标市场食品法规",
        "p3": "可提供原料规格、检测与配方建议",
        "p4": "官网统一命名：青钱柳（不再使用「金钱柳」混称）",
    }
    en = {
        "doc.title": "Cyclocarya Leaf Polyphenols - Tianyi Health Tech",
        "doc.desc": "Cyclocarya paliurus leaf polyphenols for glucose-lipid management formulas, with human study and preclinical references.",
        "m1": "Polyphenol level",
        "m2": "Human study refs",
        "m3": "Example duration",
        "m4": "Core use case",
        "s1.title": "Scientific Background",
        "s1.body": "Cyclocarya paliurus leaves contain polysaccharides, flavonoids, triterpenes and polyphenols long discussed for metabolic regulation—often nicknamed “plant insulin” in education content. Tianyi supplies standardized leaf polyphenols for metabolic food innovation, stackable with golden dark tea.",
        "s2.title": "Actives & Mechanism",
        "c1.t": "Leaf polyphenol complex",
        "c1.d": "About 25% polyphenol class (COA prevails) for antioxidant and metabolic enzyme narratives.",
        "c2.t": "Glucose pathways",
        "c2.d": "Research discusses insulin sensitivity, glycogen and gluconeogenesis pathways (e.g., AMPK).",
        "c3.t": "Lipid pathways",
        "c3.d": "Animal/human data suggest potential improvements in TG, TC, LDL-c and HDL-c profiles.",
        "c4.t": "Microbiome link",
        "c4.d": "Clinical work explores gut microbiota and metabolite modulation of metabolic phenotypes.",
        "s3.title": "Benefits & Human Evidence",
        "b1.t": "84-day human reference",
        "b1.d": "Published work: ~84-day leaf extract intervention, HbA1c from ~7.9% to ~6.9%, similar reduction vs gliclazide arm (research only, not a product claim).",
        "b2.t": "Glucose-lipid RCTs",
        "b2.d": "Studies report FBG, 2hPBG, OGTT AUC, TG, HDL-c and beneficial taxa enrichment signals.",
        "b3.t": "Gout-related exploration",
        "b3.d": "Granule studies explore anti-inflammatory comfort and attack-frequency prevention—extension scenarios only.",
        "b4.t": "Preclinical support",
        "b4.d": "HFD/STZ models show glucose-lipid, antioxidant and islet-protection signals; strong phenolic antioxidant assays.",
        "s4.title": "Process & Specs",
        "s4.body": "Hot-water extraction, concentration and drying; polyphenol grades and selenium stories per analytics. Suitable for powders, tablets and milk-powder fortification.",
        "s5.title": "Applications",
        "a1": "Glucose-management herbal powders",
        "a2": "Adult milk powder metabolic modules",
        "a3": "Stack with golden dark tea for dual glucose-lipid concepts",
        "a4": "China-chic formulas with traditional companions",
        "s6.title": "Notes",
        "p1": "Literature/clinical info for R&D reference",
        "p2": "Claims must follow target-market food law",
        "p3": "Specs, COA and formulation support available",
        "p4": "Official naming: Cyclocarya (青钱柳)",
    }
    body = metrics_html([("~25%", "m1"), ("多人群研究", "m2"), ("84 天", "m3"), ("糖脂管理", "m4")])
    en["m2"] = "Human studies"
    en["m3"] = "84 days"
    en["m4"] = "Metabolic care"
    body += text_section("Science", "s1.title", "s1.body")
    body += cards_section("Mechanism", "s2.title", [("c1.t", "c1.d"), ("c2.t", "c2.d"), ("c3.t", "c3.d"), ("c4.t", "c4.d")])
    body += cards_section("Evidence", "s3.title", [("b1.t", "b1.d"), ("b2.t", "b2.d"), ("b3.t", "b3.d"), ("b4.t", "b4.d")])
    body += text_section("Quality", "s4.title", "s4.body")
    body += list_section("Applications", "s5.title", ["a1", "a2", "a3", "a4"])
    body += list_section("Proof", "s6.title", ["p1", "p2", "p3", "p4"])
    return page_shell(
        "qingqianliu", "青钱柳叶多酚", "Cyclocarya Leaf Polyphenols",
        zh["doc.desc"], en["doc.desc"],
        "assets/p31_03.webp", "植物胰岛素方向", "Plant Insulin Direction",
        "以青钱柳叶多酚服务血糖与血脂管理类产品创新，科研与人群研究可追溯、可沟通。",
        "Cyclocarya leaf polyphenols for glucose-lipid product innovation with traceable research dialogue.",
        body, zh, en,
    )


# ─────────────────── Jinhuahongcha ───────────────────
def build_jinhua():
    zh = {
        "doc.title": "金花黑茶提取物 - 天颐健康科技",
        "doc.desc": "安化金花黑茶提取物，冠突散囊菌纯种发酵与茶褐素核心，面向靶向减脂、三高调理与肠道健康功能原料开发。",
        "m1": "发酵方式",
        "m2": "特征成分",
        "m3": "工艺工序",
        "m4": "核心功效方向",
        "s1.title": "科学背景",
        "s1.body": "金花黑茶以「金花」——冠突散囊菌发酵为特征。茶褐素等后发酵产物被称作「黄金代谢因子」，在调节糖脂代谢、体重管理与肠道健康方向具备产业价值。相关技术路线与国家科技进步奖成果转化叙事可为 B 端背书（以可公开口径为准）。",
        "s2.title": "核心成分与机制",
        "c1.t": "茶褐素",
        "c1.d": "后发酵形成的水溶性高聚物，讨论抑制胰脂肪酶、激活 AMPK、促进脂肪酸氧化等路径。",
        "c2.t": "茶多酚 / 儿茶素",
        "c2.d": "协同抗氧化与代谢酶抑制，强化减脂与三高管理叙事。",
        "c3.t": "冠突散囊菌发酵",
        "c3.d": "国家二级保密菌种纯种发酵路径，强调标准化与功效稳定。",
        "c4.t": "肠道与通便舒适",
        "c4.d": "动物实验提示调节菌群与促进肠蠕动、温和通便且不易致泻的特性讨论。",
        "s3.title": "功效与数据参考",
        "b1.t": "靶向减脂（内脏脂肪）",
        "b1.d": "抑制脂肪吸收 + 加速脂肪代谢双路径；适合体重管理与体型管理产品。",
        "b2.t": "降三高方向",
        "b2.d": "从抑制消化酶、改善胰岛素抵抗讨论到血脂谱调节，多靶点代谢支持。",
        "b3.t": "人群体验数据（弱化展示）",
        "b3.d": "历史万人健康项目等体验观察显示随饮用周期空腹血糖下降人数占比提升（科研/体验参考，不作疗效承诺）。",
        "b4.t": "降尿酸与肠道",
        "b4.d": "双重酶抑制等机制支持尿酸管理讨论；肠道舒适为常见体感卖点。",
        "s4.title": "工艺与形态",
        "s4.body": "纯种发酵 + 数控发花 + 多级膜分离 + 喷雾干燥微胶囊等技术组合，形成小分子速溶粉。强调零添加导向、无泻药依赖与高溶解性，适配固体饮料与方便即饮。",
        "s5.title": "应用与市场案例方向",
        "a1": "体重管理 / 刮油轻体固体饮料",
        "a2": "代谢支持茶粉、代餐协同模块",
        "a3": "与 AKK、藤茶、青钱柳的复配方案",
        "a4": "国内外已有黑茶粉体重与代谢类产品可对标",
        "s6.title": "品质保障",
        "p1": "21 道标准化工序与专利数控发花技术叙事",
        "p2": "SGS 等成分检测支持（茶多酚、茶氨酸、黄酮等）",
        "p3": "GMP 产线与检测设备保障",
        "p4": "可提供出口与 Halal 等方案沟通",
    }
    en = {
        "doc.title": "Golden Dark Tea Extract - Tianyi Health Tech",
        "doc.desc": "Anhua golden-flower dark tea extract via Eurotium cristatum fermentation and theabrownin for fat management, metabolic balance and gut comfort.",
        "m1": "Fermentation",
        "m2": "Signature active",
        "m3": "Process steps",
        "m4": "Focus areas",
        "s1.title": "Scientific Background",
        "s1.body": "Golden-flower dark tea is defined by Eurotium cristatum fermentation. Theabrownin—“golden metabolic factor”—supports industrial stories around lipid-glucose metabolism, weight and gut health.",
        "s2.title": "Actives & Mechanism",
        "c1.t": "Theabrownin",
        "c1.d": "Post-fermentation polymer discussed for lipase inhibition, AMPK activation and fatty-acid oxidation.",
        "c2.t": "Tea polyphenols / catechins",
        "c2.d": "Antioxidant and digestive-enzyme narratives for metabolic formulas.",
        "c3.t": "Pure-culture fermentation",
        "c3.d": "Standardized Eurotium cristatum process for consistent activity.",
        "c4.t": "Gut comfort",
        "c4.d": "Animal data discuss microbiota and gentle motility support without harsh catharsis.",
        "s3.title": "Benefits & Data",
        "b1.t": "Targeted fat management",
        "b1.d": "Reduce absorption + boost metabolism dual logic for weight/shape products.",
        "b2.t": "Metabolic balance",
        "b2.d": "Multi-target discussion from digestive enzymes to insulin sensitivity and lipids.",
        "b3.t": "Human experience data (soft)",
        "b3.d": "Historical large-scale tasting programs observed rising share of fasting-glucose responders over time (experience reference only).",
        "b4.t": "Uric acid & gut",
        "b4.d": "Enzyme-inhibition stories for uric acid; gut comfort as a common sensory benefit.",
        "s4.title": "Process & Format",
        "s4.body": "Pure-culture fermentation, controlled flowering, membrane concentration and spray-dry microencapsulation into instant powder for RTD sticks and sachets.",
        "s5.title": "Applications",
        "a1": "Weight-management instant powders",
        "a2": "Metabolic tea powders / meal-companion modules",
        "a3": "Stacks with AKK, vine tea and Cyclocarya",
        "a4": "Benchmarkable against global dark-tea metabolic SKUs",
        "s6.title": "Quality",
        "p1": "Multi-step standardized process narrative",
        "p2": "Composition testing support (polyphenols, theanine, flavonoids)",
        "p3": "GMP-oriented production & analytics",
        "p4": "Export / Halal discussions available",
    }
    body = metrics_html([("纯种发酵", "m1"), ("茶褐素", "m2"), ("21", "m3"), ("减脂/三高/肠道", "m4")])
    en["m1"] = "Pure culture"
    en["m2"] = "Theabrownin"
    en["m3"] = "21 steps"
    en["m4"] = "Fat / metabolic / gut"
    body += text_section("Science", "s1.title", "s1.body")
    body += cards_section("Mechanism", "s2.title", [("c1.t", "c1.d"), ("c2.t", "c2.d"), ("c3.t", "c3.d"), ("c4.t", "c4.d")])
    body += cards_section("Evidence", "s3.title", [("b1.t", "b1.d"), ("b2.t", "b2.d"), ("b3.t", "b3.d"), ("b4.t", "b4.d")])
    body += text_section("Quality", "s4.title", "s4.body")
    body += list_section("Applications", "s5.title", ["a1", "a2", "a3", "a4"])
    body += list_section("Proof", "s6.title", ["p1", "p2", "p3", "p4"])
    return page_shell(
        "jinhuahongcha", "金花黑茶提取物", "Golden Dark Tea Extract",
        zh["doc.desc"], en["doc.desc"],
        "assets/p13_01.webp", "黄金代谢因子", "Golden Metabolic Factor",
        "冠突散囊菌纯种发酵金花黑茶，以茶褐素为核心，服务减脂、三高与肠道健康产品。",
        "Eurotium-fermented golden dark tea with theabrownin for fat, metabolic and gut products.",
        body, zh, en,
    )


def main():
    builders = {
        "akk": build_akk,
        "enzyme": build_enzyme,
        "tengcha": build_tengcha,
        "wujitai": build_wujitai,
        "qingqianliu": build_qingqianliu,
        "jinhuahongcha": build_jinhua,
    }
    for slug, fn in builders.items():
        html = fn()
        path = OUT / f"{slug}.html"
        path.write_text(html, encoding="utf-8")
        print("wrote", path, "bytes", path.stat().st_size)

if __name__ == "__main__":
    main()
