class Start:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



question_prompts = [
    "Which country won the 2010 FIFA World Cup?\n(a) Spain\n(b) Netherlands\n(c) France \n",
    "Which team has won the most Super Rugby titles?\n(a) Blues\n(b) Hurricanes\n(c) Crusaders \n",
    "Who has the most All Black caps?\n(a) Aaron Smith\n(b) Richie Mccaw\n(c) Kieran Reid \n",
]

questions = [
    Start(question_prompts[0], "a"),
    Start(question_prompts[1], "c"),
    Start(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
