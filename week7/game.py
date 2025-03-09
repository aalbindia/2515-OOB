from week5.question import Question, QuestionLibrary

class Game:
    def __init__(self, filename = "trivia.json", category = None, difficulty=None, number=None):
        self.library = QuestionLibrary(filename)
        self.questions = self.library.get_questions(category=category, difficulty=difficulty, number=number)
        print(f"Loaded {len(self.questions)} questions")
        self.score = 0

    def play(self):
        for question in self.question:
            print(question.questions)
            for idx, answer in enumerate(question.answers, start= 1):
                print(f'{idx}. {answer}')

        while True:
            try:
                choice = int(input('Enter an answer: '))
                if choice in {1,2,3,4}:
                    break
                else:
                    print('Invalid input, try again')
            except ValueError:
                print('Wrong value.')
            
            if choice == question.correct_answer:
                points = {"easy": 1, "medium": 2, "hard": 3}.get(question.difficulty, 0)
                self.score += points
                print('You got the right answer!')
            else:
                print(f'You got the wrong answer, the correct answer was {question.correct_answer}')

        print(f'Game over, your score is {self.score}')

        