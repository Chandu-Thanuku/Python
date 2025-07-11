# randomly selecting a person to pay the total bill in restaurant
import random
names=input("enter names of persons in your group seperated by space ")
names=names.split(" ")
print(names)
bakara=random.choice(names)
print(bakara,"will pay the bill")
# another method using randint
length=len(names)
x=random.randint(0,length-1)
print(names[x],"will pay the bill")