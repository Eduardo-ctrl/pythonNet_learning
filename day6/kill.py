import os
import signal

#向65592发送信号
os.kill(65592,signal.SIGKILL)
