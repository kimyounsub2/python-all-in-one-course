from tkinter import *

window = Tk()
window.title("Miles을 Km로 바꾸기 프로그램") 
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20) # 가장자리의 여백공간을 지정한다.

def Conversion():
   miles_input = float(input.get())
   km_1 = miles_input * 1.609
   text_1.config(text= f"{km_1}")
    

Miles = Label(text="Miles" , font=("Arial", 15, "bold"))
Miles.grid(column = 3, row = 1)

Km = Label(text="Km" , font=("Arial", 15, "bold"))
Km.grid(column = 3, row = 3)

text =Label(text="is equal to" , font=("Arial", 15, "bold"))
text.grid(column = 1, row = 3)

text_1 =Label(text="0" , font=("Arial", 15, "bold"))
text_1.config(text = "0")
text_1.grid(column = 2, row = 3)

Calculate = Button(text="Calculate", command=Conversion)
Calculate.grid(column = 2, row = 4)

miles_input = Entry(width = 10)
print(miles_input.get())
miles_input.grid(column = 2, row = 1)

window.mainloop()