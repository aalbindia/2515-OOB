'''
1. Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).

'''

def user_info():
    user_age = int(input('Enter your age: '))
    user_name = input('Enter your name: ')
    year = 2025 - user_age + 100
    print(f'{user_name} will turn 100 in {year}')

user_info()


'''
2. Odd or even input
'''

def oddeven():
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        print('Number is Even')
    else:
        print('Number is odd')


oddeven()

'''
3. List Ends
'''
def ends(ls):
    return ls[0], ls[len(ls) - 1] #counts number of items in list, -1 for exclusion and then indexes at the last number to get it

print(ends([1,2,3,4,5]))

'''
20. Element Search
- Write a function that takes an ordered list of numbers (a list where the elements are in order 
from smallest to largest) and another number. The function decides whether or not 
the given number is inside the list 
and returns (then prints) an appropriate boolean. 
'''

def element_search(input_list, number):
    ordered_list = sorted(input_list)
    for num in ordered_list:
        if num == number:
            return True
    return False
    
        
print(element_search( input_list= [1,2,4,6,5,3],number= 4))

'''
39. Character Input Datetime
'''

import datetime

def character():
    year = datetime.datetime.now().year
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    print(f'{user_name} will turn 100 by {year - user_age + 100}')

character()

    
'''
33. Birthday Dictionaries
'''
import time
def dictionaries():
    stored_birthdays = {
        "Albert Einstein": "2006-07-02",
        "Steve": "2001-06-01",
        "Allen": "2006-12-08"
    }

    print("\nWelcome to the birthday dictionary we know the birthdays of:")
    for name in stored_birthdays:
        print(name)
        time.sleep(1) #simply waits 1 second after printing a name
    user_input = input('\nWhos birthday you want to look up?: ')
    if user_input in stored_birthdays:
        print(f'{user_input}s birthday is {stored_birthdays[user_input]}')

dictionaries()

'''
28. Max of three
'''
def three(a,b,c):
    print(max(a,b,c))
#without max
three(1,2,3)

def max_of_three(a,b,c):
    max_of_func = 0
    if a > b:
        if a > c:
            max_of_func = a
        else:
            max_of_func = c
    else:
        if b > c:
            max_of_func = b
        else:
            max_of_func = c
    return max_of_func

print(max_of_three(20,2,3))



