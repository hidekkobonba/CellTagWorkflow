from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Cm
import io

# A4 landscape: 29.7cm x 21cm
prs = Presentation()
prs.slide_width  = Cm(33.87)   # 16:9 widescreen
prs.slide_height = Cm(19.05)

W = prs.slide_width
H = prs.slide_height

# Colors
CREAM   = RGBColor(0xF9, 0xF7, 0xF3)
DARK    = RGBColor(0x2A, 0x22, 0x20)
GOLD    = RGBColor(0xC8, 0xA0, 0x60)
GOLD_LT = RGBColor(0xF0, 0xE8, 0xD8)
WHITE   = RGBColor(0xFF, 0xFF, 0xFF)
GRAY    = RGBColor(0x99, 0x99, 0x99)
LGRAY   = RGBColor(0xCC, 0xCC, 0xCC)
BGRAY   = RGBColor(0x1A, 0x1A, 0x1A)

def blank_slide(prs, bg=CREAM):
    layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(layout)
    bg_shape = slide.shapes.add_shape(1, 0, 0, W, H)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = bg
    bg_shape.line.fill.background()
    return slide

def add_text(slide, text, l, t, w, h, size=18, color=DARK, bold=False,
             align=PP_ALIGN.LEFT, italic=False, wrap=True):
    tx = slide.shapes.add_textbox(l, t, w, h)
    tf = tx.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    return tx

def add_rect(slide, l, t, w, h, fill=GOLD, line=None, line_w=Pt(1)):
    shp = slide.shapes.add_shape(1, l, t, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = fill
    if line:
        shp.line.color.rgb = line
        shp.line.width = line_w
    else:
        shp.line.fill.background()
    return shp

def add_line(slide, x1, y1, x2, y2, color=GOLD, w=Pt(1)):
    from pptx.util import Emu
    from pptx.oxml.ns import qn
    from lxml import etree
    cx = x2 - x1
    cy = y2 - y1
    conn = slide.shapes.add_connector(1, x1, y1, x2, y2)
    conn.line.color.rgb = color
    conn.line.width = w
    return conn

def gold_bar(slide, t, w=Cm(3), l=None):
    if l is None:
        l = (W - w) / 2
    add_rect(slide, l, t, w, Cm(0.05), fill=GOLD)

def section_header(slide, label, num):
    add_rect(slide, Cm(1.2), Cm(1.1), W - Cm(2.4), Cm(0.04), fill=GOLD)
    add_text(slide, label, Cm(1.2), Cm(0.3), Cm(12), Cm(0.7),
             size=7, color=GOLD, italic=False)
    add_text(slide, num, W - Cm(3), Cm(0.3), Cm(2), Cm(0.7),
             size=7, color=LGRAY, align=PP_ALIGN.RIGHT)

# ──────────────────────────────────────────
# SLIDE 1: COVER
# ──────────────────────────────────────────
slide = blank_slide(prs, CREAM)

gold_bar(slide, Cm(7.5))
add_text(slide, "Nose & Design", Cm(1.5), Cm(2), W - Cm(3), Cm(3.5),
         size=60, color=DARK, bold=False, italic=True, align=PP_ALIGN.CENTER)
add_text(slide, "RHINOPLASTY COUNSELING GUIDE",
         Cm(1.5), Cm(6), W - Cm(3), Cm(1),
         size=8, color=LGRAY, align=PP_ALIGN.CENTER)
gold_bar(slide, Cm(7.5))
add_text(slide, "鼻整形 カウンセリングガイド",
         Cm(1.5), Cm(8), W - Cm(3), Cm(1),
         size=14, color=RGBColor(0x6A,0x58,0x40), align=PP_ALIGN.CENTER)
add_text(slide, "あなたの理想のデザインを、一緒に選びましょう。",
         Cm(1.5), Cm(9.2), W - Cm(3), Cm(1),
         size=10, color=LGRAY, align=PP_ALIGN.CENTER)
add_text(slide, "羽根 和秀",
         Cm(1.5), Cm(12.5), W - Cm(3), Cm(1.2),
         size=18, color=GOLD, align=PP_ALIGN.CENTER)
add_text(slide, "Zetith Beauty Clinic Fukuoka",
         Cm(1.5), Cm(13.8), W - Cm(3), Cm(1),
         size=10, color=LGRAY, align=PP_ALIGN.CENTER)

# ──────────────────────────────────────────
# SLIDE 2: 羽根先生の強み
# ──────────────────────────────────────────
slide = blank_slide(prs, CREAM)
section_header(slide, "DOCTOR'S STRENGTHS", "01")

add_text(slide, "羽根先生の強み", Cm(1.2), Cm(1.5), Cm(15), Cm(1.4),
         size=28, color=DARK, bold=False)

cards = [
    ("01", "クローズド法のスペシャリスト",
     "外側に傷を残さないクローズド法を専門としています。高い技術が必要な術式ですが、ダウンタイムが短く自然な仕上がりのため、現在最も需要の高い技術です。"),
    ("02", "顔全体のデザイン設計力",
     "鼻の形・高さ・向きだけでなく、顔全体のバランスを見た上でデザインを設計します。「整形した感」が出ない自然な仕上がりにこだわっています。"),
    ("03", "正直なカウンセリング",
     "「しないほうがいい」と伝えることも仕事のうち。リスクと代替案を丁寧に説明し、患者さんが納得した上で選択できる場を作ります。"),
    ("04", "他院修正・拘縮鼻対応",
     "他院での施術後の修正に積極的に対応。状態を正確に診断し、「何ができるか・できないか」を正直にお伝えした上でプランを提案します。"),
]

cols = [(Cm(1.2), Cm(2)), (Cm(1.2 + 15.5), Cm(2)),
        (Cm(1.2), Cm(10)), (Cm(1.2 + 15.5), Cm(10))]

for i, (num, title, body) in enumerate(cards):
    lx, ly = cols[i]
    cw, ch = Cm(14.8), Cm(7.2)
    add_rect(slide, lx, ly, cw, ch, fill=WHITE,
             line=RGBColor(0xE8, 0xDE, 0xCE), line_w=Pt(1))
    add_text(slide, num, lx + Cm(0.4), ly + Cm(0.3), Cm(3), Cm(1.8),
             size=30, color=RGBColor(0xE8,0xD0,0xA0), italic=True)
    add_text(slide, title, lx + Cm(0.4), ly + Cm(1.8), cw - Cm(0.8), Cm(1),
             size=13, color=GOLD, bold=False)
    add_text(slide, body, lx + Cm(0.4), ly + Cm(3), cw - Cm(0.8), Cm(3.8),
             size=9.5, color=RGBColor(0x66,0x66,0x66))

# ──────────────────────────────────────────
# SLIDE 3: クローズド法
# ──────────────────────────────────────────
slide = blank_slide(prs, CREAM)
section_header(slide, "CLOSED RHINOPLASTY", "02")

add_text(slide, "クローズド法とは", Cm(1.2), Cm(1.5), Cm(20), Cm(1.4),
         size=28, color=DARK)

# Hero dark box (left)
add_rect(slide, Cm(1.2), Cm(3.2), Cm(15.5), Cm(9), fill=DARK)
add_text(slide, "CLOSED APPROACH RHINOPLASTY",
         Cm(1.6), Cm(3.6), Cm(15), Cm(0.8),
         size=7, color=GOLD)
add_text(slide, "傷が残らない。バレない。",
         Cm(1.6), Cm(4.5), Cm(15), Cm(2),
         size=22, color=WHITE, italic=True)
add_text(slide, "すべての切開を鼻の内側だけで行う術式。\n外側に一切傷が残らず「整形した」とわからない仕上がりに。",
         Cm(1.6), Cm(6.5), Cm(14.8), Cm(2),
         size=10, color=GRAY)
# Trend badge
add_rect(slide, Cm(1.6), Cm(9.2), Cm(7), Cm(0.8),
         fill=GOLD)
add_text(slide, "★ 現在最もトレンドの術式", Cm(1.8), Cm(9.2), Cm(6.5), Cm(0.8),
         size=9, color=WHITE, bold=False)

# Table (right)
headers = ["", "クローズド法★", "オープン法"]
rows = [
    ("外側の傷", "なし（完全に内側のみ）", "鼻柱に小さな傷が残る"),
    ("ダウンタイム", "短め（5〜7日）", "やや長め（7〜10日）"),
    ("腫れ", "比較的少ない", "やや多い"),
    ("術者への要求", "高い技術力が必要", "視野が広く操作しやすい"),
    ("適応", "多くの鼻整形に対応可能", "複雑な修正に強い"),
]

tx = Cm(17.5)
ty = Cm(3.2)
tw = Cm(14.8)
th = Cm(9)
col_w = [Cm(3.5), Cm(5.5), Cm(5.5)]

# Header row
hx = tx
for j, hdr in enumerate(headers):
    bg = DARK if j == 0 else GOLD
    add_rect(slide, hx, ty, col_w[j], Cm(0.9), fill=bg)
    add_text(slide, hdr, hx + Cm(0.1), ty + Cm(0.05), col_w[j] - Cm(0.2), Cm(0.8),
             size=8, color=WHITE, bold=False, align=PP_ALIGN.CENTER)
    hx += col_w[j]

# Data rows
for ri, row in enumerate(rows):
    ry = ty + Cm(0.9) + ri * Cm(1.62)
    rx = tx
    for ci, cell in enumerate(row):
        bg = RGBColor(0xFD,0xF9,0xF3) if ci == 0 else WHITE
        add_rect(slide, rx, ry, col_w[ci], Cm(1.6), fill=bg,
                 line=RGBColor(0xED,0xE8,0xE0), line_w=Pt(0.8))
        fc = GOLD if ci == 0 else (DARK if ci == 1 else GRAY)
        add_text(slide, cell, rx + Cm(0.15), ry + Cm(0.1), col_w[ci] - Cm(0.3), Cm(1.4),
                 size=8.5, color=fc, align=PP_ALIGN.LEFT if ci == 0 else PP_ALIGN.CENTER)
        rx += col_w[ci]

# ──────────────────────────────────────────
# SLIDE 4: 鼻の解剖図 — explanatory illustration (text-based)
# ──────────────────────────────────────────
slide = blank_slide(prs, CREAM)
section_header(slide, "NOSE ANATOMY", "03")

add_text(slide, "鼻の解剖図 — 各部位と施術の関係",
         Cm(1.2), Cm(1.5), Cm(25), Cm(1.4), size=28, color=DARK)

# Left: side view diagram (visual box with labels)
add_rect(slide, Cm(1.2), Cm(3.2), Cm(15), Cm(13.5),
         fill=WHITE, line=RGBColor(0xE8,0xDE,0xCE), line_w=Pt(1))

parts = [
    ("鼻根（びこん）", "目と鼻の境界。眼鏡が乗る部分。", "▸ プロテーゼで高さを出す起点"),
    ("鼻背（鼻筋）", "鼻の高さの稜線。正面から見た「鼻筋」。", "▸ プロテーゼの主な作用部位"),
    ("鼻先（鼻尖）", "最も前に突出した点。デザインの核心。", "▸ ストラット・軟骨形成で整える"),
    ("鼻柱（コルメラ）", "両鼻孔の間の柱状の部分。", "▸ ACR改善・鼻中隔延長の対象"),
    ("小鼻（鼻翼）", "鼻の両サイドの膨らみ。", "▸ 小鼻縮小・鼻孔縁挙上"),
    ("鼻唇角", "鼻柱と上唇のなす角度。デザインを決める数値。", "▸ アップ(110°) / ストレート(90°) / ラウンド(100°)"),
]

for i, (name, desc, proc) in enumerate(parts):
    py = Cm(3.4) + i * Cm(2.2)
    add_rect(slide, Cm(1.4), py, Cm(0.4), Cm(0.4), fill=GOLD)
    add_text(slide, name, Cm(2.1), py - Cm(0.05), Cm(5), Cm(0.6),
             size=10.5, color=DARK, bold=False)
    add_text(slide, desc, Cm(2.1), py + Cm(0.5), Cm(13.5), Cm(0.7),
             size=8.5, color=GRAY)
    add_text(slide, proc, Cm(2.1), py + Cm(1.1), Cm(13.5), Cm(0.7),
             size=8, color=GOLD)

# Right: nasolabial angle explanation
add_rect(slide, Cm(17.2), Cm(3.2), Cm(15), Cm(6),
         fill=DARK)
add_text(slide, "鼻唇角 — デザインの核心",
         Cm(17.5), Cm(3.4), Cm(14.5), Cm(0.8), size=9, color=GOLD)
add_text(slide, "鼻唇角とは、鼻柱（コルメラ）と上唇のなす角度のこと。\nこの角度がデザインの「方向感」を決定します。\n\n"
         "●  90〜95° → ストレート・忘れ鼻\n"
         "● 100〜105° → ラウンド・自然な美しさ\n"
         "● 105〜115° → アップノーズ・あざと可愛い系",
         Cm(17.5), Cm(4.3), Cm(14.5), Cm(4.6),
         size=10, color=WHITE)

add_rect(slide, Cm(17.2), Cm(9.5), Cm(15), Cm(7),
         fill=WHITE, line=RGBColor(0xE8,0xDE,0xCE), line_w=Pt(1))
add_text(slide, "施術と部位の関係",
         Cm(17.5), Cm(9.7), Cm(14.5), Cm(0.8), size=9, color=GOLD)
proc_map = [
    ("プロテーゼ", "→ 鼻根〜鼻背を高くする"),
    ("鼻尖縮小・ストラット", "→ 鼻先の形・向きを整える"),
    ("小鼻縮小", "→ 小鼻の幅・広がりを改善"),
    ("鼻中隔延長", "→ 鼻先を下・前方向へ延長"),
    ("肋軟骨移植", "→ 大量の軟骨が必要な大変化"),
    ("他院修正", "→ 既存施術の修正・やり直し"),
]
for i, (proc, desc) in enumerate(proc_map):
    iy = Cm(10.5) + i * Cm(0.95)
    add_text(slide, f"● {proc}", Cm(17.5), iy, Cm(6), Cm(0.9), size=9, color=DARK)
    add_text(slide, desc, Cm(23), iy, Cm(9), Cm(0.9), size=9, color=GRAY)

# ──────────────────────────────────────────
# SLIDE 5: デザイン型比較
# ──────────────────────────────────────────
slide = blank_slide(prs, CREAM)
section_header(slide, "NOSE TIP DESIGN GUIDE", "04")

add_text(slide, "鼻先のデザイン比較",
         Cm(1.2), Cm(1.5), Cm(25), Cm(1.4), size=28, color=DARK)

designs = [
    ("アップノーズ", "Up Nose", "105〜115°",
     "Baby & Cute 系",
     "鼻先が上を向いた、可愛らしいデザイン。\n中顔面が短縮して見え、あざと可愛い印象になります。\n\nやりすぎると「豚鼻」に見えるリスクがあるため、\n角度のすり合わせが重要です。",
     "クローズド法対応◎\n中顔面短縮 / あざと可愛い",
     GOLD),
    ("ストレート", "Straight", "90〜95°",
     "Elegant 系 / 忘れ鼻",
     "鼻筋から鼻先まで一直線の、忘れ鼻デザイン。\n最も「整形した感」が出にくく、横顔の品格が増します。\n\n「バレたくない」「自然に綺麗になりたい」方に\n圧倒的に人気のデザインです。",
     "クローズド法対応◎\n忘れ鼻 / 整形感ゼロ",
     RGBColor(0x6A,0x70,0x60)),
    ("ラウンド", "Round", "95〜105°",
     "自然 / 大人美人",
     "鼻先に自然な丸みを持たせたデザイン。\n半ラウンドは大人の色気、フルラウンドは柔らかさを演出。\n\nシャープにしすぎると不自然に見える方や、\n柔らかい印象を保ちたい方に向いています。",
     "クローズド法対応◎\n半ラウンド / 大人美人",
     RGBColor(0x8A,0x6A,0x50)),
]

col_x = [Cm(1.2), Cm(12.6), Cm(24.0)]

for i, (name, en, angle, cat, desc, tags, color) in enumerate(designs):
    cx = col_x[i]
    cw = Cm(11)

    # Angle badge
    add_rect(slide, cx, Cm(3.0), cw, Cm(2.2), fill=color)
    add_text(slide, en, cx + Cm(0.4), Cm(3.1), cw - Cm(0.8), Cm(0.8),
             size=8, color=WHITE, italic=True)
    add_text(slide, name, cx + Cm(0.4), Cm(3.8), cw - Cm(0.8), Cm(1),
             size=18, color=WHITE, bold=False)

    # Angle display
    add_rect(slide, cx, Cm(5.2), cw, Cm(1.0), fill=RGBColor(0xFF,0xFF,0xFF),
             line=color, line_w=Pt(1.5))
    add_text(slide, f"鼻唇角  {angle}", cx + Cm(0.3), Cm(5.25), cw - Cm(0.6), Cm(0.9),
             size=11, color=color, align=PP_ALIGN.CENTER)

    # Category badge
    add_rect(slide, cx, Cm(6.3), cw, Cm(0.7), fill=GOLD_LT)
    add_text(slide, cat, cx + Cm(0.3), Cm(6.32), cw - Cm(0.6), Cm(0.6),
             size=8.5, color=RGBColor(0x8A,0x70,0x60), align=PP_ALIGN.CENTER)

    # Description
    add_rect(slide, cx, Cm(7.1), cw, Cm(7.5), fill=WHITE,
             line=RGBColor(0xE8,0xDE,0xCE), line_w=Pt(0.8))
    add_text(slide, desc, cx + Cm(0.3), Cm(7.2), cw - Cm(0.6), Cm(5.5),
             size=9.5, color=RGBColor(0x44,0x44,0x44))
    add_rect(slide, cx + Cm(0.3), Cm(12), cw - Cm(0.6), Cm(0.05), fill=RGBColor(0xE8,0xDE,0xCE))
    add_text(slide, tags, cx + Cm(0.3), Cm(12.2), cw - Cm(0.6), Cm(1.5),
             size=8.5, color=color)

# ──────────────────────────────────────────
# SLIDE 6: Baby & Cute
# ──────────────────────────────────────────
def catalog_slide(prs, title_en, title_sub, designs3, note):
    slide = blank_slide(prs, CREAM)
    # Script title area
    add_rect(slide, Cm(0), Cm(0), W, Cm(3.8), fill=WHITE)
    add_text(slide, title_en,
             Cm(2), Cm(0.3), W - Cm(4), Cm(2.4),
             size=36, color=DARK, italic=True, align=PP_ALIGN.CENTER)
    add_text(slide, f'- {title_sub} -',
             Cm(2), Cm(2.5), W - Cm(4), Cm(0.9),
             size=9, color=RGBColor(0x6A,0x58,0x40), align=PP_ALIGN.CENTER)
    add_rect(slide, Cm(2), Cm(2.38), W - Cm(4), Cm(0.04), fill=GOLD)
    add_rect(slide, Cm(2), Cm(3.28), W - Cm(4), Cm(0.04), fill=GOLD)

    col_x = [Cm(1.2), Cm(12.6), Cm(24.0)]
    for i, (tag, desc, ht) in enumerate(designs3):
        cx = col_x[i]; cw = Cm(11)
        add_rect(slide, cx, Cm(4.2), cw, Cm(0.9), fill=GOLD)
        add_text(slide, tag, cx, Cm(4.2), cw, Cm(0.9),
                 size=13, color=WHITE, align=PP_ALIGN.CENTER, bold=False)
        add_text(slide, desc, cx + Cm(0.3), Cm(5.2), cw - Cm(0.6), Cm(1.5),
                 size=9, color=GRAY)
        # Before circle placeholder
        add_rect(slide, cx + Cm(0.5), Cm(6.9), Cm(4.5), Cm(4.5), fill=RGBColor(0xE0,0xDB,0xD0),
                 line=GOLD, line_w=Pt(1))
        add_text(slide, "BEFORE\n写真挿入", cx + Cm(0.5), Cm(6.9), Cm(4.5), Cm(4.5),
                 size=8, color=LGRAY, align=PP_ALIGN.CENTER)
        # After rect placeholder
        add_rect(slide, cx + Cm(5.2), Cm(6.9), Cm(5.5), Cm(4.5), fill=BGRAY,
                 line=RGBColor(0x33,0x33,0x33), line_w=Pt(0.8))
        add_text(slide, "After\n写真挿入", cx + Cm(5.2), Cm(6.9), Cm(5.5), Cm(4.5),
                 size=8, color=GRAY, align=PP_ALIGN.CENTER, italic=True)
        # Hashtag
        add_rect(slide, cx, Cm(11.6), cw, Cm(0.7), fill=GOLD_LT)
        add_text(slide, ht, cx, Cm(11.62), cw, Cm(0.65),
                 size=8.5, color=RGBColor(0x8A,0x70,0x60), align=PP_ALIGN.CENTER)

    # Note bar
    add_rect(slide, Cm(1.2), Cm(12.6), W - Cm(2.4), Cm(4.5),
             fill=WHITE, line=RGBColor(0xE8,0xDE,0xCE), line_w=Pt(1))
    add_rect(slide, Cm(1.2), Cm(12.6), Cm(0.3), Cm(4.5), fill=GOLD)
    add_text(slide, "このカテゴリについて",
             Cm(1.8), Cm(12.75), Cm(8), Cm(0.7), size=8, color=GOLD)
    add_text(slide, note, Cm(1.8), Cm(13.5), W - Cm(3.5), Cm(3.5),
             size=9.5, color=GRAY)
    return slide

catalog_slide(prs,
    "Baby & Cute",
    '"中顔面短縮"と"あざと可愛さ"を重視したデザイン',
    [
        ("アップノーズ", "鼻先を斜め上方向へ。\n可愛らしく若々しい印象に。", "#あざと可愛い"),
        ("中顔面短縮",   "鼻先の向きと高さで\n顔の縦幅を短く見せる。", "#小顔効果"),
        ("ACR改善",      "鼻柱を下ろしながら小鼻は上げる。\n正面の印象を整える。", "#バランス改善"),
    ],
    "クローズド法で対応可能なケースが多く、ダウンタイムを短くしながら可愛らしい印象を作れます。鼻先の向きは数ミリの差で印象が大きく変わるため、カウンセリングでのすり合わせが重要です。"
)

# ──────────────────────────────────────────
# SLIDE 7: Elegant & Straight
# ──────────────────────────────────────────
catalog_slide(prs,
    "Elegant & Straight",
    '"忘れ鼻"と"横顔の品格"を追求したナチュラル美デザイン',
    [
        ("ストレート", "鼻筋から鼻先まで一直線のライン。\n最も整形感が出にくい。", "#忘れ鼻"),
        ("半ラウンド", "自然な丸みを残しながら\n品のある印象に。", "#大人美人"),
        ("短鼻解消",   "鼻が上を向いた状態を改善。\n自然な向きと高さを実現。", "#立体感"),
    ],
    "「整形したことを気づかれたくない」「自然に綺麗になりたい」方に最も選ばれるカテゴリです。クローズド法との相性が非常に良く、忘れ鼻（自然すぎて気づかれない鼻）は羽根先生が特に得意とするデザインです。"
)

# ──────────────────────────────────────────
# SLIDE 8: Dramatic & Glamorous
# ──────────────────────────────────────────
catalog_slide(prs,
    "Dramatic & Glamorous",
    '"圧倒的な高さ"と"Eライン"を完成させるフルオーダーデザイン',
    [
        ("シャープ鼻", "鼻筋から鼻先までシャープな印象に。\n団子鼻を解消。", "#ハーフ顔"),
        ("Eライン",    "横顔の美しさを完成させる設計。\n口元の突出感も軽減。", "#Eライン"),
        ("貴族手術",   "鼻翼基部を持ち上げ\n横顔に奥行きを演出。", "#存在感"),
    ],
    "大きな変化を望む方向けのカテゴリです。プロテーゼ・軟骨移植・鼻中隔延長など複合施術が多く、場合によってはオープン法や肋軟骨移植が必要になります。ダウンタイムは長めですが、完成時の変化も最も大きいカテゴリです。"
)

# ──────────────────────────────────────────
# SLIDE 9: CLOSING
# ──────────────────────────────────────────
slide = blank_slide(prs, DARK)
add_text(slide, "ZETITH BEAUTY CLINIC FUKUOKA",
         Cm(2), Cm(2.5), W - Cm(4), Cm(1),
         size=8, color=GOLD, align=PP_ALIGN.CENTER)
add_text(slide, "今日、どんな鼻になりたいですか？",
         Cm(2), Cm(4.5), W - Cm(4), Cm(3),
         size=30, color=WHITE, italic=True, align=PP_ALIGN.CENTER)
add_text(slide, "デザインのイメージが固まっていなくても大丈夫です。\n「なんとなくこんな印象になりたい」から一緒に考えます。\n決めなければいけない場ではありません。",
         Cm(2), Cm(8.2), W - Cm(4), Cm(3.5),
         size=11, color=GRAY, align=PP_ALIGN.CENTER)
gold_bar(slide, Cm(12.5))
add_text(slide, "INSTAGRAM", Cm(2), Cm(13.2), W - Cm(4), Cm(0.8),
         size=8, color=GOLD, align=PP_ALIGN.CENTER)
add_text(slide, "@zetith_hane", Cm(2), Cm(14.2), W - Cm(4), Cm(1.2),
         size=16, color=LGRAY, align=PP_ALIGN.CENTER)
add_text(slide, "Zetith Beauty Clinic 福岡院", Cm(2), Cm(15.5), W - Cm(4), Cm(1),
         size=11, color=GRAY, align=PP_ALIGN.CENTER)

# ──────────────────────────────────────────
# SAVE
# ──────────────────────────────────────────
out = "/home/user/CellTagWorkflow/sns/鼻整形_カウンセリング資料.pptx"
prs.save(out)
print(f"完了: {out}")
