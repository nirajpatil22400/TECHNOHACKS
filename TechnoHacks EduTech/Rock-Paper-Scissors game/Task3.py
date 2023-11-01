import random

# Step 1: Define the choices for the game
choices = ["rock", "paper", "scissors"]

# Step 2: Get user's choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Step 3: Generate a random choice for the computer
computer_choice = random.choice(choices)

# Step 4: Determine the winner
if user_choice in choices:
    print(f"You chose {user_choice}")
    print(f"The computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")

# Explanation:
# 1. We define the possible choices (rock, paper, scissors) in a list.
# 2. We prompt the user to input their choice and convert it to lowercase.
# 3. The computer's choice is generated randomly using the random.choice function.
# 4. We compare the user's and computer's choices to determine the winner:
#    - If they're the same, it's a tie.
#    - If the user's choice beats the computer's choice, the user wins.
#    - If the computer's choice beats the user's choice, the computer wins.
#    - If the user inputs an invalid choice, we provide an error message.

# This code will let the user play Rock, Paper, Scissors against the computer.
