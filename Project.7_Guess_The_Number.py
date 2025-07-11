import random
num=random.randint(1,50)
print("Let me think of a number between 1 to 50")
level=int(input("Enter the level of number..\n   '1' for Easy \n '2' for difficult:\n "))
easy_attempts=10
difficult_attempts=5
i=True
while i is True:
    if level == 1:
        print(f"You have {easy_attempts} attempts left. ")
    elif level == 2:
        print(f"You have {difficult_attempts} attempts left. ")
    else:
        print("Invalid level")
        break
    guess = int(input("Make a guess..\n"))
    if guess == num:
        print("You got it!\nYOU Won The Game")
        i=False
        break
    elif guess > num:
        print("Your guess is too High.")
        if level==1:
            easy_attempts = easy_attempts - 1
        else:
            difficult_attempts = difficult_attempts-1
        if easy_attempts == 0 or difficult_attempts==0:
            print("Sorry, you are out of tries.")
            i=False
            break
        print("Guess Again.")
    else:
        print("Your guess is too Low.")
        if level==1:
            easy_attempts = easy_attempts - 1
        else:
            difficult_attempts = difficult_attempts-1
        if easy_attempts == 0 or difficult_attempts==0:
            print("Sorry, you are out of tries.")
            i=False
            break
        print("Guess Again.")

