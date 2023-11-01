# Define initial balance
initial_balance = 1000

# Create a dictionary to store user accounts with PIN and balance
user_accounts = {
    "1234": {
        "name": "John Doe",
        "pin": "1234",
        "balance": initial_balance,
        "transaction_history": []
    },
    "5678": {
        "name": "Jane Smith",
        "pin": "5678",
        "balance": initial_balance,
        "transaction_history": []
    }
}

# Function to check balance


def check_balance(account):
    balance = account["balance"]
    print(f"Hello, {account['name']}, your account balance is ${balance}")

# Function to deposit money


def deposit(account):
    deposit_amount = float(input("Enter the amount you want to deposit: $"))
    if deposit_amount > 0:
        account["balance"] += deposit_amount
        account["transaction_history"].append(f"Deposited ${deposit_amount}")
        print(f"${deposit_amount} has been successfully deposited.")
    else:
        print("Invalid deposit amount. Please enter a positive value.")

# Function to withdraw money


def withdraw(account):
    withdraw_amount = float(input("Enter the amount you want to withdraw: $"))
    if withdraw_amount > 0 and withdraw_amount <= account["balance"]:
        account["balance"] -= withdraw_amount
        account["transaction_history"].append(f"Withdrew ${withdraw_amount}")
        print(f"${withdraw_amount} has been successfully withdrawn.")
    elif withdraw_amount > account["balance"]:
        print("Insufficient balance. Withdrawal failed.")
    else:
        print("Invalid withdrawal amount. Please enter a positive value.")

# Function for PIN verification


def verify_pin():
    entered_pin = input("Please enter your 4-digit PIN: ")
    if entered_pin in user_accounts:
        return user_accounts[entered_pin]
    else:
        print("Invalid PIN. Please try again or contact your bank.")


# Main ATM simulation loop
while True:
    print("\nWelcome to the ATM Simulator")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Quit")

    choice = input("Please select an option (1/2/3/4/5): ")

    if choice == '1':
        user_account = verify_pin()
        if user_account:
            check_balance(user_account)
    elif choice == '2':
        user_account = verify_pin()
        if user_account:
            deposit(user_account)
    elif choice == '3':
        user_account = verify_pin()
        if user_account:
            withdraw(user_account)
    elif choice == '4':
        user_account = verify_pin()
        if user_account:
            print("Transaction History:")
            for transaction in user_account["transaction_history"]:
                print(transaction)
    elif choice == '5':
        print("Thank you for using the ATM Simulator. Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option (1/2/3/4/5).")

# End of the program
