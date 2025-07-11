# FIZZBUZZ Interview question
# we have to print numbers from 1-n
# if number is divisible by 3 then in that place FIZZ
# if number is divisible by 5 then in that place BUZZ
# if number is divisible by 3 & 5 then in that place FIZZBUZZ
# 1 2 FIZZ 4 BUZZ......
# Order important in coding
for i in range(1,100):
    if i%3==0 and i%5==0:
        print("FIZZBUZZ== ",i)
    elif i%3==0 or i%5==0:
        if i%5==0:
            print("BUZZ= ",i)
        if i%3==0:
            print("FIZZ= ",i)
    else:
        print(i)

