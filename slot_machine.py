#

import random

print ()

money_in = ""

while money_in.isalpha() == False:

    try:

        money_in = (float(input("How much money would you like to insert into the machine? ")))
        
        while money_in <= 0:
            print ()
            money_in = (float(input("YOU CANNOT BET WITH NO MONEY OR LOWER, TRY AGAIN: ")))

        format_money_in = "{:.2f}".format(money_in)
        print ()
        print (f"You have inputted ${format_money_in} into the machine")
        break

    except ValueError as e:
        
        print ()
        print ("ERROR, ENTER AN INTEGER OR FLOAT:", e)
        print ()

print ()

bet = ""

while bet.isalpha() == False:

    try:

        bet = (float(input("How much money would you like to bet? ")))
        while bet <= 0:
            print ()
            bet = (float(input("INVALID BET, TRY AGAIN: ")))
        while bet > money_in:
            print ()
            bet = (float(input("ERROR, BET CANNOT BE HIGHER THAN YOUR BALANCE. TRY AGAIN: ")))
        format_bet = "{:.2f}".format(bet)
        print ()
        print (f"You are betting ${format_bet}")
        break

    except ValueError as e:

        print ()
        print ("ERROR, ENTER AN INTEGER OR FLOAT:", e)
        print ()

print ()

profits = money_in

while True and profits != 0:

        print ("ROLLING!")
        profits -= bet

        roll_1 = ["ORANGE...", "APPLE...", "CHERRY...", "BANANA...", "PEACH...", "WATERMELON..."]
        random_choice_1 = random.choice(roll_1)

        roll_2 = ["ORANGE...", "APPLE...", "CHERRY...", "BANANA...", "PEACH...", "WATERMELON..."]
        random_choice_2 = random.choice(roll_2)

        roll_3 = ["ORANGE...", "APPLE...", "CHERRY...", "BANANA...", "PEACH...", "WATERMELON..."]
        random_choice_3 = random.choice(roll_3)

        print ()
        print (random_choice_1)
        print (random_choice_2)
        print (random_choice_3)
        print ()

        if random_choice_1 == random_choice_2 == random_choice_3:
                print ("JACKPOT!")
                print ()
                profits = (profits + (bet * 3))
                format_profits = "{:.2f}".format(profits)
                print (f"YOU HAVE ${format_profits} REMAINING")
                print ()

        elif random_choice_1 == random_choice_2 or random_choice_2 == random_choice_3 or random_choice_3 == random_choice_1:
                print ("DOUBLE!")
                print ()
                profits = (profits + (bet * 2))
                format_profits = "{:.2f}".format(profits)
                print (f"YOU HAVE ${format_profits} REMAINING")
                print ()

        elif random_choice_1 != random_choice_2 and random_choice_2 != random_choice_3 and random_choice_3 != random_choice_1:
                print ("BETTER LUCK NEXT TIME!")
                print ()
                format_profits = "{:.2f}".format(profits)
                print (f"YOU HAVE ${format_profits} REMAINING")
                print ()
        
        if profits == 0:
            print ("OUT OF MONEY")
            print ()
            break

        play_again = ""

        while play_again.isalpha() == False:
            play_again = (input("PLAY AGAIN (y/n (any key)) or CHANGE BET AMOUNT (r): ")).lower()
            print ()
            while play_again.isalpha() == False:
                play_again = (input("INVALID INPUT, TRY AGAIN: ")).lower()
                print ()
        
        if play_again == "r":

            bet = str(bet)
            bet = ""

            while bet.isalpha() == False:

                try:
                    
                    bet = (float(input("What would you like to change your bet to? ")))
                    while bet == 0:
                        print ()
                        bet = (float(input("INVALID BET, TRY AGAIN: ")))
                    while bet > profits:
                        print ()
                        bet = (float(input("ERROR, BET CANNOT BE HIGHER THAN YOUR BALANCE. TRY AGAIN: ")))
                    format_bet = "{:.2f}".format(bet)
                    print ()
                    print (f"You are betting ${format_bet}")
                    print ()
                    break

                except ValueError as e:

                    print ()
                    print ("ERROR, ENTER AN INTEGER OR FLOAT:", e)
                    print ()

        if play_again != "y" and play_again != "r":
            break

if profits > money_in:
    final_profits = profits - money_in

    format_final_profits = "{:.2f}".format(final_profits)
    format_profits = "{:.2f}".format(profits)

    print (f"YOU ARE WALKING AWAY WITH A ${format_final_profits} PROFIT FOR A TOTAL OF ${format_profits}")
    print ()
    
elif profits < money_in and profits != 0:
    loss = money_in - profits

    format_loss = "{:.2f}".format(loss)
    format_profits = "{:.2f}".format(profits)
    format_money_in = "{:.2f}".format(money_in)
    
    print (f"YOU LOST -${format_loss} FROM YOUR INPUT OF ${format_money_in} AND YOU ARE WALKING AWAY WITH A TOTAL OF ${format_profits}")
    print ()

elif profits == money_in:
    print ("YOU BROKE EVEN")
    print ()

print("THANKS FOR PLAYING")
print ()

#