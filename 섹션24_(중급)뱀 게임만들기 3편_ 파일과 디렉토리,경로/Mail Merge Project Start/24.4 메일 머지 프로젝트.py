
        
# 윗부분에 PLACEHOLDER라는 상수를 만들고 대괄호를 써서 문자열로 설정하는데 starting_letter.txt로부터 바꾸고자 하는 이름이
# 문자열이기 때문이다.

PLACEHOLDER = "[name]" 
# 아래의 경로에 있는 invited_names 명단을 리스트로 출력   
with open("/python-all-in-one-course/섹션24_(중급)뱀 게임만들기 3편_ 파일과 디렉토리,경로/Mail Merge Project Start/Input/names/invited_names.txt") as names_file:
    names = names_file.readlines() # 코드를 실행하면 이름들이 출력되고 이름은 리스트로 바뀌었다.
    print(names)
# invited_names에 있는 명단의 이름을 아래의 경로에 있는 starting_letter의 편지내용에 전체 이름을 하나씩 대입하여 출력한다.   
with open("/python-all-in-one-course/섹션24_(중급)뱀 게임만들기 3편_ 파일과 디렉토리,경로/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    Letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
# 문자열의 앞과 뒤에 있는 공백을 제거해 주는 strip이라는 메소드를 사용해서 우리는 문자열의 앞과 뒤에 어던 
# 공백도 갖지 않는 결과 값을 가질수 있다.
        new_Letter = Letter_contents.replace(PLACEHOLDER, stripped_name)
# 위에서 출력되것을 아래의 경로에 Letter_for_{} 각각의 이름별로 텍스트 파일로 저장시킨다.
        with open(f"/python-all-in-one-course/섹션24_(중급)뱀 게임만들기 3편_ 파일과 디렉토리,경로/Mail Merge Project Start/Output/ReadyToSend/Letter_for_{stripped_name}.txt", mode = "w") as completed_Letter:
            completed_Letter.write(new_Letter)

