# 循环
# for 和 c的结合
for ((i=0; i < 5; i++))
do 
	if ((i == 2))
	then
		continue
	fi
	
	echo "hello world!" $i
done

# 程序执行到for，首先执行i=0，然后判断i < 5，如果为真(非0为真)，则执行do和done之间的语句一次，然后执行i++ 然后再判断i<5, 为真，再执行do和done之间的语句一次，再执行i++,再判断i<5直到表达式为假

