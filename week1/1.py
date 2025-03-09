def do_stuff(a,b):
    return a + b

d = {
    "name": "Allen",
    "number": 123 
}

d.update({"name": "Tim"})
print(d)
#python -i creates responsive terminal

#list comprehension
l = [1,2,3,4,5,6,7,8]
l = l* 2
new_list = []
for elem in l:
    new_list.append(elem)
print(new_list)

print([elem * 2 for elem in l])


