a=0
b=1
fibonaccilist=[a, b]
for i in range (1, 11):
    c=a+b
    fibonaccilist.append(c)
    a=b
    b=c
print('The fibonacci numbers are', fibonaccilist)