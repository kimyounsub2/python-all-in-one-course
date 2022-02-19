from turtle import Turtle
# 상수이름은 대문자로 표기한다.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# 오류건찾아보자... 
class Snake:
    # Snake 클래스 안에 있는 시작 위치를 사용해서 뱀을 새로 만들수 이싸.
    def __init__(self):
        # 클래스 안에서 쓸때는 self를 써줘야 한다.
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
                
            
     # 뱀이 먹이를 먹고 꼬리가 한칸씩 늘어나게 해주는 함수
    def add_segment(self, position): # 이함수는 new_segment 추가될 위치가 필요하다.
        new_segment= Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
            # 클래스 속성인 segmesnts를 사용하기위해 self사용 그럼 이 new_segment를 Snake클래스의 segments에 추가된다.
     
    def extend(self): # 이 함수는 뱀에 new_segment를 추가한다.       
        self.add_segment(self.segments[-1].position()) # -1을 해줘야 끝에서부터 거꾸로 셀수 있다.
            
            
            
    def move(self):
        for seg_num in range(len(self.segments) -1 , 0, -1): # start =2, stop = 0, step = -1
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)        
        self.head.forward(MOVE_DISTANCE)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear() 
        self.create_snake()
        self.head = self.segments[0]
        
            
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