import random
import string

def generate_password(length):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length must be a positive integer.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
main()
