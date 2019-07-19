# 已知m个人，坐一列，报数，报道n，下一个人从1重新报。
# 凡是报道n的退出，问最后剩下的人是原来第几个人
def number_off(m:int,n:int):
    list1 = []
    for i in range(1,m+1):
        list1.append(i)
    while len(list1) != 1:
        index1 = n % len(list1) -1
        list1.pop(index1)
        list1 = list1[index1:]+list1[:index1]
    return list1[0]

print(number_off(78,2))

