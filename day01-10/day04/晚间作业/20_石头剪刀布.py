import random
'''
石头剪刀布游戏
0表示石头,1表示剪刀,2表示布
​系统随机生成0 - 2之间的任意一个数,用户输入0 - 2中的任意一个数
​验证输赢
当用户赢了之后,问用户是否继续玩
输入yes为继续,no为退出
其他时要求重新输入yes或者no
【注意： 石头 > 剪刀           剪刀 > 布          布 > 石头】
0 - 1赢了    1 - 2赢了    2 - 0赢了
User_num - sys_num == -1 or user_num - sys_num == 2
User_num == sys_num
游戏继续的状态:
主要用户回答的是yes
就玩下去
'''

def bijiao(i,j):
    if i > j:
        if i == 2 and j == 0:
            return 0
        return 1
    elif i < j:
        if i == 0 and j == 2:
            return 1
        return 0
    if i == j:
        return 2
while 1:
    user_num = random.randint(0, 2)
    print("用户：", user_num)
    sys_num = random.randint(0, 2)
    print("系统：", sys_num)
    if bijiao(user_num ,sys_num) == 1:
        print("用户赢")
        zhiling = input()
        if zhiling == "yes":
            continue
        elif zhiling == "no":
            break
        else:
            print("请重新输入yes或者no")
    elif bijiao(user_num, sys_num) == 0:
        print("用户输")
        break
    else:
        print("平局")
        continue