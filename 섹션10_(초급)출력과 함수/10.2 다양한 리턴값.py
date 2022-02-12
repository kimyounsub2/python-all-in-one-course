def format_name(f_name, l_name): 
    if f_name == "" or l_name =="": # 만일 입력자가 입력을 안하고 엔터를치면 여기서 종료된다
        return "You didn't provide valid inputs. " # 이렇게 문구를 사용할수 있다.
    # 작업자가 입려하면 if문을 안타고 아래로 문구가 내려간다
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}" # return 함수가 들어가 있으면 마지막이다
    print("tThis ot printed") # 위에 return함수가 마지막으로 들어가 있어서 출력이 안된다.
    
print(format_name(input("What is your first name?"), input("whqt is your last name")))
