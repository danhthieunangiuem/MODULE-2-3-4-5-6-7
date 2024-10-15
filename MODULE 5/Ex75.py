#Number word form in English (*)
def read_number(n):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "ten","twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if n==0: return 'Zero'
    elif n<10:
        return (units[n])
    elif n==11: return ('eleven')
    elif n==12: return ('twelve')
    elif 12<n<100:
        ten_digit = n // 10
        unit_digit = n % 10
        if unit_digit==5 and ten_digit==1:
            return ('fifteen')
        elif unit_digit>2 and ten_digit==1:
            return (f"{ units[unit_digit]}teen")
        else: return (f'{tens[ten_digit]} {units[unit_digit]}')
    else: return ('Number out of range')
n=int(input('Enter number:'))
print(read_number(n))