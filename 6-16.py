###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')
selected = ''
if program == 'j':
    total_washing_time+=40
    selected = 'jacket'
elif program == 'u':
    total_washing_time+=70
    selected = 'underwear'
elif program == 's':
    total_washing_time+=20
    selected = 'shoes'
if extra_rinse == 'y':
    total_washing_time+=15
else:
    extra_rinse = False
if extra_spin == 'y':
    total_washing_time+=9
else:
    extra_spin = False
print(f'product "{selected}"')
print(f'rinse {extra_rinse}')
print(f'spin {extra_spin}')
print(f'Total washing time {total_washing_time}')