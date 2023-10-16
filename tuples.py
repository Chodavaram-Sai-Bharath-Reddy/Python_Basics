a = (10, 23, 98, 34, 21)
print(a[0])
print(a[1:])
print(a[::-1])

# a[3] = 10 not possible

b = (32, 12, 67, 43)

print(a.index(23))
print(b.count(23))

print(max(a))
print(min(b))

a += b
print(a)

num1 = 10
num2 = 54
num3 = 67

tup1 = num1, num2, num3
print(type(tup1))

number1, number2, number3, number4 = b

print(number1, number2, number3, number4)