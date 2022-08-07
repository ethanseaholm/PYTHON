### inputs

print("")
amount_spent = (input("How much ETH did you spend? (NOTE: include gas costs for more accurate data): "))
amount_spent = float(amount_spent)

print("")
sold_at = (input("What price did you sell for?: "))
sold_at = float(sold_at)

print("")
creator_fee = (input("What is the creator fee %?: "))
creator_fee = float(creator_fee)

### math portion

a = (creator_fee + 2.5) * 0.01                      # converted decimal fee result = 0.075, .1, etc...
b = a * sold_at                       # amount to be subtracted from sold_at = .1 (converted decimal fee) * .3 (sold_at)
c = sold_at - b                      # money you make = .3 (sold_at) - 0.03 (amount to be subtracted from sold_at)
profit = c - amount_spent                      # profit = .27 (money you make) - .2 (amount_spent)

###

print("")
print ("Your total profit is: ", round(profit, 5), "ETH")                       # profit = .07 rounded to 5 decimal places
print("")

