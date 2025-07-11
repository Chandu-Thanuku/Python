# without using len() and sum()
heights=input("enter heights separated by space: ")
heights_list=heights.split()
print(heights_list)
sum=0
length=0
for i in heights_list:
    sum=sum+int(i)
for heights in heights_list:
    length = length+1
avg=sum/length
print("average height is",avg)