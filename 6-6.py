parked_hours = int(input('Enter number of hours the car was parked: '))
if parked_hours<=2 and parked_hours>=1:
    print('5 pln')
elif parked_hours<=6 and parked_hours>=3:
    print('15 pln')
elif parked_hours>6:
    print('20 pln')