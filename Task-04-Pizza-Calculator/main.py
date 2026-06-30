print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill = 17
        if extra_cheese == "Y":
            bill = 18
    elif pepperoni == "N":
        bill = 15
        if extra_cheese == "Y":
            bill = 16
    elif pepperoni == "Y":
        bill = 17
        if extra_cheese == "N":
            bill = 17
    else:
        bill = 15
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill = 23
        if extra_cheese == "Y":
            bill = 24
    elif pepperoni == "N":
        bill = 20
        if extra_cheese == "Y":
            bill = 21
    elif pepperoni == "Y":
        bill = 23
        if extra_cheese == "N":
            bill = 23
    else:
        bill = 20
elif size == "L":
    bill = 25
    if pepperoni == "Y":
        bill = 28
        if extra_cheese == "Y":
            bill = 29
    elif pepperoni == "N":
        bill = 25
        if extra_cheese == "Y":
            bill = 26
    elif pepperoni == "Y":
        bill = 28
        if extra_cheese == "N":
            bill = 28
    else:
        bill = 25
else:
    bill = 0
    print("Sorry, that's not a valid size.")
print("your total bill is $"+ str(bill))
