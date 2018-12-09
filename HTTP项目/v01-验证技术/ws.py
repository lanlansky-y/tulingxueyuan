import socket

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

#读取传入消息，
#需要注意读取的信息的长度一定要小于等于实际消息的长度，否则会假死
msg = skt.recv(100)
print(type(msg))

#decode默认utf-8
print(msg.decode())

#给对方一个反馈
msg = "I love only xxx"
skt.send(msg.encode())

skt.close()