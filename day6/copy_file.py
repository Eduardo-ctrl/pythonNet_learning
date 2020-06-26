# import multiprocessing as mp 

# def writed(text,filename):
#     f = open("process1.py")
#     f.read()
#     x = f.tell()
#     y = (x + 1)//2
#     f.seek(0,0)
#     text1 = f.read(y)
#     text2 = f.read()
#     f.close()
#     f = open(filename,'w')
#     if text == 1:
#         f.write(text1)
#     else:
#         f.write(text2)
#     f.close()

# p = mp.Process(target = writed,args = (1,'text1.py'))
# p.start()

# writed(2,'text2.py')
# p.join()

import os
from multiprocessing import Process

filename = "process1.py"
#获取文件大小
size = os.path.getsize(filename)

#如果子进程使用父进程的对象，那么相互之间有偏移量的影响
# f = open(filename,'rb')

#复制前半部分
def copy1():
    f = open(filename,'rb')
    n = size // 2
    fw = open('text1.py','wb')

    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

#复制下半部分
def copy2():
    f = open(filename,'rb')
    fw = open('text2.py','wb')

    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
    f.close()

p1 = Process(target = copy1)
p2 = Process(target = copy2)
p1.start()
p2.start()
p1.join()
p2.join()


