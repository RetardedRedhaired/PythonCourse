def prime(number):
    c = range(1, number)
    for a in c:
        if (math.factorial(a-1) + 1) % a == 0:
            yield a
            

for curr in prime(20):
    print(curr, end=' ')   
