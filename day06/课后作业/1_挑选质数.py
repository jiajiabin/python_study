# 1.声明一个函数, 可以接受任意个参数, 获得这些数据中的质数


def prime(*args):
    for a in args:
        if a is int:
            j = 0
            if a == 2:
                print(a, "是质数")
            if a == 1:
                print("1 既不是质数也不是合数")
            elif a > 2:
                for i in range(2, a):
                    if a % i == 0:
                        j = 1
                if j:
                    print(a, "不是质数")
                else:
                    print(a, "是质数")
            else:
                print(a, "不是正整数")
        else:
            print(a,"不是整数")

prime(1, 3, 5, 6, 7, 8, 9, )
