from wall import Wall
from wall import Radblock
from displayer import Displayer
from snake import Snake
from bug import Bug
import time
import threading
import msvcrt

displayer = Displayer()
wall = Wall()
snake = Snake()
radblock = Radblock()
bug = Bug(snake.points)

running = True

class InputThread(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global running,snake
        while running:
            c = str(msvcrt.getch())
            if c == "b'q'":
                running = False
            elif c == "b'w'":
                snake.set_toward("UP")
            elif c == "b's'":
                snake.set_toward("DOWN")
            elif c == "b'a'":
                snake.set_toward("LEFT")
            elif c == "b'd'":
                snake.set_toward("RIGHT")
input_thread = InputThread()
input_thread.start()

while running:
    #蛇动
    death = snake.action(bug,wall.points)
    if death:
        print("小蛇蛇死了\n按q键退出\n")
        break

    #将墙的坐标导入
    displayer.extend_points(wall.points)
    displayer.extend_points(radblock.points)

    #绘制图像
    displayer.draw_graphics(snake.score,snake.points,bug.point)
    #清屏
    displayer.clear()
    #time.sleep(snake.sleep_time)
    time.sleep(1)