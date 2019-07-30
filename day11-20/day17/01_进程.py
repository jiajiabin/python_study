import multiprocessing
import os
import time

def function(n):
    p = multiprocessing.current_process()
    for i in range(n):
        time.sleep(1)
        print(p.name, "hello world!", p.pid, os.getppid())
        # p.pid是获取当前进程【进程id】， os.getppid则是获取当前进程的【父进程id】


# 进程只能执行在主py文件中，所谓主py文件（主模块）,就是直接执行的py文件而非导入的py文件

if __name__ == '__main__':
    process = multiprocessing.Process(None, target=function, args=(8,), name="子进程")
    process.name = "子进程1号"
    process.start()     # 开辟了子进程

    multiprocessing.current_process().name = "主进程"
    # 主进程工作
    function(6)
