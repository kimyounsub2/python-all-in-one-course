# import tkinter
from tkinter import * # 이것은  기본적으로 언급된 tkinter모듈을 모두 제거해도 Tk로 윈도우를 초기화할 수 있다

# 전에 터틀로 작업할대 스크린과 같은 것이다.
window = Tk()
window.title("My First GUI Program") # 창 제목
window.minsize(width=500, height=300)

# 라벨(Label)만드는 방법
my_Label = Label(text = "I Am a Label", font=("Arial", 24, "bold")) 
# 라벨을 만들고 컴포넌트가 스크린에 보여지기 전에 어떻게 배치해야 하는지 명시해야 한다.
my_Label.pack(side="left")
# pack 함수는 위치 조정뿐만 아니라 사용용도가 다양하다.

# 위에서 만든 라벨내용을 수정한다.
my_Label["text"] = "New Text"
my_Label.config(text = "New Text")

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_Label.config(text= f"{new_text}") # 버튼클릭시 라벨 문구 변경된다.
    
# 버튼(Button)만드는 방법
button = Button(text = "Click Me", command=button_clicked)
button.pack()

# 엔트리 컴포넌트(Entry)
input = Entry(width = 10)
input.pack()
print(input.get())




#Tk창을 유지시켜준다.
window.mainloop()