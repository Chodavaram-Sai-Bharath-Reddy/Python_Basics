str1 = "hello this is a string"
list1 = str1.split()

print(str1[0])
print(str1[0:])
print(str1[2:8])
print(str1[2::1])
print(list1)

for i in range(0, len(str1)):
    print("index value of {} is {}".format(str1[i], str(i)))

str2 = 'bharath'
print(str2*3)

str3 = "   Hi, My name is "

print(str3+str2.upper())
print(str3.lower())
print((str3+str2).title())
print((str3+str2).capitalize())
print(str2.find('a'))
print(str2.rfind('a'))
print(str2.count('a'))
print(str2.upper().center(40, '*'))
print(str3.lstrip().upper()+str2.upper())
print('s' in str3)
print(len(str3))