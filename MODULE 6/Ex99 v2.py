def fibo(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
n=int(input('Enter n:'))
if n==0: print('invalid')
else:
    print(fibo(n))
def fibo_list(n):
    for i in range(1,n+1):
        print(fibo(i),end=' ')
fibo_list(n)