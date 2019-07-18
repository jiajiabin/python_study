# 字符串拥有一些乱七八糟的转换函数，我们不妨看一下，重要性一般


# 小写转大写
s = "abcEF123".upper()
print(s)

# 大写转小写
s = "abcEF123".lower()
print(s)

# 单词转标题
s = "hello world!".title()
print(s)

# 单词转句子
s = "hello world!".capitalize()
print(s)

# 从字符两侧剔除特殊的符号或文字
s = "%我是单词%".strip("%")
print(s)

# 去除左右侧字符串或符号
s = "[[我是单词]]"
print(s)
s = s.lstrip("[[")
print(s)
s = s.rstrip("]]")
print(s)

# 将字符串补齐到指定长度
# --------------hello------------
# --------------good-------------
s = "good".center(50, "-")
print(s)
s = "hello".center(50, "-")
print(s)

s = "很高".center(25, "=")
print(s)
s = "还不错".center(25, "=")
print(s)



