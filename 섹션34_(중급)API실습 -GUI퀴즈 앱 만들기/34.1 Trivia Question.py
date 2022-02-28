from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
# quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


# 출력했지만 출력 내용물 중에 알수 없는 문자들이 중간중간 들어가있는 경우가 있다
# 예를 들어  &quot;가 "(큰 따음표)라는것을 볼수가 있다. < -> &lt; 등등
# 우리가 실제로 보고 있는 건 HTML 개체라는 것인데 그리고 HTML에 있는 특정한 문자들을 교체하는 방법이 있다.
# Freeformatter라는 툴을 이용해서 우리가 API로부터 받는 HTML결과를 언이스케이핑(Unescape)해서 사람이 읽을수 있는 원래 형식으로 형식화 할수 있다.