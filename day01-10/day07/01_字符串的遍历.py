s = "天生我才必有路，Sky born me must have road!"
# python的字符串默认使用UTF-8编码格式，这个编码是linux，unix
# 也就是主流服务器和网络数据传输公认的通用的格式
# 特点是每个字符占用内存空间不一样大，但都是1个字符，比如一个中文3字节，一个英文1字节。
# 但切片时都认为是1个字符。

# 求字符串的长度
l = len(s)
print(l)
l = len("abc")
print(2)

# 遍历字符串的每一个字符
for i in range(len(s)):
    print(s[i], end="")

print("\n===============================")

for i in s:
    print(i, end="")

print("\n===============================")

# 隔一个遍历一个
for i in range(0, len(s), 2):
    print(s[i], end="")

print("\n===============================")

for i in s[::2]:
    print(i, end="")

# 逆序遍历
print("\n===============================")
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")

print("\n===============================")
for i in s[::-1]:
    print(i, end="")
print()


# 随机找出部分字符
import random
# 随机找出字符中的一个字符
c = random.choice("abcdefg")
print(c)        # character
# 随机找出字符串中多个字符
x = random.sample("abcdefg", 3)
print(x)




