import  math
def ROI(r,c):
    return (r-c)/c
def investment(ROI):
    if ROI>=0.75:
        return 'Should invest'
    else: return 'Dont invest'
r=float(input('Enter Revenue:'))
c=float(input('Enter Cost:'))
print('ROI:',ROI(r,c))
print('==>',investment(ROI(r,c)))