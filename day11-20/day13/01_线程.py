# 线程是一种工具类，是CPU同一时间完成多个任务的一种手段。
# 程序默认拥有一个线程，我们称为主线程，占用主线程执行的任务，称为同步任务，不占用主线程，开辟一个新线程即子线程完成的任务
# 称为异步任务。

import threading
import time

# 自定义一个线程类，继承自官方的线程类
class MyThread(threading.Thread):
    # 将子线程执行的任务，写在run函数中
    def run(self):      # 重写
        for i in range(10):
            print("Hello world!")
            time.sleep(1)


thread = MyThread()
thread.start()
# 启动线程，这个函数一瞬间就会结束，但是子线程会执行下去。

# 主线程可以继续完成其他任务
for i in range(10):
    print("Good morning")
    time.sleep(0.8)
