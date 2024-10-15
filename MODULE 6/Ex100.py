import math
def nested_sqrt(n):
    S = 0
    i=0
    for i in range(1,n):
        S = math.sqrt(2 + S)
        if i<=n: i+=1
    if i==n: return f'Sum S={S} '
n=int(input('Enter n:'))
print(nested_sqrt(n))