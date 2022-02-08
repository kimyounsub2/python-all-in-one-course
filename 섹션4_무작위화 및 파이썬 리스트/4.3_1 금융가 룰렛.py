# Angela, Ben, Jenny, Micheal, Chlos

import random

names_string = input("Give me everybody\'s names, seperated by a comma. ")
names = names_string.split(", ") # input 값을 입력할때 여러개를 입력할수 잇다. example ['youn', 'sub', 'kim']

#예제 1
num_items = len(names) # names에서 입력자가 몇을 입력해주는 알수 없어 입력한 숫자를 알기위에 len함수를 사용  ex) 3
random_choice = random.randint(0, num_items -1) # 0번째 부터 num_items 입력자가 입력한 수 
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "가 계산할것입니다.")

#예제2 random.choice 사용
person_who_will_pay = random.choice(names)
print(person_who_will_pay + "가 계산할거에요")
