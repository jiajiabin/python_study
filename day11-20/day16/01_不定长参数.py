# 在python当中，不定长参数有两种表示形式
def print_ever_sth(* args):     # arguments
    # 传入任意个数参数，得到一个元组
    for i in args:
        print(i)


print_ever_sth(1, 2, 3, 4)


def print_All_sth(** kwargs):
    # 传入的不定个数参数，会获得一个字典
    print(kwargs)


print_All_sth(good=1, bad=2)


def print_sth(*args, **kwargs):
    print(args)
    print(kwargs)
    print(*args)
    print(**kwargs)



print_sth(1, 2, 3, k=9, w=10)
print_sth(1, 2, 3, 4)
print_sth(k=9, w=10)

