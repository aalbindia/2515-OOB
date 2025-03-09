""""
ACIT2515 Lab

Week 2 -- complete this file!

"""
import random

# The number of turns allowed is a global constant
NB_TURNS = 10


def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    with open('word.txt', 'r') as f:
        words = [word.strip().upper() for word in f.readlines()]
        random_word = random.choice(words)
    return random_word

def reveal_letters(word, letters): 
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).
    Make sure all letters are separated by a space, then return the string.

    DO NOT USE PRINT!

    Example:
    >>> reveal_letters("VANCOUVER", ["A", "V"])   
    'V A _ _ _ _ V _ _'
    >>> reveal_letters("TIM", ["G", "V"])
    '_ _ _'
    >>> reveal_letters("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    word = word.upper()
    letters =[letter.upper() for letter in letters]

    result = ''
    for letter in word:
        if letter in letters:
            result = result + f'{letter}'
        else:
            result + '_'
    return result






def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    word = word.upper()
    letters = [letter.upper() for letter in letters]
    for letter in word:
        if letter not in letters:
            return False
    return True
    
    
def main(turns):
    """
    Runs the game. Allows for 'turns' loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the reveal_letters function to display hints about the word
    5. Remove 1 from the number of tries left
    6. Check if the player:
        - won (= word has been found)
        - lost (= word has not been found, no tries left)
    """
    word = pick_random_word()
    letters_tried = []
    print(f'Welcome to HangMan, you have {turns} left')
    
    while turns > 0:
        print('The current word is: ', reveal_letters(word, letters_tried))
        user_guess = input('Enter a letter or whole word').upper()
    

        if user_guess in letters_tried:
            print(f'You have already tried {user_guess}, please try again')
            continue

        letters_tried.append(user_guess)

        if all_letters_found(word, letters_tried):
            print(f'You have guessed the word {word}')
            return
        turns -= 1
        print(f'You have {turns} left')
    print(f'You have lost the word was {word}')
        

if __name__ == "__main__":
    main(NB_TURNS)