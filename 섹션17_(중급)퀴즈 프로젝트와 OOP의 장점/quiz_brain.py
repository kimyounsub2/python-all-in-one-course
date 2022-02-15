#########################
# 퀴즈 프로젝트 3부: 퀴즈브레인과 next_question()메소드
# QuizBrain 이 클래스에는 두 속성이 있다. 
# question_number로 디폴트 값이 0이다(질문은 항상 첫번째 부터 시작하니까) 또한 사용자가 어떤 질문을 보고 잇는지 추적한다.
# question_list는 QuizBrain객체가 초기화될때 전달된다.

class QuizBrain:
    
    def __init__(self, q_list): # 객체를 만들 때 초기화된다.그래서 init 함수가 필요
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    
# 퀴즈 프로젝트 4부: 새로운 질문을 계속 보여주는 방법
# still_has_questions이라는 메소드를 만들고 17.2 퀴즈 프로젝트.py에서 while 반복문을 만든다. 
# if문을 사용해서 퀴즈가 아직 남아 잇는지 확인        
    def still_has_questions(self):
        
        if self.question_number < len(self.question_list):
            return True
        else:
            False
            
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)

# 퀴즈 프로젝트 5부: 답변을 확인하고 점수 유지하기
# check_answer() 이 메소드는 사용자가 입력한 답을 확인하고 그것이 정답인지    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Te correct answer was: {correct_answer}.")    
        print(f"Your current score is: {self.score}/{self.question_number} ")
        print("\n")
        