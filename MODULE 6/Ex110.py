import math
def Probability():
    number_of_favorable_outcomes=(Sample-Recovered)*math.factorial(Sample-1)
    P=number_of_favorable_outcomes/math.factorial(Sample)
    return f'The probability that the last person selected is positive for COVID-19: {P}'
Sample=int(input('Enter number of people: '))
Recovered=int(input('Enter number of recovered people: '))
print(Probability())