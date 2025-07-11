# To check given number is prime or not
def prime_checker(number):
    if number==1:
        print("Composite number")
    if number==2:
        print("Prime number")
    is_prime=True
    for i in range(2,number):  #OR range(2,maths.ceil(number/2))
        if number % i == 0:
            is_prime=False

    if is_prime==True:
        print("Prime number")
    else:
        print("Not a prime number")
n=int(input("enter number: "))
prime_checker(n)