print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
total_price = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        total_price += 5
    elif age <= 18:
        total_price += 7
    else:
        total_price += 12
    include_photos = input(f"The ticket will be {total_price} dollars. Would you like to have access to pictures of the ride for 3 more dollars?(Yes or No) ")
    if include_photos == "Yes":
        total_price += 3
        print(f"Ok, so the total will be {total_price}")
    else:
        print(f"Ok the total remains {total_price}")
else:
    print("Sorry you cant ride")