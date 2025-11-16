prod_purch = int(input('enter number of purchases: '))
prod_price = int(input('enter price: '))
total = 0
if prod_purch <=2:
    total = prod_price*prod_purch
    print(f'total is {total}')
elif prod_purch > 2:
    i=1
    total = 80
    while i <= prod_purch-2:
        total += prod_price*0.75
        i+=1
    print(f'total is {total}')