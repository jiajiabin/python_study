people = 30
money = 50
for i in range(31):
    for j in range(31 - i):
        if i * 3 + j * 2 + 30 - i - j == money:
            print("男人有%d人" % i, end="")
            print("女人有%d人" % j, end="")
            print("小孩有%d人" % (30 - i - j))
