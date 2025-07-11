import os
def calculate(num1):
    operator = input('Pick an Operator: ')
    num2 = int(input('Enter Next number: '))
    if operator == '+':
        print( f'{num1} + {num2} = {num1+num2}')
        x=num1+num2

    elif operator == '-':
        print( f'{num1} - {num2} = {num1-num2}')
        x=num1-num2

    elif operator == '*':
        print( f'{num1} * {num2} = {num1*num2}')
        x=num1*num2

    elif operator == '/':
        print( f'{num1} / {num2} = {num1/num2}')
        x=num1/num2

    else:
        print('Invalid operator')
        return calculate(num1)
    next=input("Enter:\n'c' to continue\n'n' for new calculation\nother To EXIT ").lower()
    if next=='c':
        calculate(x)
    elif next=='n':
        os.system('cls')
        first()
    else:
        print("Thanks for using this calculator")
        print('-------Calculator Closed-------')

def first():
    num1 = int(input('Enter First number: '))
    print("+\n-\n*\n/\n")

    calculate(num1)
first()


