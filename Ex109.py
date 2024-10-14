Op = float(input('Original price of fixed assets: '))
y = int(input('number of years of depreciation: '))
def calculate_depreciation(Op, y, transportation=0, installation=0):
    total_initial_cost = Op + transportation + installation
    Adr = total_initial_cost / y
    Mdr=Adr/12
    yearly_depreciation=[]
    accumulated_depreciation = 0
    for year in range(1, y + 1):
        accumulated_depreciation += Adr
        remain=total_initial_cost-accumulated_depreciation
        yearly_depreciation.append({
            "Year": year,
            "Annual Depreciation": Adr,
            "Monthly Depreciation": Mdr,
            "Accumulated Depreciation": accumulated_depreciation,
            "Remaining Value": remain
        })
    return yearly_depreciation
print(calculate_depreciation(Op,y))