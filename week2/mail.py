'''
Modules
- Creating your own libraries
- If you create a file/module with the same name as a Python Library, you want have access to that module.
- File should be in same folder path
- Be in the correct directory: cd .\

import function
or (better-way) from function import function

- circular imports are bad practice

Unit Testing
- Using pytest, to test/check our code
- adding test_ infront of function tells Python this is a test function
- always resave function before testing
- to test: pytest .\filename.py
- Should not have your Unit test in the same file as your production code
- If you run pytest, it will look for every function that has test_ and test it.

'''

def check_email(address):
    if 'a' not in address:
        return False
    if '.' not in address:
        return False
    return True

#'email@.bcit.ca' ==> True
# 'email' ==> False

#adding test_ infront of function, tells Python this is a test function

# def test_check_email():
#     assert check_email("example@my.bcit.ca") == True
#     assert check_email("somewhere") == False

# def test_check_email_bogus():
#     assert check_email("yes.no@mybcit") == False