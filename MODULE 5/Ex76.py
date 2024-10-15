
def year_test(y):
    # Kiểm tra nếu năm âm hoặc bằng 0
    if y <= 0:
        raise ValueError("Năm không hợp lệ, phải là số dương lớn hơn 0.")
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def days_in_month(m, y):
    # Kiểm tra nếu tháng không hợp lệ
    if m < 1 or m > 12:
        raise ValueError("Tháng không hợp lệ, phải nằm trong khoảng từ 1 đến 12.")

    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        return 29 if year_test(y) else 28

def next_day(d, m, y):
    days_current_month = days_in_month(m, y)

    # Kiểm tra nếu ngày không hợp lệ
    if d < 1 or d > days_current_month:
        raise ValueError(f"Ngày không hợp lệ cho tháng {m}. Tháng này chỉ có {days_current_month} ngày.")

    # Tính toán ngày tiếp theo
    if d < days_current_month:
        return d + 1, m, y
    else:
        if m == 12:
            return 1, 1, y + 1
        else:
            return 1, m + 1, y


# Nhập dữ liệu từ người dùng
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

try:
    # Gọi hàm và in kết quả
    next_day_val, next_month_val, next_year_val = next_day(d, m, y)
    print(f'Ngày kế tiếp là: {next_day_val}/{next_month_val}/{next_year_val}')
except ValueError as e:
    print(e)