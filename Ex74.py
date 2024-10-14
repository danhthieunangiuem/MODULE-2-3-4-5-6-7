#Number word form(*)
def read_number(n):
    units = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    tens = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    if n==0: return 'Không'
    elif n < 10:
        return units[n]
    elif 10 <= n < 100:
        ten_digit = n // 10
        unit_digit = n % 10
        if unit_digit == 1 and ten_digit > 1:
            return f"{tens[ten_digit]} mốt"
        elif unit_digit == 5:
            return f"{tens[ten_digit]} lăm"
        else:
            return f"{tens[ten_digit]} {units[unit_digit]}"
    else:
        return "Number out of range"
n=int(input('Enter number:'))
print(read_number(n))