# Below is list add another dictionary to it
student_data=[
    {
        'name': 'chandu',
        'roll': 863,
        'age': 18
    },
    {
        'name': 'bujji',
        'roll': 123,
        'age': 15
    }
]
def add_new_student(name, roll, age):
    new_student = {}
    new_student['name'] = name
    new_student['roll'] = roll
    new_student['age'] = age
    student_data.append(new_student)
add_new_student('ramu',600,20)
print(student_data)
