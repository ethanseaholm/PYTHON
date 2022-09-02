#

import random

def random_color():
    
    list = ["red", "blue", "green"]

    for i in list:
        i = i 
        print (i)

    random_color = random.choice(list)

    print ()
    print ("your random color is: ", random_color)    

random_color()