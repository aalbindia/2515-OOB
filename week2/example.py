import mail
print(mail.check_email('aalbindia@my.bcit.ca'))
#returns True

#Instead of using mail.function
from mail import check_email
print(check_email("email"))
#returns False

import email

def print_email(address):
    is_valid = mail.check_email(address)
    print(f"{address} is valid: {is_valid}")