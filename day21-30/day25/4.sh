# 运算符
# 算术运算符
# 【注】其实shell没有属于自己的算术运算符，或者说shell本身不支持数学运算
# 但是shell可以调用系统命令 因此可以通过系统命令进行运算

ret=`date`

echo 结果是$ret

# 整型算术运算符通过expr实现
a=10
b=20
echo `expr 10 + 20`
ret=`expr 10 + 20`

echo `expr $a + $b`
ret=`expr $a + $b`
echo $ret

echo `expr $a - $b`
echo `expr $a \* $b`		# 乘法必须用转义字符
echo `expr $a / $b`			# 整数相除，结果也是整数
echo `expr $a % $b`

# 浮点数运算
echo "4.5*2.81234" | bc
echo "scale=6; 4.5/2.81234" | bc
# scale是仅用于除法保留几位小数

# 在shell编程当中，下列字符仅能用于整数运算，而且，算是算术运算符
echo $[$a == $b]
echo $[$a != $b]
echo $[5 != 7]










