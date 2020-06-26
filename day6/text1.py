import multiprocessing as mp
from time import sleep

a = 1
def fun():
    sleep(3)
    global a
    print('a = ',a)
    a = 10000
    print("子进程事件")

#