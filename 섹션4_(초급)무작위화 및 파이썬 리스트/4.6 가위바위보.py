import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("가위바위보 게임입니다.")
game_imges = [rock, paper, scissors]
user_game = int(input("What do you chose? type 0 for rock, 1 for paper or 2 for scissors. \n "))

if user_game >= 3 or user_game < 0:
    print("You typed an invalid number, you lose! ")
else:
    print(game_imges[user_game])

    # 0 묵 1 찌 2 빠
    computer_game = random.randint(0, 2)
    game_imges 

    print("computer_game")
    print(game_imges[computer_game])


    if user_game == 0 and computer_game == 2:
        print("you wuns!")
    elif computer_game == 0 and user_game ==2:
        print("You lose")
    elif computer_game > user_game:
        print(" you lose!")
    elif computer_game == user_game:
        print("It's a draw")
