# To find no of buckets of paint is required if one bucket can cover 7 Sq.met

import math

def paint_buc(h,w):
    n=(h*w)/7
    N=math.ceil(n) # math.ceil() is used to get nearest bigger whole number ex-1.2=2
    print(f"You need {N} Buckets of paint")


height=float(input("enter height of wall in meters: "))
width=float(input("enter width of wall in meters: "))
coverage=7
paint_buc(height,width)
paint_buc(w=width,h=height) #keyword arguements without need of position

