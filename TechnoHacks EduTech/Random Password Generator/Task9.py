import random
import string


def generate_password(length):
    # Define characters for each category
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # Combine characters from all categories
    all_characters = letters + digits + special_characters

    # Ensure at least one character from each category
    password = random.choice(
        letters) + random.choice(digits) + random.choice(special_characters)

    # Generate the remaining characters
    password += ''.join(random.choice(all_characters)
                        for _ in range(length - 3))

    # Shuffle the characters to make the password random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password


# Input the desired password length from the user
password_length = int(input("Enter the desired password length: "))

# Generate and print the random password
password = generate_password(password_length)
print("Random Password: ", password)
