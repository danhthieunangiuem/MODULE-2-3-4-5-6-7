x=int(input("Input x:"))
n=int(input("Input n:"))
s=x
for i in range(1,n+1):
    mu=2*i+1
    tu=x**mu
    mau=1
    for j in range(1,mu+1):
        mau= mau*j
    s=s+(tu/mau)
print("s({0},{1})={2}".format(x,n,s))
