import time
import threading

# 创建一把锁，这把锁不能写在函数里，因为Lock()只执行一次，保证是同一把锁
lock = threading.Lock()

def function(n):
    global lock     # 引入全局变量
    # 通过加锁，让下述代码片段，只能原子操作
    with lock:
        for i in range(n):
            time.sleep(1)
            print('hello world', threading.current_thread().name)

    for i in range(n):
        time.sleep(0.8)
        print("good morning", threading.current_thread().name)


for i in range(5):
    thread = threading.Thread(target=function, args=(5,))
    thread.name = "子线程{}".format(i)
    thread.start()

