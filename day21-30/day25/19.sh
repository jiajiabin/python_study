# if语句

:<< good
if [ $1 -gt 5 ]
then
	echo 大于5
elif [ $1 -lt 5 ]
then
	echo 小于5
else
	echo 等于5
fi
good

if test $1 -gt 5
then
	echo 大于5
elif test $1 -lt 5
then
	echo 小于5
else
	echo 等于5
fi

