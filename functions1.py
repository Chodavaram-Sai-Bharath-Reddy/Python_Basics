def display1():
    print('welcome')


def display2(name):
    print('Welcome {}'.format(name))


def add(x, y):
    return x+y


def operations(x, y):
    return x+y, x-y


def greeting(name, msg='How are you?'):
    print("Good Morning {}. {}".format(name, msg))


def alarm1(name, msg):
    print("{} {}".format(name, msg))


def alarm2(name, *msg):
    print("{}".format(name), end=" ")
    for val in msg:
        print(val, end=" ")


display1()

display2('Bharath')

print(add(100, 200))

r1, r2 = operations(400, 100)
print(r1, r2)

greeting('Bharath', 'How are you today?')

greeting('Sai Bharath')

alarm1(msg='Wake up', name='Bharath')

alarm2('Bharath', 'Wake up', 'It\'s late', 'time to go!!')
