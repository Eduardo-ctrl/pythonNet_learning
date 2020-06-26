创建进程对象
p = mp.Process(target = fun)

#启动进程对象
p.start()

sleep(2)
print("这是父进程")

#回收进程
p.join()

print("parent a =",a)

