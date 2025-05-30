import json


with open('question.json', 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question"])
    for index, alternative in enumerate(question["answers"]):
        print(index + 1, "-", alternative)
    answer = int(input("Enter your answer: "))
    question["user_choice"] = answer

score = 0

for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct answer!"
    else:
        result = "Incorrect answer"


    message = f"{result} {index + 1} Your answer: {question["user_choice"]}, Correct answer: {question["correct_answer"]}"
    print(message)