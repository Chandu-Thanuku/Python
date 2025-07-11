# while loop
count=1
while count < 10:
    print(count)
    count += 1
print("decerasing")
count=10
while count>0:
    print(count)
    count=count-1
else:
    print("Given work completed boss")
#   input function loop
number=int(input("Enter a number (0 to quit): "))
while number!=0:
    print(number)
    number=int(input("Enter a number (0 to quit): "))
else:
    print("reyy pandhii 0 nokkeki entha sepu bey")
# sum of positive number if 0 or negative then break
sum=0
num=int(input("Enter a number > 0 to get sum: "))
while num!=0:
    sum=sum+num
    num = int(input("Enter a number > 0 to get sum: "))
else:
    print("you entered ZERO")
print(sum)
