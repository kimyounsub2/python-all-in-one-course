height = input("enter your height in m: ")
weight = input("enter yout weight in kg: ")

# 예제 1 heigt, weight 둘다 소숫점으로 볼때
BMI = float(weight) / (float(height)*float(height))
print(BMI)

# 예제 2 heigt소숫점, weight정수 
BMI = int(weight) / float(height)**2
bmi_as_int = int(BMI) #뒤에 소숫점을 잘라주고 앞의 정수만 나오게 할려고
print(bmi_as_int)

