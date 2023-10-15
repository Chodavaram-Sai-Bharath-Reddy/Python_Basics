#Identifiers and Data Types

a = int(input('Enter a integer value : '))
b = float(input('Enter a float value : '))
com = complex(3, 5)
isCompleted = True
welocme = "Hi welcome to the page!!!"
smallNum = bytes(12)
smallNumArray = bytearray([1, 23, 45])
naturalNumbers = range(1, 11, 1)
names = ['ravi', 'hari', 'sureesh']
fixedValues = (1, 2, 5, 65)
numberSet = {1, 2, 2, 76, 12, 23, 4, 2}
numberFrozenSet = frozenset({1, 23, 43, 27, 24, 67, 38, 23, 24})
lookup = {1: 'one', 2: 'two', 3: 'three'}
index = None

print(type(a), a)
print(type(b), b)
print(type(com), com)
print(type(isCompleted), isCompleted)
print(type(welocme), welocme)
print(type(smallNum), smallNum)
print(type(smallNumArray), smallNumArray)
print(type(naturalNumbers), naturalNumbers)
print(type(names), names)
print(type(fixedValues), fixedValues)
print(type(numberSet), numberSet)
print(type(numberFrozenSet), numberFrozenSet)
print(type(lookup), lookup)
print(type(index), index)
