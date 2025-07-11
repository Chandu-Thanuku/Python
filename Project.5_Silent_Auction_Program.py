import os
def new_person(name,bid_price):
    new_person={}
    new_person['name']=name
    new_person['bid']=bid_price
    bid_members.append(new_person)

bid_members=[]
print("********** WELCOME TO SILENT BIDDER GAME ***********")
i=True
while i==True:

    person=input("Enter your name: ")
    bid=int(input("Enter your bid: "))
    new_person(person,bid)

    x=input("Enter 1 to continue || others to quit: ")
    if x=='1':
        os.system('cls')
        i=True

    else:
        i=False
        print("Thank you for playing")

max=0
for i in bid_members:


    b=i['bid']

    if b>max:
        max=b

        winner=i['name']
print(bid_members)
print(f"{winner} is the Winner of Silent Bidder Game with bid = {max}")


