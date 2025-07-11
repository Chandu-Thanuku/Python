import random #syntax
a=random.randint(0,100) #randomly selects 1 number from a-b (b included)
print(a)
b=random.randrange(0,4) # B(40 not included---randomly selects
print(b)
print(random.random()) # It randomly selects a number from 0-1 (except 1.0)
print(random.uniform(1,4)) # selects random float number btwn a and b
list=[1,65,'jenny',100,78]
print(random.choice(list)) # it selects random element from given list
random.shuffle(list) # it shuffle the given list
print(list) 