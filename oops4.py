from abc import *
class Sample1:
    def __init__(self):
        self._a = 10
        self.__aa = 100
    def display(self):
        print(self._a, self.__aa)
s = Sample1()
s.display()


class Sample2:
    @abstractmethod
    def m1(self):
        pass