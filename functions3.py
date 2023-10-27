from functools import reduce
# some inbuilt functions

s = lambda x: x * x

print(s(4))

l = list(range(1, 21))

even = list(filter(lambda x: x if x % 2 == 0 else None, l))

square = list(map(lambda x: x*x, l))

print(even)
print(square)

total = reduce(lambda x, y: x+y, l)
print(total)
