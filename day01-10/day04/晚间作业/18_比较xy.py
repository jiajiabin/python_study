import random
'''
x为0 - 99取一个数, y为0 - 199取一个数, 
如果x > y则输出x， 如果x等于y则输出
x + y，否则输出y
'''
x = random.random(0,99)
y = random.random(0,199)
if x > y:
    print("x =",x)
elif x == y:
    print("x + y",x + y)
else:
    print("y =",y)