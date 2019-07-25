a1 = 1  # 定义程序a1正在运行，用 1 表示
b1 = 1

def stop(course, status):
    if course == True and status == True:
        return True
    else:
        return False

def judge(course, status):
    if stop(bool(course), bool(status)):
        return False
    else:
        return True

Judge = judge
print(Judge(a1, b1))
print(Judge(Judge, Judge))


