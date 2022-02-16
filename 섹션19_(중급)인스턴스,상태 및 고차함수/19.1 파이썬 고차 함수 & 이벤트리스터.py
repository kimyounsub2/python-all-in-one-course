from turtle import Turtle, Screen

youn = Turtle()
screen = Screen()

def move_forwards():
    youn.forward(10)


# screen 객체를 가져온 다음 듣기를 시작하라고 명령한다.
# 듣기가 시작되고 나면 키보드의 특정 키를 누르면 촉발되는 함수를 바인딩한다.
screen.listen()
# 키 누르기를 코드 안의 이벤트에 바인딩하려면 이벤트 리스터를 사용한다.
# screen.onkey(fun, key)
# fun은 인수가 없는 함수와 키를 받아들인다. 
# key는 키보드의 a키 또는 space나 up, down과 같은 키 부호 이름을 말한다.
screen.onkey(fun = move_forwards, key = "space") # fun = move_forwards() -> X
########### 매우 중요하다 ##########
# 함수를 다른 함수에 전달할때 (fun = move_forwards())끝에 괄호를 추가하지 않는다.
# ()함수를 사용하면 함수가 그 자리에서 실행된다.
# 하지만 우리가 원하는 것은 이 onkey 메소드가 스페이스 바가 눌리는 이벤트를 듣고 
# 그 이벤트가 일어났을때 move_forwards 함수를 싱행시키도록 하기 위해
screen.exitonclick()
