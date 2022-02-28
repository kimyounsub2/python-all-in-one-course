# age: int
# name: str
# height: float
# is_human: bool


def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(19):
    print("You may pass")
else:
    print("Pay a fine.")
    
    
######파이썬에서는 이것을 타입 힌트(Type Hints)라고 부른다.
# 버그를 알려주고 코드를 더 안저나게 지켜주고 디버깅 시간을 줄이고 코드작성에 집중하도록 해준다
def greeting(name: str) -> str:
    return 'Hello' + name

print(greeting)