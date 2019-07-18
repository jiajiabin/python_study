"""
输入一个数打印图形
输入5
打印
    *
   * *
  *   *
   * *
    *
"""
def pattern(num1):
    print(" " * (num1 // 2 + 1), "*")
    for i in range(1, num1 // 2 + 1):
        print(" " * (num1 // 2 - i + 2), "*", " " * (2 * i - 1), "*", sep="")
    for i in range(1, num1 // 2):
        print(" " * (i + 2), "*", " " * (num1 - num1 % 2 - 2 * i - 1), "*", sep="")
    print(" " * (num1 // 2 + 1), "*")


pattern()
