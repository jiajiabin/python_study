import tkinter
import time

window = tkinter.Tk()  # 打开一个窗口
# 设置标题
window.title("我的窗口")
# 设置大小
window.geometry('500x600')

# 字符串变量
var = tkinter.StringVar()


# 通过Label(标签)在窗口中添加文字
# l = tkinter.Label(window, text='你好！this is Tkinter', bg='green', font=('黑体', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l = tkinter.Label(window, textvariable=var, bg='green', font=('黑体', 12), width=30, height=2)

# 相当于start，将标签显示到屏幕上
l.pack()

count = 0
def print_hello_world():
    global count
    count += 1
    var.set("点击了{}次".format(count))
    l.place(x=50, y=300)        # 修改了l的位置


# 创建button
b = tkinter.Button(window, text='按钮', font=('Arial', 12), width=10, height=2, command=print_hello_world)
b.pack()

# 进入消息循环
window.mainloop()

# 创建定时器，1秒钟执行print_hello_world一次



# 作业:
# 通过图形介面，贪食蛇，扫雷
# https://blog.csdn.net/ahilll/article/details/81531587
# 查字典