# class
# 클래스 : 객체를 만들기 위한 사용자 정의 자료형
# 인스턴스 : 클래스를 기반으로 만들어진 구체적인 객체/ 관계
# 매서드 : 객체의 기능을 반영하여 클래스 내부에 선언된 함수(def)
# 상속 : 어떤 클래스의 특성을 다른 클래스에 전달하는 기법 class 클래스이름(부모클래스)
# 매서드 오버라이딩 : 같은 함수에 여러 기능을 부여하는 구현 기법 ex) 부모와 자식의 함수 이름이 같다.

# class로 계산기 만들기
class Calculator:
    
    def __init__(self):
        self.result = 0
        
    def add(self,num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()
# 계산기 2개가 서로 아무 영향을 끼치지 않는다.
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 아무 기능도 없는 껍질 뿐인 클래스도 객체생성이 가능하다
class Cookie:
    pass
a = Cookie()
b = Cookie()

# 생성자의 개념 : 인스턴스를 생성하면서 필드값을 초기화시키는 함수 __init__(self)

# 사칙연산 클래스 만들기
class FourCal:
    pass
a = FourCal()
type(a)

class FourCal:
    def setdata(self, first, second): # class 안에 있는 함수를 매서드라 한다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
# a,b 객체를 만들어보자        
a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

b = FourCal()
b.setdata(3,7)
print(b.first)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())

# AttributeError 오류 : FourCal클래스의 객체 a에 setdata매서드를 수행하지 않고 실행하면 오류가 난다.
a = FourCal()
a.add()

# 클래스 안에 생성자 __init__를 입력하면 setdata매서드를 수행하지 않고 바로실행 할수 있다.
class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def setdata(self, first, second): # class 안에 있는 함수를 매서드라 한다.
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)
a.add()
a.sub()
b = FourCal(5,5)
b.sub()
b.div() 

# 클래스의 상속 : FourCal의 클래스의 내용을 물려 받는다.
class MoreFourCal(FourCal):
    pass
a = MoreFourCal(4, 2)
a.add()
# 클래스 상속받고 a의 b제곱을 추가하자
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4, 2)
a.pow()

# 매서드 오버라이딩 : 상속받을 대상인 클래스의 매서드와 이름은 같지만 그 행동을 다르게 해야 할때
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4,0)
a.div()

# 클래스 변수
class Family:
    lastname = "김"
print(Family.lastname)

# Famliy클래스를 만든 객체를 통해서도 클래스 변수 사용 가능
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
# Falmily 클래스의 lastname를 변경하면?
Family.lastname = "박"
# 클래스로 만든 객체의 lastname값도 모두 변경된다.
print(a.lastname)
print(b.lastname)

# 자동차 클래스를 완전한 파이썬 코드로
# class선언 부분
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150: # 속도가 150이상이면 150으로 찍히게 매서드에 추가해야 한다.
            self.speed = 150
        
    def downSpeed(self, value):
        self.speed -= value

# 메인 코드 부분
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색생은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))

myCar2.upSpeed(600)
print("자동차2의 색생은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색생은 %s이며, 현재 속도는 %dkm입니다." % (myCar3.color, myCar3.speed))

# 생성자 추가
class Car:
    color = ""
    speed = 0
    
    def __init__(self, value1, value2):
        self.color = value1
        self.speed = value2
    
    def upSpeed(self, value):
        self.speed += value
 
    def downSpeed(self, value):
        self.speed -= value

# 메인 코드 부분
myCar1 = Car("빨강",30)
myCar2 = Car("파랑",60)
print("자동차1의 색생은 %s이며, 현재 속도는 %dkm입니다." % (myCar1.color, myCar1.speed))
print("자동차2의 색생은 %s이며, 현재 속도는 %dkm입니다." % (myCar2.color, myCar2.speed))

# getName()과 getSpeed()메서드를 만들고 자동차의 이름과 현재 속도를 반환
class Car:
    name = ""
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def getName(self):
        return self.name
 
    def getSpeed(self):
        return self.speed

car1 = Car("아우디",0)
car2 = Car("벤츠",30)
print("%s의 현재 속도는 %d입니다." % (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다." % (car2.getName(), car2.getSpeed()))
