"""
Possible answers for lab 1.
Tim G @ ACIT2515
"""

import string
import operator


def str2dict(text):
    """Returns a dictionary where keys are letters and values number of times the letter appears"""

    return_value = {}

    # You can iterate through a string letter by letter
    for letter in text:
        # Using `in` with a dictionary matches on "keys" = letters
        if letter in return_value:
            return_value[letter] += 1
        else:
            # The letter is not in the dictionary: create the initial entry
            return_value[letter] = 1

    # Another approach, using sets

    # unique_letters = set(text)
    # for letter in unique_letters:
    #     return_value[letter] = text.count(letter)    

    return return_value


def str2dict_plus(text):
    """Fancy version of the previous function"""

    # We use string.punctuation to get all punctuation characters
    letters_to_remove = string.punctuation + " "

    # This is our new filtered string
    new_string = ""

    # Iterate through the string
    for letter in text:
        if letter not in letters_to_remove:
            # Add the letter to the string if it is not supposed to be filtered
            new_string += letter

    # Just reuse the previous function that already does the job
    return_value = str2dict(new_string.lower())
    return return_value


def histogram(text, sort="letters"):
    """Builds an histogram based on frequency of letters"""

    # The previous function already does the job...
    values = str2dict_plus(text)

    # Now iterate over the dictionary items (keys + values) for display
    # for letter, number in values.items():
    #     # Using `*` on a string repeats the string - "a" * 5 == "aaaaa"
    #     print(letter, "*" * number)
    
    # Below is a fancy version with sorting

    if sort == "letters":
        for letter in sorted(values.keys()):
            print(letter, "*" * values[letter])

    elif sort == "numbers":
        for letter, number in sorted(
            values.items(),
            key=operator.itemgetter(1),
            reverse=True
        ):
            print(letter, "*" * number)


def str2dic(text):
    d = {}

    for letter in text:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d

print(str2dic('hello'))

import string

def str2dic_plus(text):
    
    new_string = ''
    removed_string = string.punctuation + '' #we add '' because we want to remove spaces
    for letter in text:
        if letter not in removed_string:
            new_string += letter
    value = str2dic(new_string.lower())
    return value

print(str2dic_plus('Hello World!'))

def count_lines(filename):
    number = 0
    with open(filename, 'r') as f:
        data = f.readlines()
        for line in data:
            if line.strip() != '':
                number +=1
        return number

            




print(count_lines('people_1.txt'))
    
