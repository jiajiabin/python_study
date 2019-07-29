import re
# 关于字符的数量
# {n}表示前面的字符，应该有n个
# {3,}表示前面的字符，最少是3个
# {,5} 表示前面的字符，不超过5个
# {3,5} 表示前面字符个数为3-5个
ret = re.search("Wo{3}w", "I said Wooow!")
print(ret)
ret = re.search("Wo{3,}w", "I said Wooooooow!")
print(ret)
ret = re.search("Wo{,5}w", "I said Wooooow!")
print(ret)
ret = re.search("Wo{3,5}w", "I said Woow, Woooooow, Wooooow!!")
print(ret)


# ?表示前面字符个数为{0,1}
# +表示前面字符个数为{1,}
# *表示前面字符个数为{0,}
ret = re.search("colou?r", "I love this colour!!")
print(ret)
ret = re.search("Wo+n", "Won! said the dog!")
print(ret)
ret = re.search("cla*s{1,2}", "cls is class, or claaaass")
print(ret)
