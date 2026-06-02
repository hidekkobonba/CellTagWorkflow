html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
@page { size: A4; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Hiragino Mincho ProN', 'Yu Mincho', 'MS Mincho', Georgia, serif;
  background: #f9f7f3;
  color: #2a2220;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
.page {
  width: 210mm;
  min-height: 297mm;
  background: #f9f7f3;
  page-break-after: always;
  position: relative;
}
.cp { padding: 12mm 16mm 10mm; }

/* ── Typography ── */
h1 { font-size: 28px; font-weight: 300; color: #2a2220; margin-bottom: 4px; }
h2 { font-size: 18px; font-weight: 400; color: #c4a06a; margin-bottom: 5px; }
h3 { font-size: 13px; font-weight: 400; color: #2a2220; margin-bottom: 4px; }
p  { font-size: 9.5px; color: #444; line-height: 2; }
.en { font-family: Georgia, serif; font-style: italic; }

/* ── Page header ── */
.ph { border-bottom: 1px solid #c4a06a; padding-bottom: 6px; margin-bottom: 18px; overflow: hidden; }
.ph-label { float: left; font-size: 7px; letter-spacing: 3px; color: #c4a06a; }
.ph-num   { float: right; font-size: 8px; color: #ccc; }

/* ── Gold divider ── */
.gd { width: 36px; height: 1px; background: #c4a06a; margin: 10px 0; }

/* ── Doctor note box ── */
.note-box {
  background: #fffef9;
  border: 1px solid #e0d4b8;
  border-left: 3px solid #c4a06a;
  padding: 12px 16px;
  margin: 12px 0;
}
.note-box .note-head {
  font-size: 7.5px; letter-spacing: 2px; color: #c4a06a; margin-bottom: 6px;
}
.note-box p { font-size: 9px; color: #555; line-height: 1.95; }

/* ── Info block ── */
.info-block {
  background: #fff;
  border: 1px solid #e8dece;
  padding: 12px 14px;
  margin-bottom: 12px;
}
.info-block h3 { color: #c4a06a; font-size: 12px; margin-bottom: 6px; }
.info-block p  { font-size: 9px; color: #555; line-height: 1.9; }

/* ── Two-col ── */
.two-col { overflow: hidden; }
.col-l { float: left;  width: 47%; }
.col-r { float: right; width: 50%; }

/* ── Three-col ── */
.three-col { overflow: hidden; margin-top: 10px; }
.col3 { float: left; width: 30%; margin-right: 5%; }
.col3:last-child { margin-right: 0; }

/* ── Tag pills ── */
.tag {
  display: inline-block; font-size: 7px; color: #c4a06a;
  border: 1px solid #c4a06a; border-radius: 10px;
  padding: 2px 8px; margin-right: 5px; margin-bottom: 4px;
}
.tag-fill {
  display: inline-block; font-size: 7px; color: #fff;
  background: #c4a06a; border-radius: 10px;
  padding: 3px 9px; margin-right: 5px; margin-bottom: 4px;
}

/* ── Compare row ── */
.cmp-row { overflow: hidden; border-bottom: 1px solid #ede8e0; padding: 7px 0; }
.cmp-label { float: left; width: 28%; font-size: 8.5px; color: #c4a06a; padding-top: 1px; }
.cmp-a     { float: left; width: 34%; font-size: 8.5px; color: #2a2220; }
.cmp-b     { float: left; width: 34%; font-size: 8.5px; color: #888; }
.cmp-head  { background: #2a2220; overflow: hidden; padding: 6px 0; margin-bottom: 2px; }
.cmp-head .cmp-label { color: #fff; font-size: 7.5px; }
.cmp-head .cmp-a { color: #c4a06a; font-size: 8px; }
.cmp-head .cmp-b { color: #888; font-size: 8px; }

/* ── Timeline ── */
.tl-row { overflow: hidden; margin-bottom: 12px; }
.tl-day { float: left; width: 52px; font-size: 8.5px; color: #c4a06a; text-align: right; padding-right: 10px; padding-top: 2px; }
.tl-bar { float: left; width: 3px; background: #c4a06a; margin-right: 12px; height: 36px; }
.tl-bar.muted { background: #ddd; }
.tl-body { overflow: hidden; }
.tl-body h4 { font-size: 10px; color: #2a2220; margin-bottom: 2px; }
.tl-body p  { font-size: 8.5px; color: #777; line-height: 1.7; }

/* ── Design type card ── */
.dcard {
  text-align: center;
}
.dcard .dtitle {
  display: block; background: #c4a06a; color: #fff;
  border-radius: 20px; padding: 5px 0;
  font-size: 11px; margin-bottom: 7px;
}
.dcard .dangle {
  font-family: Georgia, serif; font-style: italic;
  font-size: 18px; color: #c4a06a; display: block;
  margin-bottom: 4px;
}
.dcard p { font-size: 8.5px; color: #555; line-height: 1.8; text-align: left; }

/* ── Cover ── */
.cover {
  width: 210mm; height: 297mm; background: #f9f7f3;
  display: table; text-align: left;
}
.cover-inner { display: table-cell; vertical-align: middle; padding: 20mm 20mm 20mm 24mm; }

/* ── Closing ── */
.closing-page {
  width: 210mm; height: 297mm; background: #2a2220;
  display: table; text-align: center;
}
.closing-inner { display: table-cell; vertical-align: middle; padding: 20mm; }

/* ── SVG box ── */
.svgwrap { background: #fff; border: 1px solid #e8dece; padding: 12px; margin-bottom: 12px; }
.svgwrap .sv-title { font-size: 7.5px; letter-spacing: 2px; color: #c4a06a; margin-bottom: 8px; }

/* ── Q&A ── */
.qa { margin-bottom: 14px; }
.qa-q { font-size: 10.5px; color: #2a2220; margin-bottom: 5px; overflow: hidden; }
.qa-q::before { content: 'Q'; float: left; width: 22px; font-family: Georgia, serif; font-size: 14px; color: #c4a06a; line-height: 0.9; margin-right: 4px; }
.qa-a { font-size: 9px; color: #666; line-height: 1.95; padding-left: 26px; }

/* ── Pro/con ── */
.merit-row { overflow: hidden; margin-bottom: 6px; }
.merit-label { float: left; width: 18px; font-size: 9px; color: #c4a06a; }
.merit-text  { overflow: hidden; font-size: 9px; color: #555; line-height: 1.8; }
.demerit-label { float: left; width: 18px; font-size: 9px; color: #888; }
</style>
</head>
<body>

<!-- ============================================================ -->
<!-- PAGE 1: COVER -->
<!-- ============================================================ -->
<div class="page">
<div class="cover"><div class="cover-inner">
  <div style="font-size:8px;letter-spacing:5px;color:#c4a06a;margin-bottom:40px;">RHINOPLASTY GUIDE</div>
  <div style="font-family:Georgia,serif;font-style:italic;font-size:52px;color:#2a2220;line-height:1.2;margin-bottom:10px;">Nose<br>Guide</div>
  <div style="width:40px;height:1px;background:#c4a06a;margin:22px 0;"></div>
  <div style="font-size:16px;color:#6a5840;margin-bottom:8px;">鼻整形 解説ガイド</div>
  <div style="font-size:10px;color:#aaa;margin-bottom:48px;">カウンセリング後のお持ち帰り用</div>

  <div style="font-size:10px;color:#555;line-height:2;margin-bottom:40px;">
    このガイドは、よくいただく質問への回答と<br>
    施術について知っておいてほしいことを<br>
    まとめたものです。<br>
    持ち帰って、ゆっくり読んでください。
  </div>
  <div style="font-size:14px;color:#c4a06a;letter-spacing:2px;margin-bottom:6px;">羽根 和秀</div>
  <div style="font-size:8px;color:#bbb;letter-spacing:1px;">Zetith Beauty Clinic Fukuoka</div>
</div></div>
</div>

<!-- ============================================================ -->
<!-- PAGE 2: 顔のゾーン / 中顔面 -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">FACE STRUCTURE</span><span class="ph-num">01</span></div>
  <h1>中顔面とは何か</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:18px;">THE MIDFACE CONCEPT</div>

  <div class="two-col">
    <div class="col-l">
      <div class="svgwrap">
        <div class="sv-title">顔の3ゾーン（側面図）</div>
        <svg viewBox="0 0 180 260" xmlns="http://www.w3.org/2000/svg" width="100%">
          <!-- Face oval -->
          <ellipse cx="90" cy="128" rx="72" ry="104" fill="#f5ece0" stroke="#c4a06a" stroke-width="1.5" opacity="0.7"/>
          <!-- Horizontal zone lines -->
          <line x1="18" y1="80"  x2="165" y2="80"  stroke="#c4a06a" stroke-width="1" stroke-dasharray="5,3"/>
          <line x1="18" y1="165" x2="165" y2="165" stroke="#c4a06a" stroke-width="1" stroke-dasharray="5,3"/>
          <!-- Zone shading - midface highlight -->
          <rect x="18" y="80" width="147" height="85" fill="#c4a06a" opacity="0.07"/>
          <!-- UPPER zone label -->
          <text x="148" y="42"  font-size="8" fill="#aaa" font-family="serif" text-anchor="middle">上顔面</text>
          <text x="148" y="52"  font-size="6.5" fill="#bbb" font-family="serif" text-anchor="middle">眉〜目</text>
          <!-- MID zone label -->
          <text x="148" y="120" font-size="8" fill="#c4a06a" font-family="serif" text-anchor="middle" font-weight="bold">中顔面</text>
          <text x="148" y="130" font-size="6.5" fill="#c4a06a" font-family="serif" text-anchor="middle">目〜鼻の底</text>
          <!-- LOWER zone label -->
          <text x="148" y="200" font-size="8" fill="#aaa" font-family="serif" text-anchor="middle">下顔面</text>
          <text x="148" y="210" font-size="6.5" fill="#bbb" font-family="serif" text-anchor="middle">口〜顎</text>
          <!-- Simple nose shape -->
          <path d="M 90,78 C 86,100 78,128 70,148 Q 65,158 70,165 C 76,170 90,172 110,168 Q 115,160 110,155 C 102,130 94,100 90,78"
            fill="#e8d4c0" stroke="#c4a06a" stroke-width="1.2" opacity="0.8"/>
          <!-- Eyes -->
          <ellipse cx="68" cy="76" rx="10" ry="5" fill="#2a2220" opacity="0.12"/>
          <ellipse cx="112" cy="76" rx="10" ry="5" fill="#2a2220" opacity="0.12"/>
          <!-- Brows -->
          <path d="M 56,64 Q 68,58 80,62" stroke="#2a2220" stroke-width="1.5" fill="none" opacity="0.2"/>
          <path d="M 100,62 Q 112,58 124,64" stroke="#2a2220" stroke-width="1.5" fill="none" opacity="0.2"/>
          <!-- Lips -->
          <path d="M 76,190 Q 90,202 104,190" stroke="#c4a06a" stroke-width="1.5" fill="none" opacity="0.6"/>
          <!-- Chin -->
          <path d="M 65,230 Q 90,248 115,230" stroke="#c4a06a" stroke-width="1" fill="none" opacity="0.3"/>
          <!-- Arrows for midface length -->
          <line x1="30" y1="82"  x2="30" y2="163" stroke="#c4a06a" stroke-width="1"/>
          <polygon points="30,80 27,86 33,86" fill="#c4a06a"/>
          <polygon points="30,165 27,159 33,159" fill="#c4a06a"/>
          <text x="5" y="128" font-size="7" fill="#c4a06a" font-family="serif">長さ</text>
        </svg>
      </div>
    </div>
    <div class="col-r">
      <p style="margin-bottom:12px;">顔を上・中・下の3つのゾーンに分けて考えます。</p>
      <div class="info-block">
        <h3>上顔面</h3>
        <p>眉から目の下まで。目の形や眉のアーチが印象を決める。</p>
      </div>
      <div class="info-block" style="border-left:3px solid #c4a06a;background:#fffef9;">
        <h3>中顔面 ← 鼻整形のゾーン</h3>
        <p>目の下から鼻の底まで。この長さが短く見えると「可愛い・小顔」な印象になります。<br>鼻先の向きを上方向（アップノーズ）にすると、中顔面が視覚的に短く見えます。</p>
      </div>
      <div class="info-block">
        <h3>下顔面</h3>
        <p>口元から顎まで。輪郭・顎のラインが印象を左右する。</p>
      </div>
      <div class="note-box">
        <div class="note-head">先生のひとこと</div>
        <p>「中顔面を短くしたい」という相談が本当に多いです。小顔に見せたい・可愛くなりたい、という方のほぼ全員が気にしているポイントです。鼻先の向きだけで驚くほど顔の印象が変わります。</p>
      </div>
    </div>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 3: デザイン解説 -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">NOSE DESIGN GUIDE</span><span class="ph-num">02</span></div>
  <h1>デザインについて</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:14px;">DESIGN TYPES EXPLAINED</div>

  <div class="svgwrap" style="margin-bottom:14px;">
    <div class="sv-title">鼻唇角の違いによるデザイン比較（鼻唇角 = 鼻柱と上唇のなす角度）</div>
    <svg viewBox="0 0 480 130" xmlns="http://www.w3.org/2000/svg" width="100%">
      <rect width="480" height="130" fill="#fff"/>
      <g transform="translate(8,0)">
        <text x="68" y="12" font-size="9" fill="#c4a06a" text-anchor="middle" font-family="serif">アップノーズ</text>
        <text x="68" y="23" font-size="7.5" fill="#aaa" text-anchor="middle">105〜115°</text>
        <line x1="112" y1="18" x2="112" y2="118" stroke="#ede8e0" stroke-width="1.2" stroke-dasharray="5,4"/>
        <path d="M 110,24 C 105,37 96,56 80,76 Q 68,88 72,98 C 78,108 100,110 110,108"
          fill="#f5ece0" stroke="#c4a06a" stroke-width="2.2" fill-opacity="0.6"/>
        <line x1="72" y1="98" x2="60" y2="78" stroke="#bbb" stroke-width="0.9" stroke-dasharray="4,3"/>
        <line x1="72" y1="98" x2="72" y2="120" stroke="#bbb" stroke-width="0.9" stroke-dasharray="4,3"/>
        <path d="M 72,108 A 12,12 0 0 0 64,88" fill="none" stroke="#c4a06a" stroke-width="1.5"/>
        <text x="46" y="122" font-size="7.5" fill="#c4a06a">110°</text>
        <rect x="10" y="124" width="116" height="12" rx="6" fill="#f0e8d8"/>
        <text x="68" y="133" font-size="7" fill="#8a7060" text-anchor="middle">Baby &amp; Cute 系</text>
      </g>
      <line x1="162" y1="10" x2="162" y2="128" stroke="#e8dece" stroke-width="1" stroke-dasharray="3,3"/>
      <g transform="translate(170,0)">
        <text x="68" y="12" font-size="9" fill="#6a7060" text-anchor="middle" font-family="serif">ストレート / 忘れ鼻</text>
        <text x="68" y="23" font-size="7.5" fill="#aaa" text-anchor="middle">90〜95°</text>
        <line x1="112" y1="18" x2="112" y2="118" stroke="#ede8e0" stroke-width="1.2" stroke-dasharray="5,4"/>
        <path d="M 110,24 C 104,38 94,60 78,82 Q 64,96 68,108 C 76,118 100,120 110,118"
          fill="#f5ece0" stroke="#6a7060" stroke-width="2.2" fill-opacity="0.6"/>
        <line x1="68" y1="108" x2="54" y2="86" stroke="#bbb" stroke-width="0.9" stroke-dasharray="4,3"/>
        <line x1="68" y1="108" x2="68" y2="128" stroke="#bbb" stroke-width="0.9" stroke-dasharray="4,3"/>
        <path d="M 68,118 A 12,12 0 0 0 57,99" fill="none" stroke="#6a7060" stroke-width="1.5"/>
        <text x="40" y="128" font-size="7.5" fill="#6a7060">92°</text>
        <rect x="10" y="124" width="116" height="12" rx="6" fill="#f0ede8"/>
        <text x="68" y="133" font-size="7" fill="#8a8a7a" text-anchor="middle">Elegant 系・整形感ゼロ</text>
      </g>
      <line x1="326" y1="10" x2="326" y2="128" stroke="#e8dece" stroke-width="1" stroke-dasharray="3,3"/>
      <g transform="translate(334,0)">
        <text x="68" y="12" font-size="9" fill="#8a6a50" text-anchor="middle" font-family="serif">ラウンド / 半ラウンド</text>
        <text x="68" y="23" font-size="7.5" fill="#aaa" text-anchor="middle">95〜105°</text>
        <line x1="112" y1="18" x2="112" y2="118" stroke="#ede8e0" stroke-width="1.2" stroke-dasharray="5,4"/>
        <path d="M 110,24 C 104,38 93,61 76,83 Q 60,98 66,110 C 74,122 100,124 110,122"
          fill="#f5ece0" stroke="#8a6a50" stroke-width="2.2" fill-opacity="0.6"/>
        <circle cx="62" cy="100" r="10" fill="none" stroke="#8a6a50" stroke-width="1" stroke-dasharray="3,2" opacity="0.5"/>
        <line x1="66" y1="110" x2="52" y2="88" stroke="#bbb" stroke-width="0.9" stroke-dasharray="4,3"/>
        <line x1="66" y1="110" x2="66" y2="128" stroke="#bbb" stroke-width="0.9" stroke-dasharray="4,3"/>
        <path d="M 66,120 A 12,12 0 0 0 55,101" fill="none" stroke="#8a6a50" stroke-width="1.5"/>
        <text x="38" y="128" font-size="7.5" fill="#8a6a50">100°</text>
        <rect x="10" y="124" width="116" height="12" rx="6" fill="#eeeae4"/>
        <text x="68" y="133" font-size="7" fill="#8a8078" text-anchor="middle">大人美人・自然な丸み</text>
      </g>
    </svg>
  </div>

  <div class="three-col">
    <div class="col3">
      <div style="font-size:11px;color:#c4a06a;font-weight:400;margin-bottom:6px;border-bottom:1px solid #e8dece;padding-bottom:4px;">アップノーズ</div>
      <p>鼻先が上を向いたデザイン。鼻唇角が大きくなる（105°以上）。中顔面が短縮して見え、可愛らしい印象に。やりすぎると「豚鼻」になるため角度設計が大切。</p>
    </div>
    <div class="col3">
      <div style="font-size:11px;color:#6a7060;font-weight:400;margin-bottom:6px;border-bottom:1px solid #e8dece;padding-bottom:4px;">ストレート・忘れ鼻</div>
      <p>鼻筋から鼻先まで一直線のライン。「整形した感」が最も出にくい。横顔に品格が生まれる。「バレたくない」方に圧倒的に人気のデザイン。</p>
    </div>
    <div class="col3">
      <div style="font-size:11px;color:#8a6a50;font-weight:400;margin-bottom:6px;border-bottom:1px solid #e8dece;padding-bottom:4px;">ラウンド・半ラウンド</div>
      <p>鼻先に自然な丸みを持たせる。半ラウンドは「大人の色気」、フルラウンドは「柔らかさ」。シャープにしすぎると不自然に見える方に特に向く。</p>
    </div>
  </div>

  <div class="note-box" style="margin-top:14px;">
    <div class="note-head">先生のひとこと — デザインについて</div>
    <p>「どれにすればいいか分からない」という方がほとんどです。カウンセリングでは顔の形・比率・希望のイメージを見ながら一緒に決めていくので、決めてこなくて大丈夫です。参考にしたい芸能人の写真などを持ってきてもらえると、イメージのすり合わせがしやすいです。</p>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 4: クローズド法 vs オープン法 -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">SURGICAL APPROACH</span><span class="ph-num">03</span></div>
  <h1>クローズド法 vs オープン法</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:14px;">CLOSED vs OPEN RHINOPLASTY</div>

  <div class="svgwrap" style="margin-bottom:14px;">
    <div class="sv-title">切開部位の比較（鼻を下から見た図）</div>
    <svg viewBox="0 0 400 160" xmlns="http://www.w3.org/2000/svg" width="100%">
      <!-- Left: Open -->
      <text x="100" y="14" font-size="10" fill="#888" text-anchor="middle" font-family="serif">オープン法</text>
      <ellipse cx="100" cy="85" rx="65" ry="56" fill="#f5ece0" stroke="#c4a06a" stroke-width="1.3"/>
      <ellipse cx="72"  cy="90" rx="22" ry="26" fill="#ddd0b8" stroke="#b89050" stroke-width="1"/>
      <ellipse cx="128" cy="90" rx="22" ry="26" fill="#ddd0b8" stroke="#b89050" stroke-width="1"/>
      <rect x="95" y="62" width="10" height="46" rx="5" fill="#eddcc4" stroke="#c4a06a" stroke-width="0.8"/>
      <line x1="100" y1="65" x2="100" y2="104" stroke="#cc4433" stroke-width="3.5" stroke-linecap="round"/>
      <circle cx="100" cy="65"  r="3.5" fill="#cc4433"/>
      <circle cx="100" cy="104" r="3.5" fill="#cc4433"/>
      <text x="100" y="130" font-size="8" fill="#cc4433" text-anchor="middle">鼻柱に切開線が入る</text>
      <text x="100" y="142" font-size="7.5" fill="#cc4433" text-anchor="middle">小さな傷が残る（数年で薄くなる）</text>
      <text x="100" y="155" font-size="7.5" fill="#cc4433" text-anchor="middle">視野が広く複雑な操作が可能</text>

      <line x1="200" y1="10" x2="200" y2="158" stroke="#e8dece" stroke-width="1.2" stroke-dasharray="5,4"/>

      <!-- Right: Closed -->
      <text x="300" y="14" font-size="10" fill="#c4a06a" text-anchor="middle" font-family="serif">クローズド法（羽根先生の得意技術）</text>
      <ellipse cx="300" cy="85" rx="65" ry="56" fill="#f5ece0" stroke="#c4a06a" stroke-width="1.3"/>
      <ellipse cx="272" cy="90" rx="22" ry="26" fill="#ddd0b8" stroke="#b89050" stroke-width="1"/>
      <ellipse cx="328" cy="90" rx="22" ry="26" fill="#ddd0b8" stroke="#b89050" stroke-width="1"/>
      <rect x="295" y="62" width="10" height="46" rx="5" fill="#eddcc4" stroke="#c4a06a" stroke-width="0.8"/>
      <text x="300" y="88" font-size="7" fill="#ccc" text-anchor="middle">傷なし</text>
      <!-- Internal incision dashes inside nostrils -->
      <path d="M 258,76 A 10,13 0 0 1 262,106" stroke="#c4a06a" stroke-width="2.5" fill="none" stroke-dasharray="5,3" stroke-linecap="round"/>
      <path d="M 342,76 A 10,13 0 0 0 338,106" stroke="#c4a06a" stroke-width="2.5" fill="none" stroke-dasharray="5,3" stroke-linecap="round"/>
      <circle cx="258" cy="76" r="3" fill="#c4a06a"/>
      <circle cx="342" cy="76" r="3" fill="#c4a06a"/>
      <text x="300" y="130" font-size="8" fill="#c4a06a" text-anchor="middle">切開は鼻の内側のみ</text>
      <text x="300" y="142" font-size="7.5" fill="#c4a06a" text-anchor="middle">外側に傷が残らない（＝バレない）</text>
      <text x="300" y="155" font-size="7.5" fill="#c4a06a" text-anchor="middle">技術的難易度は高い。ダウンタイム短め。</text>
    </svg>
  </div>

  <div class="two-col">
    <div class="col-l">
      <div class="cmp-head">
        <div class="cmp-label" style="padding-left:8px;"> </div>
        <div class="cmp-a" style="font-size:8px;color:#c4a06a;">クローズド法★</div>
        <div class="cmp-b" style="font-size:8px;">オープン法</div>
      </div>
      <div class="cmp-row"><div class="cmp-label">外側の傷</div><div class="cmp-a">なし</div><div class="cmp-b">鼻柱に小さな傷</div></div>
      <div class="cmp-row"><div class="cmp-label">ダウンタイム</div><div class="cmp-a">5〜7日</div><div class="cmp-b">7〜10日</div></div>
      <div class="cmp-row"><div class="cmp-label">腫れの程度</div><div class="cmp-a">比較的少ない</div><div class="cmp-b">やや多い</div></div>
      <div class="cmp-row"><div class="cmp-label">適応範囲</div><div class="cmp-a">多くの手術に対応</div><div class="cmp-b">複雑な修正に強い</div></div>
    </div>
    <div class="col-r">
      <div class="note-box" style="margin-top:0;">
        <div class="note-head">先生のひとこと</div>
        <p>クローズド法は技術的な難易度が高いため、得意としているドクターが少ない術式です。ダウンタイムが短く、外側に傷が残らないため、「バレたくない」「早く復帰したい」方には特におすすめしています。私はこの術式を中心に鼻整形を行っています。</p>
      </div>
    </div>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 5: プロテーゼ vs 自家組織 -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">IMPLANT vs AUTOLOGOUS TISSUE</span><span class="ph-num">04</span></div>
  <h1>プロテーゼ vs 自家組織隆鼻</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:14px;">PROSTHESIS vs OWN TISSUE</div>

  <div class="two-col" style="margin-bottom:14px;">
    <div class="col-l">
      <div class="info-block" style="border-left:3px solid #c4a06a;">
        <h3>プロテーゼ（シリコン / ePTFE）</h3>
        <p>鼻の内側から骨膜下にポケットを作り、シリコンまたはePTFE（ゴアテックス）のインプラントを挿入する方法。</p>
        <div style="margin-top:8px;">
          <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">メリット</div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">高さが長期間安定して維持される</div></div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">採取する部位がないため体への負担が少ない</div></div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">形の微調整がしやすい</div></div>
        </div>
        <div style="margin-top:8px;">
          <div style="font-size:8px;color:#888;margin-bottom:4px;">デメリット・懸念点</div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">異物を入れることへの心理的抵抗感</div></div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">まれに位置ずれ・感染のリスクがある</div></div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">将来取り出す可能性がゼロではない</div></div>
        </div>
      </div>
    </div>
    <div class="col-r">
      <div class="info-block">
        <h3>自家組織（耳軟骨）</h3>
        <p>耳の裏から軟骨を採取し、鼻に移植する方法。</p>
        <div style="margin-top:8px;">
          <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">メリット</div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">自分の組織なので感染リスクが低い</div></div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">異物を入れることへの抵抗がない</div></div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">自然な感触</div></div>
        </div>
        <div style="margin-top:8px;">
          <div style="font-size:8px;color:#888;margin-bottom:4px;">デメリット・限界</div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">採取量に限りがある</div></div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">高さアップは1〜3mm程度が限界</div></div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">少量の吸収（後戻り）が起きることがある</div></div>
        </div>
      </div>
    </div>
  </div>

  <div class="note-box">
    <div class="note-head">プロテーゼに抵抗がある方へ</div>
    <p>「自分の組織だけで高くしたい」というご希望をよくいただきます。耳軟骨だけでは1〜3mm程度しか高くできないため、「鼻筋をしっかり作りたい」「高さを大きく変えたい」という場合は、プロテーゼまたは肋軟骨移植が必要になります。プロテーゼは安全性の高い素材で、長年使われてきた実績があります。「怖い」というイメージが先行している場合が多いのですが、適切に行えばリスクは低い施術です。カウンセリングで詳しくお話しします。</p>
  </div>

  <div style="background:#fff;border:1px solid #e8dece;padding:12px 14px;margin-top:12px;">
    <div style="font-size:8px;color:#c4a06a;letter-spacing:1px;margin-bottom:7px;">後戻りの心配について</div>
    <div class="three-col">
      <div class="col3">
        <div style="font-size:10px;color:#2a2220;margin-bottom:4px;">プロテーゼ</div>
        <p>ほぼ後戻りなし。ただし長期間でまれに位置の微妙なずれが起きることがある。</p>
      </div>
      <div class="col3">
        <div style="font-size:10px;color:#2a2220;margin-bottom:4px;">耳軟骨</div>
        <p>10〜20%程度の吸収が起きることがある。大幅な後戻りは稀。</p>
      </div>
      <div class="col3">
        <div style="font-size:10px;color:#2a2220;margin-bottom:4px;">肋軟骨</div>
        <p>耳軟骨より安定している。石灰化（固くなる）が起きることがある。</p>
      </div>
    </div>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 6: 骨切り・貴族・猫手術 -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">SPECIAL PROCEDURES</span><span class="ph-num">05</span></div>
  <h1>骨切り幅寄せ・貴族手術・猫手術</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:14px;">OSTEOTOMY / NOBLE / CAT SURGERY</div>

  <div class="info-block" style="border-left:3px solid #c4a06a;margin-bottom:14px;">
    <h3>骨切り幅寄せ（オステオトミー）とは</h3>
    <p style="margin-bottom:8px;">鼻の骨（鼻骨）を切って、鼻の幅を狭くする手術です。「鼻が太い」「鼻根が広い」「正面から見たときに鼻の幅が気になる」という方に適応します。</p>
    <div class="two-col">
      <div class="col-l">
        <div style="font-size:8px;color:#c4a06a;margin-bottom:5px;">手術の流れ</div>
        <p>鼻の内側から切開し、専用の器具で鼻骨を左右から骨切りして幅を寄せます。外側の小さな傷（耳の付け根あたり）も使う場合があります。プロテーゼと同時に行うことが多いです。</p>
      </div>
      <div class="col-r">
        <div style="font-size:8px;color:#c4a06a;margin-bottom:5px;">ダウンタイム</div>
        <p>腫れが強く出ます。鼻周りのむくみが2〜4週間続くことがある。ギプス固定が必要です。「鼻が骨折したのと同じ状態」と思ってください。</p>
      </div>
    </div>
    <div class="note-box" style="margin-top:8px;margin-bottom:0;">
      <div class="note-head">先生のひとこと</div>
      <p>骨切りはダウンタイムが長めなのが正直なところです。「プロテーゼだけで印象が変わる場合」と「骨を動かす必要がある場合」はカウンセリングで見極めます。</p>
    </div>
  </div>

  <div class="two-col">
    <div class="col-l">
      <div class="info-block" style="border-left:3px solid #c4a06a;height:auto;">
        <h3>貴族手術（鼻翼基部プロテーゼ）とは</h3>
        <p>鼻の付け根（鼻翼基部）にプロテーゼを挿入して、横顔の奥行きと立体感を出す施術。「貴族」という名前の通り、横顔に品格が生まれます。</p>
        <div style="margin-top:8px;">
          <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">こんな方に</div>
          <p>・横顔がのっぺりして見える<br>・鼻の付け根が顔に埋まって見える<br>・輪郭を引き締めて見せたい<br>・中顔面を上に引き上げて見せたい</p>
        </div>
      </div>
    </div>
    <div class="col-r">
      <div class="info-block" style="height:auto;">
        <h3>猫手術（鼻孔縁挙上）とは</h3>
        <p>鼻孔縁（鼻の穴の縁）を上に引き上げる施術。正面から見たときに鼻の穴が目立つ方（鼻孔縁が下がっている方）に適応。猫が目を細めたようなシルエットになることからこの呼び名がついた。</p>
        <div style="margin-top:8px;">
          <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">こんな方に</div>
          <p>・正面から鼻の穴が目立つ<br>・鼻の穴の縁が下がっている<br>・ACR（鼻柱-小鼻の高さ関係）を整えたい</p>
        </div>
      </div>
    </div>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 7: 肋軟骨移植 -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">RIB CARTILAGE GRAFT</span><span class="ph-num">06</span></div>
  <h1>肋軟骨移植について</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:14px;">WHAT IT IS / SCAR / DOWNTIME</div>

  <div class="two-col">
    <div class="col-l">
      <div class="info-block" style="border-left:3px solid #c4a06a;margin-bottom:12px;">
        <h3>肋軟骨移植とは</h3>
        <p>胸の肋骨から軟骨を採取し、鼻の形成に使う方法。耳軟骨では量が足りない、大幅な変化が必要なケースに適応します。自家組織（自分の組織）なので感染リスクが低く、大量の軟骨が得られます。</p>
      </div>
      <div class="info-block" style="margin-bottom:12px;">
        <h3>どんな場合に使う？</h3>
        <p>・鼻先を大幅に延長したい<br>・鼻中隔延長に大量の軟骨が必要<br>・他院修正で耳軟骨が使えない<br>・拘縮鼻の根本的な改善<br>・「大きな変化が必要なケース」</p>
      </div>
      <div class="info-block">
        <h3>傷はどんな感じ？</h3>
        <p>胸の肋骨の側面（乳房下ライン付近）を2〜3cm切開して採取します。傷は時間とともに薄くなっていきますが、完全に消えるわけではありません。下着や水着で隠れる位置です。</p>
      </div>
    </div>
    <div class="col-r">
      <div class="svgwrap" style="margin-bottom:12px;">
        <div class="sv-title">肋軟骨の採取部位（正面図イメージ）</div>
        <svg viewBox="0 0 160 200" xmlns="http://www.w3.org/2000/svg" width="100%">
          <!-- Torso outline -->
          <path d="M 40,10 C 30,30 20,60 20,100 C 20,150 40,180 80,195 C 120,180 140,150 140,100 C 140,60 130,30 120,10 Z"
            fill="#f5ece0" stroke="#c4a06a" stroke-width="1.2" opacity="0.6"/>
          <!-- Collar bones -->
          <path d="M 60,20 Q 80,26 100,20" stroke="#c4a06a" stroke-width="1" fill="none" opacity="0.4"/>
          <!-- Rib cage lines (simplified) -->
          <path d="M 50,50 Q 80,58 110,50" stroke="#c4a06a" stroke-width="0.8" fill="none" opacity="0.3"/>
          <path d="M 46,65 Q 80,74 114,65" stroke="#c4a06a" stroke-width="0.8" fill="none" opacity="0.3"/>
          <path d="M 42,80 Q 80,90 118,80" stroke="#c4a06a" stroke-width="0.8" fill="none" opacity="0.3"/>
          <path d="M 38,95 Q 80,106 122,95" stroke="#c4a06a" stroke-width="0.8" fill="none" opacity="0.3"/>
          <!-- Scar location indicator (right side, below breast) -->
          <ellipse cx="52" cy="108" rx="12" ry="5" fill="#c4a06a" opacity="0.3"/>
          <line x1="64" y1="108" x2="100" y2="108" stroke="#c4a06a" stroke-width="0.8" stroke-dasharray="3,2"/>
          <text x="102" y="112" font-size="7" fill="#c4a06a">採取部位</text>
          <text x="102" y="121" font-size="6.5" fill="#aaa">約2〜3cm切開</text>
          <text x="102" y="130" font-size="6.5" fill="#aaa">下着で隠れる位置</text>
          <!-- Red scar line (simulated) -->
          <path d="M 44,108 L 60,108" stroke="#c4a06a" stroke-width="2.5" stroke-linecap="round" opacity="0.7"/>
        </svg>
      </div>
      <div class="note-box">
        <div class="note-head">肋軟骨は全身麻酔が必要</div>
        <p>肋軟骨移植を行う場合は、体の複数箇所を同時に操作するため全身麻酔が必要です。その他の鼻整形（プロテーゼ・鼻尖縮小・小鼻縮小など）は静脈麻酔で対応できます。</p>
      </div>
    </div>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 8: 麻酔について -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">ANESTHESIA</span><span class="ph-num">07</span></div>
  <h1>麻酔について</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:14px;">IV SEDATION vs GENERAL ANESTHESIA</div>

  <div class="two-col">
    <div class="col-l">
      <div class="info-block" style="border-left:3px solid #c4a06a;margin-bottom:12px;">
        <h3>静脈麻酔（点滴で眠る方法）</h3>
        <p style="margin-bottom:8px;">点滴から鎮静剤・鎮痛剤を投与して眠る方法。呼吸は自分で行っています。局所麻酔も追加して痛みをしっかりブロックします。</p>
        <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">対応施術</div>
        <p>プロテーゼ・鼻尖縮小・ストラット・小鼻縮小・骨切り・貴族手術・猫手術・耳軟骨移植など多くの鼻整形</p>
        <div style="margin-top:8px;">
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">眠っているので痛みを感じない</div></div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">回復が比較的早い（1〜2時間で帰宅可）</div></div>
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">吐き気が少ない</div></div>
        </div>
      </div>
    </div>
    <div class="col-r">
      <div class="info-block" style="margin-bottom:12px;">
        <h3>全身麻酔（気管挿管を使う方法）</h3>
        <p style="margin-bottom:8px;">気管にチューブを挿入して機械で呼吸を管理する、深い麻酔。完全に意識がなくなります。</p>
        <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">対応施術</div>
        <p>肋軟骨移植を含む手術（体の複数箇所を同時に操作するため）</p>
        <div style="margin-top:8px;">
          <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">深い麻酔で完全に意識がない</div></div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">術後に気分が悪くなることがある</div></div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">回復に時間がかかる（半日程度）</div></div>
          <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">術前の絶食が必要（前日夜から）</div></div>
        </div>
      </div>
    </div>
  </div>

  <div style="background:#fff;border:1px solid #e8dece;padding:12px 14px;margin-top:4px;">
    <div style="font-size:8px;color:#c4a06a;letter-spacing:1px;margin-bottom:8px;">まとめ：どちらを使う？</div>
    <div class="cmp-head">
      <div class="cmp-label" style="padding-left:8px;"> </div>
      <div class="cmp-a" style="color:#c4a06a;font-size:8px;">静脈麻酔</div>
      <div class="cmp-b" style="font-size:8px;">全身麻酔</div>
    </div>
    <div class="cmp-row"><div class="cmp-label">呼吸</div><div class="cmp-a">自分でしている</div><div class="cmp-b">機械で管理</div></div>
    <div class="cmp-row"><div class="cmp-label">意識</div><div class="cmp-a">ない（眠っている）</div><div class="cmp-b">完全にない</div></div>
    <div class="cmp-row"><div class="cmp-label">回復時間</div><div class="cmp-a">1〜2時間</div><div class="cmp-b">3〜5時間以上</div></div>
    <div class="cmp-row"><div class="cmp-label">使用場面</div><div class="cmp-a">ほとんどの鼻整形</div><div class="cmp-b">肋軟骨移植を含む手術</div></div>
  </div>

  <div class="note-box" style="margin-top:12px;">
    <div class="note-head">先生のひとこと</div>
    <p>「麻酔が怖い」という方が多いですが、静脈麻酔は安全性が高く、翌日にはほぼ普通の生活が送れます。肋軟骨を使わない場合は全身麻酔は不要です。麻酔についても遠慮なく質問してください。</p>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 9: ギプス・ダウンタイム・職場復帰 -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">RECOVERY & DOWNTIME</span><span class="ph-num">08</span></div>
  <h1>ダウンタイム・職場復帰のリアル</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:14px;">HONEST RECOVERY GUIDE</div>

  <div class="two-col">
    <div class="col-l">
      <div style="font-size:10px;color:#c4a06a;margin-bottom:10px;letter-spacing:1px;">ギプス固定について</div>
      <div class="info-block" style="margin-bottom:12px;">
        <p>プロテーゼを挿入した場合、術後1週間は鼻にギプスを装着します。<br><br>
        <strong style="font-size:9.5px;">見た目：</strong>白いテープ状のギプスが鼻に貼られた状態。マスクで一部は隠せますが、完全には隠せません。外出時はマスク＋帽子＋サングラスが定番です。<br><br>
        <strong style="font-size:9.5px;">7日後：</strong>抜糸とギプス除去。腫れはまだあるが、見た目がかなり改善します。</p>
      </div>

      <div style="font-size:10px;color:#c4a06a;margin-bottom:10px;letter-spacing:1px;">職場復帰の目安</div>
      <div class="info-block">
        <div style="margin-bottom:8px;">
          <div style="font-size:9px;color:#2a2220;margin-bottom:3px;">事務職・在宅勤務</div>
          <p>翌日〜3日程度から可能なことが多い。ギプス装着中でも業務可能。</p>
        </div>
        <div style="margin-bottom:8px;">
          <div style="font-size:9px;color:#2a2220;margin-bottom:3px;">接客・対面業務</div>
          <p>ギプス除去後（7日〜）が目安。腫れが残っていることは伝えておく。</p>
        </div>
        <div>
          <div style="font-size:9px;color:#2a2220;margin-bottom:3px;">肉体労働・激しい運動</div>
          <p>1ヶ月程度の休止が必要。血圧上昇が腫れに影響するため。</p>
        </div>
      </div>
    </div>
    <div class="col-r">
      <div style="font-size:10px;color:#c4a06a;margin-bottom:10px;letter-spacing:1px;">リアルな経過タイムライン</div>

      <div class="tl-row"><div class="tl-day">当日</div><div class="tl-bar"></div><div class="tl-body"><h4>施術直後</h4><p>腫れはまだ少ない。麻酔が切れると痛みが出る。処方の痛み止めで対応。</p></div></div>
      <div class="tl-row"><div class="tl-day">1〜3日</div><div class="tl-bar"></div><div class="tl-body"><h4>腫れのピーク ★一番つらい時期</h4><p>顔が大きく見える。内出血（紫色）が出ることも。冷やすと効果的。</p></div></div>
      <div class="tl-row"><div class="tl-day">4〜6日</div><div class="tl-bar"></div><div class="tl-body"><h4>腫れが引き始める</h4><p>内出血の色が黄色・緑色に変わり始める。痛みはほぼなくなる。</p></div></div>
      <div class="tl-row"><div class="tl-day">7日</div><div class="tl-bar"></div><div class="tl-body"><h4>抜糸・ギプス除去</h4><p>腫れはまだあるが人前に出られるレベルに。ほっとする時期。</p></div></div>
      <div class="tl-row"><div class="tl-day">2週間〜</div><div class="tl-bar muted"></div><div class="tl-body"><h4>ほぼ普通の生活</h4><p>まだむくみはある。「腫れてる？」と言われる時期が続く。</p></div></div>
      <div class="tl-row"><div class="tl-day">1〜3ヶ月</div><div class="tl-bar muted"></div><div class="tl-body"><h4>完成形へ</h4><p>むくみが取れ「これが自分の鼻か」という感覚になる。</p></div></div>

      <div class="note-box" style="margin-top:4px;">
        <div class="note-head">先生のひとこと</div>
        <p>「思ったより腫れた」という声はよく聞きます。術後1〜3日はピークなので、その期間に予定を入れないようにしてください。</p>
      </div>
    </div>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 10: よくある不安Q&A -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">COMMON QUESTIONS</span><span class="ph-num">09</span></div>
  <h1>よくある不安と質問</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:18px;">FREQUENTLY ASKED QUESTIONS</div>

  <div class="two-col">
    <div class="col-l">
      <div class="qa">
        <div class="qa-q">整形したことはバレますか？</div>
        <p class="qa-a">自然なデザインを選べば、ほとんどの場合バレません。「高くしすぎない」「鼻先を細くしすぎない」ことがポイントです。クローズド法なら外側に傷も残らないので、よりバレにくい仕上がりになります。</p>
      </div>
      <div class="qa">
        <div class="qa-q">プロテーゼは将来取り出せますか？</div>
        <p class="qa-a">はい、取り出せます。ただし長期間経過後は周囲組織に癒着が起きることがあります。修正・除去を希望する場合は早めにご相談ください。</p>
      </div>
      <div class="qa">
        <div class="qa-q">耳軟骨だけで鼻を高くできますか？</div>
        <p class="qa-a">1〜3mm程度が限界です。「鼻筋をしっかり作りたい」「大きく変えたい」という場合はプロテーゼまたは肋軟骨移植が必要になります。正直にお伝えします。</p>
      </div>
      <div class="qa">
        <div class="qa-q">複数の施術を同時に受けられますか？</div>
        <p class="qa-a">可能です。組み合わせることで、より自然なバランスが得られることも多いです。施術時間・ダウンタイムの増加を考慮した上でご提案します。</p>
      </div>
      <div class="qa">
        <div class="qa-q">施術を断られることはありますか？</div>
        <p class="qa-a">あります。リスクが高い・期待に応えられない・今の状態では不適と判断した場合はお断りします。それも医師としての仕事だと考えています。</p>
      </div>
    </div>
    <div class="col-r">
      <div class="qa">
        <div class="qa-q">他院で施術した鼻の修正はできますか？</div>
        <p class="qa-a">対応しています。まず現状の状態を診断し、何ができるかをお伝えします。状態によっては「今は修正しない方がいい」とお伝えすることもあります。</p>
      </div>
      <div class="qa">
        <div class="qa-q">鼻整形後、スポーツや運動はいつからできますか？</div>
        <p class="qa-a">軽いウォーキング程度は2週間後から。激しい運動（筋トレ・格闘技・水泳など）は1ヶ月以上空けてください。血圧が上がると腫れが悪化します。</p>
      </div>
      <div class="qa">
        <div class="qa-q">メイクはいつからできますか？</div>
        <p class="qa-a">施術部位以外は翌日から可能です。鼻周りは抜糸後（7日後〜）を目安にしてください。</p>
      </div>
      <div class="qa">
        <div class="qa-q">痛みはどのくらいありますか？</div>
        <p class="qa-a">麻酔が切れた後、当日〜翌日に鈍い痛みがあります。処方された痛み止めで対応できるレベルです。「想像より痛くなかった」という方が多いです。</p>
      </div>
      <div class="qa">
        <div class="qa-q">鼻をかんでいいですか？</div>
        <p class="qa-a">術後2週間は禁止です。鼻をかむと鼻の内側にかかる圧力が大きく、出血・腫れの悪化につながります。鼻水が出る場合は拭くだけにしてください。</p>
      </div>
    </div>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 11: 横顔の美しさ / おでこ・あご -->
<!-- ============================================================ -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">SIDE PROFILE BEAUTY</span><span class="ph-num">10</span></div>
  <h1>理想の横顔 — おでこ・鼻・あごの3点</h1>
  <div style="font-size:8px;letter-spacing:2px;color:#bbb;margin-bottom:12px;">FOREHEAD · NOSE · CHIN HARMONY</div>

  <div class="svgwrap" style="margin-bottom:12px;">
    <div class="sv-title">横顔バランス比較（Eライン = 鼻先〜あご先の基準線）</div>
    <svg viewBox="0 0 460 168" xmlns="http://www.w3.org/2000/svg" width="100%">
      <rect width="460" height="168" fill="#fff"/>
      <!-- Labels -->
      <text x="100" y="13" font-size="9" fill="#888" text-anchor="middle" font-family="serif">鼻だけ整形した場合</text>
      <text x="354" y="13" font-size="9" fill="#c4a06a" text-anchor="middle" font-family="serif">3点が整った横顔（理想）</text>
      <line x1="228" y1="4" x2="228" y2="165" stroke="#e8dece" stroke-width="1" stroke-dasharray="4,3"/>

      <!-- ===== LEFT PANEL: 鼻だけ ===== -->
      <!-- Profile: flat forehead, good nose, recessed chin -->
      <path d="M 84,20 C 91,24 93,38 92,50 C 91,60 86,67 82,73 C 78,79 77,89 81,96 C 85,103 100,108 106,112 C 99,120 91,125 92,132 C 92,138 91,145 88,151 C 86,156 83,161 77,165"
        fill="none" stroke="#bbb" stroke-width="2.2" stroke-linecap="round"/>
      <!-- Forehead dot: flat (hollow) -->
      <circle cx="93" cy="35" r="5" fill="#ede0cc" stroke="#ccc" stroke-width="1.5"/>
      <text x="22" y="31" font-size="7" fill="#999" font-family="serif">おでこ</text>
      <text x="22" y="40" font-size="7" fill="#999" font-family="serif">（平ら）</text>
      <line x1="46" y1="35" x2="88" y2="35" stroke="#ddd" stroke-width="0.8"/>
      <!-- Nose dot: gold (done) -->
      <circle cx="106" cy="112" r="5" fill="#c4a06a" opacity="0.8"/>
      <text x="115" y="110" font-size="7" fill="#c4a06a">鼻（完了）</text>
      <!-- Chin dot: hollow (recessed) -->
      <circle cx="88" cy="151" r="5" fill="#ede0cc" stroke="#ccc" stroke-width="1.5"/>
      <text x="22" y="147" font-size="7" fill="#999" font-family="serif">あご</text>
      <text x="22" y="156" font-size="7" fill="#999" font-family="serif">（後退）</text>
      <line x1="44" y1="151" x2="83" y2="151" stroke="#ddd" stroke-width="0.8"/>
      <!-- E-line left (misaligned) -->
      <line x1="106" y1="112" x2="88" y2="151" stroke="#ddd" stroke-width="1.5" stroke-dasharray="5,3"/>
      <text x="150" y="132" font-size="6.5" fill="#ccc" text-anchor="middle">E-line</text>
      <text x="150" y="140" font-size="6.5" fill="#ccc" text-anchor="middle">（ずれている）</text>

      <!-- ===== RIGHT PANEL: 3点バランス ===== -->
      <!-- Profile: projected forehead, good nose, projected chin -->
      <path d="M 292,20 C 304,22 320,33 323,47 C 325,59 320,67 314,73 C 309,79 308,89 312,96 C 316,103 332,108 338,112 C 331,120 323,125 323,132 C 323,138 324,145 324,151 C 324,158 320,163 313,165"
        fill="none" stroke="#c4a06a" stroke-width="2.2" stroke-linecap="round"/>
      <!-- Forehead dot: projected gold -->
      <circle cx="323" cy="40" r="5" fill="#c4a06a" opacity="0.8"/>
      <text x="238" y="36" font-size="7" fill="#c4a06a">おでこ</text>
      <text x="238" y="45" font-size="7" fill="#c4a06a">脂肪注入</text>
      <line x1="268" y1="40" x2="318" y2="40" stroke="#c4a06a" stroke-width="0.8" opacity="0.5"/>
      <!-- Nose dot: gold (same) -->
      <circle cx="338" cy="112" r="5" fill="#c4a06a" opacity="0.8"/>
      <text x="348" y="110" font-size="7" fill="#c4a06a">鼻整形</text>
      <!-- Chin dot: projected gold -->
      <circle cx="324" cy="151" r="5" fill="#c4a06a" opacity="0.8"/>
      <text x="238" y="147" font-size="7" fill="#c4a06a">あご</text>
      <text x="238" y="156" font-size="7" fill="#c4a06a">ヒアルロン酸</text>
      <line x1="266" y1="151" x2="319" y2="151" stroke="#c4a06a" stroke-width="0.8" opacity="0.5"/>
      <!-- E-line right (clean) -->
      <line x1="338" y1="112" x2="324" y2="151" stroke="#c4a06a" stroke-width="1.8" stroke-dasharray="5,3"/>
      <text x="388" y="132" font-size="6.5" fill="#c4a06a" text-anchor="middle">E-line</text>
      <text x="388" y="140" font-size="6.5" fill="#c4a06a" text-anchor="middle">（整った）</text>
      <!-- 3-point beauty triangle -->
      <path d="M 323,40 L 338,112 L 324,151" stroke="#c4a06a" stroke-width="0.8" fill="none" stroke-dasharray="4,4" opacity="0.4"/>
    </svg>
  </div>

  <div class="two-col" style="margin-bottom:10px;">
    <div class="col-l">
      <div class="info-block" style="border-left:3px solid #c4a06a;">
        <h3>おでこの脂肪注入</h3>
        <p style="margin-bottom:8px;">自分の脂肪（お腹・太ももなど）を採取・精製してデザイン注入。シリコンを使わないため異物感がなく、自然な丸みを作れます。</p>
        <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">横顔への効果</div>
        <p style="margin-bottom:7px;">おでこに丸みが出ると横顔の「奥行き」が生まれ、鼻との連動で全体の立体感が増します。のっぺりした顔が一気に「彫りの深い印象」に変わります。</p>
        <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">自分の組織なので自然な仕上がり</div></div>
        <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">定着した脂肪は長期間維持される</div></div>
        <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">鼻整形と同日施術が可能</div></div>
        <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">10〜30%程度の吸収が起きることがある</div></div>
        <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">採取部位にも小さな傷が残る</div></div>
      </div>
    </div>
    <div class="col-r">
      <div class="info-block">
        <h3>あごのヒアルロン酸</h3>
        <p style="margin-bottom:8px;">注射であごにヒアルロン酸を注入し、あご先を前・下方向に出す方法。手術不要、施術10〜20分、即日帰宅できます。</p>
        <div style="font-size:8px;color:#c4a06a;margin-bottom:4px;">横顔への効果</div>
        <p style="margin-bottom:7px;">鼻先とあご先を結ぶEラインが整い、横顔がシャープに。顔が縦に伸びて見え、スタイルアップ効果も。鼻整形との相乗効果が非常に高い施術です。</p>
        <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">手術なし、注射のみで即効性</div></div>
        <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">鼻整形との組み合わせで横顔が劇的に変わる</div></div>
        <div class="merit-row"><div class="merit-label">◎</div><div class="merit-text">Eライン・小顔・Vライン効果</div></div>
        <div class="merit-row"><div class="demerit-label">△</div><div class="merit-text">効果は12〜18ヶ月程度、定期メンテナンスが必要</div></div>
      </div>
    </div>
  </div>

  <div class="note-box">
    <div class="note-head">先生のひとこと — 横顔について</div>
    <p>「鼻を整えたのに、なんか物足りない」という声をよく聞きます。原因はたいていおでこかあごです。鼻だけが突き出た横顔は、実はバランスが悪い。おでこの丸みとあごの出方がセットで整うと、横顔の完成度が全然ちがいます。とくにあごのヒアルロン酸は手術なしで即効性があるので、鼻整形と合わせてやる方が非常に多いです。「鼻と一緒にやりたい」という方はカウンセリングで気軽に相談してください。</p>
  </div>
</div></div>

<!-- ============================================================ -->
<!-- PAGE 12: CLOSING -->
<!-- ============================================================ -->
<div class="page">
<div class="closing-page"><div class="closing-inner">
  <div style="font-size:7px;letter-spacing:5px;color:#c4a06a;margin-bottom:44px;">ZETITH BEAUTY CLINIC FUKUOKA</div>
  <div style="font-family:Georgia,serif;font-style:italic;font-size:32px;color:#fff;line-height:1.7;margin-bottom:18px;">
    迷っていることは<br>全部、聞いてください。
  </div>
  <div style="font-size:10px;color:#777;line-height:2.2;margin-bottom:50px;">
    このガイドで不明な点があれば、次のカウンセリングで。<br>
    「決めなければいけない」という場ではありません。<br>
    ゆっくり考えて、納得してから進みましょう。
  </div>
  <div style="width:40px;height:1px;background:#c4a06a;margin:0 auto 30px;"></div>
  <div style="font-size:7px;letter-spacing:3px;color:#c4a06a;margin-bottom:5px;">INSTAGRAM</div>
  <div style="font-size:13px;color:#aaa;margin-bottom:18px;">@zetith_hane</div>
  <div style="font-size:7px;letter-spacing:3px;color:#c4a06a;margin-bottom:5px;">CLINIC</div>
  <div style="font-size:12px;color:#aaa;">Zetith Beauty Clinic 福岡院</div>
</div></div>
</div>

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/鼻整形_患者ガイドブック.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
