import random
import Hangman_symbol
words=['jenny','chandu','apple','loveu','bangaram','golduu','bujji','abd','friends','puppy']
choosen=random.choice(words)
lives=6
display=[]
for i in choosen:
    display+='_'
print(display)
game_over=False
while not game_over:
     guessed=input("Guess a letter:")
     for i in range(len(choosen)):
         char=choosen[i]
         if char==guessed:
             display[i]=char
     print(display)
     if guessed not in choosen:
         lives-=1
         if lives==0:
             game_over=True
             print("You are HANGED\n   you lose   ")
     if '_' not in display:
         game_over=True
         print("YOU WON THE GAME")
     print(Hangman_symbol.symbol[lives])


