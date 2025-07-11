# To calculate GRADE and update in the dictionary
# GradinG Criteria 91-100=A+| 81-90=A|71-80=B+|61-70=B|51-60=C|41-50=D|BELOW 40=FAIL
student_marks={'jenny':92,
               'harry':78,
               'dimpu':56,
               'rahul':41,
               'aniket':99,
               'prem':34
}
print(student_marks)

for i in student_marks:

   if student_marks[i] >= 91:
    student_marks[i]='A+'
   elif student_marks[i] >= 81:
       student_marks[i] = 'A'
   elif student_marks[i] >= 71:
       student_marks[i] = 'B+'
   elif student_marks[i] >= 61:
       student_marks[i] = 'B'
   elif student_marks[i] >= 51:
       student_marks[i] = 'C'
   elif student_marks[i] >= 41:
       student_marks[i] = 'JUST PASS'
   else:
       student_marks[i] = 'FAIL'

student_grades=student_marks.copy()
print(student_grades)
