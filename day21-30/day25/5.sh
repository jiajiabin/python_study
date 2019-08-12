# 关系运算符
# -eq 等于			equal
# -ne 不等于		not equal
# -gt 大于			great then
# -lt 小于			less then
# -ge 大于等于		great or equal
# -le 小于等于		less or equal

a=10
b=20

if [ $a -eq $b ]
then
	echo 相等
else
	echo 不相等
fi


if [ $a -ne $b ]
then
	echo 不相等
else
	echo 相等
fi


if [ $a -gt $b ]
then
	echo 大于
else
	echo 不大于
fi



