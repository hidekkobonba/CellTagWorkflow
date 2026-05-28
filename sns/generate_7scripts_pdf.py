from weasyprint import HTML

html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Hiragino Sans','Yu Gothic',sans-serif; font-size:11.5px; color:#1a1a1a; line-height:1.7; }

/* COVER */
.cover { height:100vh; background:linear-gradient(155deg,#0d0d0d,#1e1e1e 60%,#2c2c2c); display:flex; flex-direction:column; justify-content:center; padding:80px; page-break-after:always; position:relative; }
.eyebrow { color:#c8a96e; font-size:10px; font-weight:700; letter-spacing:4px; margin-bottom:24px; }
.c-title { font-size:48px; font-weight:900; color:#fff; line-height:1.1; margin-bottom:18px; }
.c-title em { color:#c8a96e; font-style:normal; }
.c-sub { font-size:14px; color:#888; margin-bottom:44px; letter-spacing:1px; }
.c-line { width:52px; height:2px; background:#c8a96e; margin-bottom:32px; }
.c-desc { font-size:13px; color:#bbb; line-height:2.3; }
.c-meta { position:absolute; bottom:60px; right:72px; text-align:right; color:#444; font-size:10px; letter-spacing:2px; line-height:2; }

/* LIST PAGE */
.list-page { padding:52px 60px; page-break-after:always; }
.sh { display:flex; align-items:center; gap:12px; margin-bottom:26px; padding-bottom:13px; border-bottom:2.5px solid #1a1a1a; }
.sh-n { background:#1a1a1a; color:#c8a96e; font-size:10px; font-weight:900; letter-spacing:2px; padding:5px 11px; }
.sh-t { font-size:20px; font-weight:900; }
.sh-s { font-size:11px; color:#888; margin-top:3px; }

.list-grid { display:grid; grid-template-columns:1fr 1fr; gap:14px; }
.lc { border:1.5px solid #e5e5e5; border-top:3px solid #c8a96e; padding:16px; }
.lc-n { font-size:10px; font-weight:900; letter-spacing:2px; color:#c8a96e; margin-bottom:6px; }
.lc-title { font-size:13px; font-weight:900; margin-bottom:6px; line-height:1.4; }
.lc-type { display:inline-block; font-size:9px; font-weight:700; padding:2px 8px; margin-bottom:8px; }
.lc-why { font-size:10px; color:#555; line-height:1.7; }
.t-diag { background:#f3e5f5; color:#6a1b9a; }
.t-edu { background:#e8f5e9; color:#1b5e20; }
.t-talk { background:#fff8e1; color:#e65100; }
.t-real { background:#e0f2f1; color:#00695c; }

/* VIDEO PAGE */
.vpage { padding:0; page-break-after:always; }
.vpage:last-child { page-break-after:auto; }

.v-hero { background:#1a1a1a; padding:28px 48px 24px; }
.v-meta { display:flex; align-items:center; gap:14px; margin-bottom:10px; }
.v-num { font-size:11px; font-weight:900; letter-spacing:2px; color:#c8a96e; }
.v-tag { font-size:9px; font-weight:700; padding:3px 10px; border:1px solid #c8a96e; color:#c8a96e; }
.v-title { font-size:22px; font-weight:900; color:#fff; line-height:1.3; }
.v-hook { background:#c8a96e; color:#1a1a1a; font-size:13px; font-weight:700; padding:12px 48px; line-height:1.5; }
.v-hook::before { content:'▶ HOOK: '; font-size:10px; letter-spacing:1px; opacity:0.7; }

.v-body { padding:24px 48px; }
.v-cols { display:grid; grid-template-columns:220px 1fr; gap:24px; }

.v-left { display:flex; flex-direction:column; gap:14px; }
.info-box { border:1.5px solid #e5e5e5; }
.info-hd { background:#1a1a1a; color:#c8a96e; font-size:9px; font-weight:900; letter-spacing:2px; padding:6px 12px; }
.info-bd { padding:10px 12px; }
.info-row { margin-bottom:6px; font-size:10.5px; color:#333; }
.info-row:last-child { margin-bottom:0; }
.info-label { font-size:9px; font-weight:900; color:#888; display:block; letter-spacing:1px; margin-bottom:2px; }

.shoot-list { list-style:none; }
.shoot-list li { display:flex; gap:8px; align-items:flex-start; margin-bottom:7px; font-size:10.5px; color:#333; }
.s-dot { flex-shrink:0; width:5px; height:5px; background:#c8a96e; border-radius:50%; margin-top:5px; }

.edit-list { list-style:none; counter-reset:ec; }
.edit-list li { display:flex; gap:8px; margin-bottom:7px; align-items:flex-start; font-size:10.5px; color:#333; counter-increment:ec; }
.e-n { flex-shrink:0; width:17px; height:17px; background:#1a1a1a; color:#fff; font-size:9px; font-weight:900; display:flex; align-items:center; justify-content:center; }

/* SCRIPT BOX */
.script-wrap { }
.script-hd { background:#1a1a1a; color:#fff; padding:10px 16px; font-size:10px; font-weight:900; letter-spacing:2px; display:flex; justify-content:space-between; align-items:center; }
.script-sec { font-size:10px; color:#c8a96e; }
.script-box { background:#fafafa; border:1.5px solid #e5e5e5; border-top:none; padding:18px 20px; }
.script-text { font-size:12px; color:#1a1a1a; line-height:2.1; white-space:pre-wrap; font-family:'Hiragino Sans','Yu Gothic',sans-serif; }
.script-pause { display:inline-block; background:#f0f0f0; border-radius:2px; font-size:9px; color:#888; padding:1px 6px; margin:0 4px; vertical-align:middle; }

.buzz { background:#fffde7; border-left:3px solid #f9a825; padding:10px 14px; margin-top:14px; font-size:10.5px; color:#444; line-height:1.8; }
.buzz strong { color:#e65100; }
.buzz::before { content:'⚡ バズポイント：'; font-weight:900; color:#e65100; }

.caption-hd { background:#1a1a1a; color:#fff; padding:8px 12px; font-size:9px; font-weight:900; letter-spacing:2px; margin-top:14px; }
.caption-body { background:#f5f5f5; border:1.5px solid #e5e5e5; border-top:none; padding:12px 14px; font-size:10px; color:#444; line-height:1.9; font-family:monospace; }
</style>
</head>
<body>

<!-- COVER -->
<div class="cover">
  <div class="eyebrow">zetith_hane / Script Guide</div>
  <div class="c-title">7本の<br><em>完全</em>スクリプト</div>
  <div class="c-sub">羽根先生トーク単独で撮れる・バズ設計版</div>
  <div class="c-line"></div>
  <div class="c-desc">
    セリフ・撮影指示・編集手順・<br>
    キャプションまで全部入り。<br><br>
    このPDFを見ながら撮影すれば<br>
    そのまま投稿できます。
  </div>
  <div class="c-meta">Zetith Beauty Clinic<br>zetith_hane<br>羽根先生トーク7本</div>
</div>

<!-- LIST PAGE -->
<div class="list-page">
  <div class="sh"><div class="sh-n">INDEX</div><div><div class="sh-t">7本の一覧</div><div class="sh-s">すべて羽根先生1人で撮影できます</div></div></div>
  <div class="list-grid">
    <div class="lc"><div class="lc-n">VIDEO 01</div><span class="lc-type t-diag">自己診断型</span><div class="lc-title">この鼻の形、肋軟骨じゃないと一生変わりません</div><div class="lc-why">「自分の鼻はどのタイプ？」と思わせて保存・DM問い合わせを誘発する</div></div>
    <div class="lc"><div class="lc-n">VIDEO 02</div><span class="lc-type t-edu">比較教育型</span><div class="lc-title">クローズ法 vs オープン法、本当はどっちがいいか全部話します</div><div class="lc-why">最も検索される比較テーマ。保存率が高く術式選びの判断材料になる</div></div>
    <div class="lc"><div class="lc-n">VIDEO 03</div><span class="lc-type t-talk">不安解消型</span><div class="lc-title">鼻整形で後悔した人の共通点3つ</div><div class="lc-why">「失敗」「後悔」ワードで検討者が全員止まる。コメントが集まる</div></div>
    <div class="lc"><div class="lc-n">VIDEO 04</div><span class="lc-type t-talk">逆張り信頼型</span><div class="lc-title">正直に言います。この悩みなら手術しなくていいかもしれません</div><div class="lc-why">医師が「手術不要」と言う逆張りで信頼感が爆上がり。フォロー率No.1パターン</div></div>
    <div class="lc"><div class="lc-n">VIDEO 05</div><span class="lc-type t-talk">権威×謙虚型</span><div class="lc-title">2,000件やってわかった、一番大事なのは技術じゃなかった</div><div class="lc-why">実績×人間性の組み合わせ。「この先生に頼みたい」DM問い合わせが最も来るパターン</div></div>
    <div class="lc"><div class="lc-n">VIDEO 06</div><span class="lc-type t-real">実用情報型</span><div class="lc-title">鼻整形、全部やったらいくらかかるか正直に計算します</div><div class="lc-why">価格は検索ボリューム最上位。実用情報として保存率・シェア率が高い</div></div>
    <div class="lc"><div class="lc-n">VIDEO 07</div><span class="lc-type t-edu">逆張り信頼型</span><div class="lc-title">どのクリニックに行くにしても、カウンセリングでこれを聞いてください</div><div class="lc-why">「他院でも使える情報」を出すことで圧倒的な信頼性を構築する</div></div>
  </div>

  <div style="margin-top:20px; background:#f9f6f1; border-left:3px solid #c8a96e; padding:14px 18px;">
    <div style="font-size:10px; font-weight:900; letter-spacing:2px; color:#c8a96e; margin-bottom:8px;">撮影の共通ルール</div>
    <div style="font-size:11px; color:#444; line-height:2;">
      ■ 場所：診察室 or クリニック内の白い壁の前（清潔感重視）<br>
      ■ 服装：白衣（VIDEO 05のみ私服でもOK）<br>
      ■ カメラ：スマホ縦置き・目線の高さに三脚で固定・顔が画面中央に来るように<br>
      ■ 尺：1本60〜90秒を目安に話す（台本を読まず、セリフを理解した上で自分の言葉で話す）<br>
      ■ NG：原稿を読む目線・暗い場所・背景に物が多い場所
    </div>
  </div>
</div>

<!-- ======================================================= -->
<!-- VIDEO 01 -->
<!-- ======================================================= -->
<div class="vpage">
  <div class="v-hero">
    <div class="v-meta"><div class="v-num">VIDEO 01</div><div class="v-tag">自己診断型</div><div class="v-tag">尺：60秒</div></div>
    <div class="v-title">この鼻の形、肋軟骨じゃないと一生変わりません</div>
  </div>
  <div class="v-hook">「実は、この3タイプの鼻、プロテーゼだけでは絶対に変わりません」</div>
  <div class="v-body">
    <div class="v-cols">
      <div class="v-left">
        <div class="info-box">
          <div class="info-hd">撮影指示</div>
          <div class="info-bd">
            <div class="info-row"><span class="info-label">出演</span>羽根先生（白衣）</div>
            <div class="info-row"><span class="info-label">場所</span>診察室</div>
            <div class="info-row"><span class="info-label">目安尺</span>60秒</div>
            <div class="info-row"><span class="info-label">ポイント</span>タイプを言うたびに指を1本・2本・3本と立てると映像的にわかりやすい</div>
          </div>
        </div>
        <div class="info-box">
          <div class="info-hd">編集指示</div>
          <div class="info-bd">
            <ul class="edit-list">
              <li><div class="e-n">1</div>AI自動字幕を入れる</li>
              <li><div class="e-n">2</div>「タイプ①」「タイプ②」「タイプ③」のテキストを先生が話すタイミングで画面に大きく表示</li>
              <li><div class="e-n">3</div>各タイプの説明中に矢印テキスト（例：「軟骨が問題→肋軟骨が必要」）をオーバーレイ</li>
              <li><div class="e-n">4</div>BGMなし</li>
              <li><div class="e-n">5</div>左上に「e」ロゴ（半透明）</li>
            </ul>
          </div>
        </div>
        <div class="buzz">「自分はどれ？」と思わせる<strong>自己診断設計</strong>で保存率が高い。DM「自分のタイプが知りたい」問い合わせが来やすい。</div>
      </div>
      <div class="script-wrap">
        <div class="script-hd">完全セリフ<div class="script-sec">（このまま話してください）</div></div>
        <div class="script-box"><div class="script-text">実は、この3タイプの鼻、プロテーゼだけでは絶対に変わりません。

まず1つ目。<span class="script-pause">（指1本）</span>鼻先が丸い、団子鼻タイプ。
プロテーゼを入れると鼻筋は通るんですけど、鼻先の丸さは変わらないんですよ。鼻先の形を作っているのは「鼻翼軟骨」という軟骨で、プロテーゼでは触れられない部分なんです。だからこのタイプは、肋軟骨を移植して鼻先を作り直す必要があります。

2つ目。<span class="script-pause">（指2本）</span>鼻筋は通っているのに、鼻先だけが低いタイプ。上から見るとペタンとしている感じですね。これも同じで、鼻先に高さを出すには肋軟骨で土台を作るしかないんです。

3つ目。<span class="script-pause">（指3本）</span>小鼻が横に広がっていて、全体がボテッとしているタイプ。これは鼻先の形と小鼻の形、両方変える必要があるので、プロテーゼ単体では解決できません。

自分がどのタイプか気になる方、DMで気軽に相談してください。無料でお答えします。</div></div>
        <div class="caption-hd">キャプション</div>
        <div class="caption-body">プロテーゼだけでは変わらない鼻の形があります。

▷ タイプ①：鼻先が丸い（団子鼻）
▷ タイプ②：鼻先だけが低い
▷ タイプ③：小鼻が横に広がっている

自分のタイプが気になる方はDMください。

━━━━━━━━━━━━
🏥 ゼティスビューティークリニック 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM or LINE でご相談ください
━━━━━━━━━━━━
#鼻整形 #肋軟骨 #団子鼻 #鼻フル整形 #福岡美容外科
#鼻整形福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- ======================================================= -->
<!-- VIDEO 02 -->
<!-- ======================================================= -->
<div class="vpage">
  <div class="v-hero">
    <div class="v-meta"><div class="v-num">VIDEO 02</div><div class="v-tag">比較教育型</div><div class="v-tag">尺：90秒</div></div>
    <div class="v-title">クローズ法 vs オープン法、本当はどっちがいいか全部話します</div>
  </div>
  <div class="v-hook">「クローズとオープン、どっちがいいか聞かれすぎるので全部正直に話します」</div>
  <div class="v-body">
    <div class="v-cols">
      <div class="v-left">
        <div class="info-box">
          <div class="info-hd">撮影指示</div>
          <div class="info-bd">
            <div class="info-row"><span class="info-label">出演</span>羽根先生（白衣）</div>
            <div class="info-row"><span class="info-label">場所</span>診察室</div>
            <div class="info-row"><span class="info-label">目安尺</span>90秒</div>
            <div class="info-row"><span class="info-label">ポイント</span>「俺がクローズ法にこだわる理由」のくだりは感情込めて話す。ここが一番大事</div>
          </div>
        </div>
        <div class="info-box">
          <div class="info-hd">編集指示</div>
          <div class="info-bd">
            <ul class="edit-list">
              <li><div class="e-n">1</div>AI自動字幕</li>
              <li><div class="e-n">2</div>「クローズ法」「オープン法」をテキストで画面に交互に大きく出す</li>
              <li><div class="e-n">3</div>メリデメをテキストで箇条書き表示（話に合わせて）</li>
              <li><div class="e-n">4</div>BGMなし</li>
            </ul>
          </div>
        </div>
        <div class="buzz">比較系は<strong>保存率が最も高い</strong>カテゴリ。クリニック選びをしている人全員が保存する。コメントで「うちはオープン法と言われたのですが…」と相談が来やすい。</div>
      </div>
      <div class="script-wrap">
        <div class="script-hd">完全セリフ<div class="script-sec">（このまま話してください）</div></div>
        <div class="script-box"><div class="script-text">クローズとオープン、どっちがいいか聞かれすぎるので、全部正直に話します。

まずクローズ法。鼻の内側だけを切開する方法なので、外側に傷跡が残りません。ダウンタイムも比較的短い。ただ、視野が狭い分、医師の技術がすごく問われます。

オープン法は鼻柱、鼻の下の細い柱の部分を切開する方法です。視野が広く取れるので複雑な手術がしやすい。でも外側に小さな傷跡が残ります。

じゃあどっちが優れているかというと、正直どちらが上ということはないんです。医師の得意な術式と、その患者さんの鼻の状態によって変わります。

俺がクローズ法にこだわっている理由を話します。一番の理由は、傷跡を残したくないからです。鼻の手術って繊細で、外側に傷跡が残ると患者さんの術後のストレスになることがある。だから俺はできる限り傷跡を残さない方法を選んでいます。

ただ正直に言うと、クローズ法は視野が狭い分、技術力が問われます。経験と精度がないと仕上がりが落ちる。俺は2,000件以上クローズ法でやってきているので自信を持ってやっていますが、クリニックを選ぶときは「どの術式が得意か」を必ず確認してください。

術式のことで気になることがあればカウンセリングで何でも聞いてください。</div></div>
        <div class="caption-hd">キャプション</div>
        <div class="caption-body">クローズ法とオープン法、結局どっちがいいの？

正直に全部話しました。

どちらが優れているということはなく、医師の得意な術式×あなたの鼻の状態で決まります。

━━━━━━━━━━━━
🏥 ゼティスビューティークリニック 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM or LINE でご相談ください
━━━━━━━━━━━━
#クローズ法 #オープン法 #鼻整形 #鼻整形福岡
#美容外科 #ゼティス #羽根和秀 #福岡美容外科</div>
      </div>
    </div>
  </div>
</div>

<!-- ======================================================= -->
<!-- VIDEO 03 -->
<!-- ======================================================= -->
<div class="vpage">
  <div class="v-hero">
    <div class="v-meta"><div class="v-num">VIDEO 03</div><div class="v-tag">不安解消型</div><div class="v-tag">尺：75秒</div></div>
    <div class="v-title">鼻整形で後悔した人の共通点3つ</div>
  </div>
  <div class="v-hook">「鼻整形で失敗した人、ほぼ全員これをやってます」</div>
  <div class="v-body">
    <div class="v-cols">
      <div class="v-left">
        <div class="info-box">
          <div class="info-hd">撮影指示</div>
          <div class="info-bd">
            <div class="info-row"><span class="info-label">出演</span>羽根先生（白衣 or 私服どちらでも可）</div>
            <div class="info-row"><span class="info-label">場所</span>診察室 or 白い壁前</div>
            <div class="info-row"><span class="info-label">目安尺</span>75秒</div>
            <div class="info-row"><span class="info-label">ポイント</span>「修正相談に来る患者さんを何百人も診てきた」という実績を冒頭に入れる。数字が信頼になる</div>
          </div>
        </div>
        <div class="info-box">
          <div class="info-hd">編集指示</div>
          <div class="info-bd">
            <ul class="edit-list">
              <li><div class="e-n">1</div>AI自動字幕</li>
              <li><div class="e-n">2</div>「共通点①②③」をテキストで大きく画面に出す</li>
              <li><div class="e-n">3</div>各共通点の横に一言要約テキストを添える（例：「価格だけで選ぶ」）</li>
              <li><div class="e-n">4</div>BGMなし</li>
            </ul>
          </div>
        </div>
        <div class="buzz">「失敗」「後悔」は検索ボリュームが高いワード。<strong>検討中の人が全員止まる</strong>。リスト型なので保存率も高く、「④も追加して」とコメントが集まる。</div>
      </div>
      <div class="script-wrap">
        <div class="script-hd">完全セリフ<div class="script-sec">（このまま話してください）</div></div>
        <div class="script-box"><div class="script-text">鼻整形で失敗した人、ほぼ全員これをやってます。修正相談に来る患者さんを何百人も診てきて気づいたことを話します。

共通点の1つ目。<span class="script-pause">（指1本）</span>価格だけで選んでいる。
安いクリニックで手術して後から修正相談に来る方、本当に多いんですよ。安さには理由があって、経験の浅い医師だったり、使う素材のコストを削っていたりする。最初から適正価格のクリニックに行っていれば修正費用を払わずに済んだ、というケースを何百件も見てきました。

2つ目。<span class="script-pause">（指2本）</span>術式を理解しないまま手術している。
「先生にお任せ」でやった結果、「こんな仕上がりだとは思わなかった」という方がすごく多い。術前に「どんな変化が起きるか」「どこまで変えられるか」を必ず確認してください。

3つ目。<span class="script-pause">（指3本）</span>他院の症例写真と自分を比べてしまう。
インスタに上がってる症例って、一番うまくいったケースが出ているんですよ。骨格も違う、元の鼻の状態も違う。それと自分を比較して「なんで違うんだ」ってなる。比較するなら同じ骨格・同じ術式の症例でないと意味がないです。

カウンセリングでこの辺りは全部お話ししているので、まず来てみてください。</div></div>
        <div class="caption-hd">キャプション</div>
        <div class="caption-body">修正相談に来る患者さんに共通していること、話します。

① 価格だけで選んでいた
② 術式を理解しないまま手術した
③ 他院の症例写真と比較しすぎた

カウンセリングでこの辺りも全部お話しします。

━━━━━━━━━━━━
🏥 ゼティスビューティークリニック 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM or LINE でご相談ください
━━━━━━━━━━━━
#鼻整形 #鼻整形失敗 #他院修正 #美容整形後悔
#福岡美容外科 #鼻整形福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- ======================================================= -->
<!-- VIDEO 04 -->
<!-- ======================================================= -->
<div class="vpage">
  <div class="v-hero">
    <div class="v-meta"><div class="v-num">VIDEO 04</div><div class="v-tag">逆張り信頼型</div><div class="v-tag">尺：75秒</div></div>
    <div class="v-title">正直に言います。この悩みなら手術しなくていいかもしれません</div>
  </div>
  <div class="v-hook">「正直に言います。この鼻の悩み、手術しなくていいかもしれません」</div>
  <div class="v-body">
    <div class="v-cols">
      <div class="v-left">
        <div class="info-box">
          <div class="info-hd">撮影指示</div>
          <div class="info-bd">
            <div class="info-row"><span class="info-label">出演</span>羽根先生（白衣）</div>
            <div class="info-row"><span class="info-label">場所</span>診察室</div>
            <div class="info-row"><span class="info-label">目安尺</span>75秒</div>
            <div class="info-row"><span class="info-label">ポイント</span>「美容外科医がこれを言うのは珍しいと思うけど」という前置きを入れるとさらに効果的</div>
          </div>
        </div>
        <div class="info-box">
          <div class="info-hd">編集指示</div>
          <div class="info-bd">
            <ul class="edit-list">
              <li><div class="e-n">1</div>AI自動字幕</div></li>
              <li><div class="e-n">2</div>「手術不要かもしれないケース」をテキストで画面に出す</li>
              <li><div class="e-n">3</div>冒頭テキストオーバーレイ：「正直に言います」を大きく</li>
              <li><div class="e-n">4</div>BGMなし</li>
            </ul>
          </div>
        </div>
        <div class="buzz">美容外科医が「<strong>手術しなくていい</strong>」と言う逆張りで信頼感が爆上がりする。「この先生は本音を言ってくれる」とフォローされる最強パターン。DM問い合わせ数が最も増える動画タイプ。</div>
      </div>
      <div class="script-wrap">
        <div class="script-hd">完全セリフ<div class="script-sec">（このまま話してください）</div></div>
        <div class="script-box"><div class="script-text">正直に言います。この鼻の悩み、手術しなくていいかもしれません。

美容外科医がこれを言うのって珍しいと思うんですけど、本当のことを言います。

例えば、鼻が低いことで悩んでいる方。軽度であればヒアルロン酸注入だけで十分な場合があります。ダウンタイムもほぼなくて、30分で終わる。永続的ではないですが、まず試してみるという選択肢もあります。

鼻先が少し気になる程度の方も、軽度のケースならプロテーゼなしで鼻尖形成だけで十分なことがある。いきなり大きな手術をしなくていいんです。

俺が大事にしているのは、患者さんに合った最小限の施術を提案すること。大きな手術をたくさんやった方がお金になるのはわかってるんですけど、それよりも患者さんが後悔しない選択をしてほしい。

カウンセリングに来てもらえれば、手術が本当に必要かどうか正直に話します。場合によっては「手術しなくていいですよ」って言うこともあります。まず相談だけでも来てみてください。</div></div>
        <div class="caption-hd">キャプション</div>
        <div class="caption-body">鼻整形を考えている方へ、正直に話します。

手術しなくていいかもしれないケースがあります。
カウンセリングで正直に判断します。

「手術しなくていいですよ」と言うこともあります。

━━━━━━━━━━━━
🏥 ゼティスビューティークリニック 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM or LINE でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容整形 #美容外科 #鼻コンプレックス
#福岡美容外科 #鼻整形相談 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- ======================================================= -->
<!-- VIDEO 05 -->
<!-- ======================================================= -->
<div class="vpage">
  <div class="v-hero">
    <div class="v-meta"><div class="v-num">VIDEO 05</div><div class="v-tag">権威×謙虚型</div><div class="v-tag">尺：75秒</div></div>
    <div class="v-title">2,000件やってわかった、一番大事なのは技術じゃなかった</div>
  </div>
  <div class="v-hook">「2,000件手術してきて、一番大事なのは技術じゃないと気づきました」</div>
  <div class="v-body">
    <div class="v-cols">
      <div class="v-left">
        <div class="info-box">
          <div class="info-hd">撮影指示</div>
          <div class="info-bd">
            <div class="info-row"><span class="info-label">出演</span>羽根先生（白衣 or 私服どちらでもOK）</div>
            <div class="info-row"><span class="info-label">場所</span>診察室 or 落ち着いた場所</div>
            <div class="info-row"><span class="info-label">目安尺</span>75秒</div>
            <div class="info-row"><span class="info-label">ポイント</span>患者に「術後すごく喜んでくれてたのに、その一言が刺さって」の部分は特に感情を込めて。ここが全体のピーク</div>
          </div>
        </div>
        <div class="info-box">
          <div class="info-hd">編集指示</div>
          <div class="info-bd">
            <ul class="edit-list">
              <li><div class="e-n">1</div>AI自動字幕</li>
              <li><div class="e-n">2</div>「2,000件」の数字を冒頭テキストで強調</li>
              <li><div class="e-n">3</div>患者の言葉「最初のカウンセリングで不安で泣きそうだった」をテキストで引用表示</li>
              <li><div class="e-n">4</div>BGMなし（or 静かなBGMを小さく）</li>
            </ul>
          </div>
        </div>
        <div class="buzz">権威性（2,000件）と人間性を同時に見せる最強パターン。「<strong>この先生に頼みたい</strong>」とフォロー&DM問い合わせが最も多く来る動画タイプ。エピソードがあるほど刺さる。</div>
      </div>
      <div class="script-wrap">
        <div class="script-hd">完全セリフ<div class="script-sec">（このまま話してください）</div></div>
        <div class="script-box"><div class="script-text">2,000件手術してきて、一番大事なのは技術じゃないと気づきました。

最初はとにかく技術を磨くことだけを考えていました。より精度の高い手術、より自然な仕上がり。それだけを追いかけてやってきた。

でもある時、患者さんから言われたんですよ。「先生、ありがとうございました。でも正直、最初のカウンセリングで不安で泣きそうだったんです」って。術後はすごく喜んでくれてたんですけど、その一言が刺さって。

技術があっても、患者さんが不安なまま手術台に上がっていたら、それはまだ足りていない。俺は何かを見落としていたんだって。

それからカウンセリングの時間を今まで以上にかけるようにしました。不安なことは全部聞いてもらう。「こんなこと聞いていいのかな」って遠慮してること、全部聞いてほしい。どんな些細なことでも答えます。

2,000件やって気づいたのは、手術の質は技術だけじゃなくて、術前の対話で決まるということです。

カウンセリング、怖くないので気軽に来てください。</div></div>
        <div class="caption-hd">キャプション</div>
        <div class="caption-body">2,000件やってきて、気づいたことがあります。

一番大事なのは技術じゃなかった。

術前の「対話」が、手術の質を決めると思っています。
不安なことは全部聞いてください。

━━━━━━━━━━━━
🏥 ゼティスビューティークリニック 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM or LINE でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科 #美容外科医 #カウンセリング
#鼻整形福岡 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- ======================================================= -->
<!-- VIDEO 06 -->
<!-- ======================================================= -->
<div class="vpage">
  <div class="v-hero">
    <div class="v-meta"><div class="v-num">VIDEO 06</div><div class="v-tag">実用情報型</div><div class="v-tag">尺：90秒</div></div>
    <div class="v-title">鼻整形、全部やったらいくらかかるか正直に計算します</div>
  </div>
  <div class="v-hook">「鼻全部やったら結局いくらかかるか、正直に計算します」</div>
  <div class="v-body">
    <div class="v-cols">
      <div class="v-left">
        <div class="info-box">
          <div class="info-hd">撮影指示</div>
          <div class="info-bd">
            <div class="info-row"><span class="info-label">出演</span>羽根先生（白衣）</div>
            <div class="info-row"><span class="info-label">場所</span>診察室</div>
            <div class="info-row"><span class="info-label">目安尺</span>90秒</div>
            <div class="info-row"><span class="info-label">ポイント</span>金額は「うちの価格」ではなく「業界相場」として話す。最後に「うちの詳細はHPかDMで」と誘導</div>
          </div>
        </div>
        <div class="info-box">
          <div class="info-hd">編集指示</div>
          <div class="info-bd">
            <ul class="edit-list">
              <li><div class="e-n">1</div>AI自動字幕</li>
              <li><div class="e-n">2</div>各術式名と価格帯をテキストで画面に表示（先生が話すタイミングで出す）</li>
              <li><div class="e-n">3</div>「合計：〇〇万円〜」のまとめテキストを最後に表示</li>
              <li><div class="e-n">4</div>BGMなし</li>
            </ul>
          </div>
        </div>
        <div class="buzz">価格情報は<strong>検索ボリューム最上位</strong>。「実用情報として保存する」「友達に共有する」が起きやすいコンテンツ。「別料金が隠れてる問題」に触れることで信頼性が上がる。</div>
      </div>
      <div class="script-wrap">
        <div class="script-hd">完全セリフ<div class="script-sec">（このまま話してください）</div></div>
        <div class="script-box"><div class="script-text">鼻全部やったら結局いくらかかるか、正直に計算します。

まず一番よく聞かれる「鼻フル整形」。これは鼻尖形成、軟骨移植（肋軟骨）、プロテーゼ、必要に応じて小鼻縮小まで全部やるパターンですね。相場でいうと、だいたい30万〜55万円くらい。クリニックによってかなり差があります。

単体でいくと、鼻尖形成だけなら10〜20万、プロテーゼ単体で10〜20万、小鼻縮小で10〜20万、人中短縮で15〜25万くらいが業界相場です。

ここで知っておいてほしいのが2つ。

1つ目。複数の手術をまとめてやると、麻酔代やオペ費用が1回で済むのでトータルのコストが抑えられます。あとダウンタイムも1回で済む。分けてやると2回休みが必要になるんですよ。

2つ目。安いクリニックに注意してほしいのが「施術費用は安いけど、消耗品・麻酔・検査が全部別料金」というパターンがある。最終的な合計金額を必ず確認してください。見積もりを出してくれないクリニックは選ばない方がいいです。

うちの詳細な価格はHPに全部出してますし、カウンセリングで見積もりも出します。まず確認してみてください。</div></div>
        <div class="caption-hd">キャプション</div>
        <div class="caption-body">鼻整形、全部やったらいくらかかるか正直に話しました。

鼻フル整形の相場：30〜55万円
（鼻尖形成＋肋軟骨＋プロテーゼ＋小鼻縮小）

まとめてやる方がお得で、ダウンタイムも1回で済みます。

━━━━━━━━━━━━
🏥 ゼティスビューティークリニック 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM or LINE でご相談ください
━━━━━━━━━━━━
#鼻整形費用 #鼻整形価格 #鼻フル整形 #美容整形費用
#福岡美容外科 #鼻整形福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- ======================================================= -->
<!-- VIDEO 07 -->
<!-- ======================================================= -->
<div class="vpage">
  <div class="v-hero">
    <div class="v-meta"><div class="v-num">VIDEO 07</div><div class="v-tag">逆張り信頼型</div><div class="v-tag">尺：75秒</div></div>
    <div class="v-title">どのクリニックに行くにしても、カウンセリングでこれを聞いてください</div>
  </div>
  <div class="v-hook">「どのクリニックに行くにしても、これだけは必ず聞いてください」</div>
  <div class="v-body">
    <div class="v-cols">
      <div class="v-left">
        <div class="info-box">
          <div class="info-hd">撮影指示</div>
          <div class="info-bd">
            <div class="info-row"><span class="info-label">出演</span>羽根先生（白衣）</div>
            <div class="info-row"><span class="info-label">場所</span>診察室</div>
            <div class="info-row"><span class="info-label">目安尺</span>75秒</div>
            <div class="info-row"><span class="info-label">ポイント</span>「うちに来なくていい、どこに行っても聞いてほしい」という姿勢で話すと信頼感が最大化する</div>
          </div>
        </div>
        <div class="info-box">
          <div class="info-hd">編集指示</div>
          <div class="info-bd">
            <ul class="edit-list">
              <li><div class="e-n">1</div>AI自動字幕</li>
              <li><div class="e-n">2</div>「質問①②③」をテキストで画面に大きく出す</li>
              <li><div class="e-n">3</div>各質問は先生が言う前にテキストを表示するとテンポよく見える</li>
              <li><div class="e-n">4</div>BGMなし</li>
            </ul>
          </div>
        </div>
        <div class="buzz">「他院でも使える情報」を出すことで<strong>圧倒的な信頼性</strong>を構築する。「このアカウントをフォローしておけば損しない」と思わせる。保存率・フォロー率ともに高い。</div>
      </div>
      <div class="script-wrap">
        <div class="script-hd">完全セリフ<div class="script-sec">（このまま話してください）</div></div>
        <div class="script-box"><div class="script-text">どのクリニックに行くにしても、これだけは必ず聞いてください。美容外科医として正直に話します。

質問の1つ目。「先生の鼻整形の症例数を教えてください」。
症例数は医師の経験と技術に直結します。「たくさんやってます」じゃなくて、具体的な数字を答えてくれる先生を選んでください。答えられない先生はちょっと考えた方がいい。

2つ目。「修正が必要になった場合、どう対応してもらえますか」。
これを聞くと、クリニックの本当の姿勢がわかります。「修正は別途費用です」なのか、「保証期間内は対応します」なのか。後悔してから聞いても遅いので、必ず事前に確認してください。

3つ目。「ダウンタイムのリアルな写真を見せてもらえますか」。
きれいな術後写真だけじゃなくて、術直後の腫れや内出血の写真も見せてくれるクリニックは信頼できます。隠さないということですから。

この3つ、聞きにくいかもしれないけど、体に関わることなので遠慮しないでください。

うちのカウンセリングでもこの3つ、全部正直に答えます。</div></div>
        <div class="caption-hd">キャプション</div>
        <div class="caption-body">どのクリニックに行くにしても、この3つを聞いてください。

① 先生の鼻整形の症例数は？
② 修正が必要になった場合の対応は？
③ ダウンタイムのリアルな写真を見せてもらえますか？

聞きにくくても、体のことなので遠慮しないで。

━━━━━━━━━━━━
🏥 ゼティスビューティークリニック 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM or LINE でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容整形 #クリニック選び #美容外科選び
#福岡美容外科 #鼻整形福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/7本完全スクリプト_zetith_hane.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
