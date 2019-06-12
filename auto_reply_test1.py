#第一次的思路是错的 :(

import itchat,re
@itchat.msg_register(itchat.content.TEXT)


def text_reply(msg):
   
    match = re.search('0', msg['Text']).span()
    #还没有搞懂span怎么用
    #span只可以出现一次 不然会报错
    if match:
        reply_text = '自动回复test0'
    #原本思路是设置match0, match1...以此类推 并if/elif match1：define reply_text
    #span报错
    return reply_text
    
itchat.auto_login(hotReload=True)  #不用每次都扫码
itchat.run()