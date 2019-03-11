s = input('enter s: ')
t = input('enter t: ')
l = len(s)
k = 0
for i in range (l):
    if s[i] != t[i]:
        k = k + 1
print(f'distance is {k}')
