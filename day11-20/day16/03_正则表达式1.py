import re
# 关于单个字符的范围
# [ABC]表示该字符可以是ABC中任意一个
# [A-Za-z]表示该字符范围是所有字母
# [0-9]表示该字符范围是左右数字
# [A-Za-z0-9_]表示范围是标识符
ret = re.search("b[ae]d", "I am bad, I have a bed!")
print(ret)
ret = re.search("b[A-Ca-c]d", "I am bed, I have a bed!")
print(ret)
ret = re.search("[a-z][a-z][a-z]", "I am bad, I have a bed!")
print(ret)


# .表示任意字符，除了\n
# \w表示所有标识符字符
# \W表示所有的非标识符字符
# \s表示所有的不可见字符，例如空格，tab
# \S表示除了上述不可见字符
ret = re.search("b.d", "I am b?d, I have a bed!")
print(ret)
ret = re.search("b\wd", "I am b?d, I have a bed!")
print(ret)
ret = re.search("b\Wd", "I am b?d, I have a bed!")
print(ret)
ret = re.search("b\sd", "I am b d, I have a bed!")
print(ret)