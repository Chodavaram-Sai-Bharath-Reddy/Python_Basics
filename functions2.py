# local and global variables
a = 1000


def addition(x):
    print(a+x)


def subtraction(x):
    print(a-x)


def mul(x):
    a = 20
    print(a*x)


def division(x):
    global a
    a = 200
    print(a/x)


addition(10)
subtraction(10)
mul(10)
division(10)
