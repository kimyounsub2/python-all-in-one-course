class Animal:
    def __init__(self):
        self.num_eyes = 2
        
    def breathe(self):
        print("Inhale, exhale.")
        
class Fish(Animal):
    
    def __init__(self):
        super().__init__() # super는 상위 클래스인 Animal을 호출해준다.
        
    # 상위클래스인 Animal 내용을 수정하고 싶을때는 다시 breathe 메소드를 정의해주면 된다.
    def breathe(self):
        super().breathe() # 상위 클래스에 잇는 breathe 메소드가 하는 동작을 모두 하겠다고 한다.
        print("dong this underwater")
    
    def swim(self):
        print("mving in water.")
 
 
# Fish 클래스로 만든 객체가 이제 상위 클래스의 속성과 메소드를 모두 사용할수 있다. Animal 클래스를 상속받았으니까        
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)