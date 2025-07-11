# Identity operator cgecks the address not values
a=5
b=5
print(a is b)
print(a is not b)
'''
here it does not compare both values
it checks the address of both variables
if same then then True
print(a is b) checks adress
print(a==b) compares values
'''
print(id(a))
print(id(b))