#tcp_server.py
from socket import *

#创建套接字
socket = socket(AF_INET,SOCK_STREAM)

#绑定地址
socket.bind(('0.0.0.0',8888))

#设置监听
socket.listen(5)

#等待接收连接
while True:
    print("Waiting for connect...")
    connfd,addr = socket.accept()
    print("Connect from",addr)
    while True:
        #收发消息
        data = connfd.recv(1024).decode()
        if not data:
            break    
        print(data)
        n = connfd.send(b'Receive your message')
        print("发送了%d字节"%n)
    connfd.close()
#关闭套接字
socket.close()


