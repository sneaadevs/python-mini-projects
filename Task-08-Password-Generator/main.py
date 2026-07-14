letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
n_letter= int(input("How many letters would you like in your password?\n"))
n_number= int(input("How many numbers would you like in your password?\n"))
n_symbol = int(input("How many symbols would you like in your password?\n"))

import random

r_letter=random.choices(letters,k=n_letter)
r_symbol=random.choices(symbols,k=n_symbol)
r_number=random.choices(numbers,k=n_number)


letter=[]
symbol=[]
number=[]
for i in range(n_letter):
    letter.append(random.choice(letters))
for i in range(n_number):
    number.append(random.choice(numbers))
for i in range(n_symbol):
    symbol.append(random.choice(symbols))


random_list=letter+number+symbol
print(random_list)
random.shuffle(random_list)
print(random_list)
password = "".join(random_list)
print(f"Your password is: {password}")
