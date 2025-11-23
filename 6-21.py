amount = int(input('Enter amount in PLN: '))
pln5 = 0
pln2 = 0
pln1 = 0
remainder = 0
while amount>4:
    amount -= 5
    pln5+=1
while amount>1:
    amount -=2
    pln2+=1
while amount>0:
    amount-=1
    pln1+=1

print(f'{pln5} {pln2} {pln1}')


