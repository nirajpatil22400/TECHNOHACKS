# Step 1: Print a welcome message to the user.
print("Welcome to the Temperature Converter!")

# Step 2: Define a function to convert Fahrenheit to Celsius.


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Step 3: Define a function to convert Celsius to Fahrenheit.


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Step 4: Create a while loop to keep the program running until the user decides to exit.
while True:
    # Step 5: Ask the user for input.
    print("\nOptions:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    # Step 6: Check the user's choice.
    if choice == '1':
        # Step 7: Get the temperature in Fahrenheit from the user.
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        # Step 8: Call the fahrenheit_to_celsius function to convert and print the result.
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == '2':
        # Step 9: Get the temperature in Celsius from the user.
        celsius = float(input("Enter temperature in Celsius: "))
        # Step 10: Call the celsius_to_fahrenheit function to convert and print the result.
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '3':
        # Step 11: Exit the program if the user chooses to quit.
        print("Thank you for using the Temperature Converter. Goodbye!")
        break
    else:
        # Step 12: Handle invalid input.
        print("Invalid choice. Please enter 1, 2, or 3.")
