#abundant number
def abundant():
    sum=0
    for i in range(1,n):
        r=n%i
        if r==0:
            sum+=i
    if sum>n:
        return f'{n} is abundant number'
    else: return f'{n} is not abundant number'
n=int(input('Input n:'))
print(abundant())