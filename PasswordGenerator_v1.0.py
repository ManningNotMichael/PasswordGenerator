import random  # Importing the random module to use the choice function for selecting random characters

print('Welcome To Your Password Generator. It is simple, but effective')

# Defining the set of characters to use in the passwords
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*1234567890'

# Asking the user how many passwords to generate and converting the input to an integer
number = input('Amount of passwords to generate: ')
number = int(number)

# Asking the user for the desired length of each password and converting the input to an integer
length = input('Your password length: ')
length = int(length)

print('\nHere are your passwords: ')

# Generating the specified number of passwords
for pwd in range(number):
    passwords = ''  # Initializing an empty string to hold the password
    for c in range(length):
        # Adding a randomly chosen character from chars to the password string
        passwords += random.choice(chars)
    # Printing the generated password
    print(passwords)
