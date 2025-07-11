#Collection of things enclosed in a square bracket[] and separated by comma , including duplicate of things
#Dynamically sized array not fixed array
#it is mutable(can change)
list=[1,1.8,'chandu',True,23]
print(list)
print(list[0]) #To access element using index number
print(list[-1]) # negative means it comes from end
print(list[1:4]) # here 1 is index number from where you want to start
# 4 is length of light starts with 1, upto how much length you want to print
num=[23,51,1,0,34,56.43,0.2,-1.5]
print(num[1:6:2])
# 1 is index--<>--6 is upto required length--<>--2 is no of steps you want jump/skip
num.sort() #For Sorting
print(num)
num.reverse() #To reverse list elements
print(num)
print(max(num)) #To find max number in list
print(min(num)) #To find min
print(sum(num)) #To get sum
num.append(100) #To add element in last
num.insert(1,99) #To insert at specific index
num.extend([0.2,0.8,0.3]) #to add more at the end
num[0]=22 # to edit data
num[1:5]=[12,45,67,80] # to edit more data
num.remove(100) # to remove specific data
num.pop() # it removes from last
num.pop(2) # to remove data at specific index
num.count(2) # to count that data(2) how many times appeared in list
print(num)
#-------<>----NESTED LIST-----<>-------<>---------<>-----<>---------------

list=[1,65,'jenny',[0,0.9,0.6],100,78]
print(list[3])
print(list[3][0])