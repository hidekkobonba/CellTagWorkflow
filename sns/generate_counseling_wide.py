from pptx import Presentation
from pptx.util import Pt, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width  = Cm(33.87)  # 16:9 widescreen
prs.slide_height = Cm(19.05)

W = prs.slide_width
H = prs.slide_height

# ── Colors ──
CREAM  = RGBColor(0xF9, 0xF7, 0xF3)
DARK   = RGBColor(0x2A, 0x22, 0x20)
GOLD   = RGBColor(0xC8, 0xA0, 0x60)
GOLD_L = RGBColor(0xF0, 0xE8, 0xD8)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
GR     = RGBColor(0x88, 0x88, 0x88)
LGR    = RGBColor(0xCC, 0xCC, 0xCC)
DARK2  = RGBColor(0x1A, 0x1A, 0x1A)
BEIGE  = RGBColor(0xE8, 0xDE, 0xCE)
TAN    = RGBColor(0x6A, 0x58, 0x40)

def slide_blank(bg=CREAM):
    layout = prs.slide_layouts[6]
    s = prs.slides.add_slide(layout)
    r = s.shapes.add_shape(1, 0, 0, W, H)
    r.fill.solid(); r.fill.fore_color.rgb = bg
    r.line.fill.background()
    return s

def rect(s, l, t, w, h, fill=WHITE, line_c=None, line_w=Pt(0.8)):
    shp = s.shapes.add_shape(1, l, t, w, h)
    shp.fill.solid(); shp.fill.fore_color.rgb = fill
    if line_c:
        shp.line.color.rgb = line_c; shp.line.width = line_w
    else:
        shp.line.fill.background()
    return shp

def txt(s, text, l, t, w, h, size=14, color=DARK,
        bold=False, italic=False, align=PP_ALIGN.LEFT, wrap=True):
    tx = s.shapes.add_textbox(l, t, w, h)
    tf = tx.text_frame; tf.word_wrap = wrap
    p = tf.paragraphs[0]; p.alignment = align
    run = p.add_run(); run.text = text
    run.font.size = Pt(size); run.font.color.rgb = color
    run.font.bold = bold; run.font.italic = italic
    return tx

def hbar(s, t, l=None, w=Cm(4)):
    if l is None: l = (W - w) / 2
    rect(s, l, t, w, Cm(0.06), fill=GOLD)

def ph(s, label, num):
    rect(s, Cm(1.5), Cm(1.3), W - Cm(3), Cm(0.05), fill=GOLD)
    txt(s, label, Cm(1.5), Cm(0.5), Cm(18), Cm(0.8),
        size=7, color=GOLD)
    txt(s, num, W - Cm(3.5), Cm(0.5), Cm(2.5), Cm(0.8),
        size=8, color=LGR, align=PP_ALIGN.RIGHT)

# ══════════════════════════════════════════════════════
# SLIDE 1  COVER
# ══════════════════════════════════════════════════════
s = slide_blank(CREAM)
# Left accent bar
rect(s, Cm(0), Cm(0), Cm(0.6), H, fill=DARK)
rect(s, Cm(0.6), Cm(0), Cm(0.06), H, fill=GOLD)

txt(s, "RHINOPLASTY COUNSELING GUIDE",
    Cm(3), Cm(3.5), W - Cm(5), Cm(1),
    size=9, color=GOLD)
txt(s, "Nose & Design",
    Cm(3), Cm(4.8), W - Cm(5), Cm(4),
    size=64, color=DARK, italic=True)
hbar(s, Cm(9.6), l=Cm(3), w=Cm(5))
txt(s, "鼻整形 カウンセリングガイド",
    Cm(3), Cm(10.2), W - Cm(5), Cm(1.5),
    size=18, color=TAN)
txt(s, "あなたの理想のデザインを、一緒に選びましょう。",
    Cm(3), Cm(11.8), W - Cm(5), Cm(1.2),
    size=12, color=GR)
rect(s, Cm(3), Cm(14.5), Cm(10), Cm(0.05), fill=GOLD)
txt(s, "羽根 和秀",
    Cm(3), Cm(15), Cm(14), Cm(1.5),
    size=22, color=GOLD)
txt(s, "Zetith Beauty Clinic Fukuoka",
    Cm(3), Cm(16.5), Cm(16), Cm(1),
    size=11, color=LGR)

# ══════════════════════════════════════════════════════
# SLIDE 2  羽根先生の強み
# ══════════════════════════════════════════════════════
s = slide_blank(CREAM)
ph(s, "DOCTOR'S STRENGTHS", "01")
txt(s, "羽根先生の強み", Cm(1.5), Cm(1.8), Cm(20), Cm(1.8),
    size=34, color=DARK)

cards = [
    ("01", "クローズド法のスペシャリスト",
     "外側に傷を残さないクローズド法を専門としています。高い技術力が必要な術式ですが、ダウンタイムが短く自然な仕上がりのため、現在最も需要の高い技術です。"),
    ("02", "顔全体のデザイン設計力",
     "鼻の形・高さ・向きだけでなく、顔全体のバランスを見た上でデザインを設計します。「整形した感」が出ない自然な仕上がりにこだわっています。"),
    ("03", "正直なカウンセリング",
     "「しないほうがいい」「今はまだ早い」と伝えることも仕事のうち。リスクと代替案を丁寧に説明し、患者さんが納得した上で選択できる場を作ります。"),
    ("04", "他院修正・拘縮鼻対応",
     "他院での施術後の修正に積極的に対応します。状態を正確に診断し、「何ができるか・できないか」を正直にお伝えした上でプランを提案します。"),
]

positions = [
    (Cm(1.5),  Cm(4.0)),
    (Cm(17.8), Cm(4.0)),
    (Cm(1.5),  Cm(11.3)),
    (Cm(17.8), Cm(11.3)),
]
CW, CH = Cm(15.5), Cm(6.6)

for i, (num, title, body) in enumerate(cards):
    lx, ly = positions[i]
    rect(s, lx, ly, CW, CH, fill=WHITE, line_c=BEIGE, line_w=Pt(1))
    rect(s, lx, ly, Cm(0.35), CH, fill=GOLD)
    txt(s, num, lx + Cm(0.7), ly + Cm(0.3), Cm(3), Cm(1.6),
        size=32, color=RGBColor(0xE8,0xD0,0xA0), italic=True)
    txt(s, title, lx + Cm(0.7), ly + Cm(2.0), CW - Cm(1.2), Cm(0.9),
        size=14, color=GOLD)
    txt(s, body, lx + Cm(0.7), ly + Cm(3.1), CW - Cm(1.2), Cm(3.2),
        size=11, color=GR)

# ══════════════════════════════════════════════════════
# SLIDE 3  クローズド法
# ══════════════════════════════════════════════════════
s = slide_blank(CREAM)
ph(s, "CLOSED RHINOPLASTY", "02")
txt(s, "クローズド法とは", Cm(1.5), Cm(1.8), Cm(22), Cm(1.8),
    size=34, color=DARK)

# Left dark hero
rect(s, Cm(1.5), Cm(4.0), Cm(14.5), Cm(13.2), fill=DARK)
txt(s, "CLOSED APPROACH RHINOPLASTY",
    Cm(2), Cm(4.4), Cm(13.5), Cm(0.9), size=7.5, color=GOLD)
txt(s, "傷が残らない。\nバレない。",
    Cm(2), Cm(5.4), Cm(13.5), Cm(3.2),
    size=30, color=WHITE, italic=True)
txt(s, "すべての切開を鼻の内側だけで行う術式。\n外側に一切傷が残らず「整形した」とわからない仕上がりになります。",
    Cm(2), Cm(8.8), Cm(13.2), Cm(2.5),
    size=12, color=GR)
rect(s, Cm(2), Cm(11.6), Cm(9), Cm(1.0), fill=GOLD)
txt(s, "★ 現在最もトレンドの術式",
    Cm(2), Cm(11.65), Cm(9), Cm(0.9),
    size=12, color=WHITE, align=PP_ALIGN.CENTER)
# Small badges
for bx, bt in [(Cm(2), Cm(13)), (Cm(8), Cm(13)), (Cm(2), Cm(14.2))]:
    rect(s, bx, bt, Cm(5.5), Cm(0.8), fill=RGBColor(0x3A,0x32,0x30),
         line_c=RGBColor(0x4A,0x42,0x40), line_w=Pt(0.5))
for bx, bt, lab in [
    (Cm(2), Cm(13), "外側に傷なし"),
    (Cm(8), Cm(13), "ダウンタイム短め"),
    (Cm(2), Cm(14.2), "腫れが少ない"),
]:
    txt(s, lab, bx, bt, Cm(5.5), Cm(0.8), size=10, color=GOLD,
        align=PP_ALIGN.CENTER)

# Right: comparison table
TX = Cm(17.2)
headers = ["", "クローズド法 ★", "オープン法"]
rows_d = [
    ("外側の傷",    "なし（完全に内側のみ）",   "鼻柱に小さな傷が残る"),
    ("ダウンタイム","短め（5〜7日）",            "やや長め（7〜10日）"),
    ("腫れの程度",  "比較的少ない",              "やや多い"),
    ("術者への要求","高い技術力が必要",           "視野が広く操作しやすい"),
    ("適応",        "多くの鼻整形に対応可能",    "複雑な修正に強い"),
]
CWS = [Cm(3.8), Cm(6.2), Cm(6.2)]
for j, hdr in enumerate(headers):
    hx = TX + sum(CWS[:j])
    rect(s, hx, Cm(4.0), CWS[j], Cm(1.1),
         fill=DARK if j == 0 else GOLD)
    txt(s, hdr, hx + Cm(0.2), Cm(4.05), CWS[j] - Cm(0.4), Cm(1),
        size=10, color=WHITE, bold=False, align=PP_ALIGN.CENTER)

for ri, row in enumerate(rows_d):
    ry = Cm(5.1) + ri * Cm(2.42)
    for ci, cell in enumerate(row):
        rx = TX + sum(CWS[:ci])
        bg = RGBColor(0xFD,0xF9,0xF3) if ci == 0 else WHITE
        rect(s, rx, ry, CWS[ci], Cm(2.4),
             fill=bg, line_c=BEIGE, line_w=Pt(0.8))
        fc = GOLD if ci == 0 else (DARK if ci == 1 else GR)
        txt(s, cell, rx + Cm(0.2), ry + Cm(0.3), CWS[ci] - Cm(0.4), Cm(1.8),
            size=11, color=fc,
            align=PP_ALIGN.LEFT if ci == 0 else PP_ALIGN.CENTER)

# ══════════════════════════════════════════════════════
# SLIDE 4  鼻の解剖図
# ══════════════════════════════════════════════════════
s = slide_blank(CREAM)
ph(s, "NOSE ANATOMY", "03")
txt(s, "鼻の解剖図 — 各部位と施術の関係",
    Cm(1.5), Cm(1.8), Cm(28), Cm(1.8), size=34, color=DARK)

parts = [
    ("鼻根（びこん）",  "眉間〜鼻の始まり。眼鏡が乗る部分。",          "▸ プロテーゼで高さを出す起点"),
    ("鼻背（鼻筋）",   "鼻の高さの稜線。正面から見た「鼻筋」。",        "▸ プロテーゼの主な作用部位"),
    ("鼻先（鼻尖）",   "最も前に突出した点。デザインの核心。",           "▸ ストラット・軟骨形成で整える"),
    ("鼻柱（コルメラ）","両鼻孔の間の柱。ACR比率の要素。",              "▸ 鼻中隔延長・ACR改善"),
    ("小鼻（鼻翼）",   "鼻の両サイドの膨らみ。",                        "▸ 小鼻縮小・鼻孔縁挙上"),
    ("鼻唇角",         "鼻柱と上唇のなす角度。デザインの数値。",         "▸ アップ(110°)/ストレート(90°)/ラウンド(100°)"),
]
for i, (name, desc, proc) in enumerate(parts):
    py = Cm(4.2) + i * Cm(2.35)
    rect(s, Cm(1.5), py + Cm(0.3), Cm(0.45), Cm(0.45), fill=GOLD)
    txt(s, name,  Cm(2.3), py + Cm(0.1), Cm(7),   Cm(0.9), size=13, color=DARK)
    txt(s, desc,  Cm(2.3), py + Cm(1.0), Cm(11.5), Cm(0.8), size=10, color=GR)
    txt(s, proc,  Cm(2.3), py + Cm(1.7), Cm(12),   Cm(0.7), size=9,  color=GOLD)

# Right panel: nasolabial angle box
rect(s, Cm(15.8), Cm(4.0), Cm(16.5), Cm(7.5), fill=DARK)
txt(s, "鼻唇角（びしんかく） — デザインを決める数値",
    Cm(16.3), Cm(4.3), Cm(15.8), Cm(0.9), size=10, color=GOLD)
txt(s, "鼻柱（コルメラ）と上唇のなす角度のことで、\nこの数値がデザインの「方向感」を決定します。",
    Cm(16.3), Cm(5.3), Cm(15.8), Cm(2), size=12, color=WHITE)

angle_items = [
    ("90〜95°",    "ストレート",    "忘れ鼻・整形感ゼロ"),
    ("100〜105°",  "ラウンド",      "自然な美しさ・大人美人"),
    ("105〜115°",  "アップノーズ",  "あざと可愛い・中顔面短縮"),
]
for ai, (angle, label, desc) in enumerate(angle_items):
    ay = Cm(7.5) + ai * Cm(1.2)
    rect(s, Cm(16.3), ay, Cm(2.8), Cm(1.0), fill=GOLD)
    txt(s, angle, Cm(16.3), ay, Cm(2.8), Cm(1.0),
        size=12, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    txt(s, label, Cm(19.3), ay, Cm(4), Cm(1.0),
        size=12, color=WHITE)
    txt(s, desc,  Cm(23.5), ay, Cm(8.5), Cm(1.0),
        size=10, color=GR)

# Procedure map (bottom right)
rect(s, Cm(15.8), Cm(12.0), Cm(16.5), Cm(5.3),
     fill=WHITE, line_c=BEIGE, line_w=Pt(1))
txt(s, "施術と部位の関係",
    Cm(16.3), Cm(12.2), Cm(16), Cm(0.8), size=10, color=GOLD)
proc_map = [
    ("プロテーゼ",       "→ 鼻根〜鼻背を高くする"),
    ("鼻尖縮小・ストラット", "→ 鼻先の形・向きを整える"),
    ("小鼻縮小",         "→ 小鼻の幅・広がりを改善"),
    ("鼻中隔延長",       "→ 鼻先を下・前方向へ延長"),
    ("肋軟骨移植",       "→ 大量軟骨が必要な大変化"),
]
for pi, (proc, desc) in enumerate(proc_map):
    py = Cm(13.1) + pi * Cm(0.82)
    txt(s, f"● {proc}", Cm(16.3), py, Cm(7.5), Cm(0.8), size=10, color=DARK)
    txt(s, desc,         Cm(24.0), py, Cm(8),   Cm(0.8), size=10, color=GR)

# ══════════════════════════════════════════════════════
# SLIDE 5  デザイン型比較
# ══════════════════════════════════════════════════════
s = slide_blank(CREAM)
ph(s, "NOSE TIP DESIGN GUIDE", "04")
txt(s, "鼻先のデザイン比較",
    Cm(1.5), Cm(1.8), Cm(22), Cm(1.8), size=34, color=DARK)

designs = [
    ("アップノーズ", "Up Nose",    "105〜115°",
     "Baby & Cute 系",
     "鼻先が上を向いた、可愛らしいデザイン。\n中顔面が短縮して見え、あざと可愛い印象になります。\nやりすぎると「豚鼻」になるリスクがあるため、\n角度のすり合わせが重要です。",
     GOLD),
    ("ストレート",   "Straight",   "90〜95°",
     "Elegant 系 / 忘れ鼻",
     "鼻筋から鼻先まで一直線の、忘れ鼻デザイン。\n最も「整形した感」が出にくく、横顔の品格が増します。\n「バレたくない」「自然に綺麗になりたい」方に\n圧倒的に人気のデザインです。",
     RGBColor(0x6A,0x70,0x60)),
    ("ラウンド",     "Round",      "95〜105°",
     "自然 / 大人美人",
     "鼻先に自然な丸みを持たせたデザイン。\n半ラウンドは大人の色気、フルラウンドは柔らかさを演出。\nシャープにしすぎると不自然に見える方や、\n柔らかい印象を保ちたい方に向いています。",
     RGBColor(0x8A,0x6A,0x50)),
]
DX = [Cm(1.5), Cm(12.7), Cm(23.9)]
DW = Cm(10.5)

for i, (name, en, angle, cat, desc, col) in enumerate(designs):
    lx = DX[i]
    # Top color bar
    rect(s, lx, Cm(4.0), DW, Cm(2.8), fill=col)
    txt(s, en,    lx + Cm(0.5), Cm(4.2), DW - Cm(1), Cm(0.9),
        size=10, color=WHITE, italic=True)
    txt(s, name,  lx + Cm(0.5), Cm(5.1), DW - Cm(1), Cm(1.5),
        size=22, color=WHITE)
    # Angle badge
    rect(s, lx, Cm(6.8), DW, Cm(1.2),
         fill=WHITE, line_c=col, line_w=Pt(2))
    txt(s, f"鼻唇角  {angle}", lx, Cm(6.82), DW, Cm(1.15),
        size=14, color=col, bold=True, align=PP_ALIGN.CENTER)
    # Category tag
    rect(s, lx, Cm(8.0), DW, Cm(0.85), fill=GOLD_L)
    txt(s, cat, lx, Cm(8.02), DW, Cm(0.82),
        size=10, color=TAN, align=PP_ALIGN.CENTER)
    # Description
    rect(s, lx, Cm(8.85), DW, Cm(7.0),
         fill=WHITE, line_c=BEIGE, line_w=Pt(0.8))
    txt(s, desc, lx + Cm(0.4), Cm(9.1), DW - Cm(0.8), Cm(4.5),
        size=11, color=GR)
    rect(s, lx + Cm(0.4), Cm(13.2), DW - Cm(0.8), Cm(0.04), fill=BEIGE)
    txt(s, "クローズド法対応 ◎", lx + Cm(0.4), Cm(13.4), DW - Cm(0.8), Cm(1),
        size=11, color=col)

# ══════════════════════════════════════════════════════
# CATALOG SLIDE BUILDER
# ══════════════════════════════════════════════════════
def catalog_slide(title_en, title_sub, items, note_text):
    s = slide_blank(CREAM)
    # Header area white + script title
    rect(s, 0, 0, W, Cm(4.2), fill=WHITE)
    txt(s, title_en,
        Cm(2), Cm(0.3), W - Cm(4), Cm(2.5),
        size=40, color=DARK, italic=True, align=PP_ALIGN.CENTER)
    txt(s, f"- {title_sub} -",
        Cm(2), Cm(2.8), W - Cm(4), Cm(0.9),
        size=10, color=TAN, align=PP_ALIGN.CENTER)
    rect(s, Cm(3), Cm(2.65), W - Cm(6), Cm(0.06), fill=GOLD)
    rect(s, Cm(3), Cm(3.6),  W - Cm(6), Cm(0.06), fill=GOLD)

    CX = [Cm(1.5), Cm(12.7), Cm(23.9)]
    CW = Cm(10.5)

    for i, (tag, desc, ht) in enumerate(items):
        lx = CX[i]
        # Tag
        rect(s, lx, Cm(4.5), CW, Cm(1.1), fill=GOLD)
        txt(s, tag, lx, Cm(4.52), CW, Cm(1.08),
            size=15, color=WHITE, align=PP_ALIGN.CENTER)
        # Desc
        txt(s, desc, lx + Cm(0.3), Cm(5.7), CW - Cm(0.6), Cm(1.5),
            size=10.5, color=GR)
        # BEFORE circle (simulated as square with note)
        rect(s, lx, Cm(7.3), Cm(5), Cm(5.5),
             fill=RGBColor(0xE0,0xDB,0xD0), line_c=GOLD, line_w=Pt(1.2))
        txt(s, "BEFORE\n\n写真挿入",
            lx, Cm(7.3), Cm(5), Cm(5.5),
            size=11, color=LGR, align=PP_ALIGN.CENTER)
        # AFTER rect
        rect(s, lx + Cm(5.2), Cm(7.3), Cm(5.3), Cm(5.5),
             fill=DARK2, line_c=RGBColor(0x33,0x33,0x33), line_w=Pt(0.8))
        txt(s, "After\n\n写真挿入",
            lx + Cm(5.2), Cm(7.3), Cm(5.3), Cm(5.5),
            size=11, color=GR, align=PP_ALIGN.CENTER, italic=True)
        # Hashtag
        rect(s, lx, Cm(12.9), CW, Cm(0.85), fill=GOLD_L)
        txt(s, ht, lx, Cm(12.92), CW, Cm(0.82),
            size=10, color=TAN, align=PP_ALIGN.CENTER)

    # Note bar
    rect(s, Cm(1.5), Cm(14.0), W - Cm(3), Cm(4.0),
         fill=WHITE, line_c=BEIGE, line_w=Pt(1))
    rect(s, Cm(1.5), Cm(14.0), Cm(0.4), Cm(4.0), fill=GOLD)
    txt(s, "このカテゴリについて",
        Cm(2.3), Cm(14.2), Cm(12), Cm(0.8), size=9, color=GOLD)
    txt(s, note_text,
        Cm(2.3), Cm(15.1), W - Cm(4), Cm(2.8), size=11, color=GR)
    return s

catalog_slide(
    "Baby & Cute",
    '"中顔面短縮"と"あざと可愛さ"を重視したデザイン',
    [
        ("アップノーズ",
         "鼻先を斜め上方向へ。\nあざと可愛い印象に。",
         "#あざと可愛い  #中顔面短縮"),
        ("中顔面短縮",
         "鼻先の向きと高さで\n顔の縦幅を短く見せる。",
         "#小顔効果"),
        ("ACR改善",
         "鼻柱を下ろしながら小鼻は上げる。\n正面の印象を整える。",
         "#バランス改善"),
    ],
    "クローズド法で対応可能なケースが多く、ダウンタイムを短くしながら可愛らしい印象を作れます。鼻先の向きは数ミリの差で印象が大きく変わるため、カウンセリングでのすり合わせが重要です。"
)

catalog_slide(
    "Elegant & Straight",
    '"忘れ鼻"と"横顔の品格"を追求したナチュラル美デザイン',
    [
        ("ストレート",
         "鼻筋から鼻先まで一直線のライン。\n最も整形感が出にくい。",
         "#忘れ鼻  #整形感ゼロ"),
        ("半ラウンド",
         "自然な丸みを残しながら\n品のある印象に。",
         "#大人美人"),
        ("短鼻解消",
         "鼻が上を向いた状態を改善。\n自然な向きと高さを実現。",
         "#立体感"),
    ],
    "「整形したことを気づかれたくない」「自然に綺麗になりたい」方に最も選ばれるカテゴリです。クローズド法との相性が非常に良く、忘れ鼻（自然すぎて気づかれない鼻）は羽根先生が特に得意とするデザインです。"
)

catalog_slide(
    "Dramatic & Glamorous",
    '"圧倒的な高さ"と"Eライン"を完成させるフルオーダーデザイン',
    [
        ("シャープ鼻",
         "鼻筋から鼻先までシャープな印象に。\n団子鼻を解消。",
         "#ハーフ顔"),
        ("Eライン",
         "横顔の美しさを完成させる設計。\n口元の突出感も軽減。",
         "#Eライン"),
        ("貴族手術",
         "鼻翼基部を持ち上げ\n横顔に奥行きを演出。",
         "#存在感"),
    ],
    "大きな変化を望む方向けのカテゴリです。プロテーゼ・軟骨移植・鼻中隔延長など複合施術が多く、場合によってはオープン法や肋軟骨移植が必要になります。ダウンタイムは長めですが、完成時の変化も最も大きいカテゴリです。"
)

# ══════════════════════════════════════════════════════
# SLIDE 9  CLOSING
# ══════════════════════════════════════════════════════
s = slide_blank(DARK)
rect(s, Cm(0), Cm(0), Cm(0.6), H, fill=GOLD)

txt(s, "ZETITH BEAUTY CLINIC FUKUOKA",
    Cm(3), Cm(3), W - Cm(5), Cm(1),
    size=9, color=GOLD)
txt(s, "今日、どんな鼻に\nなりたいですか？",
    Cm(3), Cm(4.5), W - Cm(5), Cm(5),
    size=44, color=WHITE, italic=True)
hbar(s, Cm(10.5), l=Cm(3), w=Cm(5))
txt(s, "デザインのイメージが固まっていなくても大丈夫です。\n「なんとなくこんな印象になりたい」から一緒に考えます。\n決めなければいけない場ではありません。",
    Cm(3), Cm(11.3), W - Cm(5), Cm(3.5),
    size=13, color=GR)
rect(s, Cm(3), Cm(15.2), Cm(12), Cm(0.06), fill=GOLD)
txt(s, "Instagram   @zetith_hane",
    Cm(3), Cm(15.5), W - Cm(5), Cm(1.2),
    size=15, color=LGR)
txt(s, "Zetith Beauty Clinic 福岡院",
    Cm(3), Cm(16.8), W - Cm(5), Cm(1),
    size=12, color=GR)

# ──────────────────────────────────────────
out = "/home/user/CellTagWorkflow/sns/鼻整形_カウンセリング資料_wide.pptx"
prs.save(out)
print(f"完了: {out}")
