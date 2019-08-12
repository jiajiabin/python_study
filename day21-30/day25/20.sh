# 循环
# while
a=5
:<< !
while [ $a -gt 0 ]
do
	echo "hello world!"
	# a=`expr $a - 1`
	((a--))
	# a -= 1
done
!

:<<!
while ((a > 0))
do 
	echo "hello world"
	((a--))
done
!

# while ((a > 0));do echo "hello world";((a--));done

while ((a > 0));do
	echo "hello world"
	((a--))
done





 

