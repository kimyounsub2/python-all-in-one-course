programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop":"The action of doing something over and over again."}

print(programming_dictionary["Bug"]) # 오타를 내거나 없는 문구를 출력하면 KeyError가 난다.

# dictionary를 새롭게 추가할때 실행하면 위에 문구 아래에 추가되어 나온다.
programming_dictionary["YOUN"] ="피곤하다 어제 새벽에 일어나서 축구를 봤더니"
print(programming_dictionary)

# 나중 단계에서 딕셔너리에 키와 값을 추가해줄수 있다.
empty_dictionary ={}

# 딕셔너리를 통채로 지우고 싶을때 위의 내용이 지워진다.
programming_dictionary = {}
print(programming_dictionary)

# 딕셔너리 안의 내용을 수정한다. [ " " ]안에 문구가 없음 새롭게 추가될것이고 있음 안에 내용이 수정된다.
programming_dictionary["YOUN"] = "축구를 봐서 피곤해 죽겠지만 그래도 이겨서 기분이 좋다."
print(programming_dictionary)

# for(반복문)을 사용핼때도 유용하다
for Key in programming_dictionary:
    print(Key)
    print(programming_dictionary)
