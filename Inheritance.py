#Inheritance
class Human:
    def __init__(self):
        self.nose=1
        self.eyes=2
    def work(self):
        print("I can work")
    def eat(self):
        print("I can eat")
class male(Human):
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age
    def flirt(self):
        print("I can flirt")
male1=male("John",20)
print(male1.name)
print(male1.age)
print(male1.nose)
male1.flirt()
male1.work()
male1.eat()