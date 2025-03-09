'''
2 Chili Q's - Progressing One chili at a time
'''

'''
3. List Less Than Ten🌶️🌶️
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for elem in a:
    if elem < 5:
        b.append(elem)
print(b)

'''
4. Divisors
'''

number = int(input('Enter a number: '))
divisors = []
ListRange = list(range(1, number + 1))
for num in ListRange:
    if number % num == 0:
        divisors.append(num)
print(divisors)

'''
5. List Overlap
'''
c = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_list = [val for val in c if val in d]
#list comprehension makes it easier to loop and compare values

print(set(common_list))

'''
6. String Lists
'''
#level
user_string = input('Enter a string: ')
reversed_string = user_string[::-1]#simply slice from end of string to start
if user_string == reversed_string:
    print('Your input is a palindrome')
else:
    print('Not a palindrome')

'''
List Comprehension
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [elem for elem in a if elem % 2 == 0] #Don't need to append to empty list since saves elem in list 'list comprehension'
print(b)

'''
10. List Comprehension Overlap
'''

a = [1,2,3,4,5,6,7,20,30]
b = [1, 1, 30, 40 , 6 , 7, 8, 20]
c = [ elem for elem in a if elem in b]
print(c)

'''
12. Fibonacci
'''

def generate_fib():
    count = int(input('How many fibonacci numbers you want to generate? '))
    i = 1
    fib = []
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i - 1]) #at this point i is currently 1, and so index the second position in the list (1) and then add fib index 0 in this case 
            i +=1 #keep increasing i by one to keep on adding
    return fib

print(generate_fib())

'''
14. List Remove Duplicates
'''
#without sets
def duplicate(ls):
    new_list = []
    for item in ls:
        if item not in new_list:
            new_list.append(item)
        else:
            print(f'{item} is already inside list')
    return new_list

print(duplicate([1,1,1,2,3,4,4,5]))

'''
23. File Overlap
'''
# prime = []

# with open('one.txt', 'r') as file:
#     data = file.readline()
#     while data: #as long as theres a line being read, while loop keeps going
#         prime.append(int(data))
#         data = file.readline()
# happy = []
# with open('other.txt', 'r') as file:
#     data_2 = file.readline()
#     while data_2:
#         prime.append(int(data_2))
#         data_2 = file.readline()


# overlapping_numbers = [num for num in prime if num in happy]

# print(overlapping_numbers)

'''
24. Draw A Game Board
'''
board_size = int(input('How large you want your board to be (e.g. 3 = 3x3) '))
def vertical():
    print('|    ' * (board_size + 1)) #add 1 to board size, to add the end barrier

def horizontal():
    print(' --- ' * board_size)

for _ in range(board_size): #create a loop, to keep on making each new line
    horizontal()
    vertical()
horizontal()

'''
26.  Check Tic Tac Toe
'''

game = [[1,2,0],
        [0,1,0],
        [1,0,1]]


'''
Tic Tac Toe 
'''


'''
30. Pick Word
'''
import random
def pick_word():
    with open('week2.txt', 'r') as file:
        words = [word.strip() for word in file.readlines()]
        random_word = random.choice(words)
    return random_word
    
print(pick_word())
'''
Birthday JSON
'''

'''
37. Functions Refactor
'''

'''
Read from a file
'''








