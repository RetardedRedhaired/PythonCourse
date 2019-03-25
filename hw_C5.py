a = input('Please, enter string: ')
b = input('Please input substring: ')
c = []
le = len(a)
le0 = len(b)
for i in range (le - le0 + 1):
    if (a[i:i + le0] == b):
        c.append(i+1)
for i in c:
    print(f'{i}', end = ' ')
