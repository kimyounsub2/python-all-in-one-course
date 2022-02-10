print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay 5천원")
    else:
        print("Please pay 1만원")
else:
    print("Sorry, you have to grow taller before you can ride.")
    
    
    
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay 5천원")
    elif age <= 18:
        print("Please pay 7천원")
    else:
        print("Please pay 1만원")
else:
    print("Sorry, you have to grow taller before you can ride.")