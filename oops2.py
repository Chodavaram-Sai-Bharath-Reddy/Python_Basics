class P:
    def m1(self):
        print("This is m1 in class P")
class C(P):
    def m2(self):
        print("this is m2 in class C")
class CC(C):
    def m3(self):
        print("this is m3 in class CC")

c= CC()
c.m1()
c.m2()
c.m3()

class P1:
    def m1(self):
        print("from method m1 in P1")
class P2:
    def m2(self):
        print("from method m2 in P2")
class C1(P1, P2):
    def m3(self):
        print("from method m3 in C1")
c1 = C1()
c1.m1()
c1.m2()
c1.m3()

# Using Super

class SampleP1():
    def __init__(self):
        print("constructor in SampleP1")
    def m1(self):
        print("m1 in SampleP1")
class SampleC1(SampleP1):
    def __init__(self):
        super().__init__()
        print("Constructor in SampleC1")
    def m1(self):
        super().m1()
        print("m1 in SampleC1")
sampleC1 = SampleC1()
sampleC1.m1()

class SampleA:
    def m1(self):
        print("Sample A")
class SampleB(SampleA):
    def m1(self):
        print("Sample B")
class SampleC(SampleB):
    def m1(self):
        print("SampleC")
class SampleD(SampleC):
    def m1(self):
        print("SampleD")
class SampleE(SampleD):
    def m1(self):
        super(SampleC, self).m1()
        print("SampleE")

e = SampleE()
e.m1()
