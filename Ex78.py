#quarter check
def month(m):
    try:
        match m:
                case m if m in (1,2,3):
                    return f'{m} is in First Quarter'
                case m if m in (4,5,6):
                    return f'{m} is in Second Quarter'
                case m if m in (7,8,9):
                    return f'{m} is in Third Quarter'
                case m if m in (10,11,12):
                    return f'{m} is in Last Quarter'
                case _: return "Invalid"
    except: print('Invalid')
m=int(input("enter m:"))
print(month(m))