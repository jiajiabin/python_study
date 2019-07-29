import re
# 正则表达式的分组

# 我们可以对正则表达式搜索的内容进行分组
# ()表示分组
# 从字符串中找出区号和座机号
ret = re.search("\[(([0-9]{3,4})-([0-9]{8}))\]", "我的电话是[027-89708790]")
print(ret)
print(ret.group())
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))
# 分组原则
# 1.由外而内，由左而右
# 2.最外一层不用加括号，自动一组group(0)
#  ret.group() 相当于 ret.group(0)


# 非捕获性分组
pattern = "(?:.+省)(.+市)(.+区)(.*)"
ret = re.search(pattern, "湖北省武汉市江夏区光谷大道")
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))


# 给分组加标题
pattern = "(?P<省>.+省)(?P<市>.+市)(?P<区>.+区)(?P<详细地址>.*)"
ret = re.search(pattern, "湖北省武汉市江夏区光谷大道")
print(ret.group("省"))
print(ret.group("市"))
