from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()
      
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)
       
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0 #게임이 끝나면 점수를 0으로 재설정해준다.  
        self.update_scoreboard()
       
# 게임오버 함수를 쓰지 않고 대신 Scoreboard를 재설정한다.
    # def game_over(self):
    #     self.goto(0,0) 
    #     self.write("Game Over", align = ALIGNMENT, font = FONT )
 
    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        