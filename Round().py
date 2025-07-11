#it is used to get round off number
# 21.254=21
# Syntax--- round(number,no of digits)
#  if no of digits entered is positive it compares right side number and get round off
#  if no of digits entered is negative it compares left side number and get round off
round(23.4567,2) # here i give 2 digits so it round off 2 dights at last 67=100 so 460
print(round(23.4567,2))
print(round(23.4567))
print(round(23.4567,-1)) #it checks left of decimal point here 3 is nearest to 0 hen it becomes  20
print(round(7.5)) #8
#when number is .5 it gives nearest even integer
print(round(6.5)) #6