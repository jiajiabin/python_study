# 打开一个文件读取文件中的内容
path = r'C:\Users\Ace\Desktop\武汉1902\day15\dir\1.txt'
file = open(path, 'r', encoding="GBK")

# 读取文件内容，生成字符串

# 全部读入
s = file.read()
print(s)
# 在文件操作中有一个虚拟的读写指针，记录着读写的进度，下次读写只能接着读写
# 重定向读写指针
file.seek(0)        # 参数是字节数
s = file.read()
print(s)

file.seek(0)
# 读取指定字节数
s = file.read(3)
print(s)
s = file.read(3)
print(s)

# 读取一行
file.seek(0)
s = file.readline()
print(s)

file.seek(0)
l = file.readlines(20)
# 参数还是字节数，但是读的时候整行读，如果参数到了第二行，就会取2行，到了第三行，就会读取前3行
# 如果不传参，仍然全部读取
print(l)

file.seek(0)
while True:
    s = file.read(3)
    print(s)
    if len(s) == 0:
        break


# 使用完文件需要关闭，如果程序执行结束，关不关也一样。
file.close()

