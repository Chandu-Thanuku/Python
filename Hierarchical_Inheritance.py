from tkinter.font import names


class human():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"Myself {self.name} I am {self.age} years old")
    def eat(self):
        print("I can eat")
class male(human):
    def sleep(self):
        print("I can sleep")
class female(human):
    def destroy(self):
        print("I can destroy mental health")
female1=female('bujji',16)
female1.eat()
female1.destroy()
male1=male('chandu',18)
male1.eat()
female1.details()
male1.details()