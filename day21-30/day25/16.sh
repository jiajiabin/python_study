# 格式化输出，如果需要输出的数据多余格式符，且数据和格式符类型匹配，printf将被反复执行
# 直到，格式化输出完毕
a="abc"
b="efg"
c="hij"
d="klm"

printf "print: %s\n" $a $b $c $d

