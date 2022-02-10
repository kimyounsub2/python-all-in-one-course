# Step 1


word_list = ["ardvark", "baboon", "camel"]

#TODO-1 Randomly choose a word from the word_list and assign it to a variable called choses_word.
#TODO-1 word_list에서 단어를 임의로 선택하여 chose_word라는 변수에 할당합니다.
import random
hose_word = random.choice(word_list)


#TODT-2 Ask the user to guess a letter and assign theif answer to avariable called guess. Make guess lowercase.
#TODT-2 사용자에게 글자를 추측하고 추측이라는 가증 가능한 대답을 할당하도록 요청합니다. 소문자를 맞추다.

user_guess = input("Guess a letter: ").lower()

#TODO-3 Check if the letter the user guessde (guess) is one of the leters in the chosen_word.
#TODO-3 사용자가 추측하는 문자가 choose_word의 leter 중 하나인지 확인합니다.
print(hose_word)
for A in hose_word:
    if A == user_guess:
        print("Right")
    else:
        print("Wrong")