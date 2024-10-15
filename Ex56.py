def calculate_avg(math, physics, chemistry):
    avg = (math + physics + chemistry) / 3
    return round(avg, 2)
math = float(input("Math Score: "))
physics = float(input("Physics Score: "))
chemistry = float(input("Chemistry Score: "))

average = calculate_avg(math, physics, chemistry)
print("Average score =", average)
