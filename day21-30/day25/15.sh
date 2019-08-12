# 格式化输出‘
# 随着时间的发展shell语言虽然不是储存数据和管理数据为目的的编程语言
# 但是渐渐兼容了一些c语言的语法，比如printf，以及c语言的格式符

a=10
b=1.5
c="hello world"
printf "%s %d %f\n" "$c" $a $b
printf "%04d %.2f\n" $a $b

