'''
Write a function calculate_discount that calculates the final price after applying a percentage discount. 
The function should take three parameters: price (required), discount (default to 10%), and is_member (default to False). 
If is_member is True, apply an additional 5% discount. Return the final price.

Create a function divide_numbers that takes two arguments, a and b, and returns the result of dividing a by b.
 If b is zero, raise a ValueError with the message "Cannot divide by zero." 
 Use a try...except block to catch the exception and print an appropriate error message.

Write a program that reads lines from a file called input.txt and writes only those lines 
containing the word "Python" (case-sensitive) to a file named output.txt. 
Use the with statement for safe file operations.
'''

def calculate_discount (price,discount = 10,is_member = False):
    discount = discount / 100 
    if is_member:
        discount_member = discount + .05
        discount_price = price * discount_member
        final_price = price - discount_price
    else:
        discount_price = price * discount
        final_price = price - discount_price
        
    return final_price

print(calculate_discount(100))
print(calculate_discount(200, discount = 20, is_member= True))

def divide_numbers(a,b):
    
    try:
        if b == 0:
            raise ValueError('Cannot divide by Zero')
        quotient = a / b
        return quotient
    except ValueError as e:
        print(e)
        return None

print(divide_numbers(10,0))

with open('input.txt', 'r') as f:
    text = f.readlines()
    with open('output.txt', 'w') as file:
        for line in text:
            if 'Python' in line: #writes whole line to txt instead of only Python
                file.write(line)
    
            
        




