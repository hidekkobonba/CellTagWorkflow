from weasyprint import HTML, CSS

html_content = """
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Noto Sans JP', 'Hiragino Sans', 'Yu Gothic', sans-serif;
    font-size: 12px;
    color: #1a1a1a;
    background: #fff;
    line-height: 1.7;
  }

  /* ===== COVER ===== */
  .cover {
    height: 100vh;
    background: linear-gradient(135deg, #0d0d0d 0%, #1a1a1a 60%, #2d2d2d 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 80px;
    page-break-after: always;
  }
  .cover-badge {
    background: #c8a96e;
    color: #fff;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 3px;
    padding: 6px 16px;
    text-transform: uppercase;
    margin-bottom: 32px;
  }
  .cover-title {
    font-size: 42px;
    font-weight: 900;
    color: #fff;
    line-height: 1.2;
    margin-bottom: 16px;
    letter-spacing: -0.5px;
  }
  .cover-title span { color: #c8a96e; }
  .cover-sub {
    font-size: 16px;
    color: #888;
    margin-bottom: 60px;
    letter-spacing: 1px;
  }
  .cover-divider {
    width: 60px;
    height: 2px;
    background: #c8a96e;
    margin-bottom: 40px;
  }
  .cover-desc {
    font-size: 13px;
    color: #bbb;
    line-height: 2;
    max-width: 420px;
  }
  .cover-clinic {
    position: absolute;
    bottom: 60px;
    right: 80px;
    text-align: right;
    color: #555;
    font-size: 11px;
    letter-spacing: 1px;
  }

  /* ===== PAGE ===== */
  .page {
    padding: 50px 56px;
    page-break-after: always;
    min-height: 100vh;
  }
  .page:last-child { page-break-after: auto; }

  /* ===== SECTION HEADER ===== */
  .section-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 32px;
    padding-bottom: 16px;
    border-bottom: 2px solid #1a1a1a;
  }
  .section-num {
    background: #1a1a1a;
    color: #c8a96e;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2px;
    padding: 6px 12px;
  }
  .section-title {
    font-size: 22px;
    font-weight: 900;
    color: #1a1a1a;
    letter-spacing: 0.5px;
  }
  .section-subtitle {
    font-size: 12px;
    color: #888;
    margin-top: 4px;
  }

  /* ===== SCHEDULE TABLE ===== */
  .schedule-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin-bottom: 32px;
  }
  .day-card {
    border: 1.5px solid #e8e8e8;
    border-radius: 2px;
    overflow: hidden;
  }
  .day-header {
    padding: 12px 16px;
    font-size: 11px;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #fff;
  }
  .day-mon .day-header { background: #1a1a1a; }
  .day-wed .day-header { background: #2d2d2d; }
  .day-fri .day-header { background: #c8a96e; }
  .day-body { padding: 16px; }
  .day-label {
    font-size: 13px;
    font-weight: 700;
    color: #1a1a1a;
    margin-bottom: 6px;
  }
  .day-desc { font-size: 11px; color: #666; line-height: 1.6; }
  .difficulty {
    display: inline-block;
    margin-top: 10px;
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 1px;
    font-weight: 700;
  }
  .diff-easy { background: #e8f5e9; color: #2e7d32; }
  .diff-mid { background: #fff3e0; color: #e65100; }

  /* ===== CONTENT TYPE CARD ===== */
  .content-card {
    border: 1.5px solid #1a1a1a;
    margin-bottom: 28px;
    page-break-inside: avoid;
  }
  .content-card-header {
    background: #1a1a1a;
    color: #fff;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .content-card-title { font-size: 15px; font-weight: 900; letter-spacing: 0.5px; }
  .content-card-tag {
    font-size: 10px;
    background: #c8a96e;
    color: #fff;
    padding: 3px 10px;
    font-weight: 700;
    letter-spacing: 1px;
  }
  .content-card-body { padding: 20px; }

  .steps { counter-reset: step; }
  .step {
    display: flex;
    gap: 14px;
    margin-bottom: 10px;
    align-items: flex-start;
  }
  .step-num {
    flex-shrink: 0;
    width: 22px;
    height: 22px;
    background: #1a1a1a;
    color: #fff;
    font-size: 11px;
    font-weight: 900;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-top: 1px;
  }
  .step-text { font-size: 12px; color: #333; line-height: 1.6; }
  .step-text strong { color: #1a1a1a; }

  .hook-box {
    background: #f9f6f1;
    border-left: 3px solid #c8a96e;
    padding: 14px 18px;
    margin: 14px 0;
  }
  .hook-label {
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #c8a96e;
    margin-bottom: 8px;
  }
  .hook-item {
    font-size: 12px;
    color: #333;
    line-height: 1.8;
  }
  .hook-item::before { content: "「"; color: #c8a96e; font-weight: 700; }
  .hook-item::after { content: "」"; color: #c8a96e; font-weight: 700; }

  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 16px;
  }
  .col-label {
    font-size: 10px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #888;
    margin-bottom: 8px;
    border-bottom: 1px solid #eee;
    padding-bottom: 6px;
  }

  /* ===== CAPTION TEMPLATE ===== */
  .caption-box {
    background: #f5f5f5;
    border: 1px solid #e0e0e0;
    padding: 16px 18px;
    font-size: 11px;
    color: #444;
    line-height: 2;
    font-family: monospace;
    margin-top: 14px;
  }

  /* ===== MONTHLY PLAN TABLE ===== */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 16px;
    font-size: 11px;
  }
  thead tr { background: #1a1a1a; color: #fff; }
  thead th {
    padding: 10px 12px;
    text-align: left;
    font-weight: 700;
    letter-spacing: 1px;
  }
  tbody tr:nth-child(even) { background: #f9f9f9; }
  tbody td { padding: 10px 12px; border-bottom: 1px solid #eee; color: #333; }
  tbody td:first-child { font-weight: 700; color: #1a1a1a; white-space: nowrap; }

  /* ===== CHECKLIST ===== */
  .checklist { margin: 12px 0; }
  .check-item {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    margin-bottom: 8px;
  }
  .check-box {
    flex-shrink: 0;
    width: 16px;
    height: 16px;
    border: 1.5px solid #1a1a1a;
    margin-top: 2px;
  }
  .check-text { font-size: 12px; color: #333; }
  .check-sub { font-size: 10px; color: #888; margin-top: 2px; }

  /* ===== POINT BOX ===== */
  .point-box {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-top: 20px;
  }
  .point {
    padding: 16px;
    border: 1.5px solid #e8e8e8;
    border-top: 3px solid #c8a96e;
  }
  .point-title { font-size: 12px; font-weight: 900; margin-bottom: 6px; color: #1a1a1a; }
  .point-text { font-size: 11px; color: #555; line-height: 1.7; }

  /* ===== NOTICE ===== */
  .notice {
    background: #fff8e1;
    border: 1.5px solid #ffd54f;
    padding: 14px 18px;
    margin-top: 20px;
    font-size: 11px;
    color: #555;
    line-height: 1.8;
  }
  .notice-title { font-weight: 900; color: #f57c00; margin-bottom: 6px; font-size: 12px; }

  .gold { color: #c8a96e; font-weight: 900; }
  .small { font-size: 11px; color: #666; }
</style>
</head>
<body>

<!-- ===== COVER ===== -->
<div class="cover">
  <div class="cover-badge">zetith_hane / Internal Document</div>
  <div class="cover-title">Instagram<br>コンテンツ<span>運用</span>ガイド</div>
  <div class="cover-sub">SNS担当者向け 企画・撮影・編集マニュアル</div>
  <div class="cover-divider"></div>
  <div class="cover-desc">
    このガイドに沿って動けば、<br>
    羽根先生に毎回確認しなくても投稿が作れます。<br><br>
    週3本・月12本の運用を<br>
    このマニュアル1冊で回してください。
  </div>
  <div class="cover-clinic">
    Zetith Beauty Clinic<br>
    zetith_hane
  </div>
</div>

<!-- ===== PAGE 1: 基本スケジュール ===== -->
<div class="page">
  <div class="section-header">
    <div class="section-num">01</div>
    <div>
      <div class="section-title">週3本の投稿スケジュール</div>
      <div class="section-subtitle">この曜日・この種類で固定して運用する</div>
    </div>
  </div>

  <div class="schedule-grid">
    <div class="day-card day-mon">
      <div class="day-header">月曜日</div>
      <div class="day-body">
        <div class="day-label">ビフォーアフター<br>写真スライド</div>
        <div class="day-desc">術前・術後の写真を並べるだけ。症例実績を積み上げる投稿。</div>
        <span class="difficulty diff-easy">★☆☆ 編集カンタン</span>
      </div>
    </div>
    <div class="day-card day-wed">
      <div class="day-header">水曜日</div>
      <div class="day-body">
        <div class="day-label">羽根先生<br>トーク解説</div>
        <div class="day-desc">先生が1つのテーマを60〜90秒で解説。字幕を入れるだけ。</div>
        <span class="difficulty diff-mid">★★☆ 普通</span>
      </div>
    </div>
    <div class="day-card day-fri">
      <div class="day-header">金曜日</div>
      <div class="day-body">
        <div class="day-label">患者ストーリー<br>/ 症例動画</div>
        <div class="day-desc">患者さんの体験談。バズりやすい一番重要な投稿。月1本は必ず。</div>
        <span class="difficulty diff-mid">★★☆ 普通</span>
      </div>
    </div>
  </div>

  <div class="notice">
    <div class="notice-title">⚑ 投稿時間のルール</div>
    月・水・金ともに <strong>20時〜21時</strong> に投稿する。ストーリーズは翌朝 <strong>8時</strong> に告知を上げる。
  </div>

  <div style="margin-top:32px;">
    <div class="section-header">
      <div class="section-num">02</div>
      <div>
        <div class="section-title">仕事の分担</div>
        <div class="section-subtitle">羽根先生とSNS担当で役割を分ける</div>
      </div>
    </div>
    <div class="two-col">
      <div>
        <div class="col-label">羽根先生がやること</div>
        <div class="checklist">
          <div class="check-item"><div class="check-box"></div><div class="check-text">症例写真を担当に渡す<div class="check-sub">月4〜6セット</div></div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">解説トーク動画を撮影<div class="check-sub">月2本まとめて撮る</div></div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">患者ストーリーを撮影<div class="check-sub">月1〜2本</div></div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">投稿前の最終確認</div></div>
        </div>
      </div>
      <div>
        <div class="col-label">SNS担当がやること</div>
        <div class="checklist">
          <div class="check-item"><div class="check-box"></div><div class="check-text">このマニュアル通りに編集</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">キャプションを書く<div class="check-sub">テンプレートを使う</div></div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">スケジュール通りに投稿</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">月末に再生数を記録・報告</div></div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ===== PAGE 2: タイプA ===== -->
<div class="page">
  <div class="section-header">
    <div class="section-num">03</div>
    <div>
      <div class="section-title">タイプA：ビフォーアフター写真スライド</div>
      <div class="section-subtitle">月曜投稿 ／ 編集時間の目安：10〜15分</div>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">撮影指示</div>
      <div class="content-card-tag">撮影不要</div>
    </div>
    <div class="content-card-body">
      羽根先生から術前・術後の写真を <strong>2〜4枚</strong> もらうだけ。撮影は不要。<br>
      <span class="small">※ 患者さんの個人情報（名前・生年月日など）が写り込んでいないか必ず確認すること。</span>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">編集手順（CapCut）</div>
      <div class="content-card-tag">STEP BY STEP</div>
    </div>
    <div class="content-card-body">
      <div class="steps">
        <div class="step"><div class="step-num">1</div><div class="step-text">写真をCapCutに読み込む</div></div>
        <div class="step"><div class="step-num">2</div><div class="step-text">各写真の表示時間を <strong>2〜3秒</strong> に設定する</div></div>
        <div class="step"><div class="step-num">3</div><div class="step-text">最初の写真に「<strong>Before</strong>」テキストを追加（白・シンプルなフォント）</div></div>
        <div class="step"><div class="step-num">4</div><div class="step-text">最後の写真に「<strong>〇ヶ月後</strong>」テキストを追加</div></div>
        <div class="step"><div class="step-num">5</div><div class="step-text">BGM：CapCut内の「おしゃれ系・静か目」から選ぶ（<strong>著作権フリーのマークがあるもの</strong>だけ使う）</div></div>
        <div class="step"><div class="step-num">6</div><div class="step-text">左上に「e」ロゴ（透過PNG）を入れる</div></div>
        <div class="step"><div class="step-num">7</div><div class="step-text">書き出し：<strong>1080×1920 / 30fps</strong></div></div>
      </div>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">キャプション テンプレート</div>
      <div class="content-card-tag">コピーして使う</div>
    </div>
    <div class="content-card-body">
      <div class="caption-box">
【症例名】〇〇（術式名を入れる）<br><br>
▷ お悩み：（患者のビフォーの状態を一言で）<br>
▷ 施術内容：（術式名・使用素材）<br>
▷ ダウンタイム：約〇週間<br><br>
━━━━━━━━━━━━<br>
🏥 ゼティスビューティークリニック 福岡院<br>
👨‍⚕️ 院長 羽根 和秀<br>
📩 DM or LINEでご相談ください<br>
━━━━━━━━━━━━<br>
#鼻整形 #ゼティス #鼻フル整形 #肋軟骨 #クローズド法<br>
#福岡美容外科 #福岡鼻整形 #鼻整形福岡 #羽根和秀
      </div>
    </div>
  </div>
</div>

<!-- ===== PAGE 3: タイプB ===== -->
<div class="page">
  <div class="section-header">
    <div class="section-num">04</div>
    <div>
      <div class="section-title">タイプB：羽根先生トーク解説</div>
      <div class="section-subtitle">水曜投稿 ／ 編集時間の目安：15〜20分</div>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">撮影指示（羽根先生へ渡す）</div>
      <div class="content-card-tag">撮影指示書</div>
    </div>
    <div class="content-card-body">
      <div class="two-col">
        <div>
          <div class="col-label">撮影環境</div>
          <div class="check-item" style="margin-top:8px;"><div class="check-box"></div><div class="check-text">場所：診察室 or クリニック内のきれいな壁前</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">服装：白衣（清潔感重視）</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">カメラ：スマホ縦置き・目線の高さに固定</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">尺：<strong>60〜90秒以内</strong>に収める</div></div>
        </div>
        <div>
          <div class="col-label">今月の企画テーマ（1本選ぶ）</div>
          <div style="margin-top:8px; font-size:11px; line-height:2; color:#333;">
            ・肋軟骨が必要な鼻・必要ない鼻の見分け方<br>
            ・クローズ法で傷跡が残らない理由<br>
            ・他院修正でよくある3つのパターン<br>
            ・小鼻縮小で失敗する人の共通点<br>
            ・鼻整形で後悔しないために知ること
          </div>
        </div>
      </div>
      <div class="hook-box">
        <div class="hook-label">HOOK — 最初の一言（これで始める）</div>
        <div class="hook-item" style="display:block; margin-bottom:4px;">肋軟骨を使わないと一生解決しない鼻の悩みがあります</div>
        <div class="hook-item" style="display:block; margin-bottom:4px;">他院で手術して後悔している方に知ってほしいことがあります</div>
        <div class="hook-item" style="display:block;">福岡で2,000件やってわかったことを正直に話します</div>
      </div>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">編集手順（CapCut）</div>
      <div class="content-card-tag">STEP BY STEP</div>
    </div>
    <div class="content-card-body">
      <div class="steps">
        <div class="step"><div class="step-num">1</div><div class="step-text">動画をCapCutに読み込む</div></div>
        <div class="step"><div class="step-num">2</div><div class="step-text"><strong>テキスト → 自動字幕 → 日本語</strong> でAI字幕を生成する</div></div>
        <div class="step"><div class="step-num">3</div><div class="step-text">誤字を修正する（特に「肋軟骨」「鼻翼基部」などの専門用語は必ず確認）</div></div>
        <div class="step"><div class="step-num">4</div><div class="step-text">字幕フォント：<strong>太め・白・黒縁取り</strong>（見やすさ重視）</div></div>
        <div class="step"><div class="step-num">5</div><div class="step-text">冒頭3秒にテキストオーバーレイでタイトルを大きく入れる<br><span class="small">例：「肋軟骨が必要な鼻・必要ない鼻」</span></div></div>
        <div class="step"><div class="step-num">6</div><div class="step-text">左上に「e」ロゴ（半透明）を入れる</div></div>
        <div class="step"><div class="step-num">7</div><div class="step-text"><strong>BGMは入れない</strong>（トーク系はBGMなしの方が視聴維持率が上がる）</div></div>
        <div class="step"><div class="step-num">8</div><div class="step-text">書き出し：<strong>1080×1920 / 30fps</strong></div></div>
      </div>
    </div>
  </div>
</div>

<!-- ===== PAGE 4: タイプC ===== -->
<div class="page">
  <div class="section-header">
    <div class="section-num">05</div>
    <div>
      <div class="section-title">タイプC：患者ストーリー</div>
      <div class="section-subtitle">金曜投稿 ／ 月1本は必ず入れる ／ 一番バズりやすいタイプ</div>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">撮影前に患者さんへ聞くこと（羽根先生が担当）</div>
      <div class="content-card-tag">ヒアリング項目</div>
    </div>
    <div class="content-card-body">
      <div class="steps">
        <div class="step"><div class="step-num">①</div><div class="step-text">鼻にコンプレックスを持ったきっかけ<br><span class="small">（誰かに言われた？ 自分で気づいた？ いつから？）</span></div></div>
        <div class="step"><div class="step-num">②</div><div class="step-text">手術を決めた「その一言」「その瞬間」</div></div>
        <div class="step"><div class="step-num">③</div><div class="step-text">術後の変化（見た目だけでなく<strong>気持ちの変化</strong>が重要）</div></div>
      </div>
      <div class="notice" style="margin-top:16px;">
        <div class="notice-title">撮影の注意</div>
        台本はNG。<strong>患者さん自身の言葉で話してもらう</strong>のがポイント。ナチュラルなリアクションが共感を生む。<br>
        顔出しNGの場合：横顔・マスク・目線から下だけの撮影でもOK。
      </div>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">編集手順（CapCut）</div>
      <div class="content-card-tag">STEP BY STEP</div>
    </div>
    <div class="content-card-body">
      <div class="steps">
        <div class="step"><div class="step-num">1</div><div class="step-text">動画をCapCutに読み込む</div></div>
        <div class="step"><div class="step-num">2</div><div class="step-text">AI自動字幕を入れて誤字修正</div></div>
        <div class="step"><div class="step-num">3</div><div class="step-text">冒頭3秒に患者の<strong>一番刺さる言葉</strong>をテキストで大きく出す<br><span class="small">例：「友達に言われて、その日に決めました」／「20年間ずっとコンプレックスでした」</span></div></div>
        <div class="step"><div class="step-num">4</div><div class="step-text">術後ビフォーアフターカットを最後に入れる（写真でもOK）</div></div>
        <div class="step"><div class="step-num">5</div><div class="step-text">BGM：CapCutの「感動系・静か目」を選ぶ</div></div>
        <div class="step"><div class="step-num">6</div><div class="step-text">書き出し：<strong>1080×1920 / 30fps</strong></div></div>
      </div>
    </div>
  </div>

  <div class="content-card">
    <div class="content-card-header">
      <div class="content-card-title">キャプション テンプレート</div>
      <div class="content-card-tag">コピーして使う</div>
    </div>
    <div class="content-card-body">
      <div class="caption-box">
（患者さんのストーリーを3〜4行でリアルに書く）<br>
「〇〇と言われた時、本当にショックでした」<br>
でも今は、鏡を見るのが楽しいと言ってくれました。<br><br>
同じ悩みを持つ方、一度ご相談ください。<br><br>
━━━━━━━━━━━━<br>
🏥 ゼティスビューティークリニック 福岡院<br>
📩 DM or LINEでご相談ください<br>
━━━━━━━━━━━━<br>
#鼻整形 #コンプレックス解消 #自信を持つ<br>
#福岡美容外科 #鼻整形福岡 #ゼティス #羽根和秀
      </div>
    </div>
  </div>
</div>

<!-- ===== PAGE 5: 月間スケジュール ===== -->
<div class="page">
  <div class="section-header">
    <div class="section-num">06</div>
    <div>
      <div class="section-title">今月の投稿スケジュール（4週分）</div>
      <div class="section-subtitle">このテーブル通りに動けばOK</div>
    </div>
  </div>

  <table>
    <thead>
      <tr>
        <th>週</th>
        <th>月曜（写真スライド）</th>
        <th>水曜（解説トーク）</th>
        <th>金曜（ストーリー / 症例）</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1週目</td>
        <td>鼻フル症例<br><span class="small">（肋軟骨使用・6ヶ月後）</span></td>
        <td>「クローズ法で傷が<br>残らない理由」</td>
        <td>患者ストーリー①<br><span class="small">（感情フック重視）</span></td>
      </tr>
      <tr>
        <td>2週目</td>
        <td>小鼻縮小症例<br><span class="small">（1ヶ月後）</span></td>
        <td>「肋軟骨が必要な鼻・<br>必要ない鼻の見分け方」</td>
        <td>他院修正ビフォーアフター<br><span class="small">（プロテーゼ修正など）</span></td>
      </tr>
      <tr>
        <td>3週目</td>
        <td>人中短縮症例<br><span class="small">（3ヶ月後）</span></td>
        <td>「他院修正でよくある<br>3つのパターン」</td>
        <td>患者ストーリー②</td>
      </tr>
      <tr>
        <td>4週目</td>
        <td>鼻柱形成症例</td>
        <td>「鼻整形で後悔しない<br>ために知ること」</td>
        <td>保存促進系<br><span class="small">（鼻タイプ別まとめなど）</span></td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top:36px;">
    <div class="section-header">
      <div class="section-num">07</div>
      <div>
        <div class="section-title">月2回の撮影デー チェックリスト</div>
        <div class="section-subtitle">まとめて撮ることで羽根先生の負担を最小化する</div>
      </div>
    </div>
    <div class="two-col">
      <div>
        <div class="col-label">羽根先生が用意するもの</div>
        <div class="checklist" style="margin-top:12px;">
          <div class="check-item"><div class="check-box"></div><div class="check-text">症例写真（ビフォーアフター）4〜6セット</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">解説トーク動画を2本まとめて撮影</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">患者ストーリー撮影（1〜2本）</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">今月使うネタを担当に伝える</div></div>
        </div>
      </div>
      <div>
        <div class="col-label">SNS担当が用意するもの</div>
        <div class="checklist" style="margin-top:12px;">
          <div class="check-item"><div class="check-box"></div><div class="check-text">CapCutアプリ（最新版に更新済み）</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">「e」ロゴ透過PNG（共有フォルダから取得）</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">スマホスタンド or 三脚</div></div>
          <div class="check-item"><div class="check-box"></div><div class="check-text">今月の投稿スケジュール表を更新</div></div>
        </div>
      </div>
    </div>
  </div>

  <div style="margin-top:28px;">
    <div class="section-header" style="margin-bottom:16px;">
      <div class="section-num">08</div>
      <div>
        <div class="section-title">よくある質問</div>
      </div>
    </div>
    <div class="point-box">
      <div class="point">
        <div class="point-title">Q. 自動字幕の誤字が多い場合は？</div>
        <div class="point-text">修正は必須。「肋軟骨」「鼻翼基部」「人中短縮」などの専門用語は特に注意して確認する。</div>
      </div>
      <div class="point">
        <div class="point-title">Q. 患者さんが顔出しNGの場合は？</div>
        <div class="point-text">横顔・マスク・目線から下だけの撮影でOK。シルエット加工でも問題なし。</div>
      </div>
      <div class="point">
        <div class="point-title">Q. BGMの著作権は大丈夫？</div>
        <div class="point-text">CapCut内の「商用利用可」マークがついているものだけ使う。外部の音楽は絶対NG。</div>
      </div>
      <div class="point">
        <div class="point-title">Q. 羽根先生に確認するタイミングは？</div>
        <div class="point-text">投稿の24時間前までに編集を終えて確認を依頼する。修正は当日中に対応。</div>
      </div>
    </div>
  </div>
</div>

</body>
</html>
"""

from weasyprint import HTML
import os

output_path = "/home/user/CellTagWorkflow/sns/instagram_運用ガイド_zetith_hane.pdf"
HTML(string=html_content).write_pdf(output_path)
print(f"PDF生成完了: {output_path}")
