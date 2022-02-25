import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # html 모듈 안에 있는 unescape라는 메소드를 사용해서 API로 부터 받은 self.current_question.text 이문자열을 unescape해준다.
        q_text = html.unescape(self.current_question.text) # 우리가 API로부터 받은 텍스트를 사용하는 대신에 우리는 HTML모듈을 임포트 해야한다.
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
