import math
#The area of triangle
def triangle(a,b,c):
    if (a<=0 or b<=0 or c<=0) or (a+b)<=c or (a+c)<=b or (b+c)<=a:
        return ('Invalid triangle')
    else:
        cv=a+b+c
        p=cv/2
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        return ('Area of triangle=',s)
a=float(input("Enter edge (a>0):"))
b=float(input("Enter edge (b>0):"))
c=float(input("Enter edge (c>0):"))
print(triangle(a,b,c))