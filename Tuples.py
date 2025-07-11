# Tuples are used to store multiple items in a single variable
# These are immutable
# Eclosed by () separated by comma ,
x=(10,'jenny',0.3,567,3,2)
a=(10,)
b=(10)
print(type(a)) #importance of comma ,
print(type(b))
tuple1=(1,2,3,4)
tuple2=("jenny",3,True)
tuple3=(tuple1,tuple2)
print(tuple3)
tuple4=(tuple1+tuple2)
print(tuple4)
list=[1,2,3]
print(tuple(list)) #To convert list into Tuple
print(tuple1[0]) # To access data
