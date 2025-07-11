class human:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class men:
    def __init__(self,name):
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
class boy(human,men):
    def __init__(self,name,age):
        human.__init__(self,name)
        men.__init__(self,name)
        self.age=age
    def school(self):
        print("I go to school")
    def display(self):
         print(f"I am {self.age} years old")
boy1=boy('chandu',18)
boy1.eat()
boy1.flirt()
boy1.school()
boy1.work()
men.work(boy1) # To access 2nd one
print(boy.mro()) # Method resolution order
print(boy1.name)
print(boy1.age)
boy1.display()