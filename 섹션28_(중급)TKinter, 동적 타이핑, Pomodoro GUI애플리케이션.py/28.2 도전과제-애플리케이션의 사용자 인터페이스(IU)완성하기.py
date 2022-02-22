from tkinter import*
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) # 상단에 상수YELLOW를 지정했다 그리고 YELLOW는 단어가 아니기 때문에 따옴표 안에 두지 말자

title_label = Label(text="Timer" , fg=GREEN, bg =YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height =224, bg=YELLOW, highlightthickness=0) # highlightthickness는 canvas의 사각형(경계선)의 색상도 없애준다.
tomato_img = PhotoImage(file="tomato.png") # 사진파일을 가져오고 tomato_img로 변수 선언
canvas.create_image(100,112, image=tomato_img) # tomato_img변수를 가져온다.
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text = "✓" , fg=GREEN, bg=YELLOW,font=(FONT_NAME, 20, "bold") )
check_marks.grid(column=1, row=2)

window.mainloop()