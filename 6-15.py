enter_ean = input('please enter ean (13 numb): ')
if enter_ean.isnumeric() and len(enter_ean) == 13:
    print('article number is correct')
    ean3 = int(enter_ean[:3])
    if ean3 == 590:
        print('article manufactured in Poland')

