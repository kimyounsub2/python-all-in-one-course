from tkinter import*
import math
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
def start_timer():
    count_down(5 * 60)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # 카운터를 00:00분으로 표시하기 위해 300초가 아닌 
    count_min = math.floor(count/60) # math함수를 사용하면 x보다 작거나 같은 가장 큰 정수를 리턴받는다 ex) 4.8 이면 4로 리턴된다.
    count_sec = count % 60 # 100초가 있고 그걸 60으로 나눈다면 1이 될것이고 100에서 60을 빼면 나머지로 40을 얻을수 있다.
    
    
    # start를 누르면 5:0으로 표시되는데 5:00으로 표시되게 하기 위해 동적 타이핑을 알아야한다.
    # 마지막 9초부터 0:9가 아닌 0:09로 표시하기 위한 아래식으로 표시해준다.
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}") # canvas위젯에서는 text를 변경할때 itemconfig함수를 넣어줘야 한다.
    if count > 0:
        window.after(1000, count_down, count -1)
    # 코드를 실행하면 아래의 count 5를 넣어 실행하고 앞에 1000이 1초동안 대기한 다음 count_down함수를 호출하고 5 -1을 넣게 되어
    # 4가 되고 그 이후에다시 반복해서 3이된다.
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW) # 상단에 상수YELLOW를 지정했다 그리고 YELLOW는 단어가 아니기 때문에 따옴표 안에 두지 말자



title_label = Label(text="Timer" , fg=GREEN, bg =YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height =224, bg=YELLOW, highlightthickness=0) # highlightthickness는 canvas의 사각형(경계선)의 색상도 없애준다.
tomato_img = PhotoImage(file="tomato.png") # 사진파일을 가져오고 tomato_img로 변수 선언
canvas.create_image(100,112, image=tomato_img) # tomato_img변수를 가져온다.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text = "✓" , fg=GREEN, bg=YELLOW,font=(FONT_NAME, 20, "bold") )
check_marks.grid(column=1, row=2)

window.mainloop()