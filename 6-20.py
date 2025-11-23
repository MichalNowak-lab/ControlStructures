number = int(input('enter number: '))
result = ''
while number > 0:
    result = str(number%2)+result
    number //=2

print(result)