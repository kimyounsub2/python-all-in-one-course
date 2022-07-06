import os
import collections

# from sub.contact import Contact
# class Contact의 모듈화 
class Contact:
   def __init__(self, name, phone_number, e_mail, addr):
       self.name = name
       self.phone_number = phone_number
       self.e_mail = e_mail
       self.addr = addr

   def print_info(self):
       print("Name: ", self.name)
       print("Phone Number: ", self.phone_number)
       print("E-mail: ", self.e_mail)
       print("Address: ", self.addr)

def set_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")
    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def print_menu():
    print("1. 연락처 입력")
    print("2. 연락처 출력")
    print("3. 연락처 삭제")
    print("4. 종료")
    print("5. 수정")
    print("6. 연락처 이름 상세검색")
    print("7. 연락처 이름의 빈도수 정량/순위 분석")
    menu = input("메뉴선택: ")
    return int(menu)

def order_contact(contact_list):
    #1. 이름 리스트 생성
    c_list = []
    for contact in contact_list:
        c_list.append(contact.name)
    #2. 단어(이름)빈도수 사전 생성
    c_dict = collections.Counter(c_list)
    #3. 정렬 key를 구하는 람다식
    order_list = sorted(c_dict.items(), key=lambda x:x[1], reverse = True)
    return order_list


def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()    
        
# 연락처 이름으로 검색하여 새주소를 입력받아 기존 주소를 수정
def update_contact(contact_list):
    name = input("Name: ")
    for contact in contact_list:
        if contact.name == name:
            addr = input("NewAddress: ")
            contact.addr = addr
            contact.print_info()
            
# 연락처 이름 입력받아 검색하여 연락처 출력
def search_contact(contact_list):
    name = input("Name: ")
    for contact in contact_list:
        if contact.name == name:
            contact.print_info()
    
    
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]
            
def load_contact(contact_list):
    if os.path.exists("contact_db.txt"):
        f = open("contact_db.txt", "rt")
        lines = f.readlines()
        num = len(lines) / 4
        num = int(num)
    
        for i in range(num):
            name = lines[4*i].rstrip('\n')
            phone = lines[4*i+1].rstrip('\n')
            email = lines[4*i+2].rstrip('\n')
            addr = lines[4*i+3].rstrip('\n')
            contact = Contact(name, phone, email, addr)
            contact_list.append(contact)
        f.close()
            
def store_contact(contact_list):
    f = open("contact_db.txt", "wt")
    for contact in contact_list:
        f.write(contact.name + '\n')
        f.write(contact.phone_number + '\n')
        f.write(contact.e_mail + '\n')
        f.write(contact.addr + '\n')
    f.close()
    

def run(): # 메뉴번호와 함수를 매핑시켜 실행(컨트롤러,스위치)
    contact_list = []
    load_contact(contact_list)
    while 1:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            print_contact(contact_list)
        elif menu == 3:
            name = input("Name: ")
            delete_contact(contact_list, name)
        elif menu == 4:
            store_contact(contact_list)
            break
        elif menu == 5:
            update_contact(contact_list)
        elif menu == 6:
            search_contact(contact_list)
        elif menu == 7:
            print('연락처 이름:빈도수 내림차(역)정렬 리스트')
            print(order_contact(contact_list))
    

if __name__ == "__main__":
    run()