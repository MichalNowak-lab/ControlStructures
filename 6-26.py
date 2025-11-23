pin = '0805'

attemps = 0
while attemps <3:
    enter = input('Enter pin: ')
    if enter != pin:
        attemps+=1
        print('incorrect...')
    else:
        break
if attemps >=3:
    print('Sorry, your payment card has been blocked')