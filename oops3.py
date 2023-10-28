# poloymorphism
# overloading is not possible in python

class Sample1:
    def __init__(self):
        print("constructor in Sample1")
    def display(self):
        print("hello")
class Sample2(Sample1):
    def __init__(self):
        print("constructor in Sample2")
    def display(self):
        print("Hi")
s = Sample2()
s.display()
