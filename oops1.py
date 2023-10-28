class Sample1:
    def display(self):
        print('Welcome to Sample1')


s1 = Sample1()
s1.display()


class Sample2:
    def display(self, name):
        print('Welocme to Sample2 {}'.format(name))


s2 = Sample2()
s2.display('Bharath')


class Sample3:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print(a, b, c)
        print("hello")

    def display(self):
        self.aa = 100
        print(self.a, self.b, self.c)


s3 = Sample3(10, 330, 440)
s3.display()
s3.d = 550
print(s3.__dict__)
print(s3.a)

class Sample4:
    a = 1000
    def __init__(self):
        print(Sample4.a)
        Sample4.a = 2222
        print(self.a)
    def display1(self):
        print(Sample4.a)
        Sample4.a = 3333
        print(self.a)
    def display2(cls):
        print(Sample4.a)
        cls.a = 4444
        print(cls.a)

s4 = Sample4()
s4.display1()
s4.display2()
Sample4.a = 2000
print(Sample4.a)
del Sample4.a