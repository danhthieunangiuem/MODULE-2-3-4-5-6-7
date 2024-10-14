#BMI
import math
def BMI(h,w):
    return round((w/(h*h)),1)
def Classify(BMI):
    if BMI<18.5: print('Thin')
    elif (18.5<=BMI<=24.9):return ('Normal')
    elif (25<=BMI<=29.9): return ('Slightly Fat')
    elif (30<=BMI<=34.9): return ('Obesity level 1')
    elif (35 <= BMI <= 39.9):return ('Obesity level 2')
    elif (40 <= BMI):return ('Obesity level 3')
def Risk_of_diease(BMI):
    if BMI<18.5: return 'Low'
    elif BMI<=24.9: return 'Normal'
    elif BMI<=34.9: return 'High'
    elif BMI<=34.9: return 'High'
    elif BMI<=39.9: return 'Very High'
    else: return 'Danger'
h=float(input('Height(m):'))
w=float(input('Weight(Kg):'))
BMI=BMI(h,w)
print('Your BMI:',BMI)
print('Classify:',Classify(BMI))
print('Risk of Disease',Risk_of_diease(BMI))