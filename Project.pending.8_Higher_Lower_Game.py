#ONce watch jenny lecture then do this project
import random
def data():
    data=[
        {'name':'kohli',
         'rank':1,
         'type':'Batsman',
         'country':'India'
         },
        {
            'name':'AB DEVILIERS',
            'rank':2,
            'type':' 360 Batsman',
            'country':'SA'
        },
        {
            'name':'Gayle',
            'rank':3,
            'type':' opener Batsman',
            'country':'West Indies'
        },
        {
            'name':'Kane',
            'rank':4,
            'type':'captain Batsman',
            'country':'NZ'
        }
    ]
    i=random.randint(0,2)
    return data[i]
score=0
game=True
while game is True:
    compare1 = data()
    print(f"Compatre-1: {compare1['name']},a {compare1['type']},from {compare1['country']}")
    compare2 = data()
    print(f"Compare-2:{compare2['name']},a {compare2['type']},from {compare2['country']}")
    choosed = int(input("Which one is first based on Ranking: "))
    if choosed == 1 or choosed == 2:
        if choosed == 1 and compare1['name'] < compare2['name']:
            score = score + 1
            print("YOUR SCORE IS ", score)
            game = True
        elif choosed == 2 and compare1['name'] > compare2['name']:
            score = score + 1
            print("YOUR SCORE IS ", score)
            game = True
        else:
            print("YOUR SCORE IS ", score)
            break

    else:
        print("INvalid")


