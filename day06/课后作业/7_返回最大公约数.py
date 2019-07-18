# 2.编写不定长参数函数，传入n个正整数，返回最大公约数


def common_divisor(*args):
    common_divisor1 = None
    min1 = min(*args)
    for i in range(2, min1 + 1):
        for j in args:
            if j % i != 0:
                break
            elif j == args[-1] and j % i == 0:
                common_divisor1 = i
    return common_divisor1


print(common_divisor(32, 8, 16))
