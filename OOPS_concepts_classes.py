class student:
    def __init__(self,student_name,student_age):
        self.name=print(f'Student name is {student_name}')
        self.age=print(f"Age :{student_age}")
    def display(self):
        self.name=input("Student name:")
        self.age=input("Student age:")


student_1=student('chandu',18) #(attributes)-name,address,phone_no,has_book,has_laptop
student_1.display()

student_2=student('Bujji',16)
student_2.display()




