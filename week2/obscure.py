#improper way
# def obscure_text_1(text):
#     new_text = ''
#     text = text.lower()
#     text = text.split()
#     for word in text:
#         for letter in word:
#             if letter == 'o':
#                 new_text += '0'
#             if letter == 'e':
#                 new_text += '3'
#             if letter == 'I':
#                 new_text += '1'
#             if letter == 'l':
#                 new_text += '|'
#             if letter == 'a':
#                 new_text += '@'
#     return new_text

            
# print(obscure_text_1('HellO'))

def obscure_text(text):
    substituions = {
        "o": '0',
        'O': '0',
        'e': '3',
        'E': '3',
        'I': '1',
        'l': '|',
        'a': '@'
    }
    new_text = []

    for letter in text:
        if letter in substituions:
            new_text.append(substituions[letter])
        else:
            new_text.append(letter)
    return ''.join(new_text)

