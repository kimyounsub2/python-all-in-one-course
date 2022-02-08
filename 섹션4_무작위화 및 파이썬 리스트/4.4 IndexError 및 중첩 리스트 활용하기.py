states_of_Korea = ["강남3구" , "강남구", "서초구", "송파구", "금관구", "금천구", "관악구", "구로구", 
"노도강", "노원구", "도봉구", "강북구", "당여목", "당산", "여의도", "목동", "마용성", "마포구", "용산구", "성동구"]


print(len(states_of_Korea)) # 총 개수는 20개이다 len함수로 숫자를 알수 잇다

print(states_of_Korea[40]) # 해당 그룹에는 40개까지 없어서 IndexError 메세지가 나온다

fruits = ["Strawberries", "Nectarines", " Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen =[fruits, vegetables]

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])