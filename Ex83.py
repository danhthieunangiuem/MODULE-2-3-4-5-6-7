def cost_of_living(a,b,c):
    if b-a<=0: return f'Invalid'
    elif b-a<=50*c:return f'Amount to be paid: {(b-a)*1484}'
    elif b-a<=100*c: return f'Amount to be paid: {(50*c+1484)+((b-a)-50*c)*1533}'
    elif b-a<=200*c: return f'Amount to be paid: {(50*c*1484) + (50*c*1533) + ((b-a) - 100*c) * 1786}'
    elif b-a<=300*c: return f'Amount to be paid: {(50*c*1484) + (50*c*1533) + (100*c*1786) + ((b-a) - 200*c) * 2242}'
    elif b-a<=400*c:
        return f'Amount to be paid: {(50*c*1484)+(50*c*1533)+(100*c*1786)+(100*c*2242)+((b-c)-300*c)*2503}'
    else: f'Amount to be paid: {(50*c*1484) + (50*c*1533) + (100*c*1786) + (100*c*2242) + (100*c*2503) +
((b-a)-400*c) * 2587}'
def business(a,b):
    if b - a <= 0: return f'Invalid'
    else: return f'Amount to be paid: {(b-a)*2320}'
def production(a,b):
    if b - a <= 0: return f'Invalid'
    else: return f'Amount to be paid: {(b-a)*1518}'
a=float(input('Old kWh number:'))
b=float(input('New kWh number:'))
c=float(input('Number of households sharing the same electricity meter:'))
def x():
    num=int(input('Laddered cost of living:1\nBusiness electricity:2\nProduction electricity:3\nEnter number:'))
    match num:
        case 1: print(cost_of_living(a,b,c))
        case 2: print(business(a,b))
        case 3: print(production(a,b))
        case _: print('Invalid')
x()