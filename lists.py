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
