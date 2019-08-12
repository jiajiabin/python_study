# 字符串
str="abc我是 一个字符串"
echo $str

# 计算字符串长度
echo "长度是${#str}"

# 根据范围提取字符串 左闭右闭
echo "字符串的一部分是${str:1:6}"

# 查找字符串中字符的位置
echo `expr index "$str" 是我`

# echo `expr index "abc我是 一个字符串" 是我`

ret=`expr index "$str" 是我`
echo $ret


# 字符串关系运算符
a="abc"
b="bcd"
if [ $a = $b ]
then
	echo "相等"
fi

if [ $a != $b ]
then
	echo "不相等"
fi

if [ $a > $b ]
then 
	echo "大于"
elif [ $a < $b ]
then
	echo "小于"
else
	echo "等于"
fi










