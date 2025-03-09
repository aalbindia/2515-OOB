def count_lines(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = ''.join(data)
        data = data.split()
        print(len(data))
             
        
        
(count_lines('people_1.txt')) #should return 8



def list_unique(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
        data = ''.join(data)
        unique_names = set(data.split())
        sorted_names = sorted(list(unique_names))
        for name in sorted_names:
            print(name)
            
list_unique('people_1.txt')