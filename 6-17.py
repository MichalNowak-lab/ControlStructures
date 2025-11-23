from operator import index

time = input('Enter time(24-hour format): ')
splitinf = time.index(':')
if splitinf == 2:
    hours = int(time[:2])
    minutes = int(time[3:])
else:
    hours = int(time[:1])
    minutes = int(time[2:])


if hours > 12:
    hours -= 12
    print(f'Time in 12-hour format: {hours}:{minutes}pm')
else:
    print(f'Time in 12-hour format: {hours}:{minutes}am')