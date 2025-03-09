import random
import json
class Question:
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        self.question = question
        self.correct_answer = correct_answer  
        self.category = category
        self.difficulty = difficulty
        self.incorrect_answers = incorrect_answers

        self.answers = incorrect_answers + [correct_answer]
        random.shuffle(self.answers)

        self.answer_id = self.answers.index(correct_answer) + 1

        

    def __str__(self):
        output = f'Question: {self.question}\n'
        for k, v in enumerate(self.answers, start=1):
            output += f'{k}. {v}\n'
        
        return output.strip()

class QuestionLibrary:
    def __init__(self, filename='trivia.json'):
        self.questions = []
        with open(filename, 'r') as file:
            data = json.load(file)
            
            for record in data:
                question = Question(question=record["question"], correct_answer=record["correct_answer"], incorrect_answers=record["incorrect_answers"], 
                                    category=record["category"], difficulty=record["difficulty"])
                self.questions.append(question)
        
    def get_categories(self):
        categories = set()
        for cat in self.questions:
            categories.add(cat.category)
        return list(categories)
    
    def get_questions(self, category=None, difficulty=None, number=None):
        filtered = []
        for question in self.questions:
            if (category is None or question.category == category) and \
                (difficulty is None or question.difficulty == difficulty):
                filtered.append(question)
        
        if number is not None:
            return filtered[:number]
        return filtered
        
            


        
    
                        




    
        
        


    
        