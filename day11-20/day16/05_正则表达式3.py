import re
# 表示起始和结尾

# ^表示字符串的起始
# $表示字符串的结尾
# \A表示字符串起始
# \Z表示字符串结束
ret = re.search("^good", "good morning!")
print(ret)
ret = re.search("good$", "Very good")
print(ret)
ret = re.search("^good$", "good")
print(ret)


# 练习
# 1.输入一个字符串，判断字符串是否是手机电话号码？
def is_phone_num(num):
    ret = re.search("^1[3-9][0-9]{9}$", num)
    return ret != None

s = input()
print(is_phone_num(s))

