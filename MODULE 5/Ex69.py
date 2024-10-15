#Leap year test
def test(y):
    if (y%4==0 and y%100!=0) or y%400==0:
        return True
    return False
y=int(input('Enter year:'))
if test(y)==True: print(y,"is a leap year")
else: print(y,'is not a leap year')
test(y)