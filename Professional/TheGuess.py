import random

num_of_guesses=0
secret=random.randint(0,10)
# print(secret)

while num_of_guesses<3:
    num=int(input("Make a guess: "))
    if num>secret:
        print("Make a lower guess")
        num_of_guesses+=1
    elif num<secret:
        print("Choose higher")
        num_of_guesses+=1
    elif num==secret:
        print("Congrats, you won!")
        num_of_guesses+=1
        break
    
    if num_of_guesses==3:
        print("Sorry, you lost. ")