# python中提供了丰富的判断字符串内容的方法，当然在实际工作中，几乎没什么用!
# 因为可悲的是这些判断函数，碰到中文就失效了

# 判断是否全是数字字符
ret = "123".isdecimal()
print(ret)

# 判断是否全是英语字母
ret = "abc".isalpha()
print(ret)

# 判断是否是只有英文和数字
ret = "abc123你".isalnum()
print(ret)

# 判断是否是全小写字母
ret = "abc".islower()
print(ret)

# 判断是否是全大写字母
ret = "ABC".isupper()
print(ret)

# 判断是否全是空格
ret = " ".isspace()
print(ret)

# 判断是标题 每个单词首字母大写  Hello World
ret = "Hello World".istitle()
print(ret)



# 自定义一个通用的判断字符串内容的函数
# 字符串s1的内容，全在s2当中，返回True
def isinstring(s1:str, s2:str):
    for i in s1:
        if i not in s2:
            return False
    return True

print(isinstring("123a", "0123456789"))
print(isinstring("abcER你", "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))


# 二次封装
def isinnum(s:str):
    return isinstring(s, "0123456789")

def isinalpha(s:str):
    return isinstring(s, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")




ret = input()
if isinstring(ret, "0123456789"):
    print(int(ret) + 1)


