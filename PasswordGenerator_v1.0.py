import random

def generate_passwords(pwdNumber, pwdLength, chars):
    """
    Generates a list of passwords based on the specified number and length,
    using characters from the given character set.

    Parameters:
    - pwdNumber: int, number of passwords to generate
    - pwdLength: int, length of each password
    - chars: str, characters to choose from

    Returns:
    - list of generated passwords
    """
    passwords = []
    for _ in range(pwdNumber):
        # Generate a password of length pwdLength by randomly choosing characters from chars
        password = ''.join(random.choice(chars) for _ in range(pwdLength))
        passwords.append(password)
    return passwords

def main():
    """
    Main function to handle user input and generate passwords.
    """
    print('Welcome To Your Password Generator. It is simple, but effective')

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*1234567890'

    # Input validation for number of passwords to generate
    while True:
        try:
            pwdNumber = int(input('Amount of passwords to generate: '))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Input validation for password length
    while True:
        try:
            pwdLength = int(input('Your password length: '))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print('\nHere are your passwords: ')

    # Generate passwords using generate_passwords function
    passwords = generate_passwords(pwdNumber, pwdLength, chars)

    # Print each generated password
    for pwd in passwords:
        print(pwd)

if __name__ == "__main__":
    main()
