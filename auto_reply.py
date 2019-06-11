import itchat,re
@itchat.msg_register(itchat.content.TEXT)


def text_reply(msg):
   
    text = msg['Text']

    if re.search('0', text).span():
        reply_text = '自动回复test0'
    elif re.search('1', text).span():
        reply_text = '自动回复test01'
    else:
        reply_text = ''
    print (text)
    return reply_text
    
itchat.auto_login(hotReload=True)  #不用每次都扫码
itchat.run()