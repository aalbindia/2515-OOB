#1.1
def str2dict(arg):
    dic = {}
    for i in arg:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic




import string
#1.2
def str2dict_plus(arg):
    translator = str.maketrans('', '', string.punctuation)#generic mapping to remove punctuation
    edited = arg.translate(translator).lower()
    
    return str2dict(edited)

print(str2dict_plus('AaL0'))

def histogram(arg):
    edited = set(arg)
    for i in edited:
        count = arg.count(i)
        print(f'{i} {'*' * count}')

histogram('Hello World')
        