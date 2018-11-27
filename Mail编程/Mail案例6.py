import poplib  #poplib负责从MDA到MUA下载

#以下包负责相关邮件结构解析
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

#得到邮件的原始内容
#这个过程主要负责从MDA到MUA的下载并使用Parser粗略解析
def getMsg():
    #准备相应的信息
    email = "1366798119@qq.com"
    #邮箱的授权码
    pwd = "hjpovygcxmrshhcj"

    #pop3服务器地址
    pop3_srv = "pop.qq.com" #端口995

    #SSL代表是安全通道
    srv = poplib.POP3_SSL(pop3_srv)

    #user代表email地址
    srv.user(email)
    #pass_代表密码
    srv.pass_(pwd)

    #以下操作根据具体业务具体使用
    #stat返回邮件数量和占用空间
    #注意stat返回一个tuple格式
    msgs, counts = srv.stat()
    print("Messages:{0}, Size:{1}".format(msgs, counts))

    #list返回所有邮件编号列表
    #mails是所有邮件编号列表
    rsp, mails, octets = srv.list()
    #可以查看返回的mails列表，类似与[b'1 82923', b'2 2184',....]
    print(mails)

    #获取最新一封邮件，注意，邮件索引号是从1开始，最新代表索引号最高
    index = len(mails)
    #retr负责返回一个具体索引号的一封信的内容，此内容不具有可读性
    #lines存储邮件的最原始文本的每一行
    rsp, lines, octets = srv.retr(index)

    #获得整个邮件的原始文本
    msg_count = b'\r\n'.join(lines).decode("utf-8")
    #解析出邮件的整个结构体
    #参数是解码后的邮件整体
    msg = Parser().parsestr(msg_count)

    #关闭链接
    srv.quit()

    return msg

#详细解析得到的邮件内容
#msg代表是邮件的原始内容
#idnent代表的是邮件嵌套的层级
def parseMsg(msg, indent=0):
    '''
    1.邮件完全可能是有嵌套格式
    2.邮件只有一个From, To, Subject之类的信息
    :param msg:
    :param indent: 描述邮件里面有几个邮件MIMExxx类型的内容，展示的时候进行相应缩进
    :return:
    '''
    #想办法提取头部信息
    #只有在第一层的邮件中才会有相关内容
    #此内容只有一个
    if indent == 0:
        for header in ["From", "To", "Subject"]:
            #使用get可以避免如果没有相关关键字报错的可能性
            #如果没有关键字"From",我们使用msg["From"]会报错
            value = msg.get(header, '')
            if value:
                #Subject中的内容直接解码就可以，他是字符串类型
                if header == "Subject":
                    value = decodeStr(value)
                #如果是From和To字段，则内容大概是“我的邮箱<xxxx@qq.com>”这种格式
                else:
                    hdr, addr = parseaddr(value)
                    name = decodeStr(hdr)
                    #最终返回形如“我的邮箱<xxx@qq.com>”的形式
                    value = "{0}<1>".format(name, addr)
            print("{0}, {1}, {2}".format(indent, header, value))
    #下面代码关注邮件内容本身
    #邮件内容中，有可能是multipart类型，也有可能是普通邮件类型
    #下面的解析使用递归方式
    if (msg.is_multipart()):
        #如果是multipart类型，则调用递归解析
        #得到多部分邮件的一个基础邮件部分
        parts = msg.get_payload()
        #enumerate函数是内置函数
        #作用是将一个列表，此处是parts，生成一个有索引和parts原内容构成的新的列表
        #例如enumerate(['a', 'b', 'c']) 结果是：[(1. 'a'), (2, 'b'), (3, 'c')]
        for n,part in enumerate(parts):
