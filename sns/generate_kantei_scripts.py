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

/* CHARACTER PAGE */
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

/* VIDEO PAGE */
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

/* SCRIPT */
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
    圧倒的な審美眼と技術で語る7本。
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

  <div class="sh"><div class="sh-n">EDIT STYLE</div><div><div class="sh-t">編集の共通ルール</div><div class="sh-s">全7本に適用する</div></div></div>
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
        <div class="rule-item"><div class="rule-dot"></div>服装：白衣（VIDEO 04・05は私服でも可）</div>
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
    <div class="v-title">この鼻、俺ならこうする。</div>
  </div>
  <div class="v-hook-bar">「この鼻を見てください。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">使う素材</span>団子鼻タイプの症例写真1枚（術前）</div>
          <div class="sbox-row"><span class="sbox-lbl">構成</span>写真を指差しながら話す。または写真を画面の半分に出して隣で話す</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「違う。」の一言を間を空けてから言う。ここが全体のピーク</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>冒頭に症例写真をフルスクリーンで1秒表示してから先生の顔へ</li>
            <li><div class="es-n">2</div>「違う。」の直前に0.5秒の無音カットを入れる</li>
            <li><div class="es-n">3</div>「高くするんじゃなくて、軽くする。」を画面中央に大きくテキスト表示</li>
            <li><div class="es-n">4</div>AI字幕＋シネマティックBGM（小音量）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「この鼻は自分に似てる」と思った人が<strong>止まる</strong>。「俺ならこうする」という断言が鑑定士キャラを確立する最初の動画。シリーズ化できる。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける　<span class="visual">映像</span>＝編集で追加</div></div>
      <div class="script-box"><div class="script-text"><span class="visual">症例写真</span>

この鼻を見てください。<span class="pause">間</span>

鼻先が丸い。小鼻が張っている。全体に重さがある。

よくこういう方から相談を受ける。
「他のクリニックでプロテーゼを勧められました」と。

<span class="pause">間</span>違う。

この鼻に必要なのは高さじゃない。

鼻先の「抜け感」です。

プロテーゼで高さを足したら、この重さがさらに目立つ。

俺ならこうします。肋軟骨で鼻先を作り直して、小鼻を整える。鼻筋はいじらない。

高くするんじゃなくて、軽くする。<span class="pause">間</span>

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
            <li><div class="es-n">2</div>「鼻だけ別の顔から持ってきた」のくだりで、極端な整形例の参考画像（フリー素材）をオーバーレイ</li>
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

バレる鼻には共通点がある。

鼻だけ「完成」している。

目との距離感、口との比率、顔の骨格。そこと合っていない。鼻だけ別の顔から持ってきたように見える。

あとは「直線すぎる」鼻。自然な鼻には微妙なカーブがある。そこを無視して綺麗に作りすぎると、逆に不自然になる。

じゃあバレない鼻は何が違うか。<span class="pause">間</span>

存在感がない、ということです。<span class="pause">間</span>

変な言い方かもしれないけど、美しい鼻は「鼻を主張していない」。
顔全体の中に自然に溶け込んでいる。

俺が鼻を作るとき、一番時間をかけるのはそこです。

術式じゃなくて、設計。

あなたの顔に合った鼻を作る。それだけを考えています。</div></div>
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

鼻整形、安くできるクリニックが増えた。

技術が上がったから安くなったわけじゃない。<span class="pause">間</span>

安さには理由がある。

コストを削っているか、経験の浅い医師がやっているか。どちらかです。

もう一つ。「鼻整形、すぐ予約できます」というクリニック。

カウンセリングに時間をかけていない証拠です。<span class="pause">間</span>

鼻の手術は一生ものです。顔の真ん中にある。

焦って決めた手術を、俺は何件も修正してきた。

安さと速さで選ぶな、とは言わない。

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
    <div class="v-title">俺が断った手術の話。</div>
  </div>
  <div class="v-hook-bar">「俺が断った手術の話をします。」</div>
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
      <div class="script-box"><div class="script-text">俺が断った手術の話をします。

先日、こういう相談が来た。「鼻先をもっと細く、もっと高く」。

術前・術後の写真を見せてもらった。
すでに2回、他院で手術を受けていた。<span class="pause">間</span>

正直に言った。

「これ以上やると、あなたの鼻は壊れます」と。<span class="pause">間</span>

軟骨が限界まで使われていた。
これ以上削ったら、鼻先が落ちてくる。

「でもまだ気になるんです」と言われた。

わかる。<span class="pause">間</span>でも手術はしない。

俺の仕事は、患者さんが望むことを全部やることじゃない。

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
            <li><div class="es-n">3</div>「俺は仕上がりを選ぶ。」で静止画フリーズ→フェードアウト</li>
            <li><div class="es-n">4</div>BGM：ピアノ系・静か・シンプル</div></li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">短くて強い。<strong>職人のこだわりが伝わる</strong>最小単位の動画。「速さより仕上がりを選ぶ」という一言がブランドの哲学になる。保存・引用されやすい。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">0.1mmの話をします。<span class="pause">間</span>

鼻先の位置を0.1mm変えると、顔の印象が変わります。

大げさじゃなくて、本当に変わる。

だから俺は一本の手術に時間をかける。縫合だけで30分以上かけることもある。

「なんでそんなに時間をかけるんですか」とスタッフに聞かれた。<span class="pause">間</span>

答えは単純です。

0.1mmを積み重ねた先に、理想の鼻がある。<span class="pause">間</span>

速さと仕上がりはトレードオフだと思っている。

俺は仕上がりを選ぶ。<span class="pause">間</span>

それだけです。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">0.1mmで顔の印象は変わる。

速さと仕上がりはトレードオフ。
俺は仕上がりを選ぶ。

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
    <div class="v-title">カウンセリング中、俺が実は考えていること。</div>
  </div>
  <div class="v-hook-bar">「カウンセリング中に俺が実は何を考えているか、話します。」</div>
  <div class="v-body">
    <div class="v-sidebar">
      <div class="sbox">
        <div class="sbox-hd">撮影指示</div>
        <div class="sbox-bd">
          <div class="sbox-row"><span class="sbox-lbl">出演</span>羽根先生（白衣）</div>
          <div class="sbox-row"><span class="sbox-lbl">ポイント</span>「鼻先を高くしたい、と言う。俺が見ているのは鼻先じゃない。」の対比をはっきり出す。間を使う</div>
        </div>
      </div>
      <div class="sbox">
        <div class="sbox-hd">編集指示</div>
        <div class="sbox-bd">
          <ul class="edit-steps">
            <li><div class="es-n">1</div>「俺が見ているのは鼻先じゃない。」を大テキストで強調</li>
            <li><div class="es-n">2</div>「顔全体のバランス」の説明時に顔の図解（輪郭・目・鼻・口の関係）をオーバーレイ</li>
            <li><div class="es-n">3</div>「カウンセリングの1時間が全てを決める」で締め</li>
            <li><div class="es-n">4</div>AI字幕＋BGM（静か・シネマティック）</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「医師の頭の中を見せる」コンテンツは<strong>面白くて唯一無二</strong>。「この先生のカウンセリングを受けてみたい」という気持ちを直接生む。DM→予約への最短ルート。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">カウンセリング中に俺が実は何を考えているか、話します。

患者さんが「鼻先を高くしたい」と言う。<span class="pause">間</span>

俺が見ているのは鼻先じゃない。

顔全体のバランスです。目の幅、頬骨の位置、あごの形。鼻はその中の一つのパーツに過ぎない。

「高くしたい」という言葉の裏に、本当は何があるか。それを探している。

「顔全体をもっと立体的にしたいのか」
「鼻先のもたつきをなくしたいのか」
「横顔を変えたいのか」

同じ「高くしたい」でも、答えは全部違う。<span class="pause">間</span>

だからカウンセリングに時間をかける。

手術の30分より、カウンセリングの1時間が全てを決める。

そう思っています。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">「鼻先を高くしたい」という言葉を聞いた時、俺が見ているのは鼻先じゃない。

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
    <div class="v-title">俺が嫌いな鼻の話。</div>
  </div>
  <div class="v-hook-bar">「俺が嫌いな鼻の話をします。」</div>
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
            <li><div class="es-n">3</div>最後の一文「それが俺の作りたい鼻です。」で静止→フェードアウト</li>
            <li><div class="es-n">4</div>BGM：ピアノ・静か・余韻を残す終わり方</li>
          </ul>
        </div>
      </div>
      <div class="buzz-box">「嫌いなもの」を語ることで<strong>審美眼と哲学が伝わる</strong>。「好きな鼻を語る」よりも「嫌いな鼻を語る」方がキャラクターが立つ。ブランド定義の動画。</div>
    </div>
    <div class="script-area">
      <div class="script-top"><div class="script-title-label">完全セリフ</div><div class="script-note"><span class="pause">間</span>＝1〜2秒空ける</div></div>
      <div class="script-box"><div class="script-text">俺が嫌いな鼻の話をします。<span class="pause">間</span>

やりすぎた鼻、です。

高すぎる。細すぎる。整いすぎている。

見た瞬間に「手術した鼻だ」とわかる。

技術があることはわかる。でも俺には美しく見えない。<span class="pause">間</span>

美しい鼻は、その人の顔に「もともとあったかのように」存在している。

主張しすぎず。でも確かにそこにある。<span class="pause">間</span>

技術を見せるための鼻じゃなくて、その人を美しく見せるための鼻。

それが俺の作りたい鼻です。</div></div>
      <div class="caption-area">
        <div class="cap-hd">キャプション</div>
        <div class="cap-bd">俺が嫌いな鼻は「やりすぎた鼻」。

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

</body>
</html>"""

from weasyprint import HTML
out = "/home/user/CellTagWorkflow/sns/鼻の鑑定士_7本スクリプト.pdf"
HTML(string=html).write_pdf(out)
print(f"完了: {out}")
