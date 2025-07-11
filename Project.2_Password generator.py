import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i','j','k','l','m','n','o','p','q','r','s',
           't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','%','&','*','+','-','_']
print("Welcome to Password Generator:")
letters_n=int(input("How many letters do you want in your password: "))
numbers_n=int(input("How many numbers do you want in your password: "))
symbols_n=int(input("How many symbols do you want in your password: "))
password_list=[]
for i in range(1,letters_n+1): # 1 2 3 4.....n
    char=random.choice(letters)
    password_list+=char
for i in range(1,numbers_n+1): # 1 2 3 4.....n
    x=random.choice(numbers)
    password_list+=x
for i in range(1, symbols_n + 1):  # 1 2 3 4.....n
    char = random.choice(symbols)
    password_list += char
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for i in password_list:
    password += i
print(password)