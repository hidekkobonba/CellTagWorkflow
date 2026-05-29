from weasyprint import HTML

html = """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Hiragino Sans','Yu Gothic',sans-serif; font-size:11px; color:#1a1a1a; line-height:1.7; }

.cover { height:100vh; background:#0d0d0d; display:flex; flex-direction:column; justify-content:center; padding:80px; page-break-after:always; position:relative; }
.eyebrow { color:#c8a96e; font-size:9px; font-weight:700; letter-spacing:5px; margin-bottom:32px; }
.c-title { font-size:52px; font-weight:900; color:#fff; line-height:1.05; margin-bottom:24px; letter-spacing:-1px; }
.c-title em { color:#c8a96e; font-style:normal; display:block; }
.c-line { width:40px; height:1px; background:#c8a96e; margin:28px 0; }
.c-desc { font-size:12px; color:#666; line-height:2.4; }
.c-char { position:absolute; right:80px; top:50%; transform:translateY(-50%); text-align:right; }
.c-char-label { font-size:9px; letter-spacing:3px; color:#333; margin-bottom:12px; }
.c-char-name { font-size:28px; font-weight:900; color:#fff; letter-spacing:2px; }
.c-char-sub { font-size:10px; color:#c8a96e; letter-spacing:2px; margin-top:6px; }
.c-meta { position:absolute; bottom:56px; right:80px; color:#333; font-size:9px; letter-spacing:2px; line-height:2; text-align:right; }

.char-page { padding:60px; page-break-after:always; background:#fff; }
.char-def { display:grid; grid-template-columns:1fr 1fr; gap:0; border:1.5px solid #1a1a1a; margin-bottom:32px; }
.char-left { background:#1a1a1a; padding:40px; }
.char-right { padding:40px; }
.char-tagline { font-size:22px; font-weight:900; color:#c8a96e; line-height:1.4; margin-bottom:20px; }
.char-traits { list-style:none; }
.char-traits li { font-size:11px; color:#aaa; padding:8px 0; border-bottom:1px solid #2a2a2a; display:flex; gap:10px; }
.char-traits li::before { content:'—'; color:#c8a96e; flex-shrink:0; }
.char-right-title { font-size:11px; font-weight:900; letter-spacing:2px; color:#888; margin-bottom:16px; }
.tone-row { margin-bottom:16px; }
.tone-label { font-size:9px; font-weight:900; letter-spacing:2px; color:#c8a96e; margin-bottom:6px; }
.tone-bad { background:#fafafa; border-left:2px solid #ddd; padding:8px 12px; font-size:11px; color:#999; margin-bottom:4px; text-decoration:line-through; }
.tone-good { background:#fafafa; border-left:2px solid #1a1a1a; padding:8px 12px; font-size:11px; color:#1a1a1a; font-weight:700; }

.sh { display:flex; align-items:center; gap:12px; margin-bottom:24px; padding-bottom:12px; border-bottom:2px solid #1a1a1a; }
.sh-n { background:#1a1a1a; color:#c8a96e; font-size:9px; font-weight:900; letter-spacing:2px; padding:5px 11px; }
.sh-t { font-size:18px; font-weight:900; }
.sh-s { font-size:10px; color:#888; margin-top:2px; }

.edit-rule { display:grid; grid-template-columns:1fr 1fr; gap:16px; }
.rule-box { border:1.5px solid #e5e5e5; }
.rule-hd { background:#1a1a1a; color:#fff; padding:8px 14px; font-size:9px; font-weight:900; letter-spacing:2px; }
.rule-bd { padding:12px 14px; }
.rule-item { display:flex; gap:8px; margin-bottom:7px; font-size:10.5px; color:#333; align-items:flex-start; }
.rule-dot { flex-shrink:0; width:4px; height:4px; background:#c8a96e; border-radius:50%; margin-top:5px; }

.vpage { page-break-after:always; }
.vpage:last-child { page-break-after:auto; }

.v-top { background:#1a1a1a; padding:30px 52px 24px; }
.v-meta { display:flex; align-items:center; gap:12px; margin-bottom:10px; }
.v-num { font-size:10px; font-weight:900; letter-spacing:3px; color:#c8a96e; }
.v-dur { font-size:9px; color:#555; border:1px solid #333; padding:2px 8px; letter-spacing:1px; }
.v-title { font-size:24px; font-weight:900; color:#fff; line-height:1.2; letter-spacing:-0.3px; }
.v-hook-bar { background:#c8a96e; padding:11px 52px; font-size:12px; font-weight:700; color:#1a1a1a; }

.v-body { padding:24px 52px; display:grid; grid-template-columns:200px 1fr; gap:28px; }

.v-sidebar { display:flex; flex-direction:column; gap:14px; }
.sbox { border:1.5px solid #e5e5e5; }
.sbox-hd { background:#1a1a1a; color:#c8a96e; font-size:9px; font-weight:900; letter-spacing:2px; padding:6px 12px; }
.sbox-bd { padding:10px 12px; }
.sbox-row { margin-bottom:6px; font-size:10.5px; color:#333; }
.sbox-row:last-child { margin-bottom:0; }
.sbox-lbl { font-size:9px; font-weight:900; color:#999; letter-spacing:1px; display:block; margin-bottom:1px; }

.edit-steps { list-style:none; counter-reset:es; }
.edit-steps li { display:flex; gap:8px; margin-bottom:7px; counter-increment:es; align-items:flex-start; font-size:10.5px; color:#333; }
.es-n { flex-shrink:0; width:16px; height:16px; background:#1a1a1a; color:#fff; font-size:9px; font-weight:900; display:flex; align-items:center; justify-content:center; }

.buzz-box { background:#fff8e8; border-left:3px solid #c8a96e; padding:10px 12px; font-size:10.5px; color:#444; line-height:1.8; }
.buzz-box strong { color:#1a1a1a; font-weight:900; }

.script-area { }
.script-top { background:#1a1a1a; padding:10px 18px; display:flex; justify-content:space-between; align-items:center; }
.script-title-label { font-size:9px; font-weight:900; letter-spacing:2px; color:#c8a96e; }
.script-note { font-size:9px; color:#555; }
.script-box { border:1.5px solid #1a1a1a; border-top:none; padding:22px 20px; background:#fafafa; }
.script-text { font-size:12.5px; color:#1a1a1a; line-height:2.3; white-space:pre-wrap; font-family:'Hiragino Sans','Yu Gothic',sans-serif; }
.pause { display:inline-block; background:#1a1a1a; color:#c8a96e; font-size:8px; padding:1px 7px; margin:0 3px; vertical-align:middle; letter-spacing:1px; }
.visual { display:inline-block; background:#e8f5e9; color:#2e7d32; font-size:8px; padding:1px 7px; margin:0 3px; vertical-align:middle; letter-spacing:1px; border:1px solid #a5d6a7; }

.caption-area { margin-top:14px; }
.cap-hd { background:#1a1a1a; color:#fff; padding:7px 18px; font-size:9px; font-weight:900; letter-spacing:2px; }
.cap-bd { border:1.5px solid #1a1a1a; border-top:none; padding:12px 16px; font-size:10px; color:#444; line-height:1.9; font-family:monospace; background:#fff; }
</style>
</head>
<body>

<!-- COVER -->
<div class="cover">
  <div class="eyebrow">zetith_hane / Character Script</div>
  <div class="c-title">鼻の<em>鑑定士</em></div>
  <div class="c-line"></div>
  <div class="c-desc">
    言葉は少ない。でも核心を突く。<br>
    圧倒的な審美眼と技術で語る30本。
  </div>
  <div class="c-char">
    <div class="c-char-label">CHARACTER</div>
    <div class="c-char-name">羽根 和秀</div>
    <div class="c-char-sub">鼻の鑑定士</div>
  </div>
  <div class="c-meta">Zetith Beauty Clinic Fukuoka<br>zetith_hane</div>
</div>

<!-- CHARACTER PAGE -->
<div class="char-page">
  <div class="sh"><div class="sh-n">CHARACTER</div><div><div class="sh-t">「鼻の鑑定士」とは何か</div><div class="sh-s">このキャラクターを理解してから撮影する</div></div></div>

  <div class="char-def">
    <div class="char-left">
      <div class="char-tagline">黙って見ただけで<br>何が問題かわかる。</div>
      <ul class="char-traits">
        <li>言葉は少ないが、一言で核心を突く</li>
        <li>自分の判断に迷いがない</li>
        <li>感情的にならない、冷静で鋭い</li>
        <li>説明しすぎない。わかる人にわかればいい</li>
        <li>「やりすぎた美容」が嫌い</li>
        <li>断言する。「〜だと思います」は言わない</li>
      </ul>
    </div>
    <div class="char-right">
      <div class="char-right-title">話し方の違い</div>
      <div class="tone-row">
        <div class="tone-label">前の話し方（NG）</div>
        <div class="tone-bad">「プロテーゼを入れると鼻筋は通るんですけど、鼻先の丸さは変わらないんですよ」</div>
        <div class="tone-label" style="margin-top:8px;">鑑定士の話し方（OK）</div>
        <div class="tone-good">「プロテーゼで鼻筋は通る。鼻先は変わらない。」</div>
      </div>
      <div class="tone-row">
        <div class="tone-label">NG</div>
        <div class="tone-bad">「〜かもしれません」「〜と思います」「〜ですよね」</div>
        <div class="tone-label" style="margin-top:8px;">OK</div>
        <div class="tone-good">「〜です。」「〜だから。」「それだけです。」</div>
      </div>
    </div>
  </div>

  <div class="sh"><div class="sh-n">EDIT STYLE</div><div><div class="sh-t">編集の共通ルール</div><div class="sh-s">全30本に適用する</div></div></div>
  <div class="edit-rule">
    <div class="rule-box">
      <div class="rule-hd">映像・カット</div>
      <div class="rule-bd">
        <div class="rule-item"><div class="rule-dot"></div>1文ごとにカットを入れる（間を作る）</div>
        <div class="rule-item"><div class="rule-dot"></div>先生の表情が締まった瞬間を残す。笑顔のカットは使わない</div>
        <div class="rule-item"><div class="rule-dot"></div>ズームインを効果的に使う（核心の一言の前後）</div>
        <div class="rule-item"><div class="rule-dot"></div>余白を怖がらない。間（ま）がこのキャラクターの武器</div>
      </div>
    </div>
    <div class="rule-box">
      <div class="rule-hd">テキスト・音楽</div>
      <div class="rule-bd">
        <div class="rule-item"><div class="rule-dot"></div>AI自動字幕を入れる（全動画共通）</div>
        <div class="rule-item"><div class="rule-dot"></div>強調する一言だけ画面中央に大きく別テキストで出す</div>
        <div class="rule-item"><div class="rule-dot"></div>BGMは「シネマティック系・暗め・BPM遅め」を小音量で</div>
        <div class="rule-item"><div class="rule-dot"></div>過剰なエフェクトや明るいBGMはキャラと合わない、絶対NG</div>
      </div>
    </div>
    <div class="rule-box">
      <div class="rule-hd">撮影共通事項</div>
      <div class="rule-bd">
        <div class="rule-item"><div class="rule-dot"></div>服装：白衣（VIDEO 04・05・26・28は私服でも可）</div>
        <div class="rule-item"><div class="rule-dot"></div>表情：笑わない。真剣な顔でOK</div>
        <div class="rule-item"><div class="rule-dot"></div>目線：カメラを真っ直ぐ見る</div>
        <div class="rule-item"><div class="rule-dot"></div>場所：診察室。背景はシンプルに</div>
      </div>
    </div>
    <div class="rule-box">
      <div class="rule-hd">話し方の注意</div>
      <div class="rule-bd">
        <div class="rule-item"><div class="rule-dot"></div>セリフを「読む」のではなく、内容を理解して自分の言葉で話す</div>
        <div class="rule-item"><div class="rule-dot"></div>「〜ですよね」「〜なんですよ」は極力言わない</div>
        <div class="rule-item"><div class="rule-dot"></div>短い文章の後は1〜2秒間を空ける（編集で活かせる）</div>
        <div class="rule-item"><div class="rule-dot"></div>早口NG。ゆっくり、はっきり話す</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 01 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 01</div><div class="v-dur">60秒</div><div class="v-dur">自己診断型</div></div>
    <div class="v-title">この鼻、こうします。</div>
  </div>
  <div class="v-hook-bar">「この鼻を見てください。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">使う素材</span>団子鼻タイプの症例写真1枚（術前）</div>
          <div class="sbox-row"><span class="sbox-lbl">構成</span>写真を指差しながら話す。または写真を画面の半分に出して隣で話す</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「違います。」の一言を間を空けてから言う。ここが全体のピーク</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>冒頭に症例写真をフルスクリーンで1秒表示してから先生の顔へ</li>
            <li><div class="es-n">2</div>「違います。」の直前に0.5秒の無音カットを入れる</li>
            <li><div class="es-n">3</div>「高くするんじゃなくて、軽くする。」を画面中央に大きくテキスト表示</li>
            <li><div class="es-n">4</div>AI字幕＋シネマティックBGM（小音量）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「この鼻は自分に似てる」と思った人が<strong>止まる</strong>。即断言するスタイルが鑑定士キャラを確立する最初の動画。シリーズ化できる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける　<span class="visual">映像</span>＝編集で追加</div></div>
      <div class="script-box"><div class="script-text"><span class="visual">症例写真</span>

この鼻を見てください。<span class="pause">間</span>

鼻先が丸い。小鼻が張っている。全体に重さがあります。

よくこういう方から相談を受けます。
「他のクリニックでプロテーゼを勧められました」と。

<span class="pause">間</span>違います。

この鼻に必要なのは、高さじゃありません。

鼻先の「抜け感」です。

プロテーゼで高さを足したら、この重さがさらに目立ちます。

こうします。肋軟骨で鼻先を作り直して、小鼻を整える。鼻筋はいじらない。

高くするんじゃなくて、軽くします。<span class="pause">間</span>

それだけで、別の顔になります。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">プロテーゼを勧められたけど、違和感がある方へ。

「高さ」ではなく「軽さ」が必要な鼻があります。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #肋軟骨 #団子鼻 #鼻フル整形 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 02 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 02</div><div class="v-dur">60秒</div><div class="v-dur">審美眼型</div></div>
    <div class="v-title">整形がバレる鼻と、バレない鼻。</div>
  </div>
  <div class="v-hook-bar">「整形がバレる鼻と、バレない鼻。何が違うか話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生のみ（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「存在感がない、ということです。」の一言が全体の核心。ここだけ特に間を空けて、はっきり言う</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「存在感がない、ということです。」を画面中央に大テキストで表示</li>
            <li><div class="es-n">2</div>「鼻だけ別の顔から持ってきた」のくだりで参考画像をオーバーレイ</li>
            <li><div class="es-n">3</div>最後の「それだけを考えています。」でフェードアウト</li>
            <li><div class="es-n">4</div>AI字幕＋BGM（静か目）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「整形バレ」は美容整形検討者全員が検索するワード。<strong>一般層にも刺さる</strong>。「その人の顔に合った鼻」という哲学がブランドを作る。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">整形がバレる鼻と、バレない鼻。何が違うか話します。

バレる鼻には、共通点があります。

鼻だけ「完成」しています。

目との距離感、口との比率、顔の骨格。そこと合っていない。鼻だけ、別の顔から持ってきたように見えます。

あとは「直線すぎる」鼻。自然な鼻には、微妙なカーブがあります。そこを無視して綺麗に作りすぎると、逆に不自然になります。

じゃあバレない鼻は、何が違うか。<span class="pause">間</span>

存在感がない、ということです。<span class="pause">間</span>

変な言い方かもしれないけど、美しい鼻は「鼻を主張していない」。
顔全体の中に、自然に溶け込んでいます。

鼻を作るとき、一番時間をかけるのはそこです。

術式じゃなくて、設計。

あなたの顔に合った鼻を作ります。それだけを考えています。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">バレない鼻の共通点は「存在感がない」こと。

鼻だけ完成させるのが仕事じゃない。
顔全体に溶け込む鼻を設計するのが仕事。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #整形バレ #自然な鼻 #美容整形 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 03 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 03</div><div class="v-dur">60秒</div><div class="v-dur">業界内部告発型</div></div>
    <div class="v-title">同業者には怒られるかもしれない。</div>
  </div>
  <div class="v-hook-bar">「同業者には怒られるかもしれないけど、本当のことを言います。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>淡々と、でも確信を持って話す。感情的にならない。「鑑定士が事実を述べている」トーンで</div>
          <div class="sbox-row"><span class="sbox-lbl">注意</span>特定のクリニックへの言及はしない。「業界あるある」として話す</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「安さには理由がある。」を画面中央に大テキストで</li>
            <li><div class="es-n">2</div>「焦って決めた手術を、何件も修正してきた。」で一瞬暗転させるとドラマチック</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（重め・静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「業界の裏側」フォーマットは<strong>シェア率が最も高い</strong>。「この先生は正直だ」という信頼が一気に生まれる。保存・シェア両方が起きる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">同業者には怒られるかもしれないけど、本当のことを言います。

鼻整形、安くできるクリニックが増えています。

技術が上がったから安くなったわけじゃありません。<span class="pause">間</span>

安さには、理由があります。

コストを削っているか、経験の浅い医師がやっているか。どちらかです。

もう一つ。「鼻整形、すぐ予約できます」というクリニック。

カウンセリングに、時間をかけていない証拠です。<span class="pause">間</span>

鼻の手術は、一生ものです。顔の真ん中にあります。

焦って決めた手術を、何件も修正してきました。

安さと速さで選ぶな、とは言いません。

ただ、その選択の意味を理解した上で決めてほしい。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「安くて、すぐ予約できる」クリニックの裏側。

正直に話しました。

安さには理由があります。
その理由を理解した上で選んでください。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科選び #鼻整形失敗 #他院修正 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 04 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 04</div><div class="v-dur">60秒</div><div class="v-dur">倫理観型</div></div>
    <div class="v-title">断った手術の話。</div>
  </div>
  <div class="v-hook-bar">「断った手術の話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣 or 私服）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「これ以上やると、あなたの鼻は壊れます」の一言はゆっくり、はっきり言う。このセリフが全体のピーク</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>怒っていない。静かに、でも確信を持って話す</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「これ以上やると、あなたの鼻は壊れます」を画面中央に大テキスト</li>
            <li><div class="es-n">2</div>「断ることも、仕事のうちです。」で静かにフェードアウト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（シネマティック・重め）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「医師が手術を断る」という<strong>予想外の展開</strong>が視聴者を引き込む。倫理観と職人気質が同時に伝わる。コメントで「こういう先生に診てほしかった」が集まる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">断った手術の話をします。

先日、こういう相談が来ました。「鼻先をもっと細く、もっと高く」。

術前・術後の写真を見せてもらいました。
すでに2回、他院で手術を受けていました。<span class="pause">間</span>

正直に言いました。

「これ以上やると、あなたの鼻は壊れます」と。<span class="pause">間</span>

軟骨が限界まで使われていた。
これ以上削ったら、鼻先が落ちてきます。

「でもまだ気になるんです」と言われました。

わかります。<span class="pause">間</span>でも手術はしません。

仕事は、患者さんが望むことを全部やることじゃありません。

その人にとって一番いい鼻を作ること。

断ることも、仕事のうちです。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「もっとやりたい」という気持ちは理解できる。

でも断ることがある。

患者さんが望む全てをやるのが仕事じゃない。
一番いい鼻を作ることが仕事。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科 #他院修正 #鼻整形相談 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 05 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 05</div><div class="v-dur">45秒</div><div class="v-dur">職人気質型</div></div>
    <div class="v-title">0.1mmの話。</div>
  </div>
  <div class="v-hook-bar">「0.1mmの話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣 or 私服）</div>
          <div class="sbox-row"><span class="sbox-lbl">補足</span>縫合している手元の映像（オペ映像）があれば最後に入れると最高。なければ先生のみでOK</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>全体を静かに、淡々と話す。感情を抑えるほど逆に伝わる</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>冒頭「0.1mm」を画面中央に極大テキストで表示（インパクト）</li>
            <li><div class="es-n">2</div>手術中の手元映像があれば後半に挿入</li>
            <li><div class="es-n">3</div>「仕上がりを選びます。」で静止画フリーズ→フェードアウト</li>
            <li><div class="es-n">4</div>BGM：ピアノ系・静か・シンプル</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">短くて強い。<strong>職人のこだわりが伝わる</strong>最小単位の動画。「速さより仕上がりを選ぶ」という一言がブランドの哲学になる。保存・引用されやすい。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">0.1mmの話をします。<span class="pause">間</span>

鼻先の位置を0.1mm変えると、顔の印象が変わります。

大げさじゃなくて、本当に変わります。

だから一本の手術に、時間をかけます。縫合だけで30分以上かけることもあります。

「なんでそんなに時間をかけるんですか」とスタッフに聞かれました。<span class="pause">間</span>

答えは単純です。

0.1mmを積み重ねた先に、理想の鼻があります。<span class="pause">間</span>

速さと仕上がりはトレードオフだと思っています。

仕上がりを選びます。<span class="pause">間</span>

それだけです。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">0.1mmで顔の印象は変わる。

速さと仕上がりはトレードオフ。
仕上がりを選びます。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #クローズド法 #美容外科 #縫合 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 06 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 06</div><div class="v-dur">60秒</div><div class="v-dur">内側を見せる型</div></div>
    <div class="v-title">カウンセリング中、実は何を考えているか。</div>
  </div>
  <div class="v-hook-bar">「カウンセリング中に、実は何を考えているか。話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「鼻先を高くしたい、と言う。見ているのは鼻先じゃない。」の対比をはっきり出す。間を使う</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「見ているのは鼻先じゃない。」を大テキストで強調</li>
            <li><div class="es-n">2</div>「顔全体のバランス」の説明時に顔の図解をオーバーレイ</li>
            <li><div class="es-n">3</div>「カウンセリングの1時間が全てを決める」で締め</li>
            <li><div class="es-n">4</div>AI字幕＋BGM（静か・シネマティック）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「医師の頭の中を見せる」コンテンツは<strong>面白くて唯一無二</strong>。「この先生のカウンセリングを受けてみたい」という気持ちを直接生む。DM→予約への最短ルート。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">カウンセリング中に、実は何を考えているか。話します。

患者さんが「鼻先を高くしたい」と言う。<span class="pause">間</span>

見ているのは鼻先じゃありません。

顔全体のバランスです。目の幅、頬骨の位置、あごの形。鼻はその中の一つのパーツに過ぎません。

「高くしたい」という言葉の裏に、本当は何があるか。それを探しています。

「顔全体をもっと立体的にしたいのか」
「鼻先のもたつきをなくしたいのか」
「横顔を変えたいのか」

同じ「高くしたい」でも、答えは全部違います。<span class="pause">間</span>

だからカウンセリングに時間をかけます。

手術の30分より、カウンセリングの1時間が全てを決める。

そう思っています。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「鼻先を高くしたい」という言葉を聞いた時、見ているのは鼻先じゃない。

顔全体のバランス。
その人が本当に変えたいもの。

それを探すのがカウンセリング。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科カウンセリング #鼻整形相談 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 07 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 07</div><div class="v-dur">50秒</div><div class="v-dur">審美哲学型</div></div>
    <div class="v-title">嫌いな鼻の話。</div>
  </div>
  <div class="v-hook-bar">「嫌いな鼻の話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「やりすぎた鼻」と言う時、少し表情を曇らせる。嫌悪感ではなく「残念だ」という感覚で</div>
          <div class="sbox-row"><span class="sbox-lbl">注意</span>具体的な人名・クリニック名は絶対に出さない</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「やりすぎた鼻」の一言を大テキストで</li>
            <li><div class="es-n">2</div>「技術を見せるための鼻じゃなくて」の後に一瞬ポーズを入れる</li>
            <li><div class="es-n">3</div>最後の一文「それが作りたい鼻です。」で静止→フェードアウト</li>
            <li><div class="es-n">4</div>BGM：ピアノ・静か・余韻を残す終わり方</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「嫌いなもの」を語ることで<strong>審美眼と哲学が伝わる</strong>。「好きな鼻を語る」よりも「嫌いな鼻を語る」方がキャラクターが立つ。ブランド定義の動画。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">嫌いな鼻の話をします。<span class="pause">間</span>

やりすぎた鼻、です。

高すぎる。細すぎる。整いすぎている。

見た瞬間に「手術した鼻だ」とわかります。

技術があることはわかります。でも美しく見えません。<span class="pause">間</span>

美しい鼻は、その人の顔に「もともとあったかのように」存在している。

主張しすぎず。でも確かにそこにあります。<span class="pause">間</span>

技術を見せるための鼻じゃなくて、その人を美しく見せるための鼻。

それが作りたい鼻です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">嫌いな鼻は「やりすぎた鼻」。

美しい鼻は主張しない。
その人の顔に、もともとあったかのように存在している。

技術を見せるための鼻は作らない。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美鼻 #自然な仕上がり #審美眼 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 08 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 08</div><div class="v-dur">60秒</div><div class="v-dur">哲学型</div></div>
    <div class="v-title">クローズド法しかやらない理由。</div>
  </div>
  <div class="v-hook-bar">「クローズド法しかやらない理由、話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「傷がない方が、きれいだからです」の後に間を置く。確信を持って言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>静か。信念を語るように。感情は不要</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「傷がない」を画面中央に大テキスト</li>
            <li><div class="es-n">2</div>クローズ法のイメージ図があれば挿入</li>
            <li><div class="es-n">3</div>「クローズド法にこだわっています」でフェードアウト</li>
            <li><div class="es-n">4</div>AI字幕＋BGM（シネマティック・静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「なぜこのクリニックか」を技術哲学で語る動画。<strong>選択の根拠</strong>が明確になり、同じ価値観の患者を引き寄せる。保存・引用率が高い。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">クローズド法しかやらない理由、話します。<span class="pause">間</span>

鼻の中だけで、全ての操作をします。

外に傷がありません。

「なんで外を切らないんですか」とよく聞かれます。<span class="pause">間</span>

答えは単純です。

傷がない方が、きれいだからです。<span class="pause">間</span>

でも理由はそれだけじゃありません。

皮膚をめくらないということは、鼻の組織へのダメージが少ない。

ダメージが少ないということは、術後の回復が早い。

回復が早いということは、完成した鼻がより自然に見えます。<span class="pause">間</span>

「オープン法の方が難しい手術ができる」と言われることもあります。

でも難しい手術をするのが目的じゃありません。

きれいな鼻を作るのが目的です。

そのためにクローズド法にこだわっています。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">クローズド法にこだわる理由は、傷がないから。それだけじゃなく、組織へのダメージが少ないから。

ダメージが少ない＝回復が早い＝仕上がりが自然。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #クローズド法 #美容外科 #鼻整形福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 09 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 09</div><div class="v-dur">75秒</div><div class="v-dur">自己診断型</div></div>
    <div class="v-title">肋軟骨が必要な鼻・必要ない鼻。</div>
  </div>
  <div class="v-hook-bar">「肋軟骨が必要な鼻と、必要ない鼻の話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>3つの条件を話す時、指折り数えるジェスチャーを使うと視覚的にわかりやすい</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>教育的。でも淡々と</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「肋軟骨が必要な3条件」をテキストリスト表示</li>
            <li><div class="es-n">2</div>「カウンセリングで判断します」で締め</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（シネマティック）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「自分に肋軟骨は必要か」を視聴者が判断できる動画。コメントで<strong>「これに当てはまります」</strong>が集まりやすく、DM誘導に直結する。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">肋軟骨が必要な鼻と、必要ない鼻の話をします。

まず、肋軟骨とは何か。

胸から採取する軟骨です。強度があります。形も自由に作れます。

でも全員に必要なわけじゃありません。<span class="pause">間</span>

鼻先の軟骨がしっかりある方は、自分の軟骨を整えるだけで十分なことが多い。<span class="pause">間</span>

では、肋軟骨が必要な鼻はどんな鼻か。

一つ。軟骨が薄すぎて鼻先を支えられない。
二つ。他院で手術を繰り返して、元の軟骨が使えない。
三つ。大幅に鼻先の位置を変えたい。<span class="pause">間</span>

「肋軟骨を使う＝大きな手術」という怖さがある方もいます。

でも必要な鼻に使わないと、結果が出ません。

カウンセリングで一緒に判断します。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">肋軟骨は全員に必要なわけじゃない。

でも必要な鼻があります。
・軟骨が薄い
・他院修正で軟骨が残っていない
・大幅な形の変更

カウンセリングで一緒に判断しましょう。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #肋軟骨 #鼻整形相談 #美容外科 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 10 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 10</div><div class="v-dur">70秒</div><div class="v-dur">他院修正型</div></div>
    <div class="v-title">鼻整形で後悔した人が来る。</div>
  </div>
  <div class="v-hook-bar">「鼻整形で後悔した方が、毎月来ます。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣 or 私服）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>患者の声を再現する部分は、少し声のトーンを変えて話す。共感から入る</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>語りかけるように。責めない</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「手術前に先生と話せていない」を強調テキスト</li>
            <li><div class="es-n">2</div>「確認すること」の要点を箇条書きテキストで表示</li>
            <li><div class="es-n">3</div>BGMなし（トーン重視）＋AI字幕</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「自分も後悔しているかも」という視聴者の不安を刺激する。<strong>共感コメントが集まり</strong>、セカンドオピニオン層への最短アクセスになる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">鼻整形で後悔した方が、毎月来ます。<span class="pause">間</span>

「もっとよく確認すればよかった」
「値段で選んでしまった」
「先生とほとんど話せなかった」

共通点があります。<span class="pause">間</span>

手術前に、先生と話せていない。

どんな鼻にしたいか。どんなリスクがあるか。術後どう変わるか。

これを丁寧に話してくれる先生に出会えていなかった方がほとんどです。<span class="pause">間</span>

手術の技術も大事です。でも、その前のプロセスが全てを決めます。

一つお願いがあります。

カウンセリングで先生があなたの話を聞いてくれているか。

あなたの質問に、ちゃんと答えてくれているか。

それを確認してから、手術を決めてください。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">後悔した方の共通点は、先生とちゃんと話せていなかったこと。

技術より先に、コミュニケーションを確認して。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #他院修正 #美容外科選び #鼻整形相談 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 11 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 11</div><div class="v-dur">60秒</div><div class="v-dur">権威型</div></div>
    <div class="v-title">2,000件やってわかったこと。</div>
  </div>
  <div class="v-hook-bar">「2,000件やってわかったことを、話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「手術室に入った時には、もう結果は8割決まっています」は間を置いてから言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>静かな確信。数字が語るので過剰な感情は不要</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「2,000件」の数字を画面中央に極大テキスト（インパクト）</li>
            <li><div class="es-n">2</div>「3条件」をテキストリスト表示</li>
            <li><div class="es-n">3</div>「カウンセリングが、全てです。」で静止→フェードアウト</li>
            <li><div class="es-n">4</div>AI字幕＋BGM（重め・シネマティック）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">症例数が放つ<strong>圧倒的な説得力</strong>。「2,000件の医師が言うなら」という信頼を一本で形成する。新規認知層への最強の自己紹介動画。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">2,000件やってわかったことを、話します。<span class="pause">間</span>

鼻の手術を2,000件以上してきました。

1,000件を超えた頃、気づいたことがあります。

「うまくいく手術」には、パターンがあります。<span class="pause">間</span>

一つ。術前に、患者さんとの認識が一致している。
二つ。患者さんが、変化に対して現実的な期待を持っている。
三つ。解剖学的な条件が整っている。<span class="pause">間</span>

逆に言うと、うまくいかない手術にも、パターンがあります。

ほとんどの場合、術前のコミュニケーションに原因があります。<span class="pause">間</span>

手術室に入った時には、もう結果は8割決まっています。

カウンセリングが、全てです。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">2,000件の経験から言えること。

「うまくいく手術」は、手術室の前に決まっている。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科 #症例数 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 12 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 12</div><div class="v-dur">65秒</div><div class="v-dur">長期思考型</div></div>
    <div class="v-title">5年後も崩れない鼻の話。</div>
  </div>
  <div class="v-hook-bar">「5年後に崩れる鼻と、崩れない鼻の話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「無理をした鼻だからです。」を静かに、少し残念そうに言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>落ち着いた。警告ではなく情報として届ける</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>崩れやすい「3条件」をテキストリスト表示</li>
            <li><div class="es-n">2</div>「無理をしない設計」を強調テキスト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">長期視点の情報は<strong>保存率が特に高い</strong>。「5年後の自分への投資」という文脈でシェアされやすく、ファン化が加速する。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">5年後に崩れる鼻と、崩れない鼻の話をします。<span class="pause">間</span>

鼻の整形は、最初の仕上がりだけ見てもわかりません。

5年後、10年後に形が維持されているかどうかが大事です。<span class="pause">間</span>

崩れやすい鼻には特徴があります。

一つ。無理な位置に鼻先を持ってきている。
二つ。皮膚の厚さに対して、使った素材が大きすぎる。
三つ。支える構造が弱い。<span class="pause">間</span>

これは手術直後には見えません。

時間が経ってから、じわじわと現れます。<span class="pause">間</span>

術後5年で形が変わってしまった方が修正に来ます。

なぜそうなるかは、見ればわかります。

無理をした鼻だからです。<span class="pause">間</span>

長く美しい鼻を作りたいなら、無理をしない設計が必要です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">きれいな鼻は、5年後も美しいはず。

「今だけよければいい」ではなく、「長く続く鼻」を基準に選んで。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #長期経過 #他院修正 #鼻整形相談 #美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 13 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 13</div><div class="v-dur">55秒</div><div class="v-dur">審美型</div></div>
    <div class="v-title">高い鼻より、きれいな鼻の話。</div>
  </div>
  <div class="v-hook-bar">「「高い鼻」と「きれいな鼻」は、違います。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「高い鼻」と「きれいな鼻」の対比を表情で出す。「高い鼻」と言う時は少し首を振る</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>審美眼を持つ者として、静かに断言する</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「高い鼻 ≠ きれいな鼻」をテキストで大きく表示</li>
            <li><div class="es-n">2</div>顔の輪郭図に「鼻根・鼻先・小鼻」を矢印で示す図解をオーバーレイ</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（ピアノ系・静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「自分もただ高さだけ求めていた」という<strong>気づきを与える</strong>動画。共感→フォローの流れが生まれやすい。美容感度の高い層に強く刺さる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">「高い鼻」と「きれいな鼻」は、違います。<span class="pause">間</span>

「鼻を高くしたい」という相談がよくあります。

でも完成した鼻を見て、「思ってたのと違う」となる方がいます。

なぜか。<span class="pause">間</span>

高さだけを追いかけているからです。

美しい鼻には、高さだけじゃなく、角度があります。形があります。バランスがあります。

鼻根から鼻先にかけての流れ。
横顔から見た時の鼻先の出方。
小鼻との比率。<span class="pause">間</span>

この全部が整って初めて、「きれいな鼻」になります。

「高くしてください」という言葉の裏に、本当に求めているものを聞くのがカウンセリングの仕事です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「高い鼻」と「きれいな鼻」は違う。

高さ・角度・流れ・バランス——全部整ってはじめて美しい鼻になります。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #鼻の高さ #美鼻 #鼻整形相談 #美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 14 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 14</div><div class="v-dur">65秒</div><div class="v-dur">技術差型</div></div>
    <div class="v-title">クローズ法でできないと言われた鼻。</div>
  </div>
  <div class="v-hook-bar">「クローズ法ではできないと言われた方が来ます。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「できない」と言った後に少し間を置く。「その先生には」と静かに続ける</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>冷静。他院を攻撃しない。事実として話す</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「できない＝その先生には」の対比テキストを強調</li>
            <li><div class="es-n">2</div>「セカンドオピニオン」の文字を画面に出す</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（シネマティック）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「他院でNGと言われた方」に直接届く動画。<strong>セカンドオピニオン促進→問い合わせ直結</strong>の最短ルート。諦めていた層を掘り起こす。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">クローズ法ではできないと言われた方が来ます。<span class="pause">間</span>

他院でこう言われたそうです。

「あなたの鼻の状態では、オープン法でないと対応できない」と。<span class="pause">間</span>

でも、カウンセリングをして、クローズ法でできると判断した場合があります。

「なんで他の先生にはできないと言われたのか」と聞かれます。<span class="pause">間</span>

答えはシンプルです。

クローズ法は、狭い視野での操作になります。

難しいので、オープン法を選ぶ先生が多い。<span class="pause">間</span>

でも、クローズ法を2,000件以上やってきた経験があれば、見えるものがあります。

「できない」は、「その先生には」という意味のことがあります。<span class="pause">間</span>

セカンドオピニオンを求める権利は、患者さんにあります。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「クローズ法ではできない」と言われたら、セカンドオピニオンを。

「できない」は「その先生には」という意味かもしれません。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #クローズド法 #セカンドオピニオン #美容外科 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 15 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 15</div><div class="v-dur">65秒</div><div class="v-dur">インサイダー型</div></div>
    <div class="v-title">鼻整形の値段の話、正直に。</div>
  </div>
  <div class="v-hook-bar">「鼻整形の値段の話を、正直にします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣 or 私服）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「正直に」という言葉通り、フラットで誠実なトーンで話す</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>インサイダー感。「業界の人間が話す」感覚</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「値段が違う3つの理由」をテキストリスト表示</li>
            <li><div class="es-n">2</div>「一回で完成」の文字を強調テキスト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">お金の話は視聴維持率が特に高い。<strong>「安さで選ばないで」</strong>という直接的なメッセージが高単価クリニックへの信頼を作る。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">鼻整形の値段の話を、正直にします。<span class="pause">間</span>

なぜ値段がクリニックによってこんなに違うのか。

理由は3つあります。

一つ。使う素材が違います。
二つ。手術時間が違います。
三つ。先生の技術と経験が違います。<span class="pause">間</span>

安いところが悪いとは言いません。

でも、鼻の手術は安さで選ぶものではないと思っています。<span class="pause">間</span>

なぜかというと、鼻は顔の真ん中にあります。一番目立つ場所です。

やり直しが必要になった時のコストは、最初に高い選択をするより大きくなることが多い。<span class="pause">間</span>

「値段で迷っている」という方に伝えたいのは、一回の手術で完成させることを基準に考えてほしい、ということです。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">鼻整形の値段が違う理由：素材・手術時間・技術と経験。

一回で完成させることを基準に選んでほしい。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科選び #鼻整形費用 #鼻整形相談 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 16 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 16</div><div class="v-dur">60秒</div><div class="v-dur">失敗分析型</div></div>
    <div class="v-title">小鼻縮小で失敗する理由。</div>
  </div>
  <div class="v-hook-bar">「小鼻縮小で失敗する理由、話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>3つのパターンを指折り数えるようにはっきり言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>「軽い手術だと思わないで」という意志を持って話す</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「失敗の3パターン」をテキストリスト表示</li>
            <li><div class="es-n">2</div>「慎重な先生を選んで」を強調テキスト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">小鼻縮小は検索ボリュームが高い施術。失敗事例の解説は<strong>保存・シェアされやすく</strong>、信頼構築に効く。「軽い手術ほど怖い」という逆説が視聴者を引き込む。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">小鼻縮小で失敗する理由、話します。<span class="pause">間</span>

小鼻縮小は、比較的軽い手術だと思われています。

でも修正の相談が多い施術でもあります。<span class="pause">間</span>

失敗のパターンには共通点があります。

一つ目。切りすぎ。小鼻を縮小しすぎると、鼻の穴が外向きに開いて見えます。

二つ目。左右差。小鼻は元々左右非対称なことが多い。それを無視して同じ量だけ切ると、かえって非対称になります。

三つ目。傷跡。切開の位置が目立つと傷跡が残ります。<span class="pause">間</span>

小鼻縮小は、慎重にやるほど難しい手術です。

「小さい手術だから」で選ばないでください。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">小鼻縮小で失敗する理由：
・切りすぎ
・左右差を無視
・傷跡の位置

「軽い手術」だからこそ、慎重な先生を選んで。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#小鼻縮小 #鼻整形 #美容外科 #鼻整形失敗 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 17 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 17</div><div class="v-dur">60秒</div><div class="v-dur">長期型</div></div>
    <div class="v-title">整形した鼻が老化する話。</div>
  </div>
  <div class="v-hook-bar">「整形した鼻が、老化する話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「30年後の自分の顔を想像してください」は少し間を置いてゆっくり言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>淡々と。怖がらせるのではなく、知識として渡す</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「プロテーゼ」「軟骨吸収」をテキスト強調</li>
            <li><div class="es-n">2</div>「30年後」を大きく表示</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">長期経過の情報は美容外科SNSで<strong>希少価値が高い</strong>。20代の視聴者に刺さり、「最初の設計が大事」という文脈でクリニックへの信頼が深まる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">整形した鼻が、老化する話をします。<span class="pause">間</span>

あまり言われていないことです。

顔は老化します。皮膚がたるみます。軟骨も変化します。

その中で、整形した鼻はどうなるか。<span class="pause">間</span>

プロテーゼを入れた場合。長期間で皮膚が薄くなることがあります。透けて見えたり、位置がずれたりするケースがあります。

軟骨移植の場合。体の他の場所から取った軟骨は、吸収されることがあります。少しずつ形が変わることがあります。<span class="pause">間</span>

これを知っていれば、最初から長期を見越した設計ができます。

20代で手術する方に特に伝えたいことです。<span class="pause">間</span>

30年後の自分の顔を想像してください。その鼻、まだ美しいですか。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">整形した鼻も老化する。

長く美しくいるために、20代からの設計が大事です。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #鼻整形長期経過 #美容外科 #鼻整形相談 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 18 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 18</div><div class="v-dur">55秒</div><div class="v-dur">共感型</div></div>
    <div class="v-title">この質問ができる患者さん、好きです。</div>
  </div>
  <div class="v-hook-bar">「カウンセリングで、この質問ができる患者さんが好きです。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣 or 私服）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「失敗したことがありますか」の質問を再現する部分で、少し表情を緩める。好きな患者の話なので温度感を上げる</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「先生、失敗したことありますか？」を画面中央に大テキスト</li>
            <li><div class="es-n">2</div>「対応を見てください」で締め</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（少し温かめ）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「医師に聞いていいこと」の<strong>許可を与える</strong>動画。視聴者のカウンセリングへのハードルを大きく下げ、「この先生なら話せる」という安心感を生む。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">カウンセリングで、この質問ができる患者さんが好きです。<span class="pause">間</span>

「先生は、失敗したことがありますか」<span class="pause">間</span>

この質問を直球でしてくる方がいます。

いい質問だと思います。

答えます。あります。<span class="pause">間</span>

完璧な手術を目指していても、思い通りにいかないことがあります。

左右差が出たこと。回復が予想より長くかかったこと。

全部伝えます。

そしてその時どうしたか。どう対応したかも伝えます。<span class="pause">間</span>

失敗のない医師は信用しないでください。

どう対応するかを見てください。

それがその先生の本当の実力です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「先生、失敗したことありますか？」

この質問をできる患者さんが好きです。そして正直に答える先生を選んでください。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#美容外科選び #カウンセリング #鼻整形相談 #美容外科 #福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 19 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 19</div><div class="v-dur">65秒</div><div class="v-dur">教育型</div></div>
    <div class="v-title">鼻先だけじゃない。鼻根と鼻柱の話。</div>
  </div>
  <div class="v-hook-bar">「鼻は、鼻先だけじゃありません。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「鼻根」「鼻柱」を話すタイミングで自分の鼻を軽く指し示すと視覚的にわかりやすい</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>顔の図解に「鼻根・鼻先・鼻柱」を矢印で表示するオーバーレイ</li>
            <li><div class="es-n">2</div>各パーツを話すタイミングでハイライト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「知らなかった」という情報系コンテンツは<strong>保存率が最も高い</strong>カテゴリ。「鼻整形を考えている人全員が見るべき」という拡散を生む。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">鼻は、鼻先だけじゃありません。<span class="pause">間</span>

「鼻先を変えたい」という相談がほとんどです。

でもカウンセリングをすると、鼻先だけが問題じゃないことが多い。<span class="pause">間</span>

鼻には3つの部分があります。

一つ目、鼻根。目と目の間から始まる部分です。ここが低いと、鼻全体がのっぺりして見えます。

二つ目、鼻先。一番目に入る部分です。高さ、形、向き、すべて大事です。

三つ目、鼻柱。鼻の穴と穴の間の部分です。ここが短いと、横顔が間延びして見えます。<span class="pause">間</span>

「鼻先だけ変えれば解決する」と思っていると、術後に「なんか違う」となることがあります。

全体のバランスで設計することが大事です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">鼻のお悩みは「鼻先だけ」じゃないことが多い。

鼻根・鼻先・鼻柱——3つのバランスを見て設計します。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #鼻根 #鼻柱 #鼻先 #美容外科 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 20 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 20</div><div class="v-dur">55秒</div><div class="v-dur">職人型</div></div>
    <div class="v-title">手術中に気づくこと。</div>
  </div>
  <div class="v-hook-bar">「手術中に気づくことがあります。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">補足</span>手術中の手元映像（オペ映像）があれば後半に挿入すると最高</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「その瞬間、判断します」は力強く。即決力が伝わるように</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「計画」と「現実」の対比テキスト</li>
            <li><div class="es-n">2</div>手元映像（オペ映像）があれば後半に挿入</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（シネマティック・重め）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">医師の<strong>リアルな思考プロセス</strong>を見せるコンテンツ。「手術台の上の一瞬」という切り口が唯一無二で、職人として圧倒的に信頼される。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">手術中に気づくことがあります。<span class="pause">間</span>

術前の計画と、手術中に見えるものが違うことがあります。

皮膚を開けて初めてわかる、軟骨の状態。

予想より薄い。予想より厚い。非対称がある。<span class="pause">間</span>

その瞬間、判断します。

計画を変えるか、そのまま進むか。

手術台の上で、瞬時に答えを出します。<span class="pause">間</span>

経験がある手術は、この判断が速い。

「術前の計画通りにやる」だけでは、最高の仕上がりは出ません。

目の前にある組織を見て、最善を判断する。

それが手術の本質だと思っています。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">手術中に計画を変えることがある。

術前計画より、目の前の組織と向き合うこと。それが手術の本質。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科 #手術 #職人 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 21 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 21</div><div class="v-dur">65秒</div><div class="v-dur">インサイダー型</div></div>
    <div class="v-title">カウンセリングで嘘をつく患者がいる。</div>
  </div>
  <div class="v-hook-bar">「カウンセリングで、嘘をつく患者さんがいます。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「怒りません」をはっきり、でも優しく言う。責めているのではないというトーンで</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>理解と共感から入る。脅しにならないよう</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「正直に教えてください」を画面中央に大テキスト</li>
            <li><div class="es-n">2</div>「隠すとどうなるか」の要点をテキスト表示</li>
            <li><div class="es-n">3</div>BGMなし（トーン重視）＋AI字幕</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「自分も言いにくかった」という視聴者に<strong>直接届く</strong>。「この先生なら正直に話せる」という安心感がDMへのハードルを一気に下げる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">カウンセリングで、嘘をつく患者さんがいます。<span class="pause">間</span>

悪意があるわけじゃありません。

「手術回数を少なく言う」「他院でやったことを黙っている」

理由はわかります。言いにくいからです。<span class="pause">間</span>

でもこれは危険です。

過去に手術した回数や方法がわからないと、正確な判断ができません。

「一度もやったことがない」と思って見る目と、「2回やっている」と思って見る目は違います。<span class="pause">間</span>

全て正直に教えてください。

それで怒ることはありません。

むしろ、正直に話してくれた方が、より良い手術ができます。

隠すことで、あなたが損をします。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">過去の手術歴、正直に教えてください。

怒りません。でも知らないと、最善の手術ができません。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #他院修正 #カウンセリング #美容外科 #鼻整形相談 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 22 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 22</div><div class="v-dur">60秒</div><div class="v-dur">倫理型</div></div>
    <div class="v-title">やり直しが効かない手術の話。</div>
  </div>
  <div class="v-hook-bar">「やり直しが効かない手術の話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「もう何もできない」の一言はゆっくりはっきり言う。重さを持って</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>沈んだトーン。業界への静かな問題提起</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>手術回数と素材の減少を示すシンプルな図解</li>
            <li><div class="es-n">2</div>「修正前提で手術はしません」を大テキスト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（重め）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「修正できます」という業界の慣習への静かな問題提起。<strong>医師の誠実さと倫理観</strong>が伝わり、最初から任せたいという信頼を作る。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">やり直しが効かない手術の話をします。<span class="pause">間</span>

美容外科では、「修正できます」という言葉をよく聞きます。

でも本当は、何度でも修正できるわけじゃありません。<span class="pause">間</span>

鼻の手術は、やればやるほど素材が減ります。

軟骨が削れます。皮膚が薄くなります。血流が悪くなります。

3回、4回と繰り返すうちに、「もう何もできない」という状態になることがあります。<span class="pause">間</span>

そういう方が来ます。

「最初の手術がすべてを決めていた」とわかります。<span class="pause">間</span>

だから最初の一回に全力を尽くします。

修正前提で手術はしません。

完成させることだけを考えます。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「修正できる」は何度でもできる、という意味じゃない。

最初の一回で完成させる。それが最も患者さんのためになる。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #他院修正 #美容外科 #鼻整形相談 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 23 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 23</div><div class="v-dur">55秒</div><div class="v-dur">教育型</div></div>
    <div class="v-title">ダウンタイムで一番大事なこと。</div>
  </div>
  <div class="v-hook-bar">「ダウンタイムで一番大事なことを話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「触らないことです。これだけです。」の後に1〜2秒の沈黙を入れる</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>シンプルに断言する</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「触らない」を画面中央に極大テキスト（インパクト）</li>
            <li><div class="es-n">2</div>「完成は3ヶ月後」をテキスト表示</li>
            <li><div class="es-n">3</div>AI字幕＋BGM</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">術後の不安を持つ方に直接届く。「完成は3ヶ月」という知識は<strong>多くの方が知らない</strong>ため保存率が高く、術後フォロー層にリーチする。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">ダウンタイムで一番大事なことを話します。<span class="pause">間</span>

触らないことです。<span class="pause">間</span>

これだけです。<span class="pause">間</span>

でも、ほとんどの方が触ります。

鏡を見るたびに確認してしまいます。

腫れが引いているか。形がどうなっているか。<span class="pause">間</span>

気持ちはわかります。

でも腫れている間は、まだ組織が固まっていません。

触ることで、形が変わることがあります。<span class="pause">間</span>

ダウンタイム中の仕上がりで判断しないでください。

鼻の整形が完成するのは、最低でも3ヶ月後です。

その間は、信じて待つだけでいい。

それが一番いいダウンタイムの過ごし方です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">ダウンタイムで一番大事なこと。

触らない。鏡を見すぎない。信じて待つ。

完成は最低3ヶ月後です。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #ダウンタイム #術後ケア #美容外科 #鼻整形福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 24 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 24</div><div class="v-dur">50秒</div><div class="v-dur">教育型</div></div>
    <div class="v-title">鼻を触りすぎる人へ。</div>
  </div>
  <div class="v-hook-bar">「術後、鼻を触りすぎる方へ。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「良いことは一つもありません」をきっぱり言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>注意ではなく、理解を示してから伝える</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「良いことは一つもない」を強調テキスト</li>
            <li><div class="es-n">2</div>触るリスク3つをテキストリスト</li>
            <li><div class="es-n">3</div>「手より先生に聞く」で締め＋AI字幕＋BGM</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">術後患者が「先生が言っていた」として<strong>拡散しやすい</strong>動画。術後フォロー＝口コミ化のサイクルを作る。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">術後、鼻を触りすぎる方へ。<span class="pause">間</span>

「触らないでください」と言われていますよね。

それでも触ってしまう。<span class="pause">間</span>

理由は知っています。

不安だからです。

形が変わっていないか。ちゃんとできているか。腫れが引いているか。<span class="pause">間</span>

でも、触ることで起きることを伝えます。

軟骨の位置がずれることがあります。皮膚の回復が遅れることがあります。感染リスクが上がります。

良いことは一つもありません。<span class="pause">間</span>

不安な気持ちは当然です。でもその不安を手で解消しないでください。

気になることは、担当の先生に質問してください。

触るより、聞く方がいい。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">術後に触ってしまう気持ち、わかります。

でも触るほど回復が遅くなります。不安なことは手ではなく、先生に聞いてください。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #術後ケア #ダウンタイム #美容外科 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 25 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 25</div><div class="v-dur">60秒</div><div class="v-dur">職人型</div></div>
    <div class="v-title">一番難しい鼻の手術は何か。</div>
  </div>
  <div class="v-hook-bar">「一番難しい鼻の手術は何か。答えます。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「他院修正です。」の一言は間を置いてから言う。答えを出し惜しみするように</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>静かな確信</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「他院修正」を画面中央に大テキスト（間を置いてから表示）</li>
            <li><div class="es-n">2</div>難しい理由のリスト表示</li>
            <li><div class="es-n">3</div>「その瞬間のために」で締め→フェードアウト＋AI字幕＋BGM</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「最も難しい＝最もやりがいがある」という<strong>職人の哲学</strong>。他院修正を検討している方への最強のメッセージ。問い合わせの質が上がる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">一番難しい鼻の手術は何か。答えます。<span class="pause">間</span>

他院修正です。<span class="pause">間</span>

新しい鼻を作る手術より、誰かが一度作った鼻を直す手術の方が難しい。

なぜか。<span class="pause">間</span>

解剖学的な構造が変わっているからです。

元の軟骨の位置が変わっている。組織同士がくっついている。傷跡がある。血流が変わっている。

「正常な地図」がない状態で進む手術です。<span class="pause">間</span>

だから時間がかかります。計画も変わります。

でも他院修正をやる理由があります。<span class="pause">間</span>

後悔している方の顔が、変わる瞬間を見るためです。

その瞬間のために、難しい手術をやります。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">一番難しい手術は、他院修正。

でも、それをやるための理由がある。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#他院修正 #鼻整形修正 #美容外科 #鼻整形相談 #福岡美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 26 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 26</div><div class="v-dur">70秒</div><div class="v-dur">ストーリー型</div></div>
    <div class="v-title">美容外科医になった理由。</div>
  </div>
  <div class="v-hook-bar">「美容外科医になった理由を、話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（私服でもOK）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「言葉より先に、表情が変わっていました」はゆっくり、少し遠くを見るように言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>珍しく温かいトーン。「好きなものを話す時の顔」でOK</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「言葉より先に表情が変わった」をテキスト強調</li>
            <li><div class="es-n">2</div>最後「続けています。」で静止→フェードアウト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（感動系・静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">医師の原点を語るストーリー型は<strong>最もシェアされやすい</strong>カテゴリ。「この先生に診てもらいたい」という感情的な決断を生む、シリーズ最重要の一本。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">美容外科医になった理由を、話します。<span class="pause">間</span>

医師になってから、最初は別の科にいました。

ある日、美容外科の手術を見る機会がありました。<span class="pause">間</span>

術後、患者さんが鏡を見ました。

「先生、ありがとうございます」<span class="pause">間</span>

その言葉じゃありませんでした。

言葉より先に、表情が変わっていました。

何かを取り戻した顔でした。<span class="pause">間</span>

コンプレックスを持つというのは、毎日毎日その部分が気になるということです。

鏡を見るたびに、です。<span class="pause">間</span>

それが一度の手術で変わる。

その瞬間に立ち会えることが、美容外科の仕事だと思いました。

だから続けています。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">患者さんが鏡を見て、表情が変わった瞬間。

その瞬間のために、この仕事を続けています。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#美容外科医 #医師 #鼻整形 #美容外科 #福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 27 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 27</div><div class="v-dur">60秒</div><div class="v-dur">倫理型</div></div>
    <div class="v-title">手術を勧めない患者がいる。</div>
  </div>
  <div class="v-hook-bar">「手術を勧めない患者さんがいます。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「コンプレックスの原因が本当に鼻にあるか、確認したい」を丁寧に言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>患者を大切にしていることが伝わるように</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「手術を勧めないことがある」を大テキスト</li>
            <li><div class="es-n">2</div>「原因が鼻じゃないこともある」の部分を強調テキスト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「手術を断る医師」という予想外の誠実さ。<strong>信頼形成に最も効果的</strong>なタイプの動画。「売らない姿勢」が逆に購買につながる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">手術を勧めない患者さんがいます。<span class="pause">間</span>

カウンセリングをして、手術が必要じゃないと判断した時です。

「いや、でもやりたいんです」という方もいます。

それでも勧めません。<span class="pause">間</span>

なぜか。

「今の鼻が嫌い」という感情は本物です。でもその原因が本当に鼻にあるか、確認したいんです。<span class="pause">間</span>

鼻以外に原因があることもあります。ストレスや自己評価の問題のこともあります。

そういう場合、手術をしても解決しません。

変えたら変えたで、また別の部分が気になります。<span class="pause">間</span>

「手術はしなくていい」と伝えることも、仕事の一つです。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">手術が必要じゃないなら、そう言います。

コンプレックスの原因が本当に「鼻」にあるか、カウンセリングで一緒に確認したい。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #カウンセリング #美容外科 #コンプレックス #鼻整形相談 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 28 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 28</div><div class="v-dur">60秒</div><div class="v-dur">裏側型</div></div>
    <div class="v-title">美容外科医が自分の鼻を整形するとしたら。</div>
  </div>
  <div class="v-hook-bar">「美容外科医が自分の鼻を整形するとしたら、何を選ぶか。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（私服でもOK）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「患者さんに勧めることと、自分がやることは同じでなければならない」はゆっくり確信を持って言う</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>インサイダーの本音。少しカジュアルでもOK</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>選択肢3つをリストテキスト表示</li>
            <li><div class="es-n">2</div>「患者さんに勧めることと自分がやることは同じ」を強調テキスト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（静か）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「医師が自分でやるなら」は視聴者が最も知りたい情報。<strong>インサイダーの本音</strong>として圧倒的な信頼を生む。引用・保存されやすい。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">美容外科医が自分の鼻を整形するとしたら、何を選ぶか。<span class="pause">間</span>

よく聞かれます。

答えます。<span class="pause">間</span>

まず、クローズド法を選びます。外に傷を作りたくないからです。

素材は、できる限り自分の組織を使います。

プロテーゼを入れたくない理由があります。

異物は、長期で必ずリスクになります。自分の軟骨なら、その心配がない。<span class="pause">間</span>

時間は、急ぎません。仕上がりが完成するまで、6ヶ月待ちます。

そして担当する先生は、クローズド法を専門にしていて、自分の審美眼を信頼できる人を選びます。<span class="pause">間</span>

患者さんに勧めることと、自分がやることは、同じでなければならないと思っています。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">美容外科医が自分の鼻を整形するなら：
・クローズド法
・自分の組織優先
・急がない

患者さんに勧めることと自分がやることを同じにしたい。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科医 #クローズド法 #美容外科 #福岡 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 29 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 29</div><div class="v-dur">55秒</div><div class="v-dur">哲学型</div></div>
    <div class="v-title">鑑定士から見た、理想の鼻。</div>
  </div>
  <div class="v-hook-bar">「理想の鼻について、話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「鼻が最高の仕事をしている時、鼻のことは誰も気づかない」を確信を持って言う。ここが全体のピーク</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>哲学を語るように。少し上を向いても自然</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「理想の鼻＝気づかれない鼻」のテキスト対比</li>
            <li><div class="es-n">2</div>最後の一文で静止→フェードアウト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（ピアノ系・余韻を残す）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「鑑定士」キャラクターの哲学をまとめた動画。<strong>シリーズ全体の核心</strong>となる一本。引用・保存率が最も高く、ブランドを定義する。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">理想の鼻について、話します。<span class="pause">間</span>

「理想の鼻はどんな鼻か」とよく聞かれます。

答えは一つではありません。

顔が違えば、理想の鼻も違います。<span class="pause">間</span>

でも共通して言えることがあります。

理想の鼻は、顔に「質問」してきません。<span class="pause">間</span>

見た人が「鼻が気になる」じゃなくて、「この人、きれいだな」と感じる鼻です。

主役は顔全体であって、鼻ではありません。<span class="pause">間</span>

鼻が最高の仕事をしている時、鼻のことは誰も気づかない。

それが理想です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">理想の鼻は、気づかれない鼻。

顔全体が美しく見える時、鼻は黒子に徹しています。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #理想の鼻 #美鼻 #審美眼 #美容外科 #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO 30 -->
<div class="vpage">
  <div class="v-top">
    <div class="v-meta"><div class="v-num">VIDEO 30</div><div class="v-dur">65秒</div><div class="v-dur">感動型</div></div>
    <div class="v-title">最高の仕事ができた日。</div>
  </div>
  <div class="v-hook-bar">「最高の仕事ができた日の話をします。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「何が変わったかわからないって」の部分で表情が自然に緩む。それを残す</div>
          <div class="sbox-row"><span class="sbox-lbl">トーン</span>珍しく温かい。でも大げさにしない</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「何が変わったかわからないけど、きれいになった」を大テキスト</li>
            <li><div class="es-n">2</div>「気づかれない鼻が本物」で締め→フェードアウト</li>
            <li><div class="es-n">3</div>AI字幕＋BGM（感動系・余韻を残す終わり方）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">シリーズのフィナーレにふさわしい感動型。「この先生のところで手術したい」という<strong>感情的な決断</strong>を生む最後の一押し。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">最高の仕事ができた日の話をします。<span class="pause">間</span>

術後3ヶ月の検診で、患者さんが来ました。

術前は、鼻のことを常に気にしていて、外に出るのが億劫だったと話していました。<span class="pause">間</span>

3ヶ月後、来院した時の様子が違いました。

顔を上げていました。声の張りが違いました。<span class="pause">間</span>

「先生、友達から顔が変わったって言われました。でも何が変わったかわからないって」<span class="pause">間</span>

聞いた瞬間、これが成功だと思いました。

「手術した」じゃなくて、「きれいになった」と伝わる。<span class="pause">間</span>

誰にも気づかれない鼻が、最高の鼻です。

その患者さんのためにあった仕事を、その日できました。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「何が変わったかわからないけど、きれいになった」

これが最高の仕上がりです。気づかれない鼻が、本物の美しさ。

━━━━━━━━━━━━
🏥 Zetith Beauty Clinic 福岡院
👨‍⚕️ 院長 羽根 和秀
📩 DM でご相談ください
━━━━━━━━━━━━
#鼻整形 #美容外科 #ビフォーアフター #自然な仕上がり #ゼティス #羽根和秀</div>
      </div>
    </div>
  </div>
</div>

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/鼻の鑑定士_30本スクリプト.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
