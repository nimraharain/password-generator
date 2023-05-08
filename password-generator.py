import random
import string

# function to generate password
def generate_password(length, complexity):
    # define characters for each complexity level
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # create list of characters based on complexity level
    if complexity == "low":
        chars = lowercase
    elif complexity == "medium":
        chars = lowercase + uppercase + digits
    else:
        chars = lowercase + uppercase + digits + special_chars
    
    # generate random password
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password

# get user input for password length and complexity level
while True:
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Password length should be a positive integer")
        break
    except ValueError as e:
        print(e)

while True:
    complexity = input("Enter complexity level (low, medium, high): ")
    if complexity not in ["low", "medium", "high"]:
        print("Invalid complexity level. Please enter 'low', 'medium', or 'high'.")
    else:
        break

# generate and print password
password = generate_password(length, complexity)
print("Generated password:", password)
