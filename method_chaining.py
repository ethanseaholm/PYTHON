#

class Kickflip:

    def pop(self):
        print ("you pop the board")
        return self

    def flick(self):
        print ("you flick the board")
        return self

    def flip(self):
        print ("the board is flipping")
        return self
    
    def catch(self):
        print ("you catch the board")
        return self

    def land(self):
        print ("you land bolts")
        return self

kickflip = Kickflip()

kickflip.pop()\
    .flick()\
    .flip()\
    .catch()\
    .land()

#