print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage  =  bill  *  tip /   100 + bill
total_bill = tip_percentage / people
bill_per_person =  round(total_bill,2)
print(f"Each person should pay :${bill_per_person:.2f}")
#here   : .2f is known as trailing ,it means rounding of the number two digits after decimal and put zero if needed
