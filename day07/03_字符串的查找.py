# 在一段字符串中查找某个子串是否出现，在什么位置？ 重要

# in 和 not in
if "hell" in "hello world!":
    print("地狱你好!")


# 判断一个字符串，是否以一个子串开始
ret = "Hello world".startswith("Hello")
print(ret)
# 判断一个字符串，是否以一个子串结束
ret = "Hello world".endswith("world")
print(ret)


# 斗球少年

# 查找位置
s = "零一二三四五六七八九十八"
ret = s.find("八")
# 如果找不到，返回一个负数
print(ret)

ret = s.find("八", 4, 9)     # 规定了查找8的范围左闭右开区间
print(ret)

ret = s.rfind("八")          # 从右向左找，找到第一个就停
print(ret)

ret = s.rfind("八", 4, 9)
print(ret)


# index函数和find几乎一样
ret = s.index("八")
# 如果找不到，抛出异常，如果不处理异常，程序崩溃
print(ret)

ret = s.index("八", 4, 9)
print(ret)

ret = s.rindex("八")
print(ret)

ret = s.rindex("八", 4, 9)
print(ret)