import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            print("Hellow")
            time.sleep(1)

thread = MyThread()
thread.start()

for i in range(10):
    time.sleep(0.8)