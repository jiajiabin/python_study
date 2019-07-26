import os
import shutil

# 获取一个目录下的所有文件和文件夹
path = r'C:\Users\Ace\Desktop\武汉1902\day15'
# 字符串前面加一个r，表示所有的字符串中的字符，都不是转义字符或格式符
# 从盘符(Linux或unix是根目录开始)开始写的路径（文件所在的位置）是绝对路径，从当前py文件所在目录开始写的路径是相对路径。

# 返回值是一个列表，列表中是该文件夹（目录）下的所有的文件或文件夹的名字。不包括子文件夹下还有其他文件。
ls = os.listdir(path)
print(ls)

# 判断路径下，是否存在某个文件或文件夹，文件名和路径，大小写不敏感
ret = os.path.exists(path + r"\Video")
print(ret)

path += r"\video"
# 判断指定路径下文件，到底是文件还是文件夹
if os.path.isdir(path):
    print("是文件夹")
elif os.path.isfile(path):
    print("是文件")


# 在指定目录下创建一个文件夹
path += r"\dir"
# os.makedirs(path)

# 删除文件
path += r"\1.txt"
# os.remove(path)
# 删除文件夹
path = path[:-6]
# os.removedirs(path)
print(path)

path = r'C:\Users\Ace\Desktop\武汉1902\day15\video\day15_01.wmv'
# 获取文件大小
print(os.path.getsize(path))

# 复制一个文件
# shutil.copyfile(path, path + 'b')

# 修改一个文件的名字
# os.renames(path + 'b', path + "-copy")

path = r'C:\Users\Ace\Desktop\武汉1902\day15\video'
# 移动一个文件
shutil.move(path + r'\file.wmv', path + r"\..\file.wmv")
# ..表示上一级目录




