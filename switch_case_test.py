import random

#nums = ["1", "2", "3"]
#random_choice = random.choice(nums)

#your_choice = (input("CHOOSE A NUMBER BETWEEN 1 AND 3: "))

#if your_choice == random_choice:
 #   print ("WINNER!")
#else:
 #   print ("LOSER!")

#########
#########

def play():

    nums = ["1", "2", "3"]
    random_choice = random.choice(nums)

    your_choice = (input("CHOOSE A NUMBER BETWEEN 1 AND 3: "))

    if your_choice == random_choice:
        print ("WINNER!")
    else:
        print ("LOSER!")
    
    reroll = (input("REROLL? y OR n: "))

    if reroll == "y":
        play()
    elif reroll == "n":
        print ("BYE!")

play()

# hehe