# coding: utf-8

from slackbot.bot import listen_to;

'''
 メッセージに含まれる制御文字(+U0008)を削除して再投稿します。
 @param {Object} message Slackメッセージ
'''
@listen_to(r".+")
def drop_ctrlcode(message):
	text = message.body["text"];
	text_translated = text.replace(u"\u0008".encode("utf-8"), "");
	if (len(text_translated) < len(text)):
		message.send(u"%s「%s」" % (get_username(message), text_translated));

'''
 Slackメッセージオブジェクトからユーザ名を取り出します。
 @param {Object} message Slackメッセージ
 @return {String} ユーザ名
'''
def get_username(message):
	uid = message.body["user"];
	return message.channel._client.users[uid]["name"];
