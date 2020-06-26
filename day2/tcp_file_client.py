from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#建立连接
sockfd.connect(('127.0.0.1',9000))

#消息的收发
while True:
    filename = input("发送<<")
    if not filename:
        break
    file = open(filename) 
    for line in file:
        n = sockfd.send(line.encode())       
    file.close()
#关闭套接字
sockfd.close()


