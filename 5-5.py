###
# Sums numbers entered by user
#
total_sum = 0
total_numbers = 0
arithmetic_mean = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    total_numbers+=1
    arithmetic_mean = total_sum/total_numbers
print(f"The total sum of the numbers is: {total_sum}, arithmetic mean is: {arithmetic_mean}")