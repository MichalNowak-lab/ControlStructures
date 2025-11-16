curr_prod = 140
prev_prod = 200
perc = (prev_prod - curr_prod)/prev_prod
percentage = perc*100
if percentage >= 10:
    print('buy the product!!')
    print(f'Product price reduced by {percentage}')