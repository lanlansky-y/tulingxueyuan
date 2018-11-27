import socket

#模拟服务器的函数
def serverFunc():
    #1.建立socket,socket.AF_INET:使用ipv4协议族,
    # socket.SOCK_DGRAM:使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #绑定ip和port,地址是一个tuple类型：(ip, port)
    #7852:随便指定的一个端口
    addr = ('127.0.0.1', 7852)
    sock.bind(addr)

    #接受客户端的访问
    #recvfrom接收的返回值是一个tuple，前一项表示数据，后一项表示地址
    rst = sock.recvfrom(500)        #参数的含义是缓冲区的大小
    data, addr = rst

    print(data)
    print(type(data))
    print('Got connection from', addr)

    #发送过来的数据是bytes格式，必须经过解码才能得到str格式内容
    #decode默认的参数是utf-8
    text = data.decode()
    print(text)
    print(type(text))

    #给对方返回的消息
    rsp = '我不饿'
    #发送的数据需要编码成bytes格式
    #encode默认的参数是utf-8
    #编码和解码的格式必须一致
    data = rsp.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    print('Start server...')
    serverFunc()
    print('Ending server...')