celc = int(input('celsius: '))
if celc > 35:
    print('it is extremely hot')
elif celc >30 and celc <36:
    print('it is hot')
elif celc >=15 and celc <=30:
    print('it is warm')
elif celc >=0 and celc <15:
    print('it is cold')
elif celc <0:
    print('warning, frost')