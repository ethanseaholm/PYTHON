from skateboard_class import Skateboard

board_1 = Skateboard("FUCKING AWESOME", "8.25", "Independent", "Spitfire")

print (board_1.deck)
print (board_1.size)
print (board_1.trucks)
print (board_1.wheels)

print ("")

board_1.roll()
board_1.air()
board_1.stop()