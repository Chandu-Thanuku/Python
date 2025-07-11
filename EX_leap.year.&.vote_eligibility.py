#write a program to check eligibility to vote
age=int(input('enter age: '))
if age>=18:
    print('yes, you are eligible to vote')
else:
    print('no, you are not eligible to vote')
# write a program to check leap year or not
'''
Condition 1=Divisible by 4 (and) not divisible by 100 👍
Condition 2=Divisible by 4,100,400
'''
year=int(input('enter year: '))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('Leap year')
        else:
            print('Not leap year')
    else:
        print('leap year')
else:
    print("Not a Leap year")