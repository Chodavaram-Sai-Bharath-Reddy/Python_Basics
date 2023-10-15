# if

a, b = [int(x) for x in input().split()]

# if - elif - else
if a < b:
    print("b is big")

if a > b:
    print("a is big")
elif b > a:
    print("b is big")
else:
    print("both are equal")

# for loop

for i in range(1, 11, 1):
    print(i, end=" ")
print('\n')

for i in range(1, 20, 1):
    if i % 2 == 0:
        print(i, end=" ")
print('\n')

for i in range(1, 20, 1):
    if i % 2 != 0:
        print(i, end=" ")
print('\n')

list1 = [10, 20, 30, 20, 50]

for item in list1:
    print(item, end=" ")
print('\n')

i = 1
while i < 11:
    print(i, end=" ")
    i += 1
