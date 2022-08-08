class Human:

    alive = True

    def eat(self):
        print ("eating")

    def play(self):
        print ("playing")

    def sleep(self):
        print ("sleeping")

class Baby (Human):
    pass

class Teenager (Human):
    pass

class Adult (Human):
    
    def sleep (Adult):
        print ("tossing and turning")           # method overriding from the parent class

baby = Baby()
teenager = Teenager()
adult = Adult()

baby.play()
print (teenager.alive)
adult.sleep()

###