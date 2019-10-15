"""
19/04/2019
"""

with open('bill.csv', encoding='utf-8') as f:
    lines = f.readlines()

data_set = {}
for line in lines:
    code, qty, price, original_price = line.strip().split(',')
    qty = int(qty)
    price = int(price)
    original_price = int(original_price)
    sale = qty * price
    profit = qty * (price - original_price)

    if code not in data_set:
        data_set[code] = {
            'qty' : qty,
            'sale' : sale,
            'profit' : profit
        }
    else:
        acc_qty = data_set[code]['qty']
        acc_sale = data_set[code]['sale']
        acc_profit = data_set[code]['profit']
        data_set[code] = {
            'qty' : acc_qty + qty,
            'sale' : acc_sale + sale,
            'profit' : acc_profit + profit
        }

items = data_set.items()
items = sorted(items, key= lambda x : x[1]['sale'], reverse= True)

with open('output.csv','w', encoding='utf-8') as f:
    f.write('MH, Sl, Doanh so, Loi Nhuan\n')
    for code, acc in items:
        f.write(f'{code},{acc["qty"]}, {acc["sale"]}, {acc["profit"]}\n')