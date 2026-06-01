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
.page { width: 210mm; min-height: 297mm; background: #f9f7f3; page-break-after: always; }

/* COVER */
.cover { width:210mm; height:297mm; background:#f9f7f3; display:table; text-align:center; }
.cover-inner { display:table-cell; vertical-align:middle; padding:20mm; }
.cover-script { font-family:Georgia,serif; font-style:italic; font-size:50px; font-weight:400; color:#2a2220; line-height:1.3; margin-bottom:8px; }
.cover-script span { color:#c8a060; }
.gold-bar { width:50px; height:1px; background:#c8a060; margin:20px auto; }
.cover-ja { font-size:13px; color:#6a5840; letter-spacing:2px; margin-bottom:5px; }
.cover-sub { font-size:8.5px; color:#bbb; letter-spacing:1px; margin-bottom:56px; }
.cover-name { font-size:14px; color:#c8a060; letter-spacing:3px; margin-bottom:6px; }
.cover-clinic { font-size:8px; color:#aaa; letter-spacing:2px; }

/* CONTENT */
.cp { padding:11mm 16mm 10mm; min-height:297mm; }
.ph { border-bottom:1px solid #c8a060; padding-bottom:6px; margin-bottom:19px; overflow:hidden; }
.ph-label { float:left; font-size:7px; letter-spacing:3px; color:#c8a060; }
.ph-num { float:right; font-size:8px; color:#ccc; }
h2.stitle { font-size:22px; font-weight:300; color:#2a2220; margin-bottom:3px; }
.sen { font-size:7px; letter-spacing:3px; color:#bbb; margin-bottom:18px; }

/* STRENGTH CARDS */
.str-grid { overflow:hidden; }
.str-card { float:left; width:47%; background:#fff; border:1px solid #e8dece; padding:13px; min-height:86px; margin-bottom:12px; }
.str-card:nth-child(odd) { margin-right:6%; }
.str-num { font-family:Georgia,serif; font-style:italic; font-size:26px; color:#e8d0a0; line-height:1; margin-bottom:3px; }
.str-card h3 { font-size:10.5px; color:#c8a060; margin-bottom:5px; font-weight:400; }
.str-card p { font-size:8.5px; color:#666; line-height:1.8; }

/* CLOSED METHOD */
.closed-hero { background:#2a2220; padding:18px 22px; margin-bottom:18px; }
.hero-en { font-size:7px; letter-spacing:4px; color:#c8a060; margin-bottom:5px; }
.hero-title { font-family:Georgia,serif; font-style:italic; font-size:26px; color:#fff; margin-bottom:4px; }
.hero-sub { font-size:9px; color:#888; line-height:1.9; }
.trend-badge { display:inline-block; background:#c8a060; color:#fff; font-size:7.5px; padding:4px 14px; border-radius:20px; margin-top:10px; letter-spacing:1px; }
table.compare { width:100%; border-collapse:collapse; margin-bottom:16px; font-size:8.5px; }
table.compare th { background:#c8a060; color:#fff; padding:7px 8px; font-weight:400; letter-spacing:1px; font-size:8px; }
table.compare th:first-child { background:#2a2220; }
table.compare td { padding:7px 10px; border-bottom:1px solid #ede8e0; color:#555; line-height:1.6; }
table.compare td:first-child { color:#c8a060; font-size:7.5px; letter-spacing:1px; background:#fdf9f3; }
table.compare td.win { color:#2a2220; }
table.compare td.muted { color:#aaa; }

/* CATALOG */
.cat-head { text-align:center; padding:8px 0 12px; }
.cat-script { font-family:Georgia,serif; font-style:italic; font-size:34px; color:#2a2220; line-height:1; margin-bottom:5px; }
.cat-amp { color:#c8a060; }
.cat-ribbon { border-top:1px solid #c8a060; border-bottom:1px solid #c8a060; padding:5px 20px; display:inline-block; font-size:8.5px; color:#6a5840; letter-spacing:1px; margin-top:4px; }
.cols3 { overflow:hidden; margin-top:12px; }
.col3 { float:left; width:30%; margin-right:5%; text-align:center; }
.col3:last-child { margin-right:0; }
.dtag { display:block; background:#c8a060; color:#fff; border-radius:20px; padding:5px 0; font-size:10.5px; margin-bottom:7px; }
.ddesc { font-size:8px; color:#555; line-height:1.7; margin-bottom:9px; min-height:28px; }
.bef-lbl { font-size:7px; letter-spacing:2px; color:#aaa; margin-bottom:3px; }
.bef-circle { width:76px; height:76px; border-radius:50%; background:#e0dbd0; border:1px solid #c8a060; margin:0 auto 3px; line-height:76px; font-size:6.5px; color:#bbb; }
.aft-lbl { font-family:Georgia,serif; font-style:italic; font-size:10px; color:#c8a060; margin-bottom:3px; }
.aft-rect { height:84px; background:#1a1a1a; border:1px solid #333; text-align:center; padding-top:34px; margin-bottom:7px; font-size:6.5px; color:#444; }
.dhashtag { display:inline-block; font-size:7px; color:#8a7060; background:#f0e8d8; border-radius:10px; padding:3px 10px; }
.cat-note { background:#fff; border-left:3px solid #c8a060; padding:11px 14px; margin-top:14px; font-size:8.5px; color:#666; line-height:1.9; }
.cat-note-lbl { font-size:7.5px; color:#c8a060; letter-spacing:1px; margin-bottom:5px; }

/* TYPE GUIDE */
.type-block { overflow:hidden; margin-bottom:16px; background:#fff; border:1px solid #e8dece; }
.type-bar { float:left; width:24%; min-height:96px; display:table; background:#c8a060; }
.type-bar-inner { display:table-cell; vertical-align:middle; padding:10px 12px; text-align:center; }
.type-bar-en { font-family:Georgia,serif; font-style:italic; font-size:15px; color:#fff; display:block; margin-bottom:3px; }
.type-bar-ja { font-size:8px; color:rgba(255,255,255,0.8); }
.type-body { overflow:hidden; padding:11px 14px; }
.type-body h4 { font-size:10px; color:#2a2220; margin-bottom:5px; }
.type-body p { font-size:8px; color:#666; line-height:1.85; margin-bottom:6px; }
.ttag { display:inline-block; font-size:6.5px; color:#c8a060; border:1px solid #c8a060; border-radius:10px; padding:2px 7px; margin-right:5px; margin-bottom:3px; }

/* CLOSING */
.closing { width:210mm; height:297mm; background:#2a2220; display:table; text-align:center; }
.closing-inner { display:table-cell; vertical-align:middle; padding:20mm; }
.cl-script { font-family:Georgia,serif; font-style:italic; font-size:28px; color:#fff; margin-bottom:14px; line-height:1.6; }
.cl-sub { font-size:9px; color:#777; line-height:2.1; margin-bottom:44px; }
.cl-bar { width:40px; height:1px; background:#c8a060; margin:0 auto 28px; }
.cl-lbl { font-size:7px; letter-spacing:3px; color:#c8a060; margin-bottom:4px; }
.cl-val { font-size:11px; color:#aaa; margin-bottom:16px; }

/* SVG CONTAINER */
.svg-box { background:#fff; border:1px solid #e8dece; padding:14px; margin-bottom:16px; }
.svg-title { font-size:8px; letter-spacing:2px; color:#c8a060; margin-bottom:10px; }
</style>
</head>
<body>

<!-- ============================== COVER ============================== -->
<div class="page">
<div class="cover"><div class="cover-inner">
  <div class="cover-script">Nose <span>&amp;</span> Design</div>
  <div class="cover-sub">RHINOPLASTY COUNSELING GUIDE</div>
  <div class="gold-bar"></div>
  <div class="cover-ja">鼻整形 カウンセリングガイド</div>
  <div class="cover-sub" style="margin-bottom:56px;margin-top:4px;">あなたの理想のデザインを、一緒に選びましょう。</div>
  <div class="cover-name">羽根 和秀</div>
  <div class="cover-clinic">Zetith Beauty Clinic Fukuoka</div>
</div></div>
</div>

<!-- ============================== 羽根先生の強み ============================== -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">DOCTOR'S STRENGTHS</span><span class="ph-num">01</span></div>
  <h2 class="stitle">羽根先生の強み</h2>
  <div class="sen">WHAT MAKES DR. HANE DIFFERENT</div>

  <div class="str-grid">
    <div class="str-card"><div class="str-num">01</div>
      <h3>クローズド法のスペシャリスト</h3>
      <p>外側に傷を残さないクローズド法を専門としています。高い技術が必要な術式ですが、ダウンタイムが短く自然な仕上がりのため、現在最も需要の高い技術です。</p>
    </div>
    <div class="str-card"><div class="str-num">02</div>
      <h3>顔全体のデザイン設計力</h3>
      <p>鼻の形・高さ・向きだけでなく、顔全体のバランスを見た上でデザインを設計します。「整形した感」が出ない自然な仕上がりにこだわっています。</p>
    </div>
    <div class="str-card"><div class="str-num">03</div>
      <h3>正直なカウンセリング</h3>
      <p>「しないほうがいい」「今はまだ早い」と伝えることも仕事のうち。患者さんが納得した上で選択できるよう、リスクと代替案を丁寧に説明します。</p>
    </div>
    <div class="str-card"><div class="str-num">04</div>
      <h3>他院修正・拘縮鼻対応</h3>
      <p>他院での施術後の修正に積極的に対応します。状態を正確に診断し、「何ができるか・できないか」を正直にお伝えした上でプランを提案します。</p>
    </div>
  </div>

  <div style="background:#fff;border:1px solid #e8dece;padding:13px 16px;margin-top:4px;">
    <div style="font-size:7.5px;color:#c8a060;letter-spacing:2px;margin-bottom:7px;">SNS実績</div>
    <div style="font-size:9px;color:#555;line-height:1.9;">Instagram @zetith_hane のプロフィール閲覧数は月8.4万人。SNS経由での予約が月10件以上。入職半年での実績です。</div>
  </div>
</div></div>

<!-- ============================== クローズド法 + SVG ============================== -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">CLOSED RHINOPLASTY</span><span class="ph-num">02</span></div>
  <h2 class="stitle">クローズド法とは</h2>
  <div class="sen">WHY IT'S THE TRENDING TECHNIQUE</div>

  <div class="closed-hero">
    <div class="hero-en">CLOSED APPROACH RHINOPLASTY</div>
    <div class="hero-title">傷が残らない。バレない。</div>
    <div class="hero-sub">すべての切開を鼻の内側だけで行う術式。外側に一切傷が残らず「整形した」とわからない仕上がりになります。</div>
    <span class="trend-badge">★ 現在最もトレンドの術式</span>
  </div>

  <!-- SVG: Closed vs Open incision diagram -->
  <div class="svg-box">
    <div class="svg-title">切開部位の比較図（鼻の下から見た図）</div>
    <svg viewBox="0 0 360 155" xmlns="http://www.w3.org/2000/svg" width="100%">
      <!-- LEFT: Open Method -->
      <text x="90" y="14" font-size="10" fill="#888" text-anchor="middle" font-family="serif">オープン法</text>
      <!-- Outer nose oval -->
      <ellipse cx="90" cy="82" rx="60" ry="52" fill="#f5ece0" stroke="#c8a060" stroke-width="1.2"/>
      <!-- Left nostril -->
      <ellipse cx="64" cy="86" rx="20" ry="24" fill="#ded0bc" stroke="#b8944a" stroke-width="1"/>
      <!-- Right nostril -->
      <ellipse cx="116" cy="86" rx="20" ry="24" fill="#ded0bc" stroke="#b8944a" stroke-width="1"/>
      <!-- Columella strip -->
      <rect x="85" y="60" width="10" height="44" rx="5" fill="#f0dcc0" stroke="#c8a060" stroke-width="0.8"/>
      <!-- Red incision line on columella (open method) -->
      <line x1="90" y1="63" x2="90" y2="100" stroke="#d05040" stroke-width="3" stroke-linecap="round"/>
      <circle cx="90" cy="63" r="3" fill="#d05040"/>
      <circle cx="90" cy="100" r="3" fill="#d05040"/>
      <!-- Labels -->
      <text x="90" y="126" font-size="8" fill="#d05040" text-anchor="middle">鼻柱に切開線が入る</text>
      <text x="90" y="137" font-size="8" fill="#d05040" text-anchor="middle">→ 小さな傷が残る</text>
      <text x="90" y="148" font-size="7.5" fill="#d05040" text-anchor="middle">（時間とともに薄くなる）</text>

      <!-- Divider -->
      <line x1="180" y1="8" x2="180" y2="150" stroke="#e8dece" stroke-width="1.2" stroke-dasharray="5,4"/>

      <!-- RIGHT: Closed Method -->
      <text x="270" y="14" font-size="10" fill="#c8a060" text-anchor="middle" font-family="serif">クローズド法</text>
      <!-- Outer nose oval -->
      <ellipse cx="270" cy="82" rx="60" ry="52" fill="#f5ece0" stroke="#c8a060" stroke-width="1.2"/>
      <!-- Left nostril -->
      <ellipse cx="244" cy="86" rx="20" ry="24" fill="#ded0bc" stroke="#b8944a" stroke-width="1"/>
      <!-- Right nostril -->
      <ellipse cx="296" cy="86" rx="20" ry="24" fill="#ded0bc" stroke="#b8944a" stroke-width="1"/>
      <!-- Columella strip -->
      <rect x="265" y="60" width="10" height="44" rx="5" fill="#f0dcc0" stroke="#c8a060" stroke-width="0.8"/>
      <!-- Gold dashed lines inside each nostril (internal incisions) -->
      <path d="M 232,72 A 10,12 0 0 1 236,100" stroke="#c8a060" stroke-width="2.5" fill="none" stroke-dasharray="5,3" stroke-linecap="round"/>
      <path d="M 308,72 A 10,12 0 0 0 304,100" stroke="#c8a060" stroke-width="2.5" fill="none" stroke-dasharray="5,3" stroke-linecap="round"/>
      <!-- Gold dots -->
      <circle cx="232" cy="72" r="3" fill="#c8a060"/>
      <circle cx="236" cy="100" r="3" fill="#c8a060"/>
      <circle cx="308" cy="72" r="3" fill="#c8a060"/>
      <circle cx="304" cy="100" r="3" fill="#c8a060"/>
      <!-- No cut badge on columella -->
      <text x="270" y="86" font-size="7" fill="#aaa" text-anchor="middle">切開なし</text>
      <!-- Labels -->
      <text x="270" y="126" font-size="8" fill="#c8a060" text-anchor="middle">切開は鼻の内側のみ</text>
      <text x="270" y="137" font-size="8" fill="#c8a060" text-anchor="middle">→ 外側に傷が残らない</text>
      <text x="270" y="148" font-size="7.5" fill="#c8a060" text-anchor="middle">（＝バレない）</text>
    </svg>
  </div>

  <table class="compare">
    <tr><th></th><th>クローズド法 ★推奨</th><th>オープン法</th></tr>
    <tr><td>外側の傷</td><td class="win">なし（完全に内側のみ）</td><td class="muted">鼻柱に小さな傷が残る</td></tr>
    <tr><td>ダウンタイム</td><td class="win">短め（5〜7日）</td><td class="muted">やや長め（7〜10日）</td></tr>
    <tr><td>腫れ</td><td class="win">比較的少ない</td><td class="muted">やや多い</td></tr>
    <tr><td>術者への要求</td><td class="muted">高い技術力が必要</td><td class="win">視野が広く操作しやすい</td></tr>
    <tr><td>適応</td><td class="win">多くの鼻整形に対応</td><td class="win">複雑な修正に強い</td></tr>
  </table>
</div></div>

<!-- ============================== ANATOMY PAGE ============================== -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">NOSE ANATOMY</span><span class="ph-num">03</span></div>
  <h2 class="stitle">鼻の解剖図</h2>
  <div class="sen">UNDERSTANDING THE STRUCTURE OF YOUR NOSE</div>

  <!-- SVG: Side profile anatomy -->
  <div class="svg-box" style="margin-bottom:14px;">
    <div class="svg-title">側面図 — 各部位の名称と施術の関係</div>
    <svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg" width="100%">
      <!-- Background -->
      <rect width="500" height="220" fill="#ffffff"/>

      <!-- Face vertical reference line -->
      <line x1="260" y1="10" x2="260" y2="210" stroke="#ede8e0" stroke-width="1.5" stroke-dasharray="6,4"/>
      <text x="265" y="205" font-size="7" fill="#ccc">顔のライン</text>

      <!-- NOSE SILHOUETTE (filled) -->
      <path d="M 258,28 C 252,46 238,72 218,98 Q 200,116 206,132 C 214,144 240,148 258,146"
        fill="#f5ece0" stroke="#c8a060" stroke-width="2" fill-opacity="0.7"/>

      <!-- LABELED POINTS -->

      <!-- 1. 鼻根 (Nasion) -->
      <circle cx="258" cy="28" r="4" fill="#c8a060"/>
      <line x1="262" y1="28" x2="340" y2="18" stroke="#c8a060" stroke-width="0.8"/>
      <text x="344" y="16" font-size="10" fill="#2a2220" font-family="serif">鼻根（びこん）</text>
      <text x="344" y="27" font-size="7.5" fill="#999">眉間〜鼻の始まり</text>
      <text x="344" y="37" font-size="7.5" fill="#bbb">▸ プロテーゼで高くする</text>

      <!-- 2. 鼻背 (Dorsum/Bridge) -->
      <circle cx="232" cy="68" r="4" fill="#c8a060"/>
      <line x1="228" y1="68" x2="80" y2="55" stroke="#c8a060" stroke-width="0.8"/>
      <text x="10" y="50" font-size="10" fill="#2a2220" font-family="serif">鼻背（鼻筋）</text>
      <text x="10" y="61" font-size="7.5" fill="#999">鼻の高さの稜線</text>
      <text x="10" y="71" font-size="7.5" fill="#bbb">▸ プロテーゼの主な作用部位</text>

      <!-- 3. 鼻先 (Tip) -->
      <circle cx="200" cy="118" r="4" fill="#c8a060"/>
      <line x1="196" y1="118" x2="80" y2="112" stroke="#c8a060" stroke-width="0.8"/>
      <text x="10" y="107" font-size="10" fill="#2a2220" font-family="serif">鼻先（鼻尖）</text>
      <text x="10" y="118" font-size="7.5" fill="#999">最も前に出た点</text>
      <text x="10" y="128" font-size="7.5" fill="#bbb">▸ ストラット・軟骨で形成</text>

      <!-- 4. 鼻柱 (Columella) -->
      <circle cx="226" cy="140" r="4" fill="#c8a060"/>
      <line x1="230" y1="140" x2="340" y2="155" stroke="#c8a060" stroke-width="0.8"/>
      <text x="344" y="153" font-size="10" fill="#2a2220" font-family="serif">鼻柱（コルメラ）</text>
      <text x="344" y="164" font-size="7.5" fill="#999">両鼻孔の間の柱</text>
      <text x="344" y="174" font-size="7.5" fill="#bbb">▸ ACR改善・鼻中隔延長</text>

      <!-- 5. 鼻唇角 (Nasolabial angle) -->
      <!-- Columella direction line -->
      <line x1="206" y1="132" x2="192" y2="110" stroke="#8a8a8a" stroke-width="1" stroke-dasharray="4,3"/>
      <!-- Vertical line -->
      <line x1="206" y1="132" x2="206" y2="160" stroke="#8a8a8a" stroke-width="1" stroke-dasharray="4,3"/>
      <!-- Angle arc -->
      <path d="M 206,146 A 16,16 0 0 0 198,126" fill="none" stroke="#c8a060" stroke-width="1.8"/>
      <text x="155" y="162" font-size="9" fill="#c8a060">鼻唇角</text>
      <text x="152" y="173" font-size="7.5" fill="#999">デザインの核心</text>

      <!-- Small nose silhouette lines (alar) -->
      <path d="M 205,132 Q 196,138 200,148 Q 206,152 215,150" fill="none" stroke="#c8a060" stroke-width="1.5" opacity="0.5"/>
      <path d="M 205,132 Q 218,138 216,148 Q 210,152 215,150" fill="none" stroke="#c8a060" stroke-width="1.5" opacity="0.5"/>
    </svg>
  </div>

  <!-- SVG: Front view anatomy -->
  <div class="svg-box">
    <div class="svg-title">正面図 — 小鼻・鼻幅・鼻孔縁の関係</div>
    <svg viewBox="0 0 500 130" xmlns="http://www.w3.org/2000/svg" width="100%">
      <rect width="500" height="130" fill="#ffffff"/>

      <!-- Nose front silhouette (simplified) -->
      <!-- Outer shape -->
      <path d="M 220,10 C 218,28 210,55 196,80 Q 188,96 192,108 Q 200,118 220,118 L 260,118 Q 280,118 288,108 Q 292,96 284,80 C 270,55 262,28 260,10 Z"
        fill="#f5ece0" stroke="#c8a060" stroke-width="1.5" fill-opacity="0.7"/>

      <!-- Left nostril -->
      <ellipse cx="208" cy="100" rx="14" ry="12" fill="#ded0bc" stroke="#b8944a" stroke-width="1"/>
      <!-- Right nostril -->
      <ellipse cx="272" cy="100" rx="14" ry="12" fill="#ded0bc" stroke="#b8944a" stroke-width="1"/>
      <!-- Columella (center) -->
      <rect x="236" y="78" width="8" height="32" rx="4" fill="#e8d8c0" stroke="#c8a060" stroke-width="0.8"/>

      <!-- Nose bridge center line -->
      <line x1="240" y1="10" x2="240" y2="75" stroke="#c8a060" stroke-width="0.8" stroke-dasharray="3,2" opacity="0.5"/>

      <!-- Width measurement lines -->
      <line x1="192" y1="108" x2="288" y2="108" stroke="#c8a060" stroke-width="0.8" stroke-dasharray="3,2"/>
      <line x1="192" y1="104" x2="192" y2="112" stroke="#c8a060" stroke-width="1"/>
      <line x1="288" y1="104" x2="288" y2="112" stroke="#c8a060" stroke-width="1"/>
      <text x="240" y="125" font-size="8" fill="#c8a060" text-anchor="middle">小鼻の幅（縮小対象）</text>

      <!-- Labels -->
      <!-- 鼻先 -->
      <circle cx="240" cy="68" r="3.5" fill="#c8a060"/>
      <line x1="240" y1="64" x2="160" y2="48" stroke="#c8a060" stroke-width="0.8"/>
      <text x="80" y="44" font-size="9" fill="#2a2220">鼻先</text>
      <text x="80" y="54" font-size="7.5" fill="#bbb">▸ ストラット</text>

      <!-- 小鼻 -->
      <circle cx="194" cy="90" r="3.5" fill="#c8a060"/>
      <line x1="190" y1="90" x2="140" y2="80" stroke="#c8a060" stroke-width="0.8"/>
      <text x="60" y="78" font-size="9" fill="#2a2220">小鼻（鼻翼）</text>
      <text x="60" y="88" font-size="7.5" fill="#bbb">▸ 小鼻縮小</text>

      <!-- 鼻孔縁 -->
      <circle cx="286" cy="90" r="3.5" fill="#c8a060"/>
      <line x1="290" y1="90" x2="340" y2="78" stroke="#c8a060" stroke-width="0.8"/>
      <text x="344" y="75" font-size="9" fill="#2a2220">鼻孔縁</text>
      <text x="344" y="85" font-size="7.5" fill="#bbb">▸ 鼻孔縁挙上</text>

      <!-- 鼻根 top -->
      <circle cx="240" cy="16" r="3.5" fill="#c8a060"/>
      <line x1="244" y1="16" x2="330" y2="14" stroke="#c8a060" stroke-width="0.8"/>
      <text x="334" y="18" font-size="9" fill="#2a2220">鼻根</text>
    </svg>
  </div>
</div></div>

<!-- ============================== DESIGN TYPE GUIDE + SVG ============================== -->
<div class="page"><div class="cp">
  <div class="ph"><span class="ph-label">NOSE TIP DESIGN GUIDE</span><span class="ph-num">04</span></div>
  <h2 class="stitle">鼻先のデザイン比較</h2>
  <div class="sen">UPTURNED / STRAIGHT / ROUND</div>

  <!-- SVG: Three nose profiles comparison -->
  <div class="svg-box" style="margin-bottom:14px;">
    <div class="svg-title">鼻唇角の違いによるデザイン比較（側面シルエット）</div>
    <svg viewBox="0 0 480 160" xmlns="http://www.w3.org/2000/svg" width="100%">
      <rect width="480" height="160" fill="#ffffff"/>

      <!-- ===== 1. アップノーズ (left, offset 0) ===== -->
      <g transform="translate(10,0)">
        <!-- Title -->
        <text x="72" y="14" font-size="10" fill="#c8a060" text-anchor="middle" font-family="serif">アップノーズ</text>
        <!-- Face reference line -->
        <line x1="115" y1="18" x2="115" y2="145" stroke="#ede8e0" stroke-width="1.2" stroke-dasharray="5,4"/>
        <!-- Nose profile path -->
        <path d="M 113,22 C 108,36 98,58 82,80 Q 70,92 74,104 C 80,114 102,117 113,115"
          fill="#f5ece0" stroke="#c8a060" stroke-width="2.2" fill-opacity="0.6"/>
        <!-- Angle dashed lines from columella base -->
        <line x1="76" y1="106" x2="62" y2="84" stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
        <line x1="76" y1="106" x2="76" y2="135" stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
        <!-- Angle arc -->
        <path d="M 76,118 A 14,14 0 0 0 68,96" fill="none" stroke="#c8a060" stroke-width="1.8"/>
        <!-- Angle text -->
        <text x="42" y="130" font-size="9" fill="#c8a060">105〜115°</text>
        <!-- Design badge -->
        <rect x="22" y="140" width="100" height="15" rx="7" fill="#f5e8d8"/>
        <text x="72" y="151" font-size="7.5" fill="#8a7060" text-anchor="middle">Baby &amp; Cute 系</text>
        <!-- Arrow showing tip direction -->
        <line x1="70" y1="96" x2="56" y2="80" stroke="#c8a060" stroke-width="1.5" stroke-dasharray="3,2"/>
        <polygon points="56,80 62,82 60,88" fill="#c8a060"/>
      </g>

      <!-- Divider 1 -->
      <line x1="170" y1="10" x2="170" y2="150" stroke="#e8dece" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- ===== 2. ストレート (center, offset 165) ===== -->
      <g transform="translate(165,0)">
        <text x="77" y="14" font-size="10" fill="#6a7060" text-anchor="middle" font-family="serif">ストレート</text>
        <line x1="120" y1="18" x2="120" y2="145" stroke="#ede8e0" stroke-width="1.2" stroke-dasharray="5,4"/>
        <path d="M 118,22 C 112,37 100,61 82,85 Q 68,100 72,114 C 79,124 104,126 118,124"
          fill="#f5ece0" stroke="#6a7060" stroke-width="2.2" fill-opacity="0.6"/>
        <!-- Angle lines -->
        <line x1="72" y1="114" x2="56" y2="90" stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
        <line x1="72" y1="114" x2="72" y2="143" stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
        <!-- Angle arc -->
        <path d="M 72,126 A 14,14 0 0 0 62,106" fill="none" stroke="#6a7060" stroke-width="1.8"/>
        <text x="42" y="140" font-size="9" fill="#6a7060">90〜95°</text>
        <!-- Badge -->
        <rect x="27" y="148" width="100" height="15" rx="7" fill="#f0ede8"/>
        <text x="77" y="159" font-size="7.5" fill="#8a8a7a" text-anchor="middle">Elegant 系・忘れ鼻</text>
        <!-- Arrow straight forward -->
        <line x1="68" y1="100" x2="52" y2="98" stroke="#6a7060" stroke-width="1.5" stroke-dasharray="3,2"/>
        <polygon points="52,98 59,95 59,101" fill="#6a7060"/>
      </g>

      <!-- Divider 2 -->
      <line x1="332" y1="10" x2="332" y2="150" stroke="#e8dece" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- ===== 3. ラウンド (right, offset 328) ===== -->
      <g transform="translate(328,0)">
        <text x="72" y="14" font-size="10" fill="#8a6a50" text-anchor="middle" font-family="serif">ラウンド</text>
        <line x1="115" y1="18" x2="115" y2="145" stroke="#ede8e0" stroke-width="1.2" stroke-dasharray="5,4"/>
        <path d="M 113,22 C 107,37 96,62 77,87 Q 62,103 68,117 C 76,128 104,130 113,128"
          fill="#f5ece0" stroke="#8a6a50" stroke-width="2.2" fill-opacity="0.6"/>
        <!-- Bigger tip radius marker -->
        <circle cx="64" cy="106" r="12" fill="none" stroke="#8a6a50" stroke-width="1" stroke-dasharray="3,2" opacity="0.6"/>
        <!-- Angle lines -->
        <line x1="68" y1="117" x2="52" y2="93" stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
        <line x1="68" y1="117" x2="68" y2="147" stroke="#aaa" stroke-width="1" stroke-dasharray="4,3"/>
        <!-- Angle arc -->
        <path d="M 68,130 A 14,14 0 0 0 57,110" fill="none" stroke="#8a6a50" stroke-width="1.8"/>
        <text x="38" y="142" font-size="9" fill="#8a6a50">95〜105°</text>
        <!-- Badge -->
        <rect x="22" y="148" width="100" height="15" rx="7" fill="#eeebe6"/>
        <text x="72" y="159" font-size="7.5" fill="#8a8078" text-anchor="middle">自然・大人美人</text>
        <!-- Curve radius label -->
        <text x="44" y="100" font-size="7" fill="#8a6a50" opacity="0.8">丸み</text>
      </g>
    </svg>
  </div>

  <!-- Three type explanation blocks -->
  <div class="type-block">
    <div class="type-bar"><div class="type-bar-inner">
      <span class="type-bar-en">Up Nose</span>
      <span class="type-bar-ja">アップノーズ</span>
    </div></div>
    <div class="type-body">
      <h4>鼻先が上を向いた、可愛らしいデザイン</h4>
      <p>鼻唇角（鼻と上唇の間の角度）を大きくすることで鼻先が上向きになります。中顔面が短縮して見え、あざと可愛い印象に。やりすぎると「豚鼻」になるリスクがあるため、角度のすり合わせが重要です。</p>
      <span class="ttag">Baby &amp; Cute系</span><span class="ttag">中顔面短縮</span><span class="ttag">クローズド法◎</span>
    </div>
  </div>
  <div class="type-block">
    <div class="type-bar" style="background:#6a7060;"><div class="type-bar-inner">
      <span class="type-bar-en">Straight</span>
      <span class="type-bar-ja">ストレート</span>
    </div></div>
    <div class="type-body">
      <h4>鼻筋から鼻先まで一直線の、忘れ鼻デザイン</h4>
      <p>最も「整形した感」が出にくいデザイン。横顔の品格が増し、どんな顔型にも馴染みます。「バレたくない」「自然に綺麗になりたい」方に圧倒的に人気です。</p>
      <span class="ttag">Elegant系</span><span class="ttag">忘れ鼻</span><span class="ttag">クローズド法◎</span>
    </div>
  </div>
  <div class="type-block">
    <div class="type-bar" style="background:#8a6a50;"><div class="type-bar-inner">
      <span class="type-bar-en">Round</span>
      <span class="type-bar-ja">ラウンド</span>
    </div></div>
    <div class="type-body">
      <h4>鼻先に自然な丸みを持たせた、柔らかいデザイン</h4>
      <p>過度にシャープにせず、自然な丸みを残したデザイン。半ラウンドは大人の色気、フルラウンドは柔らかさ・優しさを演出します。シャープにしすぎると不自然に見える方に特に向いています。</p>
      <span class="ttag">Elegant〜Cute系</span><span class="ttag">半ラウンド</span><span class="ttag">大人美人</span>
    </div>
  </div>
</div></div>

<!-- ============================== Baby & Cute ============================== -->
<div class="page"><div class="cp" style="padding-top:10mm;">
  <div class="cat-head">
    <div class="cat-script">Baby <span class="cat-amp">&amp;</span> Cute</div>
    <div class="cat-ribbon">- "中顔面短縮"と"あざと可愛さ"を重視したデザイン -</div>
  </div>
  <div class="cols3">
    <div class="col3">
      <span class="dtag">アップノーズ</span>
      <div class="ddesc">鼻先を斜め上方向へ。<br>可愛らしく若々しい<br>印象になります。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#あざと可愛い</span>
    </div>
    <div class="col3">
      <span class="dtag">中顔面短縮</span>
      <div class="ddesc">鼻先の向きと高さで<br>顔の縦幅を短く<br>見せるデザイン。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#小顔効果</span>
    </div>
    <div class="col3">
      <span class="dtag">ACR改善</span>
      <div class="ddesc">鼻柱を下ろしながら<br>小鼻は上げる。<br>正面の印象を整える。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#バランス改善</span>
    </div>
  </div>
  <div class="cat-note"><div class="cat-note-lbl">このカテゴリについて</div>クローズド法で対応可能なケースが多く、ダウンタイムを短くしながら可愛らしい印象を作れます。鼻先の向きは数ミリの差で印象が大きく変わるため、カウンセリングでのすり合わせが重要です。</div>
</div></div>

<!-- ============================== Elegant & Straight ============================== -->
<div class="page"><div class="cp" style="padding-top:10mm;">
  <div class="cat-head">
    <div class="cat-script">Elegant <span class="cat-amp">&amp;</span> Straight</div>
    <div class="cat-ribbon">- "忘れ鼻"と"横顔の品格"を追求したナチュラル美デザイン -</div>
  </div>
  <div class="cols3">
    <div class="col3">
      <span class="dtag">ストレート</span>
      <div class="ddesc">鼻筋から鼻先まで<br>一直線のライン。<br>最も整形感が出にくい。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#忘れ鼻</span>
    </div>
    <div class="col3">
      <span class="dtag">半ラウンド</span>
      <div class="ddesc">自然な丸みを残しながら<br>品のある印象に。<br>大人な雰囲気へ。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#大人美人</span>
    </div>
    <div class="col3">
      <span class="dtag">短鼻解消</span>
      <div class="ddesc">鼻が上を向いた状態を<br>改善。自然な向きと<br>高さを実現。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#立体感</span>
    </div>
  </div>
  <div class="cat-note"><div class="cat-note-lbl">このカテゴリについて</div>「整形したことを気づかれたくない」「自然に綺麗になりたい」方に最も選ばれるカテゴリです。クローズド法との相性が非常に良く、忘れ鼻（自然すぎて気づかれない鼻）は羽根先生が特に得意とするデザインです。</div>
</div></div>

<!-- ============================== Dramatic & Glamorous ============================== -->
<div class="page"><div class="cp" style="padding-top:10mm;">
  <div class="cat-head">
    <div class="cat-script">Dramatic <span class="cat-amp">&amp;</span> Glamorous</div>
    <div class="cat-ribbon">- "圧倒的な高さ"と"Eライン"を完成させるフルオーダーデザイン -</div>
  </div>
  <div class="cols3">
    <div class="col3">
      <span class="dtag">シャープ鼻</span>
      <div class="ddesc">鼻筋から鼻先まで<br>シャープな印象に。<br>団子鼻を解消。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#ハーフ顔</span>
    </div>
    <div class="col3">
      <span class="dtag">Eライン</span>
      <div class="ddesc">横顔の美しさを<br>完成させる設計。<br>口元の突出感も軽減。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#Eライン</span>
    </div>
    <div class="col3">
      <span class="dtag">貴族手術</span>
      <div class="ddesc">鼻翼基部を持ち上げ<br>横顔に奥行きを演出。<br>存在感のある顔に。</div>
      <div class="bef-lbl">BEFORE</div><div class="bef-circle">写真</div>
      <div class="aft-lbl">After</div><div class="aft-rect">写真挿入</div>
      <span class="dhashtag">#存在感</span>
    </div>
  </div>
  <div class="cat-note"><div class="cat-note-lbl">このカテゴリについて</div>大きな変化を望む方向けのカテゴリです。プロテーゼ・軟骨移植・鼻中隔延長など複合的な施術が多く、場合によってはオープン法や肋軟骨移植が必要になります。ダウンタイムは長めですが、完成時の変化も最も大きいカテゴリです。</div>
</div></div>

<!-- ============================== CLOSING ============================== -->
<div class="page">
<div class="closing"><div class="closing-inner">
  <div style="font-size:7px;letter-spacing:5px;color:#c8a060;margin-bottom:40px;">ZETITH BEAUTY CLINIC FUKUOKA</div>
  <div class="cl-script">今日、どんな鼻に<br>なりたいですか？</div>
  <div class="cl-sub">デザインのイメージが固まっていなくても大丈夫です。<br>「なんとなくこんな印象になりたい」から一緒に考えます。<br>決めなければいけない場ではありません。</div>
  <div class="cl-bar"></div>
  <div class="cl-lbl">INSTAGRAM</div>
  <div class="cl-val">@zetith_hane</div>
  <div class="cl-lbl">CLINIC</div>
  <div class="cl-val">Zetith Beauty Clinic 福岡院</div>
</div></div>
</div>

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/鼻整形_カウンセリング資料v4.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
