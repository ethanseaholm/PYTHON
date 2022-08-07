while True:

#

    secret_word = "banana"
    guess = ""
    guess_limit = 3

    while guess.isalpha() == False:
        guess = (input("enter the secret word: "))
        if guess.isalpha() == False:
            print ("NO NUMBERS ALLOWED, TRY AGAIN.")
    
    guess_limit -= 1

    while guess != secret_word and guess_limit != 0:
        print ("INCORRECT!", guess_limit, "guess(es) remaining!")
        guess = (input("enter the secret word: "))
        guess_limit -= 1
        
        while guess.isalpha() == False:
            print ("NO NUMBERS ALLOWED, TRY AGAIN.")
            guess = (input("enter the secret word: "))
    
    if guess != secret_word and guess_limit == 0:
        print ("you're out of guesses! the secret word is:", secret_word.upper())

    if guess == secret_word:
        print ("CONGRATULATIONS! you guessed the secret word:", secret_word.upper())

#

    play_again = (input("play again? (y/n): ")).lower()

    if play_again == "y":
        print ("NEW GAME!")

    if play_again != "y":
        break

print ("THANKS FOR PLAYING!")

