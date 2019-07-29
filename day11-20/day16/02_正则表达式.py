# 正则表达式，正则表达式是查找字符串，提取指定字符串片段的一种工具，可以实现字符串的模糊查找。
# 对解析网络数据，尤其爬虫数据有奇效。

# 首先认识三个函数
import re

ret = re.match("www", "www.baidu.com")      # 看后面字符串，是否以前面字符串开头
print(ret, ret.span(), ret.group())

ret = re.search("baidu", "www.baidu.com")   # 查找，找到第一个
print(ret, ret.span(), ret.group())

ret = re.findall("\.",  "www.baidu.com")     # 找到所有，返回列表
print(ret)


# 以上三个函数，找不到，都返回None
# 以上三个函数支持正则表达式