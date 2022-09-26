#

import random

rounds_played = 0

while True:
    pot = int(input("\nHow much money would you like to add to the pot? "))
    
    while pot <= 0:
        pot = int(input("\nYour bet cannot be 0 or lower, try again: "))            # solving/avoiding potential input errors
    
    break

format_pot = "{:.2f}".format(pot)
print (f"\nYou have added ${format_pot} to the pot.")
print ("\n------------------")

rounds_played + 1           # the first manually incremented round played since it's outside of the main loop's incrementation

while True and pot != 0:

    dice1 = [1, 2, 3, 4, 5, 6]
    random_num1 = random.choice(dice1)          # using the 'import random' module (line 3) to get a random number from the array

    dice2 = [1, 2, 3, 4, 5, 6]
    random_num2 = random.choice(dice2)          # same thing to get a second random number from the array

    sum = random_num1 + random_num2

    print ("\nFirst roll:", random_num1)
    print ("Second roll:", random_num2)
    print ("\nTotal:", sum)

    if sum == 7:
        print ("\nYour dice add up to 7! YOU WON $4.00!")
        pot += 4            # adding wins to the pot via incrementing
        format_pot = "{:.2f}".format(pot)
        print (f"\nMoney in the pot: ${format_pot}")
    else:
        print ("\nYour dice do not add up to 7! YOU LOST $1.00!")
        pot -= 1            # subtraction losses to the pot via incrementing
        format_pot = "{:.2f}".format(pot)
        print (f"\nMoney in the pot: ${format_pot}")

    rounds_played += 1          # automatically incrementing the rounds played

    if pot == 0:
        print ("\n------------------")
        print ("\nYou lost all your money... Better luck next time!")
        break

    # to play again or quit:

    print ("\n------------------")
    play_again = input("\nPress enter to play again or type Q to quit: ")
    print ("\n------------------")

    if play_again == 'Q' or play_again == 'q':
        print ("\nYou quit. Bye!")
        break

print ("\nRounds played:", rounds_played)
format_pot = "{:.2f}".format(pot)
print (f"\nFinal pot: ${format_pot}")
print ()

#