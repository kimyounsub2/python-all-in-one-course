THEME_COLOR = "#375362"
# 기존과는 다르게 UI를 클래스를 활용하여 코딩해보자
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    # quiz_brain모듈에서 QuizBrain클래스를 가져오기 위해
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text = "Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text (
            150,
            125,
            width = 280, # 텍스트의 질문이 길어 넓이 조정
            text="Some Question Text" , 
            fill =THEME_COLOR,
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        
        true_image = PhotoImage(file ="섹션34_(중급)API실습 -GUI퀴즈 앱 만들기/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed) # class안에 있기때문에 버튼이 실제로 클릭을 감지하면 이 메소드를 트리거하기만 원하기 때문에 괄호는 없애줘야 한다.
        self.true_button.grid(row=2, column=0)
        
        false_image = PhotoImage(file ="섹션34_(중급)API실습 -GUI퀴즈 앱 만들기/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
                
        self.get_next_question()
            
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white") # 다시 돌아왔을때 배경 색을 다시 지정해준다.
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quize")
            self.true_button.config(state="disabled") # 퀴즈가 끝났을때 버튼을 비활성화 한다.
            self.false_button.config(state="disabled")
            
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True")) ##### 아래의 false_pressed에서 같은역할을 한다.
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False") 
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question) # 색이 변하고 다시 돌아오는 시간을 정한다.