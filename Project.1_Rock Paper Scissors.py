# Rock Paper Scissor GAME
a=int(input("Enter\n 1 for Rock\n 2 for Paper\n 3 for Scissors "))
import random
x=random.choice([1,2,3])
print("computer selected ",x)
if (a==1 and x==2) or (a==2 and x==1) or (a==3 and x==2):
    print("YOU WON THE GAME")
elif a==x:
    print("GAME DRAWN")
else:
    print("You Lose")