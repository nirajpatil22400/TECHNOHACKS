# Define initial balance
balance = 1000

# Function to check balance


def check_balance():
    global balance  # Access the global balance variable
    print(f"Your account balance is ${balance}")

# Function to deposit money


def deposit():
    global balance
    deposit_amount = float(input("Enter the amount you want to deposit: $"))
    if deposit_amount > 0:
        balance += deposit_amount
        print(f"${deposit_amount} has been successfully deposited.")
    else:
        print("Invalid deposit amount. Please enter a positive value.")

# Function to withdraw money


def withdraw():
    global balance
    withdraw_amount = float(input("Enter the amount you want to withdraw: $"))
    if withdraw_amount > 0 and withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"${withdraw_amount} has been successfully withdrawn.")
    elif withdraw_amount > balance:
        print("Insufficient balance. Withdrawal failed.")
    else:
        print("Invalid withdrawal amount. Please enter a positive value.")


# Main ATM simulation loop
while True:
    print("\nWelcome to the ATM Simulator")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")

    choice = input("Please select an option (1/2/3/4): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using the ATM Simulator. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option (1/2/3/4).")

# End of the program
