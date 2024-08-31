from question_model import question
from data import question_data
from quiz import Quizbrain

quistion_bank = []
for quistion in question_data:
    quistion_text = quistion['text']
    quistion_answer = quistion['answer']
    new_quistion = question(quistion_text, quistion_answer)
    quistion_bank.append(new_quistion)

quiz = Quizbrain(quistion_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Thanks for completing that.\n Your final score is :{quiz.score}/{quiz.question_number}")