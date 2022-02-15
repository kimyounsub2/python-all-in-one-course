###########################################
# 퀴즈 프로젝트 1부: 질문클래스 만들기

# Question이라는 새 클래스를 만드세요
# Question앞에 text와, answer, 두 속성을 초기화 하는 init 메소드가 있어야 한다.
# 이 각각의 문제들은 self.text 와 self.answer이라는 두개의 속성이 있다.

class Question:
    def __init__(self, q_text, q_answer): # 객체를 만들 때 초기화된다.그래서 init 함수가 필요
        self.text = q_text
        self.answer = q_answer

# 문제가될 텍스트와 대답으로서 treu.false가 있다
# new_q = Question("질문","False")
# print(new_q.text)