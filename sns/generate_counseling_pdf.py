html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
@page { size: A4; margin: 0; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Hiragino Mincho ProN', 'Yu Mincho', 'MS Mincho', Georgia, serif;
  background: #0d0d0d;
  color: #f5f5f5;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ── PAGE BASE ── */
.page {
  width: 210mm;
  min-height: 297mm;
  background: #0d0d0d;
  page-break-after: always;
  position: relative;
  overflow: hidden;
}

/* ── COVER ── */
.cover {
  width: 210mm;
  height: 297mm;
  display: table;
  text-align: center;
}
.cover-inner {
  display: table-cell;
  vertical-align: middle;
  padding: 20mm;
}
.cover-en {
  font-size: 8px;
  letter-spacing: 5px;
  color: #c8a96e;
  margin-bottom: 44px;
}
.cover-title {
  font-size: 36px;
  font-weight: 300;
  color: #ffffff;
  line-height: 1.5;
  margin-bottom: 18px;
}
.cover-subtitle {
  font-size: 12px;
  color: #888888;
  font-weight: 300;
  margin-bottom: 60px;
}
.gold-divider {
  width: 44px;
  height: 1px;
  background: #c8a96e;
  margin: 0 auto 56px;
}
.cover-doctor {
  font-size: 15px;
  color: #c8a96e;
  letter-spacing: 3px;
  margin-bottom: 10px;
}
.cover-clinic {
  font-size: 9px;
  color: #555555;
  letter-spacing: 1px;
}

/* ── CONTENT PAGES ── */
.content-page {
  padding: 13mm 18mm;
  min-height: 297mm;
}
.page-header {
  border-bottom: 1px solid #c8a96e;
  padding-bottom: 7px;
  margin-bottom: 26px;
  overflow: hidden;
}
.section-label {
  float: left;
  font-size: 7px;
  letter-spacing: 3px;
  color: #c8a96e;
}
.page-num {
  float: right;
  font-size: 8px;
  color: #3a3a3a;
}
h2.section-title {
  font-size: 23px;
  font-weight: 300;
  color: #ffffff;
  margin-bottom: 5px;
}
.section-en {
  font-size: 7px;
  letter-spacing: 3px;
  color: #555;
  margin-bottom: 26px;
}

/* ── PROFILE PAGE ── */
.profile-wrap {
  overflow: hidden;
  margin-bottom: 24px;
}
.profile-photo {
  float: left;
  width: 72px;
  height: 92px;
  background: #141414;
  border: 1px solid #2a2a2a;
  margin-right: 20px;
  text-align: center;
  line-height: 92px;
  font-size: 7px;
  color: #3a3a3a;
}
.profile-info h3 {
  font-size: 19px;
  font-weight: 300;
  color: #c8a96e;
  margin-bottom: 4px;
}
.profile-info .title {
  font-size: 8px;
  color: #777;
  margin-bottom: 13px;
  letter-spacing: 1px;
}
.profile-info p {
  font-size: 9.5px;
  color: #bbbbbb;
  line-height: 1.9;
}
.career-list {
  list-style: none;
  margin-top: 20px;
  clear: both;
}
.career-list li {
  font-size: 8.5px;
  color: #999999;
  padding: 6px 0;
  border-bottom: 1px solid #191919;
  overflow: hidden;
}
.career-list .year {
  float: left;
  color: #c8a96e;
  width: 40px;
}
.philosophy-block {
  background: #0f0f0f;
  border-left: 2px solid #c8a96e;
  padding: 15px 18px;
  margin-top: 22px;
}
.philosophy-block p {
  font-size: 9.5px;
  color: #bbbbbb;
  line-height: 2.1;
}

/* ── PROCEDURE GRID ── */
.proc-row {
  overflow: hidden;
  margin-bottom: 14px;
}
.proc-card {
  float: left;
  width: 48%;
  background: #0f0f0f;
  border: 1px solid #1e1e1e;
  padding: 14px;
  min-height: 110px;
}
.proc-card:nth-child(odd) { margin-right: 4%; }
.proc-card h3 {
  font-size: 12px;
  color: #c8a96e;
  font-weight: 400;
  margin-bottom: 4px;
}
.proc-card .en {
  font-size: 6.5px;
  letter-spacing: 2px;
  color: #444;
  margin-bottom: 9px;
}
.proc-card p {
  font-size: 8.5px;
  color: #999999;
  line-height: 1.8;
}
.proc-tag {
  display: inline-block;
  margin-top: 9px;
  font-size: 6.5px;
  color: #c8a96e;
  border: 1px solid #4a3820;
  padding: 2px 7px;
}

/* ── BEFORE/AFTER ── */
.case-section { margin-bottom: 22px; }
.case-label {
  font-size: 8px;
  color: #c8a96e;
  letter-spacing: 2px;
  margin-bottom: 9px;
}
.case-photos { overflow: hidden; margin-bottom: 7px; }
.photo-box {
  float: left;
  width: 31%;
  height: 84px;
  background: #111111;
  border: 1px solid #222222;
  margin-right: 3.5%;
  text-align: center;
  padding-top: 32px;
}
.photo-box:last-child { margin-right: 0; }
.photo-box .ph-label {
  font-size: 6.5px;
  color: #444;
  letter-spacing: 2px;
}
.case-note {
  font-size: 8px;
  color: #777777;
  line-height: 1.7;
  clear: both;
}

/* ── FLOW ── */
.flow-step {
  padding-left: 22px;
  margin-bottom: 22px;
  position: relative;
}
.flow-dot {
  position: absolute;
  left: 0;
  top: 5px;
  width: 8px;
  height: 8px;
  border: 1px solid #c8a96e;
  background: #0d0d0d;
}
.flow-line {
  position: absolute;
  left: 3px;
  top: 13px;
  width: 1px;
  height: 100%;
  background: #222;
}
.flow-step h3 {
  font-size: 12px;
  color: #c8a96e;
  font-weight: 400;
  margin-bottom: 5px;
}
.flow-step p {
  font-size: 9px;
  color: #999999;
  line-height: 1.9;
}

/* ── DOWNTIME ── */
.dt-row {
  overflow: hidden;
  margin-bottom: 16px;
  min-height: 44px;
}
.dt-day {
  float: left;
  width: 56px;
  font-size: 8.5px;
  color: #c8a96e;
  text-align: right;
  padding-right: 12px;
  padding-top: 2px;
}
.dt-bar {
  float: left;
  width: 3px;
  background: #1a1a1a;
  margin-right: 14px;
  margin-top: 2px;
  height: 40px;
}
.dt-bar.active { background: #c8a96e; }
.dt-content { overflow: hidden; }
.dt-content h4 {
  font-size: 10px;
  color: #eeeeee;
  margin-bottom: 3px;
}
.dt-content p {
  font-size: 8.5px;
  color: #777777;
  line-height: 1.7;
}

/* ── FAQ ── */
.faq-item {
  margin-bottom: 18px;
  padding-bottom: 18px;
  border-bottom: 1px solid #161616;
}
.faq-q {
  font-size: 10px;
  color: #c8a96e;
  margin-bottom: 7px;
}
.faq-a {
  font-size: 9px;
  color: #999999;
  line-height: 1.9;
  padding-left: 14px;
}

/* ── CLOSING ── */
.closing {
  width: 210mm;
  height: 297mm;
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
  color: #ffffff;
  line-height: 1.7;
  margin-bottom: 18px;
}
.closing p {
  font-size: 9.5px;
  color: #777;
  line-height: 2.1;
  margin-bottom: 48px;
}
.sns-block { margin-bottom: 16px; }
.sns-block .sns-label {
  font-size: 7px;
  letter-spacing: 3px;
  color: #c8a96e;
  margin-bottom: 5px;
}
.sns-block .sns-value {
  font-size: 11px;
  color: #aaaaaa;
}
</style>
</head>
<body>

<!-- ======== PAGE 1: COVER ======== -->
<div class="page">
  <div class="cover">
    <div class="cover-inner">
      <div class="cover-en">RHINOPLASTY CONSULTATION</div>
      <div class="cover-title">鼻整形の<br>カウンセリング</div>
      <div class="cover-subtitle">あなたの理想の鼻へ。</div>
      <div class="gold-divider"></div>
      <div class="cover-doctor">羽根 和秀</div>
      <div class="cover-clinic">Zetith Beauty Clinic Fukuoka</div>
    </div>
  </div>
</div>

<!-- ======== PAGE 2: DOCTOR ======== -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <span class="section-label">DOCTOR PROFILE</span>
      <span class="page-num">01</span>
    </div>
    <h2 class="section-title">担当医師について</h2>
    <div class="section-en">ABOUT YOUR DOCTOR</div>

    <div class="profile-wrap">
      <div class="profile-photo">写真</div>
      <div class="profile-info">
        <h3>羽根 和秀</h3>
        <div class="title">美容外科医 ／ 鼻整形専門</div>
        <p>鼻の構造を熟知した上で、<br>
        その人にとって自然で美しいバランスを追求しています。<br>
        「整形した」とわからない鼻が、私の考える理想の仕上がりです。</p>
      </div>
    </div>

    <ul class="career-list">
      <li><span class="year">専門</span>鼻整形・他院修正・複合施術</li>
      <li><span class="year">対応</span>鼻筋・鼻先・小鼻・鼻中隔延長・肋軟骨移植</li>
      <li><span class="year">勤務</span>Zetith Beauty Clinic 福岡院</li>
    </ul>

    <div class="philosophy-block">
      <p>「鼻は顔の中心にあります。<br>
      だからこそ、少しの違いが顔全体の印象を変えます。<br>
      私は施術を決める前に、まず『しないほうがいいケース』を考えます。<br>
      その判断ができるドクターに、任せてください。」</p>
    </div>
  </div>
</div>

<!-- ======== PAGE 3: PROCEDURE MENU ======== -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <span class="section-label">PROCEDURE MENU</span>
      <span class="page-num">02</span>
    </div>
    <h2 class="section-title">施術メニュー</h2>
    <div class="section-en">RHINOPLASTY OPTIONS</div>

    <div class="proc-row">
      <div class="proc-card">
        <h3>鼻筋（鼻根）形成</h3>
        <div class="en">NOSE BRIDGE</div>
        <p>シリコンプロテーゼまたはePTFEを挿入し、鼻筋を整えます。高さ・幅・形状を個別に設計します。</p>
        <span class="proc-tag">プロテーゼ</span>
      </div>
      <div class="proc-card">
        <h3>鼻尖縮小・形成</h3>
        <div class="en">NOSE TIP</div>
        <p>軟骨を縫合・形成し、丸みのある鼻先をシャープにします。耳介軟骨を使う場合もあります。</p>
        <span class="proc-tag">軟骨形成</span>
      </div>
    </div>

    <div class="proc-row">
      <div class="proc-card">
        <h3>小鼻縮小</h3>
        <div class="en">ALAR REDUCTION</div>
        <p>小鼻の幅・広がりを改善します。クローズ法（傷が目立たない）とオープン法から選択します。</p>
        <span class="proc-tag">切開 / クローズ</span>
      </div>
      <div class="proc-card">
        <h3>鼻中隔延長</h3>
        <div class="en">SEPTAL EXTENSION</div>
        <p>鼻先を下方・前方に延長する施術。向きや高さを大きく変えたい方に適しています。</p>
        <span class="proc-tag">軟骨移植</span>
      </div>
    </div>

    <div class="proc-row">
      <div class="proc-card">
        <h3>肋軟骨移植</h3>
        <div class="en">RIB CARTILAGE GRAFT</div>
        <p>耳介軟骨では足りない量が必要な場合、胸部の肋軟骨を採取・移植します。変形しにくく強度が高い素材です。</p>
        <span class="proc-tag">高難度施術</span>
      </div>
      <div class="proc-card">
        <h3>他院修正</h3>
        <div class="en">REVISION SURGERY</div>
        <p>他院での施術後の修正・やり直しに対応します。状態を丁寧に診断した上でプランをご提案します。</p>
        <span class="proc-tag">修正専門対応</span>
      </div>
    </div>

  </div>
</div>

<!-- ======== PAGE 4: BEFORE/AFTER ======== -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <span class="section-label">CASE GALLERY</span>
      <span class="page-num">03</span>
    </div>
    <h2 class="section-title">症例のご紹介</h2>
    <div class="section-en">BEFORE &amp; AFTER</div>

    <div class="case-section">
      <div class="case-label">CASE 01 ／ プロテーゼ ＋ 鼻尖縮小</div>
      <div class="case-photos">
        <div class="photo-box"><div class="ph-label">BEFORE</div></div>
        <div class="photo-box"><div class="ph-label">AFTER</div></div>
        <div class="photo-box"><div class="ph-label">AFTER（側面）</div></div>
      </div>
      <p class="case-note">施術：鼻プロテーゼ（シリコン）＋ 鼻尖縮小 ／ ダウンタイム：約1週間 ／ 抜糸：7日後</p>
    </div>

    <div class="case-section">
      <div class="case-label">CASE 02 ／ 小鼻縮小（クローズ法）</div>
      <div class="case-photos">
        <div class="photo-box"><div class="ph-label">BEFORE</div></div>
        <div class="photo-box"><div class="ph-label">AFTER</div></div>
        <div class="photo-box"><div class="ph-label">AFTER（正面）</div></div>
      </div>
      <p class="case-note">施術：小鼻縮小クローズ法 ／ 傷は鼻の付け根の目立たない位置 ／ 内側のみのケースも対応可</p>
    </div>

    <div class="case-section">
      <div class="case-label">CASE 03 ／ 他院修正（プロテーゼ入れ替え）</div>
      <div class="case-photos">
        <div class="photo-box"><div class="ph-label">BEFORE</div></div>
        <div class="photo-box"><div class="ph-label">AFTER</div></div>
        <div class="photo-box"><div class="ph-label">AFTER（側面）</div></div>
      </div>
      <p class="case-note">施術：他院プロテーゼ除去 ＋ 再挿入 ／ 不自然な高さ・位置の修正 ／ ダウンタイム：約10日</p>
    </div>

  </div>
</div>

<!-- ======== PAGE 5: SURGERY FLOW ======== -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <span class="section-label">PROCEDURE FLOW</span>
      <span class="page-num">04</span>
    </div>
    <h2 class="section-title">施術の流れ</h2>
    <div class="section-en">FROM CONSULTATION TO COMPLETION</div>

    <div class="flow-step">
      <div class="flow-dot"></div>
      <div class="flow-line"></div>
      <h3>カウンセリング</h3>
      <p>お悩みをお聞きし、理想のイメージをすり合わせます。施術の適否・リスク・代替案を丁寧にご説明します。「しないほうがいい」とお伝えすることもあります。</p>
    </div>

    <div class="flow-step">
      <div class="flow-dot"></div>
      <div class="flow-line"></div>
      <h3>デザイン確認・お見積り</h3>
      <p>施術プランと使用素材を決定します。シミュレーション画像でイメージをご確認いただけます。ご納得いただけたら施術日をご予約ください。</p>
    </div>

    <div class="flow-step">
      <div class="flow-dot"></div>
      <div class="flow-line"></div>
      <h3>施術当日</h3>
      <p>麻酔後、施術を行います。所要時間は施術内容により異なります。単体施術：60〜90分 ／ 複合施術：2〜3時間。施術後は院内で休憩いただきます。</p>
    </div>

    <div class="flow-step">
      <div class="flow-dot"></div>
      <div class="flow-line"></div>
      <h3>ダウンタイム期間（7〜10日）</h3>
      <p>腫れ・内出血が出ます。ギプス固定（プロテーゼの場合）が1週間あります。抜糸は施術7日後に行います。</p>
    </div>

    <div class="flow-step">
      <div class="flow-dot"></div>
      <h3>完成・アフターケア</h3>
      <p>1〜3ヶ月かけて最終的な形に落ち着きます。施術後の修正相談もいつでも承ります。</p>
    </div>

  </div>
</div>

<!-- ======== PAGE 6: DOWNTIME ======== -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <span class="section-label">DOWNTIME GUIDE</span>
      <span class="page-num">05</span>
    </div>
    <h2 class="section-title">ダウンタイムの目安</h2>
    <div class="section-en">RECOVERY TIMELINE</div>

    <div class="dt-row">
      <div class="dt-day">当日</div>
      <div class="dt-bar active"></div>
      <div class="dt-content">
        <h4>施術直後</h4>
        <p>腫れが出始めます。ギプス固定（プロテーゼの場合）を装着したまま帰宅します。<br>痛みは軽度で、処方された鎮痛剤で対応可能です。</p>
      </div>
    </div>

    <div class="dt-row">
      <div class="dt-day">1〜3日</div>
      <div class="dt-bar active"></div>
      <div class="dt-content">
        <h4>腫れのピーク</h4>
        <p>腫れと内出血が最も強く出る時期です。<br>アイスノンで冷やすと効果的です。安静を心がけてください。</p>
      </div>
    </div>

    <div class="dt-row">
      <div class="dt-day">7日</div>
      <div class="dt-bar active"></div>
      <div class="dt-content">
        <h4>抜糸・ギプス除去</h4>
        <p>抜糸を行い、ギプスを外します。<br>腫れはまだ残りますが、日常生活への支障は大きく減ります。</p>
      </div>
    </div>

    <div class="dt-row">
      <div class="dt-day">2〜4週</div>
      <div class="dt-bar"></div>
      <div class="dt-content">
        <h4>社会復帰・安定期</h4>
        <p>腫れが引き、他者に気づかれにくくなります。<br>メイクも可能になります（施術部位以外は翌日から可）。</p>
      </div>
    </div>

    <div class="dt-row">
      <div class="dt-day">1〜3ヶ月</div>
      <div class="dt-bar"></div>
      <div class="dt-content">
        <h4>完成形へ</h4>
        <p>むくみが取れ、最終的な形に落ち着きます。<br>固い感じは時間とともに自然になります。</p>
      </div>
    </div>

    <div class="philosophy-block" style="margin-top: 22px;">
      <p>ダウンタイム中で一番大事なのは「触らないこと」です。<br>
      形が定まる前に動かすと、仕上がりに影響します。<br>
      不安なことがあれば、いつでもご連絡ください。</p>
    </div>
  </div>
</div>

<!-- ======== PAGE 7: FAQ ======== -->
<div class="page">
  <div class="content-page">
    <div class="page-header">
      <span class="section-label">FREQUENTLY ASKED QUESTIONS</span>
      <span class="page-num">06</span>
    </div>
    <h2 class="section-title">よくあるご質問</h2>
    <div class="section-en">FAQ</div>

    <div class="faq-item">
      <div class="faq-q">Q. 鼻整形したことはバレますか？</div>
      <p class="faq-a">自然なデザインを選べば、ほとんどの場合バレません。ただし、高さを出しすぎる・鼻先を細くしすぎる場合はリスクが上がります。「自分の顔に合っているか」を最優先に設計します。</p>
    </div>

    <div class="faq-item">
      <div class="faq-q">Q. 一度入れたプロテーゼは将来取り出せますか？</div>
      <p class="faq-a">はい、取り出すことができます。ただし、長期間経過している場合は周囲組織に癒着が起きることがあります。修正・除去希望の場合は早めのご相談をお勧めします。</p>
    </div>

    <div class="faq-item">
      <div class="faq-q">Q. 複数の施術を同時に受けられますか？</div>
      <p class="faq-a">可能です。組み合わせることでよりバランスの良い仕上がりになるケースも多いです。施術時間・ダウンタイムの増加を考慮した上でご提案します。</p>
    </div>

    <div class="faq-item">
      <div class="faq-q">Q. 他院で施術した鼻の修正はできますか？</div>
      <p class="faq-a">対応しています。まず現状の状態を診断し、何ができるかをお伝えします。状態によっては「今は修正しない方がいい」とお伝えすることもあります。</p>
    </div>

    <div class="faq-item">
      <div class="faq-q">Q. 施術を断られることはありますか？</div>
      <p class="faq-a">あります。リスクが高い・期待に応えられない・今の状態では不適と判断した場合はお断りします。それも医師としての仕事だと考えています。</p>
    </div>

  </div>
</div>

<!-- ======== PAGE 8: CLOSING ======== -->
<div class="page">
  <div class="closing">
    <div class="closing-inner">
      <div class="cover-en" style="margin-bottom:44px;">ZETITH BEAUTY CLINIC FUKUOKA</div>
      <h2>今日のカウンセリングで<br>疑問は解消されましたか？</h2>
      <p>不安なこと、迷っていること、何でもお聞きください。<br>「決めなければいけない」という場ではありません。</p>
      <div class="gold-divider"></div>
      <div class="sns-block">
        <div class="sns-label">INSTAGRAM</div>
        <div class="sns-value">@zetith_hane</div>
      </div>
      <div class="sns-block" style="margin-top:14px;">
        <div class="sns-label">CLINIC</div>
        <div class="sns-value">Zetith Beauty Clinic 福岡院</div>
      </div>
    </div>
  </div>
</div>

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/鼻整形_カウンセリング資料.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
