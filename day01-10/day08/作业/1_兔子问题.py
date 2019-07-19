# 兔子问题？
# 已知第一月有一对兔子，兔子长到第三个月会生一对兔子，
# 这对儿涨到第三个月也会开始生兔子
# 假设兔子都不死，问第n月共有多少兔子
def rabbit(num1):
    litter_rabbit = 1
    big_rabbit = 0
    grow_rabbit = 0
    for i in range(num1-1):
        grow_rabbit += big_rabbit
        big_rabbit = litter_rabbit
        litter_rabbit = grow_rabbit
    return (grow_rabbit + litter_rabbit + big_rabbit)*2

print(rabbit(8))