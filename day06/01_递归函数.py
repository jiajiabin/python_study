# 函数递归，可以解决循环能做的所有事，思路比循环更直接，更清晰。
# 打印5个helloworld

# 步骤
# 1.递归函数必须有一个临界值，即无需计算，就能直接返回的值。
# 2.找出，传参为n，和传参为n-1，该函数的关系
# 3.假设当前函数已经可以使用，调用自身，求出传参为n-1的结果，再计算除传参为n的结果

def print_n_hello_world(n):
    if n == 0:
        return
    print_n_hello_world(n - 1)
    print("hello world!")

print_n_hello_world(5)

# 计算1+2+3+。。。+100的和
def count(n):
    if n == 1:
        return 1
    return count(n - 1) + n

print(count(100))


# 传入 n,m 如n==4， m==3则求  3 + 33 + 333 + 3333
def count_num(n, m):
    if n == 0:
        return 0

    s = 0
    for i in range(n):
        s += m * 10 ** i

    return count_num(n - 1, m) + s

print(count_num(4, 1))










