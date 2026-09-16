from questionmodel import Question
from data import question_data
from quizbrain import QuizBrain
questions = [Question(q["text"], q["answer"]) for q in question_data]
quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz completed! Your final score is: {quiz.score}/{len(questions)}")
