# 循环
# until
a=5
until [ $a -le 0 ]
do
	echo "hello world!"
	((a--))
done


