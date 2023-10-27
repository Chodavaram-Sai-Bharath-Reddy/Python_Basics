people = ['tharun', 'ramesh', 'sureesh', 'ravi', 'mohan']
person = 'david'
customers = ['ram', 'surya']

people.append(person)
print(people)
customers.extend(people)
print(customers)
customers.remove('ram')
print(customers)
customers.pop()
print(customers)
customers.append('lakshman')
print(customers)
customers.insert(2, 'ram')
print(customers)
print(customers.count('ravi'))
print(len(customers))
print(customers.index('lakshman'))
customers.sort()
print(customers)
customers.reverse()
print(customers)

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list,
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new
# list.
list1 = ["M", "na", "i", "Ke", "j", "k"]
list2 = ["y", "me", "s", "lly", "ames", "evin", "ary"]
list3 = []

if len(list1) == len(list2):
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
elif len(list1) >= len(list2):
    for i in range(len(list2)):
        list3.append(list1[i] + list2[i])
    for item in list1[-(len(list1)-len(list2)):]:
        list3.append(item)
else:
    for i in range(len(list1)):
        list3.append(list1[i] + list2[i])
    for item in list2[-(len(list2)-len(list1)):]:
        list3.append(item)

print(list3)

#  Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for item in list1:
    if item == "":
        list1.remove(item)
print(list1)

# Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]

num1 = list(map(lambda x: x*x, numbers))

print(num1)

#  Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for item in list1:
    if item == "":
        list1.remove(item)
print(list1)
