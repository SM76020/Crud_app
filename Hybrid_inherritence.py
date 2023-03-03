class A:
    def __init__(self):
        self.n=input("Enter Name: ")

class B(A):
    def frnd1(self):
        self.f1=str(input("Enter your 1st Friend Name: "))

class C(A):
    def frnd2(self):
        self.f2=str(input("Enter your 2nd Friend Name: "))

class D(B,C):
    def show(self):
        print("Name: ",self.n)
        print("First Friend Name: ",self.f1)
        print("Second Friend Name: ",self.f2)

o1=D()
o1.frnd1()
o1.frnd2()
o1.show()