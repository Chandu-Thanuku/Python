def greet(name,dept,college="srm"):
    print(f"Hii {name}")
    print(f"you are from {dept} department right?")
    print(f"you are studying in {college} ")
greet("John","cs")  #Positional ( position of order is necessary
greet(dept="cs",name="John") # Keyword arguement (no needs of orfer)
greet("john","cs") # without giving arguement it takes default--DEFAULT arguement

def add(*numbers):     #arbitrary arguements
    sum=0
    for i in numbers:
        sum=sum+i
    print("sum is ",sum)
add(1,2,3,4,5)

