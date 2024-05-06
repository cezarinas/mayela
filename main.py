from data import question_data
from question_model import Question

question_bank = []
for question in question_data:
    n = Question(question["text"], question["answer"])
    question_bank.append(n)
print(question_bank[1].text)