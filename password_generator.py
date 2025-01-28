import random
import string

# alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
# print(alphabet)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

print("Welcome to the PyPassword Generator")

def ask():
    pg_letters = int(input("How many letters would you like in your password?\n"))
    pg_numbers = int(input("How many numbers would you like?\n"))
    pg_symbols = int(input("How many symbols would you like?\n"))
    
    return pg_letters, pg_numbers, pg_symbols

def thee_generator():
    password_list = []

    pg_letters, pg_numbers, pg_symbols = ask()

    for i in range(0, pg_letters):
        password_list.append(random.choice(alphabet))

    for j in range(0, pg_numbers):
        password_list.append(random.choice(numbers))
    
    for k in range(0, pg_symbols):
        password_list.append(random.choice(symbols))

    return password_list

def shuffel():
    password_list = thee_generator()

    random.shuffle(password_list)
    final = ''.join(str(x) for x in password_list)

    print(final)

if __name__ == "__main__":
    shuffel()


# Add safety checks
# Save password to data base