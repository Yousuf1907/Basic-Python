import random

score=random.randint(0,50)
name=input("Name? ")
def game():
    with open('high_score.txt','a') as f:
        f.write(f"{name} scored {score}n")
        
game()