# 条件跳转语句
# case in

case $1 in
	1) echo "One"
	;;
	2) echo "Two"
	;;
	3) echo "Three"
	;;
	*) echo "Other"
	;;
esac
# $1 的值是多少，就跳到哪一个标签执行
