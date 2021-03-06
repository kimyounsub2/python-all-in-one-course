from turtle import Turtle
# 상수이름은 대문자로 표기한다.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    # Snake 클래스 안에 있는 시작 위치를 사용해서 뱀을 새로 만들수 이싸.
    def __init__(self):
        # 클래스 안에서 쓸때는 self를 써줘야 한다.
        self.segmesnts = []
        self.create_snake()
        self.head = self.segmesnts[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment= Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segmesnts.append(new_segment)
            # 클래스 속성인 segmesnts를 사용하기위해 self사용 그럼 이 new_segment를 Snake클래스의 segments에 추가된다.
            
    def move(self):
        for seg_num in range(len(self.segmesnts) -1 , 0, -1): # start =2, stop = 0, step = -1
            new_x = self.segmesnts[seg_num - 1].xcor()
            new_y = self.segmesnts[seg_num - 1].ycor()
            self.segmesnts[seg_num].goto(new_x, new_y)        
        self.head.forward(MOVE_DISTANCE)
            
    def up(self): 
        if self.head.heading() !=DOWN: # 현재 방향이 아래쪽이면 위쪽으로 갈수 없다. 하지만 다른방향은 방향을 위로 갈수 있다.      
            self.head.setheading(UP)
            
    def down(self): 
        if self.head.heading() !=UP:   
            self.head.setheading(DOWN)
         
    def left(self):   
        if self.head.heading() !=RIGHT: 
            self.head.setheading(LEFT) 
              
    def right(self): 
        if self.head.heading() !=LEFT:   
            self.head.setheading(RIGHT)