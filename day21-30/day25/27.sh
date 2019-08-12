path="./dir"
if [ -d $path ]
then
	echo "是目录"
else
	echo "不是目录"
fi

if [ -e $path ]
then
	echo "存在"
else
	echo "不存在"
fi
