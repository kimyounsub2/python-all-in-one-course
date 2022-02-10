# 156 178 165 171 187
student_heights = input("Iput a list of student heights ").split()
# 아래 for문구 없이는 안되는것인가 슈밤
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


# 반복문 없이 평균 구하기
# total_height = sum(student_heights) # 합계 구하는 함수
# number_of_students = len(student_heights) # 입력한 숫자 구하는 함수
# average_height = round(total_height / number_of_students) # 반올림 평균
# print(average_height)

# fot문 사용하여 평균 구하기
total_height = 0 # 합계
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0 # 학생수
for number in student_heights:
    number_of_students += 1
print(number_of_students)
# 평균
average_height = round(total_height / number_of_students) # 반올림
print(average_height)
