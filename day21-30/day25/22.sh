# 循环
# for
array=(1 2 3 4 5)
for x in ${array[@]}
do
	echo hello world! $x
done

for x in 1 2 3 4 5 6
do 
	echo $x
done

for x in "a" "b" "c"
do 
	echo $x
done

for x in "a b c"
do 
	echo $x
done

