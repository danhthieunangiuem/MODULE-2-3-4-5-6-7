import math
#calculate +,-,*,/
a=float(input('Enter a='))
o=input('Enter operation (+,-,*,/):')
b=float(input('Enter b='))
if o=='+':
    print(f'{a}+{b}={a+b}')
elif o=='-':
    print(f'{a}-{b}={a-b}')
elif o=='*':
    print(f'{a}*{b}={a*b}')
elif o=='/':
    print(f'{a}/{b}={a/b}')