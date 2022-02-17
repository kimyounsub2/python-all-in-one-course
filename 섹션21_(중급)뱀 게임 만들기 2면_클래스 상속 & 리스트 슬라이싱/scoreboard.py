from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
      
    def update_scoreboard(self): # 아래처럼 하드코딩해서 글씨 위치나 폰트를 정해버릴수 있지만 맨위에 
        #지정해줘서 작업자가 다음에 변경하기 쉽게하기 위해 상수입력
        # self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))
       self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
       
    def game_over(self):
        self.goto(0,0) 
        self.write("Game Over", align = ALIGNMENT, font = FONT )
 
    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        