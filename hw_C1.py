a = input('Enter with spaces: ')
b = a.split()
for i in range (len(b)-1):
    if (b[i+1]>b[i]):
        print(b[i+1], end = ' ')
