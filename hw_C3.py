a = input('Please, enter string: ')
b = a.split()
c = len(b[0])
for i in b:
    if (len(i) < c):
        c = len(i)
print(c)
