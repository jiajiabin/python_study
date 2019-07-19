list1 = []
for i in range(10):
    a = float(input("打分："))
    list1.append(a)

max = max(list1)
min = min(list1)
list1.pop(list1.index(max))
list1.pop(list1.index(min))
print(list1)
sum = 0
for i in range(8):
    sum += list1[i]
sum /= 8
print(sum)

