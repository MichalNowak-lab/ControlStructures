compsci = input('SURVEY Are you interested in computer science? (y/n): ')
games = input('Do you like playing computer games? (y/n): ')
insta = input('Do you have an Instagram account? (y/n): ')
if compsci == 'n':
    compsci = 'No'
else:
    compsci = 'Yes'

if games == 'n':
    games = 'No'
else:
    games = 'Yes'

if insta == 'n':
    insta = 'No'
else:
    insta = 'Yes'
print(f'SURVEY RESULTS Interested in computer science: {compsci}')
print(f'Playing computer games: {games}')
print(f'Has an Instagram account: {insta}')