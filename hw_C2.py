a = input('Please, enter number: ')
b = 0
c = 1
for i in a:
    b += int(i)
    c = c*int(i)
print(f'Sum of digits is {b}, multiple of digits is {c}')
