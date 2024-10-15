def days_in_month(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31  # January, March, May, July, August, October, December
        case 4 | 6 | 9 | 11:
            return 30  # April, June, September, November
        case 2:
            return "28 or 29"  # February (can have 28 or 29 days depending on the leap year)
        case _:
            return "Invalid month"
month=int(input('Enter month: '))
print(days_in_month(month))