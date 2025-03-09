# 
#     Registers a user by returning a dictionary with their details.
#     Parameters:
#         user_id (str): The user's unique ID.
#         username (str): The username.
#         is_admin (bool): Whether the user is an admin (default: False).
#         is_active (bool): Whether the user is active (default: True).
#     Returns:
#         dict: A dictionary containing the user's information.
#     

def register_user(user_id,username,is_admin = False,is_active = True):
    user_dictionary = {
        "user_id": user_id,
        "username": username,
        "is_admin": is_admin,
        "is_active": is_active
    }

    return user_dictionary
print(register_user("U001", "Alice"))
print(register_user("U003", "Charlie", is_active=False))



"""
    Validates the given name. Raises a RuntimeError if the name is "Admin".
    Parameters:
        name (str): The name to validate.
    Returns:
        None
    """
def validate(name):
    try:
        if name == 'Admin':
            raise RuntimeError('Admin name is not allowed.')
        else:
            print(f'Welcome {name}')
    except RuntimeError as e:
        print(f' Invalid name provided {e}')

validate("Admin")

with open('log.txt', 'w') as f:
    f.write('Line 1: File Handling in Python')
with open('log.txt', 'r') as file:
    text = file.readline()
    print(text)

    