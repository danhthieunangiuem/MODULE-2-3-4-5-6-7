n=int(input('n'))
def shape1(n):
    for i in range(0,n):
        for j in range(0,n):
            if j==0 or j==n-1 or i==0 or i==n-1:
                print('*',end='  ')
            else:
                print(" ",end='  ')
            j=j+1
        print()
        i=i+1
print(shape1(n))
def shape2(n):
    for i in range(0,n):
        for j in range(0,n):
            if j==n-1 or i==n-1 or j==n-i or j==n-i+1 or j==n-i+2 or j==n-i-1:
                print('*',end='  ')
            else:
                print(" ",end='  ')
            j=j+1
        print()
        i=i+1
print(shape2(n))
def shape3(n):
    for i in range(0, n):
        for j in range(0, n):
            if j==i  or i<=(n//2) and j==0  or i==n//2 or i>(n//2) and j==n-1 :
                print('*',end='  ')
            else:
                print(" ",end='  ')
            j=j+1
        print()
        i=i+1
print(shape3(n))