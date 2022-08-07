def math():     # defines the function called 'math'

    print("")       # aesthetics
    print ("---------------------")     # aesthetics
    print("")       # aesthetics
    first_number = input("enter a number: ")        # input first number
    first_number = int(first_number)        #converts str to int
    second_number = input("enter another number: ")     # input second number
    second_number = int(second_number)      # converts str to int
    result = (first_number*second_number)       # multiples the first input by the second input
    print("")       # aesthetics
    print (first_number, "*", second_number, "=", result)      # prints the result
    
    if result == 20:
        print("")       # aesthetics
        print ("lucky number!")     # random easter egg just for fun

math()      # calls the function and can be continued to be called later on


########################
########################
########################


def multiplication(num1,num2):
    return num1 * num2

result = multiplication(6, 5)

print("")       # aesthetics
print("---------")      # aesthetics
print("")       # aesthetics
print("multiplied result of numbers (arguments) passed into the function:", result)
print("")       # aesthetics
print("---------")      # aesthetics
print("")       # aesthetics


########################
########################
########################


def multiplication_two(num3,num4):        
    more_multiplied_numbers = num3 * num4     
    print (num3, "*", num4, "=", more_multiplied_numbers)
    print("")
    

multiplication_two(12,3)

multiplication_two(20,20)

multiplication_two(8,4)

######
######
######

print("---------------------")
print("")

