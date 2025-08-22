from question_model import Question
from data import question_data
import random




list_length = len(question_data)
print(list_length)


# Create question bank from questions.
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


print(question_bank[random.randint(0, len(question_bank) - 1)])


#      print(question_data["text"])
#     # print(data.question_data[i]["answer"])


# question1 = Question("A slug's blood is green.", "True")
# print(question1.text)
# print(question1.answer)