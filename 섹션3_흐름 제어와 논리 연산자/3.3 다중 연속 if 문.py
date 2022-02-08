from tkinter.tix import Balloon


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5천원")
    elif age <= 18:
        bill = 7
        print("Youth tickets are 7천원")
    else:
        bill = 10
        print("Adult tickets are 1만원")
        
    want_photo = input("Do you want a photo taken? Y or N. ")
    if want_photo == "Y":
        bill += 3 # bill = bill + 3 이렇게 써도 같은 의미이다
    
    print(f"Your final bill is {bill}")
        
else:
    print("Sorry, you have to grow taller before you can ride.")