class Human:

    alive = True

    def eat(self):
        print ("eating")

    def shit(self):
        print ("shitting")

    def sleep(sleep):
        print ("sleeping")

class Baby (Human):
    pass

class Teenager (Human):
    pass

class Adult (Human):
    pass

baby = Baby()
teenager = Teenager()
adult = Adult()

print (baby.alive)
teenager.eat()
adult.shit()

###