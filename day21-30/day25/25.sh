# 函数
func(){
	echo "hello world!"
}

# 调用函数
func


add(){
	return `expr $1 + $2`
}

add 5 6

echo $?

add 4 7
ret=$?

echo $ret

