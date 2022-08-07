#

class Skateboard:

    # attributes

    def __init__(self, deck, size, trucks, wheels):
        self.deck = deck
        self.size = size
        self.trucks = trucks
        self.wheels = wheels

    # methods

    def roll(self):
        print ("the", self.deck, "board is rolling")

    def stop(self):
        print ("the board is stationary")

    def air(self):
        print ("the board is in the air")