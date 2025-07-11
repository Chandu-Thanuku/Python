class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=self.radius**2*3.14
        print(f"The area of the circle is {area}")
    def perimeter(self):
        perimeter=self.radius*2*3.14
        print(f"The perimeter of the circle is {perimeter}")
circle1=circle(7)
circle1.area()
circle1.perimeter()