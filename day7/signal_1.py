from signal import *
import time,os

def handler(sig,frame):
    if sig == SIGALRM:
        print("接收到时钟信号")
    elif sig == SIGINT:
        print("就不结束")
    elif sig == SIGUSR1:
        print("老司机")

alarm(5)

signal(SIGALRM,handler)
signal(SIGINT,handler)
signal(SIGUSR1,handler)

os.kill(os.getpid(),SIGUSR1)

while True:
    print("Waiting for a signal")
    time.sleep(2)