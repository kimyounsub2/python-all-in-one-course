print("Welcome to the tip calculator!")

total_bill = float(input("what was the total bill? "))

percent = int(input("what percentage tip would you like to give? 10, 12, or 15? 12"))

person = int(input("How many people to split the bill?"))

percent_100 = percent / 100 
bill = total_bill * percent_100
bill_1 = total_bill + bill
bill_2 = bill_1 / person
bill_fianl = round(bill_2, 2)

print(f"Each person should pay {bill_fianl} 원")


# Each person should pay: 소숫점 둘째자리까지만