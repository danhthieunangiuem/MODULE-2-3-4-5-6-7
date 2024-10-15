def time(t):
    h=(t//3600)%24
    m=(t%3600)//60
    s=(t%3600)%60
    return [f'{h}:{m}:{s},AM',f'{h-12}:{m}:{s},PM'][h>12]
t=int(input('Second:'))
print(time(t))