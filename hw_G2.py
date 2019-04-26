import math

def prime(n):
    if (math.factorial(n-1) + 1) % n == 0:
        return n
n = input('Enter last number:')
a = range(2, int(n))
a = list(filter(prime,a))
print(a)
