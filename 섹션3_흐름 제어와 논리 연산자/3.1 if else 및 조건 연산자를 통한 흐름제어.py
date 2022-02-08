water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Contiue")
# water_lever이 80보다 작아 else 조건문으로 출력

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

Game_height = 140
if Game_height < height:
    print("탑승 가능합니다.")
else:
    print("죄송하지만 탑승 불가입니다. ")
    
    
if height >= 140:
    print("You can ride the rollercoaster!")
else: # if문과 같이 들여쓰기 되어 있어야 한다.
    print("Sorry, you have to grow taller before you can ride.")