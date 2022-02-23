from tkinter import* # 실제로는 모든 클래스와 상수만을 임포트한다.
from tkinter import messagebox # messagebox는 그냥 또 다른 코드 모듈이기 때문에 따로 임포트 해줘야 한다.
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numberst = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numberst
    random.shuffle(password_list)

    password = "".join(password_list) # join함수를 사용 하면 아래의 세줄을 한줄로 줄일수 있다.
    # password = ""
    # for char in password_list:
    #   password += char
    password_entry.insert(0, password)
 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) ==0 : 
        messagebox.showinfo(title= "manger", message="Please make sure you haven't left any fields empty." )
    else:
        
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}"
                            f"\n password: {password} \n Is it ok to save")
        
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END) # add를 클릭했을때 이 두부분이 삭제된다.
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx= 50 , pady= 50)

canvas = Canvas(width=200, height=200)
MyPass_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image=MyPass_img) # tomato_img변수를 가져온다.
canvas.grid(row=0, column=1)

# 라벨
websie_label = Label(text = "Website:")
websie_label.grid(row=1, column=0)
email_label = Label(text = "Email/Usernamer:")
email_label.grid(row=2, column=0)
password_label = Label(text = "password:")
password_label.grid(row=3, column=0)

# 엔트리
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus() # 실행시 포커스 조정
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "younsub@gmail.com") # 0번째로 입력해줘야지 실행지 가장 먼저 입력되어 출력된다.
password_entry = Entry(width=19)
password_entry.grid(row=3, column=1,columnspan=1)

# 버튼
generate_password_buton = Button(text="Generate Password", command=generate_password)
generate_password_buton.grid(row=3, column=2)
add_button = Button(text="Add", width=36 , command= save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()