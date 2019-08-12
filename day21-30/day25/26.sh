# 函数
add(){
	n=$#		# 获取参数个数
	echo $n
	echo $@    	# 获取每一个参数

	s=0
	for x in $@	# "1" "2" "3" "4" "5" "6"
	do
		s=`expr $s + $x`
	done
	
	return $s
}

add 1 2 3 4 5 6
echo $?

