### DO DOKOŃCZENIA
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Check pin")
    print("6. Change pin")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        while True:
            userinput = input('input 0 to exit: ')
            if userinput == pin and userinput.isdigit():
                print('pin you entered is correct')
            else:
                print('print you entered is incorrect')
            if int(userinput) == 0:
                break
    elif choice == '6':
        pin_correct = False
        while pin_correct == False:
            new_pin = input('Enter new pin: ')
            new_pin_len = len(new_pin)
            if new_pin_len == 4 and new_pin.isdigit():
                pin = new_pin
                pin_correct = True
            else:
                print("Pin has to be 4 characters long and must consist of only numbers")
    else:
        print("Invalid option. Please try again.")