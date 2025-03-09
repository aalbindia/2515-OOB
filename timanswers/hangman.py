"""
ACIT2515 Lab
Tim G @ ACIT2515
"""
import random
import sys

def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    with open("words.txt") as fp:
        lines = fp.readlines()
        word = random.choice(lines)
        return word.strip()


def reveal_letters(word, letters):
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> reveal_letters("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> reveal_letters("TIM", ["G", "V"])
    '_ _ _'
    >>> reveal_letters("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    uppercase = [let.upper() for let in letters]
    word = word.upper()
    filtered = [letter if letter in uppercase else "_" for letter in word]
    return " ".join(filtered)


def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""

    # Very easy - if there is a "_" left, we did not find all letters...
    return "_" not in reveal_letters(word, letters)

    # OPTION 2
    # Substracting the set of letters from the set of word should be the empty set
    return set(word.upper()) - set([let.upper() for let in letters]) == set()



def main(turns, word=None):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the reveal_letters function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    # These are the letters tried by the player
    letters = []
    
    # Get a word
    if word is None:
        word = pick_random_word()
    
    # Cheat: this is the word we are looking for
    print(word)

    # We can assume that turns will be > 1 the first run
    print(reveal_letters(word, letters))

    for turn_number in range(turns):
        # Ask the player for a letter
        letter = ""
        keep_going = True
        while keep_going:
            letter = input("Letter? ")
            # Make it uppercase
            letter = letter.upper().strip()

            if letter == "":
                print("You have to provide a letter.")
            elif len(letter) > 1:
                if letter.upper() == word.upper():
                    print("You found the word!")
                else:
                    print("This is not the word.")
                keep_going = False
            elif letter in letters:
                print("You already tried this letter.")
            else:
                letters.append(letter.upper())
                keep_going = False

            # Check if we win
            if all_letters_found(word, letters) or letter.upper() == word.upper():
                print("You win!")
                return True
        
            # Show the hint
            print()
            print("Showing with letters:", " ".join(sorted(letters)))
            print(reveal_letters(word, letters))
            print()

    print("You lost!")


if __name__ == "__main__":
    turns = 10
    word_to_find = None
    
    # We have a number of turns provided
    if len(sys.argv) >= 2:
        turns = int(sys.argv[1])
    
    # We have a word provided
    if len(sys.argv) >= 3:
        word_to_find = sys.argv[2].strip()

    try:
        main(turns, word=word_to_find)
    except KeyboardInterrupt:
        print()
        print("You don't like the game? Bye!")
    
