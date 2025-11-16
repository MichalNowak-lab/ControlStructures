dog_age = int(input('Enter dogs age: '))
if dog_age<=2:
    print(f'The dogs age in dogs years is {dog_age*10.5} years')
elif dog_age>2:
    dog_age1 = dog_age - 2
    print(f'the dogs age in dogs years is {dog_age1*4+2*10.5} years')