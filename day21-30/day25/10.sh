# 数组
# 创建一个数组
array=(1 2 3 4 5)
echo ${array[@]}
echo $array
echo ${array[*]}


array2=${array[@]}
echo ${array2[@]}

array3=(1 2 3 "good" 5)
echo ${array3[@]}


# 取出数组的每一个元素
echo ${array[0]} ${array[1]} ${array[2]}


# 给数组添加元素
array[5]=6
array[7]=8

echo ${array[0]} ${array[1]} ${array[2]} ${array[5]} ${array[7]}

# 获取数组的长度
echo ${#array[@]}

