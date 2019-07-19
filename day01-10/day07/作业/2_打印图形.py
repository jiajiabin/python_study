"""
编写函数传入一个字符串，打印如下图形
传入 abcdefg
打印
abcdefg
     f
    e
   d
  c
 b
abcdefg
"""


def pattern(str1):
    print(str1)
    for i in range(2, len(str1)):
        print(" " * (len(str1) - i), str1[len(str1) - i], sep="")
    print(str1)


pattern("abcdefg")
