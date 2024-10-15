#Count the number of days in a month
def month(m):
    if m in (1,3,5,7,8,10,12):
        return f'{m} has 31 days'
    elif m in (4,6,9,11):
        return f'{m} has 30 days'
    elif m==2:
        year = int(input("Enter year:"))
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return f'{m} has 29 days'
        else:
            return f'{m} has 28 days'
    else:
        return f'{m} is not valid'
m=int(input('Enter a month:'))
print(month(m))