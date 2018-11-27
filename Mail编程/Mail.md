电子邮件
邮件工作流程
MUA（Mail User Agent）邮件用户代理
MTA(Mail Transfer Agent)邮件传输代理
MDA(Mail Delivery Agent)邮件投递代理
laoshi@qq.com,老师，北京海淀
xuesheng@sina.com，学生，上海静安区
流程：
    1.MUA -> MTA,邮件已经在服务器上了
    2.qq MTA -> ......->sina MTA,邮件在新浪的服务器上了
    3.sina MTA -> sina MDA,此时邮件已经在你的邮箱里了
    4.sina  MDA  -> MUA(Foxmail/Outlook),邮件下载到本地电脑
    
编写邮件
    发送：MUA->MTA with SMTP(Simple Mail Transfer Protocal)
    接收：MDA->MUA with POP3 and IMAP(Post Office Protocal v3) 
    and Internet Message Access Protocal v4
准备工作
    注册邮箱（以qq邮箱为例）
    第三方邮箱需要特殊设置，以qq邮箱为例
        进入设置中心
        取得授权码
Python for mail
    SMTP协议负责发送邮件
        使用email模块构造邮件
        使用smtplib模块发送邮件
            纯文本邮件（案例：Mail案例1.py）
        HTML格式发送邮件
            准备HTML代码作为内容
            把邮件的subtype设为html
            发送
            案例：Mail案例2.py
        发送带附件的邮件
            可以把邮件看作是一个文本邮件和一个附件的合体
            一封邮件如果涉及多个部分，需要使用MIMEMultipart格式构建
            添加一个MIMEText正文
            添加一个MIMEBase或者MIMEText作为附件
            案例：Mail案例3.py
        添加邮件头，抄送等信息
            mail["From"] 表示发送者信息，包括姓名和邮件地址
            mail["To"] 表示接收者信息，包括姓名和邮件地址
            mail["Subject"] 表示摘要或者主题信息
            案例：Mail案例4.py
        同时支持html格式和text格式
            构建一个MIMEMultipart格式邮件
            MIMEMultipart的subtype设置成alternative格式
            添加HTML和text邮件
            案例：Mail案例5.py
    POP3协议接收邮件
        本质上是MDA到MUA的一个过程
        从MDA下载下来的是一个完整的邮件结构体，需要解析才能得到每个具体的文字信息
        步骤：
            1.用poplib下载邮件结构体原始内容
                1.准备相应的内容（邮件地址， 密码，POP3实例）
                2.身份认证
                3.一般会得到邮箱内邮件的整体列表
                4.根据相应序号，得到某一封信的数据流
                5.利用解析函数进行解析出相应的邮件结构体
            2.用email解析邮件的具体内容
        案例:Mail案例6.py