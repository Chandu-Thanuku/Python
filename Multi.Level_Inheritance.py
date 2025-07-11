class human:
    def __init__(self):


        print("Calling init from human class:")
        self.eyes = 2

    def eat(self):
        print("I can eat")
class men(human):
    def __init__(self):
        human.__init__(self)
        self.nose=1
    def work(self):
        print("I can work")
class boy(men):
    def __init__(self):
        men.__init__(self)
        human.__init__(self)
        self.heart = 1
    def work(self):
        men.work(self)
        print("I can code")
    def school(self):
        print("I go to school")

boy1=boy()
boy1.eat()
boy1.work()
boy1.school()
print(boy1.eyes)
men1=men()
print(men1.eyes)