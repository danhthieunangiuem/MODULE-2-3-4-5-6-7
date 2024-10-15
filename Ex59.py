#Logarit
import math
def log(a, x):
    return math.log(x) / math.log(a)
a=float(input('Enter a (a>0 and a!=1) :'))
x=float(input('Enter x (x>0) :'))
print(f'log{a}({x})=',log(a,x))
