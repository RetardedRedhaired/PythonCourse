t = input('enter string: ')
l = len(t)
u = ''
for i in range (l):
    #u = u + t[l-1-i]
    if t[l-1-i] == 'A':
        u = u + 'T'
    elif t[l-1-i] == 'T':
        u = u + 'A'
    elif t[l-1-i] == 'C':
        u = u + 'G'
    elif t[l-1-i] == 'G':
        u = u + 'C'
print(f'new string is: {u}')
