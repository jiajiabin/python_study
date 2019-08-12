# 布尔运算符
# 表示 与或非的关系
# !表示非
echo $[!0]
echo $[!1]

a=10
if [ $[!$[a == 10]] -eq 0 ]
then
	echo good
fi

# -o 表示或
if [ $a -eq 10 -o $a -gt 5 ]
then
	echo good
fi

# -a 表示与
if [ $a -eq 6 -a $a -lt 12 ]
then
	echo less
fi

# 逻辑运算符
# && 与，用法和-a相同
if [[ $a -eq 10 && $a -gt 5 ]]
then
	echo equal
fi

# || 或 作用和-o相同
if [[ $a -eq 10 || $a -lt 5 ]]
then
	echo or
fi















