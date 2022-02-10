age = input("what is yout current age?")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = days_remaining * 52
months_remainig = weeks_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remainig} months left. "
print(message)

# 30세 기준 90살까지 살면 You have 21900 days, 1138800 weeks, and 13665600 months left. 