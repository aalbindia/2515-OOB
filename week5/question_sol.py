import random
import json

class Question:
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.category = category
        self.difficulty = difficulty

        # Combine correct and incorrect answers and shuffle them
        self.answers = incorrect_answers + [correct_answer]
        random.shuffle(self.answers)

        # Find the index of the correct answer and adjust to start at 1
        self.answer_id = self.answers.index(correct_answer) + 1

    def __str__(self):
        # Display the question and answers with indexes starting at 1
        question_str = f"{self.question}\n"
        for idx, answer in enumerate(self.answers, start=1):
            question_str += f"{idx} {answer}\n"
        return question_str.strip()
    


class QuestionLibrary:
    def __init__(self, filename="trivia.json"):
        self.questions = []
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                question = Question(
                    question=item['question'],
                    correct_answer=item['correct_answer'],
                    incorrect_answers=item['incorrect_answers'],
                    category=item['category'],
                    difficulty=item['difficulty']
                )
                self.questions.append(question)

    def get_categories(self):
        categories = set()
        for question in self.questions:
            categories.add(question.category)
        return list(categories)

    def get_questions(self, category=None, difficulty=None, number=None):
        filtered_questions = []
        for question in self.questions:
            if (category is None or question.category == category) and \
               (difficulty is None or question.difficulty == difficulty):
                filtered_questions.append(question)
        
        if number is not None:
            return filtered_questions[:number]
        return filtered_questions