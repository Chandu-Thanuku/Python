class A:
    def displayA(self):
        print("I am  from A class")
class B(A):
    def displayB(self):
        print("I am  from B class")
class C:
    def show(self):
        print("I am  from C class")
class D(B,C):
    def display(self):

        print("I am  from D class")
d=D()
d.displayA()
d.show()
