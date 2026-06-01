html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
@page { size: A4; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Hiragino Mincho ProN', 'Yu Mincho', 'MS Mincho', Georgia, serif;
  background: #f7f5f1;
  color: #1a1a1a;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ── BASE ── */
.page {
  width: 210mm;
  min-height: 297mm;
  background: #f7f5f1;
  page-break-after: always;
  position: relative;
}

/* ── COVER ── */
.cover {
  width: 210mm;
  height: 297mm;
  background: #1a1a1a;
  display: table;
  text-align: center;
}
.cover-inner {
  display: table-cell;
  vertical-align: middle;
  padding: 20mm;
}
.cover-en {
  font-size: 7.5px;
  letter-spacing: 6px;
  color: #b8944a;
  margin-bottom: 48px;
}
.cover-title {
  font-size: 40px;
  font-weight: 300;
  color: #ffffff;
  line-height: 1.5;
  margin-bottom: 20px;
}
.cover-sub {
  font-size: 12px;
  color: #888;
  margin-bottom: 64px;
}
.gold-line {
  width: 40px;
  height: 1px;
  background: #b8944a;
  margin: 0 auto 56px;
}
.cover-name {
  font-size: 15px;
  color: #b8944a;
  letter-spacing: 3px;
  margin-bottom: 10px;
}
.cover-clinic {
  font-size: 9px;
  color: #555;
  letter-spacing: 1px;
}

/* ── CONTENT PAGE ── */
.cp {
  padding: 12mm 17mm 10mm;
  min-height: 297mm;
}
.ph {
  border-bottom: 1px solid #b8944a;
  padding-bottom: 7px;
  margin-bottom: 22px;
  overflow: hidden;
}
.ph-label {
  float: left;
  font-size: 7px;
  letter-spacing: 3px;
  color: #b8944a;
}
.ph-num {
  float: right;
  font-size: 8px;
  color: #bbb;
}
h2.stitle {
  font-size: 24px;
  font-weight: 300;
  color: #1a1a1a;
  margin-bottom: 4px;
}
.sen {
  font-size: 7px;
  letter-spacing: 3px;
  color: #aaa;
  margin-bottom: 24px;
}

/* ── DOCTOR ── */
.doc-wrap { overflow: hidden; margin-bottom: 20px; }
.doc-photo {
  float: left;
  width: 80px;
  height: 100px;
  background: #e0dbd4;
  margin-right: 20px;
  text-align: center;
  line-height: 100px;
  font-size: 7px;
  color: #999;
}
.doc-name {
  font-size: 20px;
  font-weight: 300;
  color: #b8944a;
  margin-bottom: 3px;
}
.doc-title {
  font-size: 8px;
  color: #888;
  margin-bottom: 12px;
  letter-spacing: 1px;
}
.doc-text {
  font-size: 9.5px;
  color: #444;
  line-height: 2;
}
.career { list-style: none; margin-top: 18px; clear: both; }
.career li {
  font-size: 9px;
  color: #666;
  padding: 6px 0;
  border-bottom: 1px solid #e5e0d8;
  overflow: hidden;
}
.career li span {
  float: left;
  color: #b8944a;
  width: 44px;
}
.quote-block {
  background: #ffffff;
  border-left: 3px solid #b8944a;
  padding: 15px 18px;
  margin-top: 22px;
}
.quote-block p {
  font-size: 9.5px;
  color: #555;
  line-height: 2.1;
}

/* ── PROCEDURE PAGE ── */
.proc-header {
  background: #1a1a1a;
  color: #ffffff;
  padding: 14px 18px;
  margin: -12mm -17mm 0;
  overflow: hidden;
}
.proc-header-inner {
  padding: 12mm 17mm 16px;
}
.proc-name-en {
  font-size: 7px;
  letter-spacing: 4px;
  color: #b8944a;
  margin-bottom: 6px;
}
.proc-name-ja {
  font-size: 26px;
  font-weight: 300;
  color: #ffffff;
}
.proc-tags { margin-top: 8px; }
.proc-tag {
  display: inline-block;
  font-size: 7px;
  color: #b8944a;
  border: 1px solid #4a3820;
  padding: 2px 8px;
  margin-right: 6px;
  letter-spacing: 1px;
}

/* ── TWO-COL LAYOUT ── */
.two-col { overflow: hidden; margin-top: 18px; }
.col-left {
  float: left;
  width: 47%;
}
.col-right {
  float: right;
  width: 50%;
}

/* ── PROC EXPLANATION ── */
.exp-block { margin-bottom: 16px; }
.exp-heading {
  font-size: 9px;
  color: #b8944a;
  letter-spacing: 2px;
  margin-bottom: 7px;
  border-bottom: 1px solid #e5ddd0;
  padding-bottom: 4px;
}
.exp-text {
  font-size: 9px;
  color: #444;
  line-height: 1.95;
}
.step-list { list-style: none; }
.step-list li {
  font-size: 8.5px;
  color: #555;
  padding: 4px 0;
  padding-left: 14px;
  position: relative;
  line-height: 1.7;
}
.step-list li::before {
  content: '';
  position: absolute;
  left: 0;
  top: 10px;
  width: 5px;
  height: 1px;
  background: #b8944a;
}
.who-block {
  background: #ffffff;
  border: 1px solid #e5ddd0;
  padding: 11px 13px;
  margin-top: 14px;
}
.who-heading {
  font-size: 7.5px;
  color: #b8944a;
  letter-spacing: 2px;
  margin-bottom: 7px;
}
.who-list { list-style: none; }
.who-list li {
  font-size: 8.5px;
  color: #555;
  padding: 2px 0;
  padding-left: 12px;
  position: relative;
}
.who-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #b8944a;
  font-size: 7px;
}

/* ── CASE PHOTOS ── */
.case-box { margin-bottom: 12px; }
.case-head {
  font-size: 7px;
  letter-spacing: 2px;
  color: #b8944a;
  margin-bottom: 6px;
}
.case-photos-wrap { overflow: hidden; }
.case-photo {
  float: left;
  width: 47%;
  background: #1a1a1a;
  margin-right: 6%;
}
.case-photo:last-child { margin-right: 0; }
.case-photo-box {
  height: 100px;
  background: #222;
  border: 1px solid #333;
  text-align: center;
  padding-top: 38px;
}
.case-photo-box .cp-label {
  font-size: 6.5px;
  color: #555;
  letter-spacing: 2px;
}
.case-photo-caption {
  background: #1a1a1a;
  padding: 5px 8px;
  font-size: 7px;
  color: #888;
  text-align: center;
}
.case-note-text {
  font-size: 7.5px;
  color: #888;
  line-height: 1.7;
  margin-top: 8px;
  clear: both;
  background: #fffef9;
  border: 1px solid #e8e0d0;
  padding: 8px 10px;
}

/* ── DOWNTIME ── */
.dt-row {
  overflow: hidden;
  margin-bottom: 14px;
  min-height: 42px;
}
.dt-day {
  float: left;
  width: 54px;
  font-size: 8.5px;
  color: #b8944a;
  text-align: right;
  padding-right: 12px;
  padding-top: 3px;
}
.dt-bar {
  float: left;
  width: 3px;
  background: #ddd;
  margin-right: 14px;
  height: 38px;
}
.dt-bar.act { background: #b8944a; }
.dt-content { overflow: hidden; }
.dt-content h4 {
  font-size: 10px;
  color: #1a1a1a;
  margin-bottom: 3px;
}
.dt-content p {
  font-size: 8.5px;
  color: #777;
  line-height: 1.7;
}

/* ── FAQ ── */
.faq-item {
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid #e5ddd0;
}
.faq-q {
  font-size: 10px;
  color: #1a1a1a;
  margin-bottom: 6px;
  overflow: hidden;
}
.faq-q::before {
  content: 'Q';
  float: left;
  width: 20px;
  color: #b8944a;
  font-size: 12px;
  line-height: 1;
  margin-right: 4px;
}
.faq-a {
  font-size: 9px;
  color: #666;
  line-height: 1.9;
  padding-left: 24px;
}

/* ── CLOSING ── */
.closing {
  width: 210mm;
  height: 297mm;
  background: #1a1a1a;
  display: table;
  text-align: center;
}
.closing-inner {
  display: table-cell;
  vertical-align: middle;
  padding: 20mm;
}
.closing h2 {
  font-size: 20px;
  font-weight: 300;
  color: #fff;
  line-height: 1.8;
  margin-bottom: 18px;
}
.closing p {
  font-size: 9.5px;
  color: #777;
  line-height: 2.1;
  margin-bottom: 48px;
}
.sns-lbl {
  font-size: 7px;
  letter-spacing: 3px;
  color: #b8944a;
  margin-bottom: 5px;
}
.sns-val {
  font-size: 11px;
  color: #aaa;
  margin-bottom: 20px;
}
</style>
</head>
<body>

<!-- ========== COVER ========== -->
<div class="page">
<div class="cover">
<div class="cover-inner">
  <div class="cover-en">RHINOPLASTY CONSULTATION GUIDE</div>
  <div class="cover-title">鼻整形<br>カウンセリング</div>
  <div class="cover-sub">あなたの理想の鼻へ、一緒に考えます。</div>
  <div class="gold-line"></div>
  <div class="cover-name">羽根 和秀</div>
  <div class="cover-clinic">Zetith Beauty Clinic Fukuoka</div>
</div>
</div>
</div>

<!-- ========== DOCTOR ========== -->
<div class="page">
<div class="cp">
  <div class="ph"><span class="ph-label">DOCTOR PROFILE</span><span class="ph-num">01</span></div>
  <h2 class="stitle">担当医師について</h2>
  <div class="sen">ABOUT YOUR DOCTOR</div>

  <div class="doc-wrap">
    <div class="doc-photo">写真</div>
    <div>
      <div class="doc-name">羽根 和秀</div>
      <div class="doc-title">美容外科医 ／ 鼻整形専門</div>
      <div class="doc-text">
        鼻の構造を熟知した上で、その人にとって自然で<br>
        美しいバランスを追求しています。<br>
        「整形した」とわからない鼻が、<br>
        私の考える理想の仕上がりです。
      </div>
    </div>
  </div>

  <ul class="career">
    <li><span>専門</span>鼻整形・他院修正・複合施術</li>
    <li><span>対応</span>鼻筋・鼻先・小鼻・鼻中隔延長・肋軟骨移植</li>
    <li><span>SNS</span>Instagram @zetith_hane（月8.4万人閲覧）</li>
    <li><span>勤務</span>Zetith Beauty Clinic 福岡院</li>
  </ul>

  <div class="quote-block">
    <p>「鼻は顔の中心にあります。<br>
    だからこそ、少しの違いが顔全体の印象を変えます。<br>
    私は施術を決める前に、まず『しないほうがいいケース』を考えます。<br>
    その判断ができるドクターに、任せてください。」</p>
  </div>
</div>
</div>

<!-- ========== PROC 1: プロテーゼ ========== -->
<div class="page">
<div style="background:#1a1a1a; padding: 14mm 17mm 16px;">
  <div style="font-size:7px; letter-spacing:4px; color:#b8944a; margin-bottom:6px;">NOSE BRIDGE AUGMENTATION</div>
  <div style="font-size:26px; font-weight:300; color:#ffffff;">鼻筋形成（プロテーゼ）</div>
  <div style="margin-top:10px;">
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">シリコン</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">ePTFE</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px;">ダウンタイム 約1週間</span>
  </div>
</div>
<div class="cp" style="padding-top: 16px;">
  <div class="two-col">
    <div class="col-left">
      <div class="exp-block">
        <div class="exp-heading">どんな施術か</div>
        <div class="exp-text">鼻の内側（鼻孔）から切開し、骨と軟骨の間にシリコンまたはePTFEのプロテーゼを挿入します。外側に傷が残らず、鼻筋の高さ・幅・形状を個別に設計できます。</div>
      </div>
      <div class="exp-block">
        <div class="exp-heading">施術の流れ</div>
        <ul class="step-list">
          <li>局所麻酔または静脈麻酔を使用</li>
          <li>鼻孔内側を数ミリ切開</li>
          <li>骨膜下にポケットを形成</li>
          <li>プロテーゼを挿入・位置を調整</li>
          <li>溶ける糸で縫合（抜糸不要）</li>
          <li>所要時間：約45〜60分</li>
        </ul>
      </div>
      <div class="who-block">
        <div class="who-heading">こんな方に向いています</div>
        <ul class="who-list">
          <li>鼻筋が低く、正面から鼻筋が通っていない</li>
          <li>鼻根（目と鼻の間）が平坦な方</li>
          <li>顔の立体感を出したい方</li>
          <li>切開を最小限にしたい方</li>
        </ul>
      </div>
    </div>
    <div class="col-right">
      <div class="case-box">
        <div class="case-head">CASE 01</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1週間後</div></div>
            <div class="case-photo-caption">1 WEEK AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：プロテーゼ（シリコン）<br>鼻根の高さと鼻筋のラインを整えました</div>
      </div>
      <div class="case-box" style="margin-top:12px;">
        <div class="case-head">CASE 02</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1ヶ月後</div></div>
            <div class="case-photo-caption">1 MONTH AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：ストラット ＋ プロテーゼ<br>鼻先から鼻筋まで複合的に整えた症例</div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ========== PROC 2: 鼻尖縮小 ========== -->
<div class="page">
<div style="background:#1a1a1a; padding: 14mm 17mm 16px;">
  <div style="font-size:7px; letter-spacing:4px; color:#b8944a; margin-bottom:6px;">NOSE TIP REFINEMENT</div>
  <div style="font-size:26px; font-weight:300; color:#ffffff;">鼻尖縮小・ストラット</div>
  <div style="margin-top:10px;">
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">軟骨形成</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">耳介軟骨</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px;">ダウンタイム 約1週間</span>
  </div>
</div>
<div class="cp" style="padding-top: 16px;">
  <div class="two-col">
    <div class="col-left">
      <div class="exp-block">
        <div class="exp-heading">どんな施術か</div>
        <div class="exp-text">鼻先の軟骨を縫合・形成して丸みを改善します。「ストラット」とは鼻柱に軟骨支柱を立てる技術で、鼻先の向きや高さを精密にコントロールできます。耳の裏から軟骨を採取する場合もあります。</div>
      </div>
      <div class="exp-block">
        <div class="exp-heading">施術の流れ</div>
        <ul class="step-list">
          <li>鼻孔内側から切開（オープンの場合は鼻柱も）</li>
          <li>左右の鼻翼軟骨を露出</li>
          <li>縫合して軟骨を寄せ、鼻先を整形</li>
          <li>ストラット用軟骨を鼻柱に固定</li>
          <li>形を確認して縫合</li>
          <li>所要時間：約60〜90分</li>
        </ul>
      </div>
      <div class="who-block">
        <div class="who-heading">こんな方に向いています</div>
        <ul class="who-list">
          <li>鼻先が丸い、団子鼻が気になる</li>
          <li>鼻先が下を向いている</li>
          <li>鼻先だけシャープにしたい</li>
          <li>プロテーゼと組み合わせたい</li>
        </ul>
      </div>
    </div>
    <div class="col-right">
      <div class="case-box">
        <div class="case-head">CASE 01</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1週間後</div></div>
            <div class="case-photo-caption">1 WEEK AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：鼻尖縮小 ＋ ストラット<br>正面・側面ともに自然なシャープさを実現</div>
      </div>
      <div class="case-box" style="margin-top:12px;">
        <div class="case-head">CASE 02</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1ヶ月後</div></div>
            <div class="case-photo-caption">1 MONTH AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：プロテーゼ ＋ 鼻尖縮小<br>鼻筋から鼻先まで一体的にデザイン</div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ========== PROC 3: 小鼻縮小 ========== -->
<div class="page">
<div style="background:#1a1a1a; padding: 14mm 17mm 16px;">
  <div style="font-size:7px; letter-spacing:4px; color:#b8944a; margin-bottom:6px;">ALAR REDUCTION</div>
  <div style="font-size:26px; font-weight:300; color:#ffffff;">小鼻縮小（クローズド法）</div>
  <div style="margin-top:10px;">
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">傷が目立たない</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">鼻穴縮小</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px;">ダウンタイム 5〜7日</span>
  </div>
</div>
<div class="cp" style="padding-top: 16px;">
  <div class="two-col">
    <div class="col-left">
      <div class="exp-block">
        <div class="exp-heading">どんな施術か</div>
        <div class="exp-text">小鼻の付け根（鼻翼基部）を切除・縫合して、小鼻の幅や広がりを改善します。クローズド法は傷を鼻の付け根の折れ目に沿わせるため、正面から傷がほぼ見えません。内側のみの切除で対応するケースもあります。</div>
      </div>
      <div class="exp-block">
        <div class="exp-heading">クローズ法 vs オープン法</div>
        <ul class="step-list">
          <li><strong>クローズ法：</strong>傷が鼻の付け根のライン沿い。目立ちにくく回復が早い</li>
          <li><strong>オープン法：</strong>広い範囲の縮小が可能。傷はやや残るが、時間と共に薄くなる</li>
          <li>状態に合わせてどちらを選ぶかカウンセリングで決定します</li>
        </ul>
      </div>
      <div class="who-block">
        <div class="who-heading">こんな方に向いています</div>
        <ul class="who-list">
          <li>小鼻が横に広がっている</li>
          <li>鼻の穴の大きさが気になる</li>
          <li>正面から見たときの鼻の幅が大きい</li>
          <li>「お鼻の大きさを解消したい」</li>
        </ul>
      </div>
    </div>
    <div class="col-right">
      <div class="case-box">
        <div class="case-head">CASE 01</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1ヶ月後</div></div>
            <div class="case-photo-caption">1 MONTH AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：小鼻縮小クローズド法<br>傷は付け根ラインに沿って目立たない位置</div>
      </div>
      <div class="case-box" style="margin-top:12px;">
        <div class="case-head">CASE 02</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">3ヶ月後</div></div>
            <div class="case-photo-caption">3 MONTHS AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：小鼻縮小 ＋ 鼻尖縮小<br>正面の印象を大きく改善した複合症例</div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ========== PROC 4: 他院修正 ========== -->
<div class="page">
<div style="background:#1a1a1a; padding: 14mm 17mm 16px;">
  <div style="font-size:7px; letter-spacing:4px; color:#b8944a; margin-bottom:6px;">REVISION SURGERY</div>
  <div style="font-size:26px; font-weight:300; color:#ffffff;">他院修正・拘縮鼻の改善</div>
  <div style="margin-top:10px;">
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">プロテーゼ入れ替え</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">軟骨移植</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px;">要診断</span>
  </div>
</div>
<div class="cp" style="padding-top: 16px;">
  <div class="two-col">
    <div class="col-left">
      <div class="exp-block">
        <div class="exp-heading">どんな施術か</div>
        <div class="exp-text">他院で受けた鼻整形の修正・やり直しに対応します。プロテーゼの位置ずれ・高さの修正・拘縮（皮膚が縮んで鼻先が上を向く状態）の改善など、状態を正確に診断した上でプランを提案します。</div>
      </div>
      <div class="exp-block">
        <div class="exp-heading">修正で対応できる主なケース</div>
        <ul class="step-list">
          <li>プロテーゼが高すぎる・位置がずれている</li>
          <li>鼻先が不自然に上を向いている（拘縮）</li>
          <li>仕上がりが理想と違う</li>
          <li>感染・炎症が起きている</li>
          <li>「中顔面が短縮して見える」状態</li>
        </ul>
      </div>
      <div class="who-block">
        <div class="who-heading">修正の大原則</div>
        <ul class="who-list">
          <li>まず現状を正確に診断します</li>
          <li>「今は修正しないほうがいい」とお伝えすることもあります</li>
          <li>前回施術から6ヶ月以上経過が目安</li>
          <li>状態によっては段階的な施術が必要な場合も</li>
        </ul>
      </div>
    </div>
    <div class="col-right">
      <div class="case-box">
        <div class="case-head">CASE 01 ／ 拘縮鼻の他院修正</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1週間後</div></div>
            <div class="case-photo-caption">1 WEEK AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：プロテーゼ除去 ＋ 軟骨移植による修正<br>他院で入れた高すぎるプロテーゼを除去し再設計</div>
      </div>
      <div class="case-box" style="margin-top:12px;">
        <div class="case-head">CASE 02 ／ 中顔面短縮の改善</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1ヶ月後</div></div>
            <div class="case-photo-caption">1 MONTH AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：鼻中隔延長 ＋ 鼻尖形成 ＋ 軟骨移植<br>鼻先の向きを修正し、顔全体のバランスを改善</div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ========== PROC 5: 肋軟骨 ========== -->
<div class="page">
<div style="background:#1a1a1a; padding: 14mm 17mm 16px;">
  <div style="font-size:7px; letter-spacing:4px; color:#b8944a; margin-bottom:6px;">RIB CARTILAGE GRAFT</div>
  <div style="font-size:26px; font-weight:300; color:#ffffff;">肋軟骨移植</div>
  <div style="margin-top:10px;">
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">大きな変化に</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px; margin-right:6px;">高難度施術</span>
    <span style="display:inline-block; font-size:7px; color:#b8944a; border:1px solid #4a3820; padding:2px 8px;">ダウンタイム 10〜14日</span>
  </div>
</div>
<div class="cp" style="padding-top: 16px;">
  <div class="two-col">
    <div class="col-left">
      <div class="exp-block">
        <div class="exp-heading">どんな施術か</div>
        <div class="exp-text">胸の肋骨から軟骨を採取し、鼻中隔延長・鼻先形成・大幅な鼻の再建に使用します。耳介軟骨では量・強度が不足する大きな変化が必要なケースに適しています。自家組織なので感染リスクが低く、変形しにくいのが特徴です。</div>
      </div>
      <div class="exp-block">
        <div class="exp-heading">主な適応ケース</div>
        <ul class="step-list">
          <li>大幅な鼻先の延長・方向変更</li>
          <li>鼻中隔延長に大量の軟骨が必要な場合</li>
          <li>他院修正で耳介軟骨が不足している場合</li>
          <li>拘縮鼻の根本的な改善</li>
          <li>「大きな変化が必要なケース」</li>
        </ul>
      </div>
      <div class="who-block">
        <div class="who-heading">肋軟骨を使う理由</div>
        <ul class="who-list">
          <li>採取量が多く、強度が高い</li>
          <li>自家組織なので体に馴染みやすい</li>
          <li>プロテーゼが使えないケースでも対応可能</li>
          <li>長期的に安定した結果が得られる</li>
        </ul>
      </div>
    </div>
    <div class="col-right">
      <div class="case-box">
        <div class="case-head">CASE 01 ／ 肋軟骨による大幅改善</div>
        <div class="case-photos-wrap">
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">術前</div></div>
            <div class="case-photo-caption">BEFORE</div>
          </div>
          <div class="case-photo">
            <div class="case-photo-box"><div class="cp-label">1ヶ月後</div></div>
            <div class="case-photo-caption">1 MONTH AFTER</div>
          </div>
        </div>
        <div class="case-note-text">施術：肋軟骨 ＋ 鼻中隔延長 ＋ プロテーゼ<br>全体的な鼻の再設計が必要だったケース</div>
      </div>
      <div style="background:#fff; border:1px solid #e5ddd0; padding:14px; margin-top:14px;">
        <div style="font-size:8px; color:#b8944a; letter-spacing:1px; margin-bottom:8px;">採取部位について</div>
        <div style="font-size:8.5px; color:#666; line-height:1.8;">
          胸の肋骨脇（乳房下ライン付近）から小さく切開して採取します。傷は約2〜3cmで、時間とともに目立たなくなります。採取後の痛みは1〜2週間ほどあります。
        </div>
      </div>
    </div>
  </div>
</div>
</div>

<!-- ========== DOWNTIME ========== -->
<div class="page">
<div class="cp">
  <div class="ph"><span class="ph-label">DOWNTIME GUIDE</span><span class="ph-num">06</span></div>
  <h2 class="stitle">ダウンタイムの目安</h2>
  <div class="sen">RECOVERY TIMELINE</div>

  <div class="dt-row">
    <div class="dt-day">当日</div>
    <div class="dt-bar act"></div>
    <div class="dt-content">
      <h4>施術直後</h4>
      <p>腫れが出始めます。ギプス固定（プロテーゼの場合）を装着したまま帰宅。痛みは軽度で処方された鎮痛剤で対応できます。</p>
    </div>
  </div>

  <div class="dt-row">
    <div class="dt-day">1〜3日</div>
    <div class="dt-bar act"></div>
    <div class="dt-content">
      <h4>腫れのピーク</h4>
      <p>腫れと内出血が最も強く出ます。アイスノンで冷やすと効果的です。安静を心がけてください。</p>
    </div>
  </div>

  <div class="dt-row">
    <div class="dt-day">7日</div>
    <div class="dt-bar act"></div>
    <div class="dt-content">
      <h4>抜糸・ギプス除去</h4>
      <p>抜糸を行い、ギプスを外します。腫れはまだ残りますが、日常生活への支障は大きく減ります。</p>
    </div>
  </div>

  <div class="dt-row">
    <div class="dt-day">2〜4週</div>
    <div class="dt-bar"></div>
    <div class="dt-content">
      <h4>社会復帰・安定期</h4>
      <p>腫れが引き、他者に気づかれにくくなります。メイクも可能（施術部位以外は翌日から可）。</p>
    </div>
  </div>

  <div class="dt-row">
    <div class="dt-day">1〜3ヶ月</div>
    <div class="dt-bar"></div>
    <div class="dt-content">
      <h4>完成形へ</h4>
      <p>むくみが取れ、最終的な形に落ち着きます。固い感じも時間とともに自然になります。</p>
    </div>
  </div>

  <div class="quote-block" style="margin-top: 22px;">
    <p>ダウンタイム中で一番大事なのは「触らないこと」です。<br>
    形が定まる前に動かすと、仕上がりに影響します。<br>
    不安なことがあれば、いつでもご連絡ください。</p>
  </div>
</div>
</div>

<!-- ========== FAQ ========== -->
<div class="page">
<div class="cp">
  <div class="ph"><span class="ph-label">FREQUENTLY ASKED QUESTIONS</span><span class="ph-num">07</span></div>
  <h2 class="stitle">よくあるご質問</h2>
  <div class="sen">FAQ</div>

  <div class="faq-item">
    <div class="faq-q">鼻整形したことはバレますか？</div>
    <p class="faq-a">自然なデザインを選べば、ほとんどの場合バレません。「高くしすぎない」「鼻先を細くしすぎない」ことがポイントです。「自分の顔に合っているか」を最優先に設計します。</p>
  </div>

  <div class="faq-item">
    <div class="faq-q">一度入れたプロテーゼは将来取り出せますか？</div>
    <p class="faq-a">はい、取り出すことができます。ただし長期間経過している場合は周囲組織に癒着が起きることがあります。修正・除去希望の場合は早めのご相談をお勧めします。</p>
  </div>

  <div class="faq-item">
    <div class="faq-q">複数の施術を同時に受けられますか？</div>
    <p class="faq-a">可能です。組み合わせることでよりバランスの良い仕上がりになるケースも多いです。施術時間・ダウンタイムの増加を考慮した上でご提案します。</p>
  </div>

  <div class="faq-item">
    <div class="faq-q">他院で施術した鼻の修正はできますか？</div>
    <p class="faq-a">対応しています。まず現状の状態を診断し、何ができるかをお伝えします。状態によっては「今は修正しない方がいい」とお伝えすることもあります。</p>
  </div>

  <div class="faq-item">
    <div class="faq-q">施術を断られることはありますか？</div>
    <p class="faq-a">あります。リスクが高い・期待に応えられない・今の状態では不適と判断した場合はお断りします。それも医師としての仕事だと考えています。</p>
  </div>

</div>
</div>

<!-- ========== CLOSING ========== -->
<div class="page">
<div class="closing">
<div class="closing-inner">
  <div class="cover-en" style="margin-bottom:44px;">ZETITH BEAUTY CLINIC FUKUOKA</div>
  <h2>今日のカウンセリングで<br>疑問は解消されましたか？</h2>
  <p>不安なこと、迷っていること、何でもお聞きください。<br>「決めなければいけない」という場ではありません。</p>
  <div class="gold-line"></div>
  <div class="sns-lbl">INSTAGRAM</div>
  <div class="sns-val">@zetith_hane</div>
  <div class="sns-lbl">CLINIC</div>
  <div class="sns-val">Zetith Beauty Clinic 福岡院</div>
</div>
</div>
</div>

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/鼻整形_カウンセリング資料v2.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
