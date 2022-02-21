######## 딕셔너리 컴프리헨션(Dictionary Comprehension)
#students_scores = {new_key:new_value for (key, vaiue) in dictionary}

names = ['Alex', 'Beth', 'Dave', 'Caroline', 'Eleanor', 'freddie']
import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)
# in 다음에 그 딕셔너리(students_scores)의 item()메소드를 호출해야 한다. item은 속성값이 아니기 때문에 반드시 괄호
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60 }
print(passed_students)