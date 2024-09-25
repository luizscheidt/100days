#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_items = []

for i in range(nr_letters):
    new_item = random.choice(letters)
    password_items.append(new_item)

for i in range(nr_symbols):
    new_item = random.choice(symbols)
    password_items.append(new_item)

for i in range(nr_numbers):
    new_item = random.choice(numbers)
    password_items.append(new_item)

print(password_items)

real_password = []

for i in range(len(password_items)):
    index = random.randint(0, len(password_items)-1)
    real_password.append(password_items[index])
    password_items.remove(password_items[index])

password = ''.join(real_password)

print(password)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P