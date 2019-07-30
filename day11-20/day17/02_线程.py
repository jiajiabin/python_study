import threading
import time
# 线程的使用

def function(n):
    for i in range(n):
        time.sleep(1)
        print('hello world', threading.current_thread().name)

        

# 创建线程对象
thread = threading.Thread(target=function, args=(5,))
thread.name = "子线程1"
thread.start()

# 主线程
threading.current_thread().name = "主线程"
function(6)
