import smtplib
from email.mime.text import MIMEText
#MIMEText三个主要参数
#1.邮件内容
#2.MIME子类型，在此案例我们用plain表示text（纯文本）类型
#3.邮件编码格式

msg = MIMEText("Hello, i am beijing tulingxueyuan ", "plain", "utf-8")

#发送email地址，此处地址直接使用我的qq邮箱，密码一般需要临时输入，此处偷懒
from_addr = "1366798119@qq.com"
#此处密码是经过申请设置后的授权码，不是你的qq邮箱密码
from_pwd = "hjpovygcxmrshhcj"

#收件人信息
#此处使用qq邮箱，我给自己发送
to_addr = "1366798119@qq.com"

#输入SMTP服务器地址
#此处根据不同的邮件服务商有不同的值
#现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
#腾讯qq邮箱所用的smtp地址是smtp.qq.com

smtp_srv = "smtp.qq.com"

try:
    #smtplib.SMTP_SSL()有两个参数
    #第一个是服务器地址，但一定是bytes格式，所以要编码
    #第二个参数是服务器接收访问端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)  #465是访问smtplib.SMTP_SSL的默认端口
    #登录邮箱发送
    srv.login(from_addr, from_pwd)
    #发送邮件
    #三个参数
    #1.发送地址
    #2.接收地址，必须是list形式
    #3.发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)