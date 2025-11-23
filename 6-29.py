n = int(input('Enter number of primes: '))
for num in range(2,n):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
