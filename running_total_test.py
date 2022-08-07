#
# import time

# list = ["A", "B", "C"]

# for letters in list:
   # print (letters)

#########
#########

# for numbers in range(1, 11):          # can pass in a third number to be used for a count. with a '2' passed in, the loop would count up by 2 instead of 1
   # print (numbers)
   # time.sleep(1)

# print ("BANG!")

#########
#########

total = 0

while (total <= 100):
    nums = int(input("ENTER A NUMBER: "))
    if nums < 0:
        print ("TRY AGAIN...")
    total = total + nums

print ("")
print ("TOTAL =", total)
print ("100 HAS BEEN BROKEN!")
print ("")