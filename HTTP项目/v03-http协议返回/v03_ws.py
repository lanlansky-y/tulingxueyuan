import socket



def getHttpHeader(skt):
    '''
    得到传入socket的http请求头
    :param skt: 通信的socket
    :return: 解析后的请求头内容(字典格式)
    '''

    #读取某一行直到读取的行返回空行为止

    #用来存放结果，dict类型
    rst = {}
    line = getLine(skt)
    while line:
        '''
        判断得到的行是报头还是首部行，两个的操作方法不一样
        算法：
        1.利用冒号或者空格作为分隔符，分割字符串
        2.如果是首部行，则一定会把字符串分成两个子串
        3.否则就是一个字符串
        '''
        r = line.split(r': ')

        if len(r)==2:
            rst[r[0]] = r[1]
        else:
            r = line.split(r' ')
            rst['methor'] = r[0]
            rst['url'] = r[1]
            rst['version'] = r[2]

        line = getLine(skt)
    return rst


def getLine(skt):
    '''
    从socket中读取某一行
    :param skt: socket
    :return: 返回读取到的一行str格式内容
    '''
    '''
    前提：
    1.http协议传输内容是ascii编码
    2.真正传输的内容是通过网络流传输
    3.回车换行：b'\r',b'\n',b表示是一个bytes格式
    '''

    #每次从socket读取一个byte内容
    b1 = skt.recv(1)
    b2 = 0
    #data用来存放读取的行的内容
    data = b''

    while b2 != b'\r' and b1 != b'\n':
        b2 = b1
        b1 = skt.recv(1)

        data += bytes(b2)

    return data.strip(b'\r').decode()

#理解两个参数的含义
#理解创建一个socket的过程
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#注意addr的格式是tuple
#以及tuple两个元素的含义：ip和端口
sock.bind(('127.0.0.1', 7852))

#监听
sock.listen()

#接收一个传进来的socket
skt, addr = sock.accept()

#实际处理请求内容
httpinfo = getHttpHeader(skt)
print(httpinfo)

#给对方一个反馈
msg = "I love only xxx"
skt.send(msg.encode())

skt.close()