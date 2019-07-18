# 排序就是按照一定的规律将散乱的数据按照顺序排列
# 冒泡排序  选择排序  插入排序

# 插入排序的逻辑(从小到大为例)
# [5, 1, 2, 4, 3] []
# [1, 2, 4, 3]  -> [5]
# [2, 4, 3] -> [1, 5]
# [4, 3] -> [1, 2, 5]
# [3] -> [1, 2, 4, 5]
# [] -> [1, 2, 3, 4, 5]

def insert_sort(ls:list):
    n_ls = []                                       # [1, 5]
    for i in ls:                                    # i == 1
        for j in range(0, len(n_ls) + 1):           # j == 0
            # j是索引，如果j是新列表长度，则将新的元素插在最后
            # 如果n_ls[j]比需要插入的那个值大，就把那个值插在j的位置，原j位置和之后数据后移
            if j == len(n_ls) or n_ls[j] > i:       # n_lis[j] == 5 > 1
                n_ls.insert(j, i)                   # n_ls.insert(0, 1)
                break
    ls.clear()          # 清空
    ls.extend(n_ls)     # 导入

ls = [5, 1, 2, 4, 3]
insert_sort(ls)
print(ls)
