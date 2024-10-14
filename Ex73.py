'''Giải phương trình bậc 2'''
import math
def gptb2(a,b,c):
    DT = b * b - 4 * a * c
    if a==0:
        if b==0:
            if c==0: return 'Infinite Solution'
            else: return 'No Solution'
        else: return -c/b
    if DT<0: return 'No Solution'
    elif DT==0: x=-b/(2*a); return f'Double solution x={x}'
    else:
        x1=((-b+math.sqrt(DT))/2*a)
        x2=((-b-math.sqrt(DT))/2*a)
        return f'x1={x1},x2={x2}'
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
print(gptb2(a,b,c))