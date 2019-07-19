"""
3.编写函数，传入一个字符串，打印如下图形：
传入：ABCDE
打印:
    A
   BAB
  CBABC
 DCBABCD
EDCBABCDE
"""


def print_pattern(str):
    str1 = str
    for i in range(1, len(str1) + 1):
        print(" " * (len(str) - i), str1[(i - 1):0:-1], str1[0:i], sep="")


print_pattern("ABCDEG")
