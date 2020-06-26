from multiprocessing import Process,Queue
from signal import *
import os,time,sys

q = Queue()

#售票员接收信号处理
def func1(sig,frame):
    if sig == SIGINT:
        os.kill(os.getppid(),SIGUSR1)
    elif sig == SIGQUIT:
        os.kill(os.getppid(),SIGUSR2)
    elif sig == SIGUSR1:
        print("\n"+"售票员: 到站了，请下车")
        sys.exit("售票员下车了")

#司机接收信号处理
def func2(sig,frame):
    if sig == SIGUSR1:
        print("\n"+"司机: 老司机开车了")
    elif sig == SIGUSR2:
        print("\n"+"司机: 车速有点快，系好安全带")
    elif sig == SIGTSTP:
        os.kill(q.get(),SIGUSR1)


def sales():
    q.put(os.getpid())
    signal(SIGINT,func1)
    signal(SIGQUIT,func1)
    signal(SIGUSR1,func1)  
    signal(SIGUSR2,SIG_IGN)
    signal(SIGTSTP,SIG_IGN)
    while True:
        pause()


p = Process(target = sales)

p.start()

signal(SIGINT,SIG_IGN)
signal(SIGQUIT,SIG_IGN)
signal(SIGUSR2,func2)
signal(SIGTSTP,func2)
signal(SIGUSR1,func2)

p.join()
print("司机下车")
