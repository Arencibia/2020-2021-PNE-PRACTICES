a=0
b=1
fibonacciNums=[a, b]
for i in range (1, 11):
    c=a+b
    fibonacciNums.append(c)
    a=b
    b=c
print('The first 11 fibonacci numbers are', fibonacciNums)