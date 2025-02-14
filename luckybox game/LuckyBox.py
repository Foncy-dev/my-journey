import random

class Lucky_box:
    def __init__(self,awards):
        self.awards = awards

    # def luckybox (self):
    #     return f"You won this {awards}"

awards = ["  ","  "," ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","  ","pen","pencil","1$","TV","Books","Sweater","lamb","Ketchup","$100"
"headphones"," "," "," "," "," "," "," "," "]

total_games = 0
total_wins = 0


while True:
    total_games += 1
    play = input("Would like to be a winner:(yes/no): ")
    if play != 'yes':
        # print("Lets continue then")
        break
    

    print("Choose you lucky box and win a prize." )
    print("1.LuckyBox 1")
    print("2.LuckyBox 2")
    print("3.LuckyBox 3")
    print("4.LuckyBox 4")
    print("5.LuckyBox 5")
    print("6.LuckyBox 6")

    
    choosing = input("We provide you with this luckyboxes and you have to choose one to win a prize:(1/2/3/4/5/6): ")

    if choosing not in ['1','2','3','4','5','6']:
        print("Invalid choice. Please retry.")
        continue

    
    box_awards = random.choice(awards)

    
    if box_awards.strip() != "":
        total_wins += 1

    
    p1 = Lucky_box([box_awards])
    print(f"Congrates you won this award {p1.awards}")
    print(f"Games played : {total_games} | Games won : {total_wins}")