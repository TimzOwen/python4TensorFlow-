# create a questions class to keep track of user input and answers
class Question:
    def __init__(self, prompt, answers):
        self.prompt_user = prompt
        self.choose_answer = answers
