#Find the day after
d = int(input("Enter day: "))
m = int(input("Enter month: "))
y = int(input("Enter year: "))
def year_test(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    else: return False
def days_in_month(m,y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m==2:
        return 29 if year_test(y) else 28
def next_day(d,m,y):
    days_current_month=days_in_month(m,y)
    if d<days_current_month:
        return d+1,m,y
    else:
        if m==12:
            return 1,1,y+1
        else: return 1,m+1,y
next_day_val, next_month_val, next_year_val = next_day(d, m, y)
print(f'The next day is:{next_day_val}/{next_month_val}/{next_year_val}')