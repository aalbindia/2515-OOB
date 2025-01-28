
import random

NB_TURNS = 10

class SecretWord:
    def __init__(self, word=None):
        if word is not None:
            # Make sure our word is always uppercase
            self.word = word.upper()
            return
            
        with open("words.txt") as fp:
            lines = fp.readlines()
            word = random.choice(lines)
            # Make sure our word is always uppercase
            self.word = word.strip().upper()

    def show_letters(self, letters):

        uppercase = [let.upper() for let in letters]
        filtered = [letter if letter in uppercase else "_" for letter in self.word]
        return " ".join(filtered)


    def check_letters(self, letters):
        """Returns True if all letters in word are in the list 'letters'"""
        return "_" not in self.show_letters(letters)
    
    def check(self, text):
        return self.word == text.strip().upper()


def main(turns):
    # These are the letters tried by the player
    letters = []
    # Get a word
    word = SecretWord()
    # Cheat: this is the word we are looking for
    print(word.word)

    # We can assume that turns will be > 1 the first run
    print(word.show_letters(letters))

    for turn_number in range(turns):
        # Ask the player for a letter
        letter = ""
        while letter.upper() not in letters:
            letter = input("Letter? ")
            if letter.upper() not in letters:
                letters.append(letter.upper())
            else:
                print("You already tried this.")
        # Show the hint
        print(word.show_letters(letters))

        # Check if we win
        if word.check_letters(letters):
            print("You win!")
            return True

    print("You lost!")






class Game:
    def __init__(self, turns = NB_TURNS):
        self.turns = turns
        self.secret_word = SecretWord()
        self.letters_tried = []
    
    def play_one_round(self):
            user_input = input('Enter a letter: ').upper()
            #check if input is a word
            if len(user_input) > 1:
                self.turns -= 1 #automatically take off a turn since guessing the whole word
                if self.secret_word.check(user_input):
                    print('You have guessd the word')
                    return True
                else:
                    print('Guessed wrong')
                    return False
            #check if input is a letter
            elif len(user_input) == 1:
                if user_input in self.letters_tried:
                    print('You have already tried that letter')
                    return False
                self.letters_tried.append(user_input) #if not in letters_tried append letter automatically
               
                
                if user_input in self.secret_word.word:
                        print('Correct Letter!')
                else:
                    print('Incorrect guess')
                    self.turns -= 1

                print(self.secret_word.show_letters(self.letters_tried))
                if self.secret_word.check_letters(self.letters_tried):
                        print('You have guessed all letters')
                        return True
                    
            else:
                print('Invalid input, enter only a letter or word')
                return False
            return False
            
    def play(self):
        while self.turns > 0:
            if self.play_one_round():
                print('You win!')
                return True
            if self.turns == 0:
                print('No turns left')
                return False
        print('Game over!')
        return False

        
        


if __name__ == "__main__":
    my_game = Game(10)
    my_game.play()