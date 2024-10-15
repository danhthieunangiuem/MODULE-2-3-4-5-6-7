import math
def perimeter(r):
    p = 2 * math.pi * r
    return p
def area(r):
    S = math.pi * r ** 2
    return S
r=float(input('radius:'))
if perimeter(r)>=0 and area(r)>=0:
        print('Area:',area(r))
        print('Perimeter:',perimeter(r))
else:   print('Error!')
