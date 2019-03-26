new = 1
teen = 0
eld = 0
n = int(input('Enter n: '))
k = int(input('Enter k: '))
for i in range (n-1):
    eld = eld + teen
    teen = new
    new = eld * k
print(f'vsego: {eld + teen + new}')
