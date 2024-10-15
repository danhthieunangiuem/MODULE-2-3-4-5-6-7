
def total(A,r,N):
    term=4*N
    for i in range((term)):
        A=A*(1+r/100)**3
        total=round(A,-3)
        return total
A=int(input('Input amount: '))
r=int(input('Input interest rate: '))
N=int(input('Input terms: '))
print(total(A,r,N))
