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

/* ── BASE ── */
.page {
  width: 210mm;
  min-height: 297mm;
  background: #f9f7f3;
  page-break-after: always;
  position: relative;
}

/* ── COVER ── */
.cover {
  width: 210mm; height: 297mm;
  background: #f9f7f3;
  display: table; text-align: center;
}
.cover-inner { display: table-cell; vertical-align: middle; padding: 20mm; }
.cover-script {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 52px;
  font-weight: 400;
  color: #2a2220;
  line-height: 1.3;
  margin-bottom: 8px;
}
.cover-script span { color: #c8a060; }
.cover-gold-bar {
  width: 60px; height: 1px;
  background: #c8a060;
  margin: 20px auto;
}
.cover-ja {
  font-size: 13px;
  color: #6a5840;
  letter-spacing: 2px;
  margin-bottom: 6px;
}
.cover-sub {
  font-size: 9px;
  color: #aaa;
  letter-spacing: 1px;
  margin-bottom: 60px;
}
.cover-name {
  font-size: 14px;
  color: #c8a060;
  letter-spacing: 3px;
  margin-bottom: 6px;
}
.cover-clinic {
  font-size: 8px;
  color: #aaa;
  letter-spacing: 2px;
}

/* ── CONTENT PAGE ── */
.cp { padding: 12mm 16mm 10mm; min-height: 297mm; }
.ph {
  border-bottom: 1px solid #c8a060;
  padding-bottom: 6px;
  margin-bottom: 20px;
  overflow: hidden;
}
.ph-label { float: left; font-size: 7px; letter-spacing: 3px; color: #c8a060; }
.ph-num { float: right; font-size: 8px; color: #ccc; }
h2.stitle { font-size: 22px; font-weight: 300; color: #2a2220; margin-bottom: 3px; }
.sen { font-size: 7px; letter-spacing: 3px; color: #bbb; margin-bottom: 20px; }

/* ── STRENGTH CARDS ── */
.str-grid { overflow: hidden; margin-bottom: 16px; }
.str-card {
  float: left;
  width: 47%;
  background: #fff;
  border: 1px solid #e8dece;
  padding: 14px;
  min-height: 90px;
  margin-bottom: 14px;
}
.str-card:nth-child(odd) { margin-right: 6%; }
.str-card-num {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 28px;
  color: #e8d0a0;
  line-height: 1;
  margin-bottom: 4px;
}
.str-card h3 {
  font-size: 11px;
  color: #c8a060;
  margin-bottom: 6px;
  font-weight: 400;
}
.str-card p {
  font-size: 8.5px;
  color: #666;
  line-height: 1.8;
}

/* ── CLOSED METHOD ── */
.closed-hero {
  background: #2a2220;
  padding: 20px 24px;
  margin-bottom: 20px;
}
.closed-hero-en {
  font-size: 7px;
  letter-spacing: 4px;
  color: #c8a060;
  margin-bottom: 6px;
}
.closed-hero-title {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 28px;
  color: #fff;
  margin-bottom: 4px;
}
.closed-hero-sub {
  font-size: 9px;
  color: #888;
  line-height: 1.8;
}
.trend-badge {
  display: inline-block;
  background: #c8a060;
  color: #fff;
  font-size: 8px;
  padding: 4px 14px;
  border-radius: 20px;
  margin-top: 10px;
  letter-spacing: 1px;
}

.compare-table { width: 100%; border-collapse: collapse; margin-bottom: 18px; }
.compare-table th {
  background: #c8a060;
  color: #fff;
  font-size: 9px;
  padding: 8px;
  font-weight: 400;
  letter-spacing: 1px;
}
.compare-table th:first-child { background: #2a2220; }
.compare-table td {
  font-size: 8.5px;
  color: #555;
  padding: 8px 10px;
  border-bottom: 1px solid #ede8e0;
  line-height: 1.7;
}
.compare-table td:first-child {
  color: #c8a060;
  font-size: 8px;
  letter-spacing: 1px;
  background: #fdf9f3;
}
.compare-table td.win {
  color: #2a2220;
  font-weight: normal;
}
.compare-table td.neutral { color: #aaa; }

.closed-merit { overflow: hidden; }
.merit-item {
  float: left;
  width: 30%;
  margin-right: 5%;
  text-align: center;
  padding: 14px 10px;
  background: #fff;
  border: 1px solid #e8dece;
}
.merit-item:last-child { margin-right: 0; }
.merit-icon {
  font-size: 22px;
  color: #c8a060;
  margin-bottom: 6px;
}
.merit-label {
  font-size: 9px;
  color: #2a2220;
  margin-bottom: 4px;
}
.merit-note {
  font-size: 7.5px;
  color: #999;
  line-height: 1.6;
}

/* ── DESIGN CATALOG ── */
.catalog-header {
  text-align: center;
  padding: 10px 0 14px;
  position: relative;
}
.catalog-script {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 36px;
  color: #2a2220;
  line-height: 1;
  margin-bottom: 6px;
}
.catalog-amp { color: #c8a060; }
.catalog-ribbon {
  border-top: 1px solid #c8a060;
  border-bottom: 1px solid #c8a060;
  padding: 5px 20px;
  display: inline-block;
  font-size: 8.5px;
  color: #6a5840;
  letter-spacing: 1px;
  margin-top: 4px;
}

.design-cols { overflow: hidden; margin-top: 14px; }
.design-col {
  float: left;
  width: 30%;
  margin-right: 5%;
  text-align: center;
}
.design-col:last-child { margin-right: 0; }
.dtag {
  display: block;
  background: #c8a060;
  color: #fff;
  border-radius: 20px;
  padding: 5px 0;
  font-size: 10.5px;
  margin-bottom: 7px;
  letter-spacing: 0.5px;
}
.ddesc {
  font-size: 8px;
  color: #555;
  line-height: 1.7;
  margin-bottom: 10px;
  min-height: 30px;
}
.before-label {
  font-size: 7px;
  letter-spacing: 2px;
  color: #aaa;
  margin-bottom: 4px;
}
.before-circle {
  width: 80px; height: 80px;
  border-radius: 50%;
  background: #e0dbd0;
  border: 1px solid #c8a060;
  margin: 0 auto 4px;
  line-height: 80px;
  font-size: 7px;
  color: #bbb;
}
.after-label {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 11px;
  color: #c8a060;
  margin-bottom: 4px;
}
.after-rect {
  height: 90px;
  background: #1a1a1a;
  border: 1px solid #333;
  text-align: center;
  padding-top: 38px;
  margin-bottom: 7px;
  font-size: 7px;
  color: #444;
}
.dhashtag {
  display: inline-block;
  font-size: 7.5px;
  color: #8a7060;
  background: #f0e8d8;
  border-radius: 12px;
  padding: 3px 10px;
}

/* ── DESIGN TYPE GUIDE ── */
.type-block {
  overflow: hidden;
  margin-bottom: 18px;
  background: #fff;
  border: 1px solid #e8dece;
}
.type-label-bar {
  background: #c8a060;
  color: #fff;
  padding: 8px 14px;
  font-size: 12px;
  float: left;
  width: 26%;
  min-height: 100px;
  display: table;
}
.type-label-inner { display: table-cell; vertical-align: middle; }
.type-label-en {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 16px;
  display: block;
  margin-bottom: 3px;
}
.type-label-ja { font-size: 9px; color: rgba(255,255,255,0.8); }
.type-content { overflow: hidden; padding: 12px 14px; }
.type-content h4 {
  font-size: 10px;
  color: #2a2220;
  margin-bottom: 5px;
}
.type-content p {
  font-size: 8.5px;
  color: #666;
  line-height: 1.9;
  margin-bottom: 6px;
}
.type-tags { overflow: hidden; }
.type-tag {
  float: left;
  font-size: 7px;
  color: #c8a060;
  border: 1px solid #c8a060;
  border-radius: 10px;
  padding: 2px 8px;
  margin-right: 6px;
  margin-bottom: 4px;
}

/* ── CLOSING ── */
.closing {
  width: 210mm; height: 297mm;
  background: #2a2220;
  display: table; text-align: center;
}
.closing-inner { display: table-cell; vertical-align: middle; padding: 20mm; }
.closing-script {
  font-family: Georgia, serif;
  font-style: italic;
  font-size: 30px;
  color: #fff;
  margin-bottom: 14px;
  line-height: 1.5;
}
.closing-sub { font-size: 9.5px; color: #888; line-height: 2.1; margin-bottom: 48px; }
.closing-gold-bar { width: 40px; height: 1px; background: #c8a060; margin: 0 auto 30px; }
.cinfo-label { font-size: 7px; letter-spacing: 3px; color: #c8a060; margin-bottom: 4px; }
.cinfo-val { font-size: 11px; color: #aaa; margin-bottom: 18px; }

</style>
</head>
<body>

<!-- ========== COVER ========== -->
<div class="page">
<div class="cover">
<div class="cover-inner">
  <div class="cover-script">Nose<br><span>&amp;</span> Design</div>
  <div class="cover-sub">RHINOPLASTY COUNSELING GUIDE</div>
  <div class="cover-gold-bar"></div>
  <div class="cover-ja">鼻整形 カウンセリングガイド</div>
  <div class="cover-sub" style="margin-bottom:60px; margin-top:4px;">あなたの理想のデザインを、一緒に選びましょう。</div>
  <div class="cover-name">羽根 和秀</div>
  <div class="cover-clinic">Zetith Beauty Clinic Fukuoka</div>
</div>
</div>
</div>

<!-- ========== 羽根先生の強み ========== -->
<div class="page">
<div class="cp">
  <div class="ph"><span class="ph-label">DOCTOR'S STRENGTHS</span><span class="ph-num">01</span></div>
  <h2 class="stitle">羽根先生の強み</h2>
  <div class="sen">WHAT MAKES DR. HANE DIFFERENT</div>

  <div class="str-grid">
    <div class="str-card">
      <div class="str-card-num">01</div>
      <h3>クローズド法のスペシャリスト</h3>
      <p>外側に傷を残さないクローズド法を得意としています。高い技術が必要な術式ですが、ダウンタイムが短く仕上がりが自然なため、現在最もニーズの高い技術です。</p>
    </div>
    <div class="str-card">
      <div class="str-card-num">02</div>
      <h3>デザイン設計力</h3>
      <p>鼻の形・高さ・向きだけでなく、顔全体のバランスを見た上でデザインを設計します。「整形した感」が出ない自然な仕上がりにこだわっています。</p>
    </div>
    <div class="str-card">
      <div class="str-card-num">03</div>
      <h3>正直なカウンセリング</h3>
      <p>「しないほうがいい」「今はまだ早い」と伝えることも仕事のうち。リスクと代替案を丁寧に説明した上で、患者さんが納得した選択ができる場を作ります。</p>
    </div>
    <div class="str-card">
      <div class="str-card-num">04</div>
      <h3>他院修正・拘縮鼻の対応</h3>
      <p>他院での施術後の修正・やり直しに積極的に対応します。状態を正確に診断し、「何ができるか・できないか」を正直にお伝えします。</p>
    </div>
  </div>

  <div style="background:#fff; border:1px solid #e8dece; padding:14px 18px; margin-top:8px;">
    <div style="font-size:8px; color:#c8a060; letter-spacing:2px; margin-bottom:8px;">SNS実績</div>
    <div style="font-size:9px; color:#555; line-height:1.9;">
      Instagram @zetith_hane のプロフィール閲覧数は月8.4万人。<br>
      SNS経由での予約が月10件以上。入職半年での実績です。
    </div>
  </div>
</div>
</div>

<!-- ========== クローズド法 ========== -->
<div class="page">
<div class="cp">
  <div class="ph"><span class="ph-label">CLOSED RHINOPLASTY</span><span class="ph-num">02</span></div>
  <h2 class="stitle">クローズド法とは</h2>
  <div class="sen">WHY IT'S THE TRENDING TECHNIQUE</div>

  <div class="closed-hero">
    <div class="closed-hero-en">CLOSED APPROACH RHINOPLASTY</div>
    <div class="closed-hero-title">傷が残らない。<br>バレない。</div>
    <div class="closed-hero-sub">すべての切開を鼻の内側だけで行う術式です。<br>外側に一切傷が残らないため、「整形した」とわからない仕上がりになります。</div>
    <span class="trend-badge">★ 現在最もトレンドの術式です</span>
  </div>

  <table class="compare-table">
    <tr>
      <th></th>
      <th>クローズド法</th>
      <th>オープン法</th>
    </tr>
    <tr>
      <td>外側の傷</td>
      <td class="win">なし（完全に内側）</td>
      <td class="neutral">鼻柱に小さな傷が残る</td>
    </tr>
    <tr>
      <td>ダウンタイム</td>
      <td class="win">短め（5〜7日）</td>
      <td class="neutral">やや長め（7〜10日）</td>
    </tr>
    <tr>
      <td>腫れの程度</td>
      <td class="win">比較的少ない</td>
      <td class="neutral">やや多い</td>
    </tr>
    <tr>
      <td>手術時間</td>
      <td class="win">短め（45〜90分）</td>
      <td class="neutral">長め（1.5〜3時間）</td>
    </tr>
    <tr>
      <td>術者への要求</td>
      <td class="neutral">高い技術力が必要</td>
      <td class="win">視野が広く操作しやすい</td>
    </tr>
    <tr>
      <td>適応範囲</td>
      <td class="win">鼻尖・鼻筋・小鼻の多くに対応</td>
      <td class="win">複雑な修正に強い</td>
    </tr>
  </table>

  <div class="closed-merit">
    <div class="merit-item">
      <div class="merit-icon">◎</div>
      <div class="merit-label">バレない</div>
      <div class="merit-note">外側に傷が<br>一切残りません</div>
    </div>
    <div class="merit-item">
      <div class="merit-icon">◎</div>
      <div class="merit-label">早い回復</div>
      <div class="merit-note">仕事への復帰が<br>オープン法より早い</div>
    </div>
    <div class="merit-item">
      <div class="merit-icon">◎</div>
      <div class="merit-label">自然な仕上がり</div>
      <div class="merit-note">腫れが少なく<br>完成が早い</div>
    </div>
  </div>
</div>
</div>

<!-- ========== DESIGN CATALOG 1: Baby & Cute ========== -->
<div class="page">
<div class="cp" style="padding-top: 10mm;">
  <div class="catalog-header">
    <div class="catalog-script">Baby <span class="catalog-amp">&amp;</span> Cute</div>
    <div class="catalog-ribbon">- "中顔面短縮"と"あざと可愛さ"を重視したデザイン -</div>
  </div>

  <div class="design-cols">
    <div class="design-col">
      <span class="dtag">アップノーズ</span>
      <div class="ddesc">鼻先を斜め上方向へ。<br>可愛らしく若々しい<br>印象になります。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#あざと可愛い</span>
    </div>
    <div class="design-col">
      <span class="dtag">中顔面短縮</span>
      <div class="ddesc">鼻先の向きと高さで<br>顔の縦幅を短く<br>見せるデザイン。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#小顔効果</span>
    </div>
    <div class="design-col">
      <span class="dtag">ACR改善</span>
      <div class="ddesc">鼻柱を下ろしながら<br>小鼻は上げる。<br>正面の印象を整える。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#バランス改善</span>
    </div>
  </div>

  <div style="background:#fff; border-left:3px solid #c8a060; padding:12px 16px; margin-top:18px;">
    <div style="font-size:8px; color:#c8a060; margin-bottom:6px; letter-spacing:1px;">このカテゴリの施術</div>
    <div style="font-size:8.5px; color:#666; line-height:1.9;">
      クローズド法で対応可能なケースが多いカテゴリです。ダウンタイムを短くしながら、可愛らしい印象を作れます。鼻先の向きは数ミリの差で大きく印象が変わるため、カウンセリングでのすり合わせが重要です。
    </div>
  </div>
</div>
</div>

<!-- ========== DESIGN CATALOG 2: Elegant & Straight ========== -->
<div class="page">
<div class="cp" style="padding-top: 10mm;">
  <div class="catalog-header">
    <div class="catalog-script">Elegant <span class="catalog-amp">&amp;</span> Straight</div>
    <div class="catalog-ribbon">- "忘れ鼻"と"横顔の品格"を追求したナチュラル美デザイン -</div>
  </div>

  <div class="design-cols">
    <div class="design-col">
      <span class="dtag">ストレート</span>
      <div class="ddesc">鼻筋から鼻先まで<br>一直線のライン。<br>最も「整形感」が出にくい。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#忘れ鼻</span>
    </div>
    <div class="design-col">
      <span class="dtag">半ラウンド</span>
      <div class="ddesc">自然な丸みを残しながら<br>品のある印象に。<br>大人な雰囲気へ。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#大人美人</span>
    </div>
    <div class="design-col">
      <span class="dtag">短鼻解消</span>
      <div class="ddesc">鼻が短く上を向いている<br>状態を改善。自然な<br>向きと高さを実現。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#立体感</span>
    </div>
  </div>

  <div style="background:#fff; border-left:3px solid #c8a060; padding:12px 16px; margin-top:18px;">
    <div style="font-size:8px; color:#c8a060; margin-bottom:6px; letter-spacing:1px;">このカテゴリの施術</div>
    <div style="font-size:8.5px; color:#666; line-height:1.9;">
      「整形したことを気づかれたくない」「自然に綺麗になりたい」という方に最も選ばれるカテゴリです。クローズド法との相性が非常に良く、ダウンタイムも短めです。忘れ鼻（自然すぎて気づかれない鼻）は羽根先生が特に得意とするデザインです。
    </div>
  </div>
</div>
</div>

<!-- ========== DESIGN CATALOG 3: Dramatic & Glamorous ========== -->
<div class="page">
<div class="cp" style="padding-top: 10mm;">
  <div class="catalog-header">
    <div class="catalog-script">Dramatic <span class="catalog-amp">&amp;</span> Glamorous</div>
    <div class="catalog-ribbon">- "圧倒的な高さ"と"Eライン"を完成させるフルオーダーデザイン -</div>
  </div>

  <div class="design-cols">
    <div class="design-col">
      <span class="dtag">シャープ鼻</span>
      <div class="ddesc">鼻筋から鼻先まで<br>シャープな印象に。<br>団子鼻を解消。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#ハーフ顔</span>
    </div>
    <div class="design-col">
      <span class="dtag">Eライン</span>
      <div class="ddesc">横顔の美しさを<br>完成させる設計。<br>口元の突出感も軽減。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#Eライン</span>
    </div>
    <div class="design-col">
      <span class="dtag">貴族手術</span>
      <div class="ddesc">鼻翼基部を持ち上げ<br>横顔に奥行きを演出。<br>存在感のある顔立ちに。</div>
      <div class="before-label">BEFORE</div>
      <div class="before-circle">写真</div>
      <div class="after-label">After</div>
      <div class="after-rect">写真挿入</div>
      <span class="dhashtag">#存在感</span>
    </div>
  </div>

  <div style="background:#fff; border-left:3px solid #c8a060; padding:12px 16px; margin-top:18px;">
    <div style="font-size:8px; color:#c8a060; margin-bottom:6px; letter-spacing:1px;">このカテゴリの施術</div>
    <div style="font-size:8.5px; color:#666; line-height:1.9;">
      大きな変化を望む方向けのカテゴリです。プロテーゼ・軟骨移植・鼻中隔延長など複数の施術を組み合わせることが多く、オープン法や肋軟骨移植が必要なケースもあります。ダウンタイムは長めですが、完成したときの変化も最も大きいカテゴリです。
    </div>
  </div>
</div>
</div>

<!-- ========== デザイン型別解説 ========== -->
<div class="page">
<div class="cp">
  <div class="ph"><span class="ph-label">NOSE TIP DESIGN GUIDE</span><span class="ph-num">06</span></div>
  <h2 class="stitle">鼻先のデザイン解説</h2>
  <div class="sen">UPTURNED / STRAIGHT / ROUND</div>

  <div class="type-block">
    <div class="type-label-bar">
      <div class="type-label-inner">
        <span class="type-label-en">Up Nose</span>
        <span class="type-label-ja">アップノーズ</span>
      </div>
    </div>
    <div class="type-content">
      <h4>鼻先が上を向いた、可愛らしいデザイン</h4>
      <p>鼻唇角（鼻と口の間の角度）を大きくすることで、鼻先が上を向いた印象になります。正面から見ると中顔面が短縮して見え、横顔は口元がすっきり見えます。やりすぎると「豚鼻」に見えるリスクがあるため、自然な範囲でのデザインが重要です。</p>
      <div class="type-tags">
        <span class="type-tag">Baby &amp; Cute系</span>
        <span class="type-tag">中顔面短縮</span>
        <span class="type-tag">あざと可愛い</span>
        <span class="type-tag">クローズド法対応◎</span>
      </div>
    </div>
  </div>

  <div class="type-block">
    <div class="type-label-bar" style="background:#8a7060;">
      <div class="type-label-inner">
        <span class="type-label-en">Straight</span>
        <span class="type-label-ja">ストレート</span>
      </div>
    </div>
    <div class="type-content">
      <h4>鼻筋から鼻先まで一直線の、忘れ鼻デザイン</h4>
      <p>鼻筋・鼻先が一本の直線上に揃った形。最も「整形した感」が出にくく、「バレたくない」方に圧倒的に人気のデザインです。横顔の品格が増し、どんな顔の形にも馴染む汎用性の高さが特徴です。プロテーゼ＋ストラットの組み合わせで実現できるケースが多いです。</p>
      <div class="type-tags">
        <span class="type-tag">Elegant系</span>
        <span class="type-tag">忘れ鼻</span>
        <span class="type-tag">整形感ゼロ</span>
        <span class="type-tag">クローズド法対応◎</span>
      </div>
    </div>
  </div>

  <div class="type-block">
    <div class="type-label-bar" style="background:#4a3828;">
      <div class="type-label-inner">
        <span class="type-label-en">Round</span>
        <span class="type-label-ja">ラウンド</span>
      </div>
    </div>
    <div class="type-content">
      <h4>鼻先に自然な丸みを持たせた、柔らかいデザイン</h4>
      <p>鼻先を過度にシャープにせず、自然な丸みを残したデザイン。半ラウンドは「大人の色気」、フルラウンドは「柔らかさ・優しさ」を演出します。シャープすぎると不自然に見えるリスクがある方や、柔らかい印象を保ちたい方に向いています。</p>
      <div class="type-tags">
        <span class="type-tag">Elegant〜Cute系</span>
        <span class="type-tag">半ラウンド</span>
        <span class="type-tag">大人美人</span>
        <span class="type-tag">クローズド法対応◎</span>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ========== CLOSING ========== -->
<div class="page">
<div class="closing">
<div class="closing-inner">
  <div style="font-size:7.5px; letter-spacing:5px; color:#c8a060; margin-bottom:44px;">ZETITH BEAUTY CLINIC FUKUOKA</div>
  <div class="closing-script">今日、どんな鼻に<br>なりたいですか？</div>
  <div class="closing-sub">デザインのイメージが固まっていなくても大丈夫です。<br>「なんとなくこんな印象になりたい」から一緒に考えます。<br>決めなければいけない場ではありません。</div>
  <div class="closing-gold-bar"></div>
  <div class="cinfo-label">INSTAGRAM</div>
  <div class="cinfo-val">@zetith_hane</div>
  <div class="cinfo-label">CLINIC</div>
  <div class="cinfo-val">Zetith Beauty Clinic 福岡院</div>
</div>
</div>
</div>

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/鼻整形_カウンセリング資料v3.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
