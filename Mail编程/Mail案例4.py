from email.mime.text import MIMEText
from email.header import Header

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码格式
msg = MIMEText("Hello world", "plain", "utf-8")
'''
下面代码故意写错，说明所谓的发送者的地址只是一个Header的第一个参数作为字符串构建的
用utf-8编码是因为很可能内容包含非英文字符
'''
header_from = Header("从图灵学院邮箱发出去的<TuLingXueYuan@qq.com>", "utf-8")
msg["From"] = header_from

#填写接收者信息
header_to = Header("去王晓静的地方<wangxiaojing@sina.com>", "utf-8")
msg["To"] = header_to

header_sub = Header("这是图灵学院的主题", 'utf-8')
msg["Subject"] = header_sub

#构建发送者地址和登录信息
from_addr = "1366798119@qq.com"
from_pwd = "hjpovygcxmrshhcj"

#构建邮件接收者信息
to_addr = "1366798119@qq.com"
smtp_srv = "smtp.qq.com"

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
    srv.login(from_addr, from_pwd)
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)