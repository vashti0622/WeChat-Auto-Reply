import itchat,re
@itchat.msg_register(itchat.content.TEXT)

def text_reply(msg):
    reply_text = msg['Text']
    if msg['Text'] == '？':
        reply_text = '自动回复：欢迎来到复读机模式。'

    return reply_text


    
itchat.auto_login(hotReload=True)  #不用每次都扫码
itchat.run()