# Function for calculating the sum of the
# N first integers

def sumn(n):
    res = 0
    for i in range(1, n + 1):
        res +=i
    return res


print('The sum of the first 20 integers is', sumn(20))
print('The sum of the first 100 integers is', sumn(100))
