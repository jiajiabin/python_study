#1！+2！+3！+4!+5!+6! = ?
m = 4
sum = 0
for i in range(1,m+1):
    n = 1
    for j in range(1,i+1):
        n *= j
    sum += n
print(sum)