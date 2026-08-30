import random

minimum_length = 10

print("\nRandom Password Generator\n")

print("This program will generate a random password for you.\n")

length = int(input(f"Please enter the desired length of your password (minimum {minimum_length} characters): "))

while not isinstance(length, int) or length < minimum_length:
    length = int(input(f"\nInvalid input. Please enter a valid integer greater than or equal to {minimum_length}: "))

require_number = input("\nDoes your password require a number? ([y]/n): ")

while require_number.lower() not in ['y', 'n', '']:
    print("\nInvalid input.")
    require_number = input("\nDoes your password require a number? ([y]/n): ")

if require_number.lower() == 'y' or require_number == "":
    require_number = True
elif require_number.lower() == 'n':
    require_number = False

require_special = input("\nDoes your password require a special character? ([y]/n): ")

while require_special.lower() not in ['y', 'n', '']:
    print("\nInvalid input.")
    require_special = input("\nDoes your password require a special character? ([y]/n): ")

if require_special.lower() == 'y' or require_special == "":
    require_special = True
elif require_special.lower() == 'n':
    require_special = False

message = "\nYour password will contain captial and lowercase letters"
choice_list = ['lower', 'upper']

if require_number and not require_special:
    message += ", and a number."
    choice_list.append('number')
elif require_special and not require_number:
    message += ", and a special character."
    choice_list.append('special')
elif require_number and require_special:
    message += ", a number, and a special character."
    choice_list.extend(['number', 'special'])
else:
    message += "."

print(message)

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%^&*()-+'

password = ''

for i in range(length):
    char_type = random.choice(choice_list)

    if char_type == 'lower':
        password += random.choice(alphabet_lower)
    elif char_type == 'upper':
        password += random.choice(alphabet_upper)
    elif char_type == 'number' and require_number:
        password += random.choice(numbers)
    elif char_type == 'special' and require_special:
        password += random.choice(special_characters)


if not any(c in password for c in numbers) and require_number:
    password += random.choice(numbers)

if not any(c in password for c in special_characters) and require_special:
    password += random.choice(special_characters)

if not any(c in password for c in alphabet_lower):
    password += random.choice(alphabet_lower)

if not any(c in password for c in alphabet_upper):
    password += random.choice(alphabet_upper)

while len(password) > length:
    lower_count = sum(1 for c in password if c in alphabet_lower)
    upper_count = sum(1 for c in password if c in alphabet_upper)
    number_count = sum(1 for c in password if c in numbers)
    special_count = sum(1 for c in password if c in special_characters)

    max_count = max(lower_count, upper_count, number_count, special_count)

    if max_count == lower_count:
        lower_indices = [i for i, c in enumerate(password) if c in alphabet_lower]
        removal_index = random.choice(lower_indices)

        password = password[:removal_index] + password[removal_index + 1:]

    elif max_count == upper_count:
        upper_indices = [i for i, c in enumerate(password) if c in alphabet_upper]
        removal_index = random.choice(upper_indices)

        password = password[:removal_index] + password[removal_index + 1:]

    elif max_count == number_count: 
        number_indices = [i for i, c in enumerate(password) if c in numbers]
        removal_index = random.choice(number_indices)

        password = password[:removal_index] + password[removal_index + 1:]

    elif max_count == special_count:
        special_indices = [i for i, c in enumerate(password) if c in special_characters]
        removal_index = random.choice(special_indices)

        password = password[:removal_index] + password[removal_index + 1:]

print("\nYour randomly generated password is ", password)

print("\nMake sure to keep it safe!\n")
