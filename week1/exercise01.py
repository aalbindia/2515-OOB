def str2dict(a):
    d = {}
    for i in a:
        if i == '': #skips empty spaces
            continue
        if i not in d: 
            d[i] = 1
        else:
            d[i] += 1
    return d

print(str2dict('hello'))

import re
def str2dict_plus(b):
    b = re.sub(r'[^\w\s]', '', b) #r = tells python string is a raw string
    #^
    return str2dict(b)
    
print(str2dict_plus('hello!'))

def histogram(a):
    no_duplicates = set(a)
    for i in no_duplicates:
        count = a.count(i)
        print(f'{i} {'*' * count}') #when not properly indented, only prints out the last iteration of the loop 'n *'


        
histogram('allen')











    
