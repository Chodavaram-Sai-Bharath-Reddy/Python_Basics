d1 = {}
d2 = {1: 'coffee', 2: 'tea', 3: 'milk'}

print(d2[3])

d2[4] = 'latee'

print(d2)

d2[1] = 'milk'

d2[3] = 'coffee'

print(d2)

d2.popitem()
print()

d2.pop(3)

print(d2)

d2.setdefault(3, 'coffee')
d2.setdefault(4, 'latee')
print(d2)


d2.update({5: 'expresso', 6: 'double shot expresso'})
print(d2)
