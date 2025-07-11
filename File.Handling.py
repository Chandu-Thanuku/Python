# f1=open("file1.txt","x") # 'x' is used to create a file
# f1=open("file1.txt","r") # 'r' is used to open file
# data=f1.read()
# print(data)
# f1=open("file1.txt","w")  # 'w' is used to write, it clears previous data
# f1.write("Welcome to my File")
f1=open("file1.txt","r+")  # 'r+' is used to read and write
print(f1.tell())  # tell() is used to know the position
print(f1.read())
f1.write("hello")
print(f1.tell())



