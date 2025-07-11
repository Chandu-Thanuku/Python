# Find max number from the list without busing max()
num=input("enter numbers separated by space ")
num_list=num.split()
print(num_list)
max=0
for i in num_list:
    if int(i)>max:
        max=int(i)
print(max)
