print("Welcome to the tip calclulator")
total = float(input("What was the total bill?"))
tip = int(input("How much would you like to tip? 10, 12 or 15"))
total_people = int(input("How many people will split the bill?"))

total_for_each = (total * (1 + tip/100)) / total_people

print(f"Each person should pay {total_for_each}")