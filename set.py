s1 = set()
s2= {24, 32, 12, 45}

print(s2)

s1.add(10)
s1.update([100, 200], s2)

print(s1)

s3 = s1.copy()
s4 = s1

print(id(s3), id(s1))
print(id(s4), id(s1))

print(s1.pop())

s1.remove(100)

print(s1)

# s1.remove(1000)  throws error
s1.discard(1000)

print(s1)

s1 = {10, 20, 30 , 40}
s2 = {30 , 40, 50, 60}

print(s1.union(s2))

print(s1.intersection(s2))

print(s1.difference(s2))

print(s2.difference(s1))

print(s1.symmetric_difference(s2))

