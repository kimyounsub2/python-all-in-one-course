height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI =round(weight / height**2)

if BMI > 35:
    print(f"{BMI} 초고도 비만입니다.")
elif BMI > 30:
    print(f"{BMI} 비만입니다.")
elif BMI > 25:
    print(f"{BMI} 과체중입니다.")
elif BMI > 18.5:
    print(f"{BMI} 정상체중입니다.")
else:
    print(f"{BMI} 저체중입니다.")
