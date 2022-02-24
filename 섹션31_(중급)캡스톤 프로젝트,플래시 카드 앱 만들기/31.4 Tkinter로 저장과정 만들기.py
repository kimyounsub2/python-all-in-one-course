BACKGROUND_COLOR = "#B1DDC6"
from email.mime import image
from tkinter import*
import pandas
import random

current_card = {} 

try:
   data = pandas.read_csv("섹션31_(중급)캡스톤 프로젝트,플래시 카드 앱 만들기/data/words_to_learn.csv")   
except FileNotFoundError:
   original_data = pandas.read_csv("섹션31_(중급)캡스톤 프로젝트,플래시 카드 앱 만들기/data/french_words.csv")
   to_learn = original_data.to_dict(orient = "records")
else:
   to_learn = data.to_dict(orient = "records")# records는 리스트를 [{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}]로 바꿔준다.


def next_card():
   global current_card ,filp_timer # 프랑스어 목록과 영어 쌍 목록으로부터 random.choice(to_learn)를 저장할수 있다.
   window.after_cancel(filp_timer)
   current_card = random.choice(to_learn)
   #print(current_card["French"]) # 무작위로 프랑스 단어를 가져올수있다.
   canvas.itemconfig(card_title, text="French" , fill ="black")
   canvas.itemconfig(card_word, text = current_card["French"],fill ="black")
   canvas.itemconfig(card_backgound, image = card_front_img)
   #window.after(3000, func = flip_card) # 이대로 실행하면 버튼 클릭후 3초가 아니라 실행후 3초로 읽어 문제가된다.
   filp_timer = window.after(3000, func = flip_card)
   
def flip_card():
   canvas.itemconfig(card_title, text = "English" , fill="white" )
   canvas.itemconfig(card_word, text = current_card["English"], fill="white")
   canvas.itemconfig(card_backgound, image=card_back_img) # card_back_img이미지는 영어가 나올떄 색이 변해야 하기 때문에 flip_card함수에 넣어줘야 한다.

def is_known():
   to_learn.remove(current_card) # remove함수 목록에서 특정 요소들을 제거한다.
   # 이제 유저가 is_known이라고 선언하면 current_card는 to_learn단어 목록에서 제거 될것이다.
   data = pandas.DataFrame(to_learn) #DataFrame은 to_learn 리스트로부터 만들어질 것이다.
   data.to_csv("섹션31_(중급)캡스톤 프로젝트,플래시 카드 앱 만들기/data/words_to_learn.csv", index =False)
   
   next_card()
   



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
 
filp_timer = window.after(3000, func = flip_card)# 시간을 밀리초로 명시해서 3초 = 3000
 

canvas = Canvas(width=800, height =526 ) 
card_front_img = PhotoImage(file="섹션31_(중급)캡스톤 프로젝트,플래시 카드 앱 만들기/images/card_front.png")
card_back_img = PhotoImage(file="섹션31_(중급)캡스톤 프로젝트,플래시 카드 앱 만들기/images/card_back.png")
card_backgound = canvas.create_image(400, 263, image= card_front_img)
card_title = canvas.create_text(400, 150, text = "", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file = "섹션31_(중급)캡스톤 프로젝트,플래시 카드 앱 만들기/images/wrong.png")
unknown_button = Button(image = cross_image, command=next_card, highlightthickness=0)
unknown_button.grid(row=1, column=0,)

check_image = PhotoImage(file = "섹션31_(중급)캡스톤 프로젝트,플래시 카드 앱 만들기/images/right.png")
known_button = Button(image = check_image, command=is_known, highlightthickness=0)
known_button.grid(row=1, column=1)

next_card() # 프로그램을 실행시킬때 next_card함수를 버튼클릭하지 않고 바로 실행하기 위해서
# 전체 UI를 실행시키고 next_card()를 생성해서 Data를 구하고 card_title과 card_word에 넣는다.

window.mainloop()