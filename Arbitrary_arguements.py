#KWARGS----Arbitrary Keyword arguements
def info(**info):
    for key,value in info.items():  #syntax
        print(key,value)
info(name="chandu",age=18,dept="cs")
info(name="chandu",age=18,count=0)
#ARGS-----Arbitrary Positional arguements
def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("sum is ",sum)
add(1,2,3,4,5)