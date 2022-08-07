#name = input("what is your name? ")
#if name.isalpha():
 #   print ("hey", name)
#else:
 #   # while name.isalpha() == False:
  #      print ("error: try again...")
   #     name = input("what is your name? ")
    #    if name.isalpha():
     #       print ("hey", name)

name2 = input("what is your name? ")

while name2.isalpha() == False:
    print ("error: try again...")
    name2 = input("what is your name? ")
print ("hey", name2)