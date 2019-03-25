import math
a = input('Please, enter a, b and c separated by spaces(example: 1 2 4): ')
b = a.split()
d = int(b[1])*int(b[1]) - 4*int(b[0])*int(b[2])
if (d < 0):
    x1 = complex(-int(b[1])/2*int(b[0]), math.sqrt(abs(d))/2*int(b[0]))
    x2 = complex(-int(b[1])/2*int(b[0]), -1*math.sqrt(abs(d))/2*int(b[0]))
else:
    x1 = (-int(b[1]) + math.sqrt(d))/2*int(b[0])
    x2 = (-int(b[1]) - math.sqrt(d))/2*int(b[0])
print(f'x1 = {x1}, x2 = {x2}')
