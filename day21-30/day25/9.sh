# 判断字符串的一些其他运算符
a=""
if [ -z $a ]
then
	echo "字符串为空"
fi

if [ -n "$a" ]
then
	echo "n字符串不为空"
fi

if [ $a ]
then
	echo "字符串不为空"
fi
