# 打开文件写入数据
path = r'C:\Users\Ace\Desktop\武汉1902\day15\dir\1.txt'
file = open(path, "w", encoding="GBK")
# 这样打开文件，会将数据全部清空，重写文件
file.write("我是一个粉刷匠！")

file.write(str([1, 2, 3, 4]))

file.close()