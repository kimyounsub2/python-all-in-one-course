print('''

                     %%%%
                    %%%%-(
                  _%%%%%_/                        \ ' /
                _%%%%%%%%                        - (_) -
              _%%%%%%%/ \%                        / , \
             %%%%%%%%%\\ \_
               %%%%%%   \ \\
                   )    /\_/
                 /(___. \
                 '----' (
                /       )
    ---....____/        (_____ __ _ ___ ___ __ _ _ _____ _ _ ___
              /         )---...___ =-= = -_= -=_= _-=_-_ -=- =-_
            ,'          (         ```--.._= -_= -_= _-=- -_= _=-
         ,-'            )                 ``--._=-_ =-=_-= _-= _
         '-._    '-..___(                       ``-._=_-=_- =_-=
             ``---....__)                            `-._-=_-_=-
                   )|)|                                  `-._=-_
        gnv       '-'-.\_                                    `-.


    
''')
print("Welcome to Tresure Island")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "Left" or "right".').lower()#대문자나 소문자아무거다 입력해도 소문자로 변환해줘 문제 없다

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "Wait" to wait for a oat. Type "Swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is a house wuth 3 doors. one yellow and one blue. Which colour do you choose? ').lower()
        if choice3 == "red":
            print("It\'s a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over." )
        else:
            print("You chose a door that doesn\'t exist. Game Over")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over. ")