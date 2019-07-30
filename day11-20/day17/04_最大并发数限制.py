# 线程锁有的时候不是为了原子操作，只是为了限制最大并发数
import time
import threading

lock = threading.Semaphore(3)

def function(n):
    global lock     # 引入全局变量
    # 通过加锁，让下述代码片段，只能原子操作
    with lock:
        for i in range(n):
            time.sleep(1)
            print('hello world', threading.current_thread().name,
                  threading.current_thread().is_alive())


for i in range(5):
    thread = threading.Thread(target=function, args=(5,))
    thread.name = "子线程{}".format(i)
    thread.start()