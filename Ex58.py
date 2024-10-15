import math
print('Coordinate point of A(xA,yA)')
xA=float(input('xA:'))
yA=float(input('yA:'))
print('Coordinate point of B(xB,yB)')
xB=float(input('xB:'))
yB=float(input('yB:'))
dAB=math.sqrt(((xB-xA)**2)+((yB-yA)**2))
print('The distance between A and B :',dAB)