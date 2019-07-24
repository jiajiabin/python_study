a1 = 1  # 定义程序a1正在运行，用 1 表示
a2 = 1
b2 = 1

def stop(course, status):
    if course == 1 and status == 1:
        return True
    else:
        return False

def judge(course, status):
    if stop(a2, b2):
        return False
    else:
        return True

a3 = judge
print(judge(a3, a3))


