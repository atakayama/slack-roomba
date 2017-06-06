# Slackおそうじロボット

吸引力が落ちない

## せつめい
MacでIME発動中にバックスペースを押すとゴミ(制御文字)が残ってしまうことがあり、このゴミが含まれる投稿をWindowsで参照すると文字化けして読めません。

このBotは投稿されたメッセージ本文からゴミ掃除して再投稿します。

## つかいかた
* Slack管理画面からBot連携を設定し、APIトークンを発行します。
* slackbot_settings.pyを開き、変数API_TOKENにトークンを記述します。
* python2系でrun.pyを起動します。
* チャネルにbotを招待すると監視が始まり、以後の投稿からゴミ掃除してくれます。

## 参考サイト
[PythonのslackbotライブラリでSlackボットを作る(Qiita)](http://qiita.com/sukesuke/items/1ac92251def87357fdf6)
