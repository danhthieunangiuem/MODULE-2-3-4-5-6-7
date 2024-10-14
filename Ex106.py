def multiplication_table():
    for i in range(1, 11):
        for j in range(2, 10):
            print(f"{j} * {i:2} = {j * i:2}", end="   ")
        print()  # Xuống dòng sau mỗi hàng

multiplication_table()
