"""
Possible answers for lab 1.
Tim G @ ACIT2515
"""

def count_people(filename):
    """Reads the file and returns the length of the list = the number of lines"""
    with open(filename, "r") as fp:
        return len(fp.readlines())
print(count_people('people_1.txt'))

def count_lines(filename):
    number = 0
    with open(filename, "r") as fp:
        for line in fp:
            if line.strip() != "":
                number += 1


    print(number)
    return number

print(count_lines('people_1.txt'))

def list_unique(filename):
    # We start with a list
    
    names = []
    
    with open(filename, "r") as fp:
        data = fp.readlines()
        for line in data:
            clean = line.strip()
            # We only append non-empty lines
            if clean != "":
                names.append(clean)

    for unique_name in set(names):
        print(unique_name)
