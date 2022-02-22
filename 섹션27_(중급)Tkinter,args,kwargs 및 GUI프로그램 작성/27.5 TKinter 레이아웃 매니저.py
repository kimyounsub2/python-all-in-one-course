
from tkinter import *
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_Label.config(text= f"{new_text}") # 버튼클릭시 라벨 문구 변경된다.
    
def button2_clicked():
    print("I got clicked")
    new_text = input.get()
    my_Label.config(text= f"{new_text}") # 버튼클릭시 라벨 문구 변경된다.

window = Tk()
window.title("My First GUI Program") 
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # 가장자리의 여백공간을 지정한다.


my_Label = Label(text = "I Am a Label", font=("Arial", 24, "bold")) 
my_Label.config(text = "New Text")
# my_Label.place(x=0,y=0) # 왼쪽 제일위에 생성된다. 하지만 갯수가 많아지면 하나씩 지정해줘야 해서 복잡하다.
my_Label.grid(column = 0, row = 0)
# 단 grid와 back는 같은 프로그램에서 쓸수 없다.

# 버튼(Button)만드는 방법
button = Button(text = "Button", command=button_clicked)
#button.pack(side="left")
button.grid(column = 1, row = 1)

button_1 = Button(text = "New Button", command=button2_clicked)
#button.pack(side="left")
button_1.grid(column = 2, row = 0)

# 엔트리 컴포넌트(Entry)
input = Entry(width = 10)
print(input.get())
#input.pack(side="left")
input.grid(column = 3, row = 2)

window.mainloop()