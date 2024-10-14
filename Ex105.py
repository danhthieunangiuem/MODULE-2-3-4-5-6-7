while True:
    def p_number(n):
        count=0
        for i in range(1,n+1):
            if n%i==0: count+=1
            i+=1
        if count==2:
            return f'{n} is prime number'
        else: return f'{n} is not prime number'
    n = int(input('Input n:'))
    print(p_number(n))
    ask = input("Continue?(y/n):")
    if ask == "y":
        n = int(input('Input n:'))
        print(p_number(n))
    else:
        print('BYE')
    break
