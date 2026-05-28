from weasyprint import HTML

html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Hiragino Sans','Yu Gothic',sans-serif; font-size:11px; color:#1a1a1a; background:#fff; line-height:1.6; }

/* COVER */
.cover { height:100vh; background:linear-gradient(160deg,#0d0d0d 0%,#1c1c1c 70%,#2a2a2a 100%); display:flex; flex-direction:column; justify-content:center; padding:80px; page-break-after:always; position:relative; }
.cover-eyebrow { color:#c8a96e; font-size:10px; font-weight:700; letter-spacing:4px; margin-bottom:28px; }
.cover-title { font-size:46px; font-weight:900; color:#fff; line-height:1.15; margin-bottom:20px; }
.cover-title em { color:#c8a96e; font-style:normal; }
.cover-sub { font-size:14px; color:#888; margin-bottom:48px; letter-spacing:1px; }
.cover-line { width:56px; height:2px; background:#c8a96e; margin-bottom:36px; }
.cover-desc { font-size:13px; color:#aaa; line-height:2.2; max-width:440px; }
.cover-meta { position:absolute; bottom:64px; right:80px; text-align:right; color:#444; font-size:10px; letter-spacing:2px; line-height:1.8; }

/* PAGE */
.page { padding:48px 56px; page-break-after:always; }
.page:last-child { page-break-after:auto; }

/* SECTION HEADER */
.sh { display:flex; align-items:center; gap:12px; margin-bottom:28px; padding-bottom:14px; border-bottom:2px solid #1a1a1a; }
.sh-num { background:#1a1a1a; color:#c8a96e; font-size:10px; font-weight:900; letter-spacing:2px; padding:5px 11px; }
.sh-title { font-size:20px; font-weight:900; }
.sh-sub { font-size:11px; color:#888; margin-top:3px; }

/* BUZZ PATTERN */
.patterns { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:20px; }
.pat { border:1.5px solid #e8e8e8; border-top:3px solid #c8a96e; padding:16px; }
.pat-label { font-size:9px; font-weight:900; letter-spacing:2px; color:#c8a96e; margin-bottom:6px; }
.pat-title { font-size:13px; font-weight:900; margin-bottom:6px; }
.pat-desc { font-size:10px; color:#555; line-height:1.7; }
.pat-eg { font-size:10px; color:#888; margin-top:6px; font-style:italic; }

/* CALENDAR TABLE */
.cal { width:100%; border-collapse:collapse; font-size:10px; }
.cal thead tr { background:#1a1a1a; color:#fff; }
.cal thead th { padding:9px 10px; text-align:left; font-weight:700; letter-spacing:0.5px; }
.cal tbody td { padding:8px 10px; border-bottom:1px solid #eee; vertical-align:top; }
.cal tbody tr:nth-child(even) { background:#f9f9f9; }
.day-n { font-weight:900; color:#1a1a1a; white-space:nowrap; }
.tag { display:inline-block; font-size:9px; font-weight:700; padding:2px 7px; margin-bottom:4px; }
.tag-story { background:#fff0f0; color:#c0392b; }
.tag-edu { background:#e8f5e9; color:#1b5e20; }
.tag-ba { background:#e3f2fd; color:#0d47a1; }
.tag-talk { background:#fff8e1; color:#e65100; }
.tag-diag { background:#f3e5f5; color:#4a148c; }
.tag-real { background:#e0f2f1; color:#004d40; }
.cal-title { font-size:11px; font-weight:700; margin-bottom:3px; }
.cal-hook { font-size:10px; color:#555; }

/* VIDEO BRIEF CARD */
.brief-wrap { margin-bottom:22px; page-break-inside:avoid; }
.brief-head { background:#1a1a1a; color:#fff; padding:12px 18px; display:flex; justify-content:space-between; align-items:center; }
.brief-day { font-size:10px; color:#c8a96e; font-weight:900; letter-spacing:1px; }
.brief-title { font-size:14px; font-weight:900; margin-top:2px; }
.brief-body { border:1.5px solid #1a1a1a; border-top:none; padding:16px 18px; }
.brief-tags { display:flex; gap:6px; margin-bottom:12px; flex-wrap:wrap; }
.brief-row { display:grid; grid-template-columns:80px 1fr; gap:8px; margin-bottom:8px; align-items:start; }
.brief-label { font-size:9px; font-weight:900; letter-spacing:1.5px; color:#c8a96e; padding-top:2px; }
.brief-val { font-size:11px; color:#333; line-height:1.7; }
.hook-text { background:#f9f6f1; border-left:3px solid #c8a96e; padding:8px 12px; font-size:11px; color:#333; font-weight:700; }
.flow-list { list-style:none; }
.flow-list li { display:flex; gap:8px; margin-bottom:6px; align-items:flex-start; }
.flow-n { flex-shrink:0; width:18px; height:18px; background:#1a1a1a; color:#fff; font-size:9px; font-weight:900; display:flex; align-items:center; justify-content:center; }
.flow-text { font-size:11px; color:#333; line-height:1.6; }
.buzz-box { background:#fffde7; border-left:3px solid #ffd54f; padding:8px 12px; font-size:10px; color:#555; line-height:1.7; }
.buzz-box strong { color:#e65100; }

/* 2-col layout */
.two { display:grid; grid-template-columns:1fr 1fr; gap:18px; }
.col-hd { font-size:9px; font-weight:900; letter-spacing:2px; color:#888; margin-bottom:8px; padding-bottom:5px; border-bottom:1px solid #eee; }

.week-banner { background:#1a1a1a; color:#fff; padding:14px 20px; margin-bottom:24px; display:flex; align-items:center; gap:16px; }
.week-num { font-size:28px; font-weight:900; color:#c8a96e; }
.week-title { font-size:16px; font-weight:900; }
.week-sub { font-size:11px; color:#aaa; margin-top:2px; }

.notice { background:#f0f4ff; border:1.5px solid #c5cae9; padding:12px 16px; font-size:11px; color:#333; line-height:1.8; margin-top:16px; }
.nt { font-weight:900; color:#3949ab; margin-bottom:4px; font-size:12px; }

.gold { color:#c8a96e; font-weight:900; }
</style>
</head>
<body>

<!-- COVER -->
<div class="cover">
  <div class="cover-eyebrow">zetith_hane / Instagram Strategy</div>
  <div class="cover-title">毎日1リール<br><em>30日間</em><br>バズ設計ガイド</div>
  <div class="cover-sub">SNS担当者向け 完全詳細版</div>
  <div class="cover-line"></div>
  <div class="cover-desc">
    30本すべてのリールに<br>
    フック・構成・バズポイント・撮影メモを記載。<br><br>
    このガイドを見れば<br>
    羽根先生に確認しなくても動けます。
  </div>
  <div class="cover-meta">Zetith Beauty Clinic<br>zetith_hane<br>毎日投稿プラン</div>
</div>

<!-- PAGE: バズ設計の5原則 -->
<div class="page">
  <div class="sh"><div class="sh-num">01</div><div><div class="sh-title">バズる設計の5パターン</div><div class="sh-sub">この5種類を組み合わせて30日間回す</div></div></div>

  <div class="patterns">
    <div class="pat">
      <div class="pat-label">PATTERN 01</div>
      <div class="pat-title">自己診断型</div>
      <div class="pat-desc">「あなたはどのタイプ？」と思わせる。自分ごとになるので保存・シェア率が高い。</div>
      <div class="pat-eg">例：「この鼻の形、肋軟骨じゃないと一生変わりません」</div>
    </div>
    <div class="pat">
      <div class="pat-label">PATTERN 02</div>
      <div class="pat-title">感情ストーリー型</div>
      <div class="pat-desc">患者のリアルな体験談。コンプレックスへの共感で最後まで見られ、バズりやすい。</div>
      <div class="pat-eg">例：「友達に言われた一言から3年後」</div>
    </div>
    <div class="pat">
      <div class="pat-label">PATTERN 03</div>
      <div class="pat-title">不安解消型</div>
      <div class="pat-desc">「失敗したら」「傷跡が」という不安を先に提示してから解消する。コメントが集まる。</div>
      <div class="pat-eg">例：「鼻整形で後悔した人の共通点3つ」</div>
    </div>
    <div class="pat">
      <div class="pat-label">PATTERN 04</div>
      <div class="pat-title">暴露・本音型</div>
      <div class="pat-desc">「正直に言います」「全部話します」でクリック率UP。信頼感が爆上がりする。</div>
      <div class="pat-eg">例：「この手術、正直やめた方がいいケースがあります」</div>
    </div>
    <div class="pat" style="grid-column:1/3;">
      <div class="pat-label">PATTERN 05</div>
      <div class="pat-title">権威×謙虚型</div>
      <div class="pat-desc">実績（2,000件・クローズ法特化）を権威として見せながら、「わかったこと」「気づいたこと」という謙虚な言葉と組み合わせる。フォロー率が最も上がるパターン。</div>
      <div class="pat-eg">例：「2,000件やってきて、一番大事なのは技術じゃないと気づきました」</div>
    </div>
  </div>

  <div class="notice">
    <div class="nt">毎日投稿のルール</div>
    投稿時間：<strong>毎日20時〜21時</strong>（週末も変えない）。ストーリーズで翌朝8時に告知。
    動画尺の目安：<strong>45秒〜90秒</strong>が最適。90秒を超えると視聴維持率が下がるので注意。
    字幕は全動画に入れる（AI自動字幕＋誤字修正）。
  </div>

  <div class="sh" style="margin-top:32px;"><div class="sh-num">02</div><div><div class="sh-title">30日間カレンダー（概要）</div></div></div>
  <table class="cal">
    <thead><tr><th>Day</th><th>タイプ</th><th>タイトル</th><th>フック</th></tr></thead>
    <tbody>
      <tr><td class="day-n">Day 1</td><td><span class="tag tag-diag">自己診断</span></td><td class="cal-title">この鼻の形、肋軟骨じゃないと一生変わりません</td><td class="cal-hook">「実は...この3タイプの鼻、プロテーゼだけでは絶対変わりません」</td></tr>
      <tr><td class="day-n">Day 2</td><td><span class="tag tag-story">患者ストーリー</span></td><td class="cal-title">20年間隠し続けた鼻が変わった日</td><td class="cal-hook">「20年間、正面から写真撮れなかったんですよ」</td></tr>
      <tr><td class="day-n">Day 3</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">クローズ法 vs オープン法、本当はどっちがいいのか全部話します</td><td class="cal-hook">「聞かれすぎるので全部正直に答えます」</td></tr>
      <tr><td class="day-n">Day 4</td><td><span class="tag tag-ba">BA</span></td><td class="cal-title">鼻先の溝が消えるまで（クローズ法・3ヶ月後）</td><td class="cal-hook">テキスト：「鼻先の溝、コンプレックスの方へ」</td></tr>
      <tr><td class="day-n">Day 5</td><td><span class="tag tag-talk">本音トーク</span></td><td class="cal-title">鼻整形で後悔した人の共通点3つ</td><td class="cal-hook">「失敗する人、ほぼ全員これをやってます」</td></tr>
      <tr><td class="day-n">Day 6</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">他院修正：20年前のプロテーゼを全部やり直した話</td><td class="cal-hook">「20年前に入れたプロテーゼが曲がってきました、という相談を受けた話」</td></tr>
      <tr><td class="day-n">Day 7</td><td><span class="tag tag-real">リアル情報</span></td><td class="cal-title">術後7日間のダウンタイム、全部公開します</td><td class="cal-hook">「ダウンタイムのリアル、全部見せます」</td></tr>
      <tr><td class="day-n">Day 8</td><td><span class="tag tag-talk">本音トーク</span></td><td class="cal-title">正直に言います。この悩みなら手術しなくていいかもしれません</td><td class="cal-hook">「この鼻の悩み、手術しなくていいかもしれません」</td></tr>
      <tr><td class="day-n">Day 9</td><td><span class="tag tag-story">患者ストーリー</span></td><td class="cal-title">友達の一言から3年後</td><td class="cal-hook">「友達に『その鼻どうにかしないの』って言われて」</td></tr>
      <tr><td class="day-n">Day 10</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">小鼻縮小の傷跡、全部本当のことを言います</td><td class="cal-hook">「小鼻縮小やりたいけど傷跡が怖い方へ」</td></tr>
      <tr><td class="day-n">Day 11</td><td><span class="tag tag-ba">BA</span></td><td class="cal-title">団子鼻→シュッ。肋軟骨＋鼻尖形成の6ヶ月後</td><td class="cal-hook">テキスト：「団子鼻でお悩みの方へ」</td></tr>
      <tr><td class="day-n">Day 12</td><td><span class="tag tag-real">リアル情報</span></td><td class="cal-title">鼻整形、全部やったらいくらかかるか正直計算します</td><td class="cal-hook">「鼻全部やったら結局いくら？正直に計算します」</td></tr>
      <tr><td class="day-n">Day 13</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">手術後にこれをやると後悔します（5つ）</td><td class="cal-hook">「手術後にやってはいけないこと、全部言います」</td></tr>
      <tr><td class="day-n">Day 14</td><td><span class="tag tag-talk">本音トーク</span></td><td class="cal-title">2,000件やって一番大事だと気づいたこと</td><td class="cal-hook">「2,000件手術してきて、一番大事なのは技術じゃないと気づきました」</td></tr>
      <tr><td class="day-n">Day 15</td><td><span class="tag tag-diag">自己診断</span></td><td class="cal-title">鷲鼻、削るだけが正解じゃない話</td><td class="cal-hook">「鷲鼻を削るだけで解決しようとすると失敗します」</td></tr>
      <tr><td class="day-n">Day 16</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">鼻の低さに悩む人へ。原因は3タイプあります</td><td class="cal-hook">「鼻が低い原因、実は3タイプあります。あなたはどれ？」</td></tr>
      <tr><td class="day-n">Day 17</td><td><span class="tag tag-ba">BA</span></td><td class="cal-title">人中短縮（Cカール形成）1ヶ月後</td><td class="cal-hook">テキスト：「人中が長いと感じる方へ」</td></tr>
      <tr><td class="day-n">Day 18</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">プロテーゼと肋軟骨、何が違うのか全部説明します</td><td class="cal-hook">「プロテーゼと肋軟骨、どう違うか正直に全部説明します」</td></tr>
      <tr><td class="day-n">Day 19</td><td><span class="tag tag-story">患者ストーリー</span></td><td class="cal-title">彼氏にずっと言えなかった話</td><td class="cal-hook">「鼻のこと、彼氏に3年間ずっと言えなかったんです」</td></tr>
      <tr><td class="day-n">Day 20</td><td><span class="tag tag-talk">本音トーク</span></td><td class="cal-title">カウンセリングで絶対に聞いてほしいこと3つ</td><td class="cal-hook">「どのクリニックに行くにも、これだけは聞いてください」</td></tr>
      <tr><td class="day-n">Day 21</td><td><span class="tag tag-real">リアル情報</span></td><td class="cal-title">術後1ヶ月・3ヶ月・6ヶ月、鼻はどう変わっていくか</td><td class="cal-hook">「術後、鼻はどう変化していくか全部見せます」</td></tr>
      <tr><td class="day-n">Day 22</td><td><span class="tag tag-talk">本音トーク</span></td><td class="cal-title">鼻整形を迷っている人に伝えたいこと</td><td class="cal-hook">「迷っている方に、正直に一つだけ言わせてください」</td></tr>
      <tr><td class="day-n">Day 23</td><td><span class="tag tag-ba">BA</span></td><td class="cal-title">成人式の2ヶ月前に手術した話（垢抜け記録）</td><td class="cal-hook">テキスト：「成人式前の鼻整形」</td></tr>
      <tr><td class="day-n">Day 24</td><td><span class="tag tag-diag">自己診断</span></td><td class="cal-title">メンズの鼻整形、実はこんなに多い話</td><td class="cal-hook">「男性の鼻整形、実は思ってるより多いです」</td></tr>
      <tr><td class="day-n">Day 25</td><td><span class="tag tag-story">患者ストーリー</span></td><td class="cal-title">40代で初めて手術した話</td><td class="cal-hook">「40代で初めて鼻整形を決意した理由を聞かせてください」</td></tr>
      <tr><td class="day-n">Day 26</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">傷跡が残らないクローズ法、縫合のこだわりを全部見せます</td><td class="cal-hook">「傷跡が残らない理由、縫合を見れば全部わかります」</td></tr>
      <tr><td class="day-n">Day 27</td><td><span class="tag tag-real">リアル情報</span></td><td class="cal-title">ゼティスを選んだ理由、患者さん3人に聞いた</td><td class="cal-hook">「なぜゼティスを選んだか、患者さんに直接聞きました」</td></tr>
      <tr><td class="day-n">Day 28</td><td><span class="tag tag-ba">BA</span></td><td class="cal-title">鼻フル整形（肋軟骨）6ヶ月後の完成形</td><td class="cal-hook">テキスト：「6ヶ月後、これが完成形です」</td></tr>
      <tr><td class="day-n">Day 29</td><td><span class="tag tag-edu">教育</span></td><td class="cal-title">鼻整形後の1年間に起こること、全部話します</td><td class="cal-hook">「術後1年間で何が起きるか、全部正直に話します」</td></tr>
      <tr><td class="day-n">Day 30</td><td><span class="tag tag-talk">本音トーク</span></td><td class="cal-title">今月の振り返り＋来月予告（フォロワーへのメッセージ）</td><td class="cal-hook">「今月も見てくれてありがとうございました」</td></tr>
    </tbody>
  </table>
</div>

<!-- WEEK 1 DETAIL -->
<div class="page">
  <div class="week-banner"><div class="week-num">W1</div><div><div class="week-title">Week 1（Day 1〜7）：権威確立週</div><div class="week-sub">最初の1週間でアカウントの専門性と信頼感を打ち立てる</div></div></div>

  <!-- Day 1 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 1</div><div class="brief-title">この鼻の形、肋軟骨じゃないと一生変わりません</div></div><span class="tag tag-diag" style="align-self:center;">自己診断型</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「実はこの3タイプの鼻、プロテーゼだけでは絶対に変わりません」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">羽根先生（白衣）＋ 図解テキストオーバーレイ</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">
        <ul class="flow-list">
          <li><div class="flow-n">1</div><div class="flow-text">フックの一言を言う（0〜3秒）</div></li>
          <li><div class="flow-n">2</div><div class="flow-text">「タイプ① 鼻先が丸い（団子鼻）」→軟骨が問題と説明（10秒）</div></li>
          <li><div class="flow-n">3</div><div class="flow-text">「タイプ② 鼻筋は通っているのに鼻先だけ低い」→肋軟骨移植が必要（10秒）</div></li>
          <li><div class="flow-n">4</div><div class="flow-text">「タイプ③ 小鼻が横に広がっていて全体的にボテッとしている」→複合手術の必要性（10秒）</div></li>
          <li><div class="flow-n">5</div><div class="flow-text">「自分がどのタイプか気になる方はDMください」でCTA（5秒）</div></li>
        </ul>
      </div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box"><strong>「自分はどのタイプ？」</strong>と思わせる自己診断設計。画面を止めて見てもらえる。保存率が高い＝アルゴリズムに乗る。</div></div>
      <div class="brief-row"><div class="brief-label">撮影メモ</div><div class="brief-val">編集でタイプ名をテキストとして画面に大きく出す（先生が話すタイミングに合わせて）。図は手書き感のある矢印で充分。</div></div>
    </div>
  </div>

  <!-- Day 2 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 2</div><div class="brief-title">20年間隠し続けた鼻が変わった日</div></div><span class="tag tag-story" style="align-self:center;">患者ストーリー</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">患者「20年間、正面から写真を撮れなかったんですよ」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">患者さん（顔出し or 横顔）</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60〜75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">
        <ul class="flow-list">
          <li><div class="flow-n">1</div><div class="flow-text">冒頭：上記フックの言葉を患者に語ってもらう（冒頭カット）</div></li>
          <li><div class="flow-n">2</div><div class="flow-text">いつからコンプレックスだったか・何が一番嫌だったか</div></li>
          <li><div class="flow-n">3</div><div class="flow-text">手術を決めたきっかけの一言・瞬間</div></li>
          <li><div class="flow-n">4</div><div class="flow-text">術後の気持ちの変化（「鏡を見るのが楽しくなった」等）</div></li>
          <li><div class="flow-n">5</div><div class="flow-text">最後にビフォーアフター写真（3秒）</div></li>
        </ul>
      </div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box"><strong>「20年間」という具体的な数字</strong>が共感を呼ぶ。「自分も同じ」と感じた人がコメント・シェアする。</div></div>
      <div class="brief-row"><div class="brief-label">撮影メモ</div><div class="brief-val">患者に台本は渡さない。自分の言葉で話してもらう。感情が出てきたらそのカットを使う。顔出しNGなら横顔でOK。</div></div>
    </div>
  </div>
</div>

<div class="page">
  <!-- Day 3 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 3</div><div class="brief-title">クローズ法 vs オープン法、本当はどっちがいいのか全部話します</div></div><span class="tag tag-edu" style="align-self:center;">教育</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「クローズとオープン、どっちがいいか聞かれすぎるので全部正直に答えます」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">羽根先生（白衣）</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">90秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">
        <ul class="flow-list">
          <li><div class="flow-n">1</div><div class="flow-text">「クローズ法とは何か」を10秒で説明</div></li>
          <li><div class="flow-n">2</div><div class="flow-text">「オープン法とは何か」を10秒で説明</div></li>
          <li><div class="flow-n">3</div><div class="flow-text">それぞれのメリット・デメリットを比較（画面にテキスト表示しながら）</div></li>
          <li><div class="flow-n">4</div><div class="flow-text">「俺がクローズ法にこだわる理由」を話す（ここが一番大事・感情込めて）</div></li>
          <li><div class="flow-n">5</div><div class="flow-text">「どちらが向いているかはDMで相談してください」</div></li>
        </ul>
      </div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">比較系教育コンテンツは<strong>保存率が最も高い</strong>。クリニック選びの判断材料になるため、検討中の人が全員保存する。</div></div>
      <div class="brief-row"><div class="brief-label">撮影メモ</div><div class="brief-val">編集時に「クローズ法」「オープン法」のテキストを交互に画面に出す。羽根先生の「こだわり」の部分はカットせず丁寧に使う。</div></div>
    </div>
  </div>

  <!-- Day 4 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 4</div><div class="brief-title">鼻先の溝が消えるまで（クローズ法・3ヶ月後）</div></div><span class="tag tag-ba" style="align-self:center;">ビフォーアフター</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">テキスト大きく：「鼻先の溝が気になる方へ」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">写真スライドのみ（患者写真）</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">30〜40秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">Before正面→Before横→Before斜め→施術内容テキスト3秒→After正面→After横→After斜め→「3ヶ月後」テキスト</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">「鼻先の溝」という<strong>ニッチな悩みに特化</strong>した投稿はその悩みを持つ人に100%刺さる。ターゲットが明確なほど反応率が上がる。</div></div>
    </div>
  </div>

  <!-- Day 5 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 5</div><div class="brief-title">鼻整形で後悔した人の共通点3つ</div></div><span class="tag tag-talk" style="align-self:center;">本音トーク</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「鼻整形で失敗した人、ほぼ全員これをやってます」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">羽根先生（白衣 or 私服どちらでも可）</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75〜90秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">
        <ul class="flow-list">
          <li><div class="flow-n">1</div><div class="flow-text">「共通点① 価格だけで選ぶ」→なぜそれが失敗につながるか</div></li>
          <li><div class="flow-n">2</div><div class="flow-text">「共通点② 術式を理解しないまま手術する」→後で「聞いてなかった」になる</div></li>
          <li><div class="flow-n">3</div><div class="flow-text">「共通点③ 他院の症例写真と比べてしまう」→比較基準が違いすぎる問題</div></li>
          <li><div class="flow-n">4</div><div class="flow-text">「この3つを知った上でカウンセリングに来てください」</div></li>
        </ul>
      </div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">「失敗」「後悔」ワードは検索ボリュームが高く、<strong>検討中の人が必ず保存する</strong>。コメントで「④も追加してほしい」などの議論も生まれやすい。</div></div>
    </div>
  </div>

  <!-- Day 6 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 6</div><div class="brief-title">他院修正：20年前のプロテーゼを全部やり直した話</div></div><span class="tag tag-edu" style="align-self:center;">教育</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「20年前に入れたプロテーゼが曲がってきた、という相談を受けた話をします」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">羽根先生（解説）＋ビフォーアフター写真</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">患者の状態説明 → なぜ修正が難しいか → 手術内容 → 術後写真 → 「他院修正はどのクリニックでもできるわけではありません」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">「将来自分の鼻も曲がる？」という<strong>不安を持っているプロテーゼ経験者</strong>に刺さる。他院修正の専門性を示す最高のコンテンツ。</div></div>
    </div>
  </div>

  <!-- Day 7 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 7</div><div class="brief-title">術後7日間のダウンタイム、全部公開します</div></div><span class="tag tag-real" style="align-self:center;">リアル情報</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「ダウンタイムのリアル、全部正直に見せます」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">患者さんの経過写真スライド</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">45〜60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">術直後→1日目→3日目→5日目→7日目→1ヶ月後の写真を順番に。各写真に日数テキスト＋「腫れ・むくみ状態」のメモテキストを添える。</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">手術検討者が<strong>一番知りたいのはダウンタイムのリアル</strong>。正直に見せることで信頼感UP。保存率・シェア率ともに高い。</div></div>
    </div>
  </div>
</div>

<!-- WEEK 2 DETAIL -->
<div class="page">
  <div class="week-banner"><div class="week-num">W2</div><div><div class="week-title">Week 2（Day 8〜14）：共感・悩み刺し週</div><div class="week-sub">視聴者の「自分のことだ」という感覚を最大化する</div></div></div>

  <!-- Day 8 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 8</div><div class="brief-title">正直に言います。この悩みなら手術しなくていいかもしれません</div></div><span class="tag tag-talk" style="align-self:center;">本音トーク</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「この鼻の悩み、実は手術しなくていいかもしれません。正直に言います」</div></div>
      <div class="brief-row"><div class="brief-label">出演</div><div class="brief-val">羽根先生</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">注入系（ヒアルロン酸）で解決できるケースを説明 → 手術が必要なケースとの違いを明確に → 「まずカウンセリングで判断しましょう」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">美容外科医が<strong>「手術しなくていい」と言う逆張り</strong>は信頼感が爆上がりする。「この先生は本音を言ってくれる」とフォローされる最強パターン。</div></div>
    </div>
  </div>

  <!-- Day 9 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 9</div><div class="brief-title">友達の一言から3年後</div></div><span class="tag tag-story" style="align-self:center;">患者ストーリー</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">患者：「友達に『その鼻どうにかしないの』って言われて」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">友達の一言のエピソード → 3年間悩み続けた理由（怖かった・お金・踏み切れなかった）→ 決断したきっかけ → 術後「なんで3年も悩んでたんだろう」という一言 → BA写真</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">「友達に言われた」経験は多くの人に刺さる。<strong>「3年も悩んでた」という後悔の言葉</strong>は同じ立場の検討者の背中を押す。</div></div>
    </div>
  </div>

  <!-- Day 10 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 10</div><div class="brief-title">小鼻縮小の傷跡、全部本当のことを言います</div></div><span class="tag tag-edu" style="align-self:center;">教育</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「小鼻縮小やりたいけど傷跡が怖い方へ、全部正直に話します」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">傷跡が目立つケースと目立たないケースの違い → 医師の技術が傷跡に直結する話 → 羽根先生の縫合へのこだわり → 術後ケアの重要性 → 実際の傷跡写真（時間経過）</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">小鼻縮小を検討している人の<strong>最大の不安が傷跡</strong>。この不安に直接答えるコンテンツは100%保存される。</div></div>
    </div>
  </div>

  <!-- Day 11 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 11</div><div class="brief-title">団子鼻→シュッ。肋軟骨＋鼻尖形成の6ヶ月後</div></div><span class="tag tag-ba" style="align-self:center;">ビフォーアフター</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">テキスト：「団子鼻、6ヶ月でここまで変わります」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">35秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">Before（正面・横・斜め）→ 施術内容テキスト → After（3方向）→「6ヶ月後」テキスト → DM誘導</div></div>
    </div>
  </div>

  <!-- Day 12 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 12</div><div class="brief-title">鼻整形、全部やったらいくらかかるか正直計算します</div></div><span class="tag tag-real" style="align-self:center;">リアル情報</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「鼻全部やったら結局いくら？正直に計算します」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">90秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">鼻尖形成・鼻柱形成・小鼻縮小・人中短縮・プロテーゼの相場を画面に出しながら説明 → セット手術のメリット（ダウンタイムが1回で済む）→「安さだけで選ぶリスク」を最後に</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">価格情報は<strong>検索ボリューム最上位</strong>。実用情報として保存率が高く、「参考になった」コメントが集まる。</div></div>
    </div>
  </div>

  <!-- Day 13 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 13</div><div class="brief-title">手術後にこれをやると後悔します（5つ）</div></div><span class="tag tag-edu" style="align-self:center;">教育</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「手術後にやってはいけないこと、知らないと後悔します」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">①触りすぎる ②激しい運動を早くやる ③日焼け ④飲酒 ⑤他の人の経過と比べて焦る → それぞれ「なぜダメか」を短く説明</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">リスト型は<strong>保存率が高い</strong>。術後の患者・術後検討者の両方に刺さる。「①はやってた…」というコメントが集まる。</div></div>
    </div>
  </div>

  <!-- Day 14 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 14</div><div class="brief-title">2,000件やって一番大事だと気づいたこと</div></div><span class="tag tag-talk" style="align-self:center;">本音トーク</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「2,000件手術してきて、一番大事なのは技術じゃないと気づきました」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">「技術より大事なのは患者との対話だと気づいた」エピソード → 具体的なエピソード（患者が本当に望んでいたことと、最初に聞いていたことが違った話）→「だからカウンセリングに時間をかけています」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">権威性（2,000件）と人間性を同時に見せる。<strong>「この先生に頼みたい」とフォロー＆DM問い合わせが一番来るパターン</strong>。</div></div>
    </div>
  </div>
</div>

<!-- WEEK 3 DETAIL -->
<div class="page">
  <div class="week-banner"><div class="week-num">W3</div><div><div class="week-title">Week 3（Day 15〜21）：専門性深掘り週</div><div class="week-sub">技術と知識の深さを見せて「ここでしかできない」を感じさせる</div></div></div>

  <!-- Day 15 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 15</div><div class="brief-title">鷲鼻、削るだけが正解じゃない話</div></div><span class="tag tag-diag" style="align-self:center;">自己診断型</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「鷲鼻を削るだけで解決しようとすると、逆に失敗します」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">鷲鼻の種類（骨が原因 vs 軟骨が原因）→ それぞれに必要な術式が違う説明 → 「削るだけ」でうまくいかないケースの解説 → 適切なアプローチの紹介</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">鷲鼻コンプレックスは検索ボリュームが高い。<strong>「削れば治る」という思い込みを覆す</strong>内容で共有されやすい。</div></div>
    </div>
  </div>

  <!-- Day 16 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 16</div><div class="brief-title">鼻の低さに悩む人へ。原因は3タイプあります</div></div><span class="tag tag-diag" style="align-self:center;">自己診断型</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「鼻が低い原因、実は3タイプあります。あなたはどれ？」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">①鼻筋が低い（骨格） ②鼻先が低い（軟骨） ③全体的に低い（複合）→ タイプ別に必要な術式を説明 → 「自分のタイプはDMで相談を」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">「自分はどれ？」と思わせる自己診断型。<strong>DM誘導との相性が最高</strong>。</div></div>
    </div>
  </div>

  <!-- Day 17 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 17</div><div class="brief-title">人中短縮（Cカール形成）1ヶ月後</div></div><span class="tag tag-ba" style="align-self:center;">ビフォーアフター</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">テキスト：「人中が長いと感じている方へ」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">35秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">Before（正面・斜め）→ 施術テキスト → After（正面・斜め）→ 「1ヶ月後・傷跡なし」のテキスト → DM誘導</div></div>
    </div>
  </div>

  <!-- Day 18 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 18</div><div class="brief-title">プロテーゼと肋軟骨、何が違うのか全部説明します</div></div><span class="tag tag-edu" style="align-self:center;">教育</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「プロテーゼと肋軟骨の違い、全部正直に説明します」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">90秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">プロテーゼのメリデメ → 肋軟骨のメリデメ → どちらが向いているか（鼻の状態・予算・希望によって違う）→「どちらが正解とは言えません」という正直な結論</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">最も検索される医療用語の比較。<strong>「結論を出さない正直さ」</strong>が信頼感を生み、フォローされる。</div></div>
    </div>
  </div>

  <!-- Day 19 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 19</div><div class="brief-title">彼氏にずっと言えなかった話</div></div><span class="tag tag-story" style="align-self:center;">患者ストーリー</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">患者：「鼻のこと、彼氏に3年間ずっと言えなかったんです」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">「言えなかった理由」→「バレたくなかった」→「術後に彼氏が気づいたかどうか」→術後の自分への感想 → BA写真</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">「バレるかどうか」という<strong>美容整形で最も共通する不安</strong>を扱うコンテンツ。同じ悩みを持つ人が全員止まる。</div></div>
    </div>
  </div>

  <!-- Day 20 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 20</div><div class="brief-title">カウンセリングで絶対に聞いてほしいこと3つ</div></div><span class="tag tag-talk" style="align-self:center;">本音トーク</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「どのクリニックに行くにも、これだけは必ず聞いてください」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">①この先生はどのくらいの症例数をこなしているか ②修正が必要になった場合の対応は ③ダウンタイムの実際（写真を見せてもらえるか）→「聞きづらくても聞いてください」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box"><strong>クリニック選びの判断材料</strong>として保存される。他院を含む情報なのに信頼性が上がるという逆説的なコンテンツ。</div></div>
    </div>
  </div>

  <!-- Day 21 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 21</div><div class="brief-title">術後1ヶ月・3ヶ月・6ヶ月、鼻はどう変わっていくか</div></div><span class="tag tag-real" style="align-self:center;">リアル情報</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「術後、鼻がどう変化していくか全部見せます」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">術直後（腫れ）→ 1ヶ月後（まだ固い）→ 3ヶ月後（だいぶ落ち着く）→ 6ヶ月後（完成）を1人の患者で時系列で見せる。各フェーズにコメントテキストを添える。</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">「完成まで何ヶ月かかるか」という<strong>全員が気になる質問</strong>に答えるコンテンツ。保存率最高クラス。</div></div>
    </div>
  </div>
</div>

<!-- WEEK 4 DETAIL -->
<div class="page">
  <div class="week-banner"><div class="week-num">W4</div><div><div class="week-title">Week 4（Day 22〜30）：決断促進週</div><div class="week-sub">「行動したい」という気持ちを後押しするコンテンツで締める</div></div></div>

  <!-- Day 22 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 22</div><div class="brief-title">鼻整形を迷っている人に伝えたいこと</div></div><span class="tag tag-talk" style="align-self:center;">本音トーク</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「迷っている方に、一つだけ正直に言わせてください」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">「迷っている理由は大体この3つ（怖い・高い・バレる）」→ それぞれを正直に答える → 「カウンセリングだけでも来てください、無料です」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">潜在顧客への直接的な背中押しコンテンツ。<strong>「無料カウンセリング」への誘導</strong>と相性が良い。</div></div>
    </div>
  </div>

  <!-- Day 23 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 23</div><div class="brief-title">成人式の2ヶ月前に手術した話（垢抜け記録）</div></div><span class="tag tag-ba" style="align-self:center;">ビフォーアフター</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">テキスト：「成人式の2ヶ月前に手術した記録」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">45秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">手術2ヶ月前のBefore → 成人式当日のAfter写真 → 「間に合う？」という疑問に先生が短くコメント</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">季節・イベントに紐づけたコンテンツは拡散されやすい。<strong>「成人式前に間に合う？」という検索需要</strong>に直撃する。</div></div>
    </div>
  </div>

  <!-- Day 24 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 24</div><div class="brief-title">メンズの鼻整形、実はこんなに多い話</div></div><span class="tag tag-diag" style="align-self:center;">自己診断型</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「男性の鼻整形、思ってるより全然多いです」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">男性に多い鼻の悩みを紹介（鷲鼻・高すぎる鼻・横に広い等）→ 男性の術後BA写真 → 「男性も気軽にご相談ください」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box"><strong>男性層へのリーチ拡大</strong>。女性向けコンテンツが多い美容整形アカウントで差別化できる。男性フォロワーの獲得につながる。</div></div>
    </div>
  </div>

  <!-- Day 25 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 25</div><div class="brief-title">40代で初めて手術した話</div></div><span class="tag tag-story" style="align-self:center;">患者ストーリー</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">患者：「40代で初めて手術するって、おかしいですか？」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">なぜ今まで踏み切れなかったか → 40代で決意した理由 → 「年齢の壁」を感じていたことへの先生のコメント → 術後の変化と「もっと早くやればよかった」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box"><strong>30〜40代の潜在顧客層</strong>に直撃する。「自分も遅くないかも」という共感が生まれる。ターゲット層の拡大。</div></div>
    </div>
  </div>

  <!-- Day 26 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 26</div><div class="brief-title">傷跡が残らないクローズ法、縫合のこだわりを全部見せます</div></div><span class="tag tag-edu" style="align-self:center;">教育</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「傷跡が残らない理由、縫合を見れば全部わかります」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">縫合の丁寧さが傷跡を左右する説明 → 羽根先生が縫合に時間をかける理由（エピソード） → 実際の縫合後の写真（術直後と3ヶ月後比較）→ 「クローズ法を選ぶのはこの技術があるから」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">zetith_haneの<strong>最大の差別化ポイント「クローズ法×縫合技術」</strong>を深掘りする。他院との差を感じさせる専門性コンテンツ。</div></div>
    </div>
  </div>

  <!-- Day 27 -->
  <div class="brief-wrap">
    <div class="brief-head"><div><div class="brief-day">DAY 27</div><div class="brief-title">ゼティスを選んだ理由、患者さん3人に聞いた</div></div><span class="tag tag-real" style="align-self:center;">リアル情報</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「なぜゼティスを選んだか、患者さん3人に直接聞きました」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">60〜75秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">患者A「クローズ法でやってくれる先生が少なかった」→ 患者B「インスタで信頼できると思った」→ 患者C「カウンセリングが丁寧だった」→ 羽根先生の一言コメント</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">社会的証明の最強コンテンツ。<strong>「選ばれる理由」が明確になる</strong>ことで検討者の背中を押す。</div></div>
    </div>
  </div>

  <div class="two" style="margin-top:4px;">
    <!-- Day 28 -->
    <div class="brief-wrap" style="margin-bottom:0;">
      <div class="brief-head"><div><div class="brief-day">DAY 28</div><div class="brief-title">鼻フル整形（肋軟骨）6ヶ月後の完成形</div></div><span class="tag tag-ba" style="align-self:center;">BA</span></div>
      <div class="brief-body">
        <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">テキスト：「6ヶ月後、これが完成形です」</div></div>
        <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">40秒</div></div>
        <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">Before全方向 → After全方向 → 施術一覧テキスト → 「6ヶ月かけて完成しました」</div></div>
      </div>
    </div>
    <!-- Day 29 -->
    <div class="brief-wrap" style="margin-bottom:0;">
      <div class="brief-head"><div><div class="brief-day">DAY 29</div><div class="brief-title">術後1年間に起こること、全部話します</div></div><span class="tag tag-edu" style="align-self:center;">教育</span></div>
      <div class="brief-body">
        <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「術後1年間で何が起きるか、全部正直に話します」</div></div>
        <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">75秒</div></div>
        <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">腫れが引くタイムライン → 固さが取れるタイミング → 完成の判断基準 → 「1年は経過を見ましょう」の理由</div></div>
      </div>
    </div>
  </div>

  <!-- Day 30 -->
  <div class="brief-wrap" style="margin-top:18px;">
    <div class="brief-head"><div><div class="brief-day">DAY 30</div><div class="brief-title">今月の振り返り＋来月予告（フォロワーへのメッセージ）</div></div><span class="tag tag-talk" style="align-self:center;">本音トーク</span></div>
    <div class="brief-body">
      <div class="brief-row"><div class="brief-label">フック</div><div class="hook-text">「今月30本投稿しました。見てくれてありがとうございました」</div></div>
      <div class="brief-row"><div class="brief-label">尺</div><div class="brief-val">45〜60秒</div></div>
      <div class="brief-row"><div class="brief-label">構成</div><div class="brief-val">今月の投稿振り返り（どんなテーマをやったか）→ フォロワーへの感謝 → 来月やること予告（「来月は〇〇の特集をやります」）→「フォローしてくれると嬉しいです」</div></div>
      <div class="brief-row"><div class="brief-label">バズポイント</div><div class="buzz-box">月末の人間的なコンテンツで<strong>フォロワーとの信頼関係を強化</strong>する。来月への期待感を作ることでフォロー継続率UP。</div></div>
    </div>
  </div>
</div>

</body>
</html>
"""

from weasyprint import HTML
output = "/home/user/CellTagWorkflow/sns/30日間バズ設計_毎日リール.pdf"
HTML(string=html).write_pdf(output)
print(f"完了: {output}")
