#成功啦！！下一步设置词库！
#注意if statement的优先级

import itchat

@itchat.msg_register('Text')

def text_reply(msg):

    message = msg['Text']
    # 无关键词自动回复replay
    replay = u'自动回复测试中 请给我发数字/一串数字/包含数字的一句话'  

    #关键词设置
    if u'0' in message:
        replay = u'自动回复 Test0'
    elif u'1' in message:
        replay = u'自动回复 Test1'
    elif u'2' in message:
        replay = u'自动回复 Test2'
    elif u'3' in  message:
        replay = u'自动回复 Test3'
    elif u'4' in message:
        replay = u'自动回复 Test4'
    elif u'5' in message:
        replay = u'自动回复 Test5'
    elif u'6' in message:
        replay = u'自动回复 Test6'
    elif u'7' in message:
        replay = u'自动回复 Test7'
    elif u'8' in message:
        replay = u'自动回复 Test8'
    elif u'9' in message:
        replay = u'自动回复 Test9'
    return replay

itchat.auto_login(hotReload=True) #避免重复扫码
itchat.run()