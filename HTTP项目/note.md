#HTTP项目实战
    深入理解HTTP协议
    模拟后台服务程序基本流程和大致框架
    
    推荐书籍
        图解http协议，
        图解tcp/ip协议
        严重推荐图解系列

##v01-验证技术
    验证socket-tcp技术
    使用浏览器访问案例：ws.py内的服务器地址,首先要先启动服务器
    
##v02-解析传入http协议
    根据http协议格式，逐行读取信息
    按行读取后的信息，需要进行拆解
    
##v03-http协议封装返回内容
    返回头："HTTP/1.1 200 OK\r\n" 
    首部行：
        "Content-Length: xxx\r\n"
        "Date: 20181209\r\n"
    空行：
        "\r\n"
    返回内容：
        "I love beijingtulingxueyuan"
    案例：v03