print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        bill = 5
    elif age >= 12 and age <= 18:
        bill = 7
    else:
        bill = 12
    photo=input("Do you want a photo?Type y for yes and n for no.")
    if photo == "y":
        bill += 3
    print(f"your final bill is: {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
