import re
# 其他

# | 多个字符串选1
ret = re.search("bad|good", "You are good!")
print(ret)
# | 的优先级最低

# python的re 提供了三个模式
# re.I模式 忽略大小写匹配
# re.S模式 单行模式
# re.M模式 多行模式
# 比如.*按说任何字符串，但是.是不能换行的。使用单行模式，则字符串中\n会被忽略。
# <p>
#   <a>XXXX</a>
#   <a>QQQ</a>
# </p>
ret = re.search("Mon|Tue|Wed|TUR|FIR|SAT|SUN", "Today is mon!", re.I)
print(ret)

s = """
<p>
    <a>XXXX</a>
    <a>QQQ</a>
</p>
"""
ret = re.search("<P>(.*)</P>", s, re.S | re.I)
print(ret.group(1))
print(re.S.value, re.I.value)

# 0001 0000      0000 0010  -> |  ->  0001 0010

# 下载模块 requests
# File->setting/Preference->Project->Project interpreter->MySpider->+号
# 搜索requests -> install package

