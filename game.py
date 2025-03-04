from question import QuestionLibrary

class Game:
    def __init__(self, filename="trivia.json", category=None, difficulty=None, number=None):
        self.library = QuestionLibrary(filename)
        self.questions = self.library.get_questions(category=category, difficulty=difficulty, number=number)
        self.score = 0

    def play(self):
        for question in self.questions:
            print(question)
            while True:
                try:
                    user_answer = int(input("Enter the number of your answer: "))
                    if 1 <= user_answer <= 4:
                        break
                    else:
                        print("Please enter a number between 1 and 4.")
                except ValueError:
                    print("Please enter a valid number.")

            if user_answer == question.answer_id:
                if question.difficulty == "easy":
                    self.score += 1
                elif question.difficulty == "medium":
                    self.score += 2
                elif question.difficulty == "hard":
                    self.score += 3
                print("Correct!")
            else:
                print("Incorrect!")
            print(f"Your current score is: {self.score}\n")

        print(f"Game over! Your final score is: {self.score}")

game = Game(category="Geography", difficulty="easy", number=2)
game.play()