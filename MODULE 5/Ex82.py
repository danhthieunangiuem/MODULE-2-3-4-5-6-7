
def price(e):
    if e<=50:
        return 1549
    elif e<=100:
        return 1600
    elif e<=200:
        return 1858
    elif e<=300:
        return 2340
    elif e<=400:
        return 2615
    else: return 2701
def electricity(e):
     return e*price(e)
n=input('Customer Name:')
g=input('Customer Group:')
e=float(input('Number of kWh used:'))
x=input('Do you use prepaid card meters:')
if x in ('yes','Yes','YES','yES',"YEs",'yeS','YeS'):
        print(f'Amount to be paid: {e*2271} VND')
else:
        print(f'Amount to be paid: {electricity(e)} VND')