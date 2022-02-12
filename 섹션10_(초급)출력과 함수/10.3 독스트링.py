# Docstrings 독스트링은 기본적으로 작은 문서를 만든느 방법이다.

def format_name(f_name, l_name): # 아래줄 들여쓰기를 한 첫 번재 줄이 독스트링이 된다
    """Take a first and last name and format it to return the title case version of the name, 
    이름과 성을 가져와서 이름의 대/소문자 버전을 반환하도록 형식 지정합니다."""
    # 독스트링을 사용하면 원하는 만큼 줄을 작성할수 있고 작성한 내용 모두가 동일한것으로 해석한다.
    if f_name == "" or l_name =="": 
        return "You didn't provide valid inputs. " 
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f"Result: {format_f_name} {format_l_name}" 
