def reverse_number(n):
    hundreds = n // 100
    tens = (n % 100) // 10
    ones = n % 10
    reversed_num = ones * 100 + tens * 10 + hundreds
    return reversed_num
number = int(input("Enter a 3-digit positive integer: "))
if 100 <= number <= 999:
    reversed_num = reverse_number(number)
    print(f"The reverse of {number} is {reversed_num}")
else:
    print("The number entered is not a 3-digit integer.")
