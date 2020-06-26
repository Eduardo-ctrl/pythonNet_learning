from socket import *
import os

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定服务端地址
sockfd.bind(('0.0.0.0',9000))

#设置监听套接字
sockfd.listen(5)

#等待接收连接
connfd,addr = sockfd.accept()
print("与",addr,"连接成功")
file = open('newfile.py',"w")
while True:
    data = connfd.recv(1024).decode()
    if not data:
        break
    print("收到消息:",data)
    file.write(data)
file.close()
connfd.close()

#关闭套接字
sockfd.close()


