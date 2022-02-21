##### List Comprehension(리스트 컴프리헨션)

numbers = [1, 2, 3]
# for loop
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)
print(new_list)

# Comprehension(리스트 컴프리헨션)
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "youn"
new_list = [letter for letter in name]
print(new_list)

range(1,5)
new_range = [number*2 for number in range(1,5)]
print(new_range)

names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'freddie']
# short_names = [new_item for item in list if test]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# 글자수가 5나 그 이상인 이름 
names = ['Alex', 'Beth', 'kyoun', 'Caroline', 'Eleanor', 'freddie']
# short_names = [new_item for item in list if test]
long_names = [name.upper() for name in names if len(name) > 5 or len(name) == 5]
print(long_names)