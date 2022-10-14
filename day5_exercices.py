# Learning python basics
# GDSC 30 days challenge : day 4

# Exercice 1 : STOCK TRANSACTION PROGRAM
shares_number = 2000
share_price = 40.00
amount_paid = share_price*shares_number
commision = 3*amount_paid/100
total_paid = amount_paid + commision

sell_price = 42.75
sell_amount = shares_number*sell_price
commision2 = 3*sell_amount/100
total_cost = total_paid + commision2
profit = sell_amount - total_cost

print("This program display Joe's purchases amount : \n")
print("Joe paid "+str(amount_paid)+"$ for the stock.")
print("He paid "+str(commision)+"$ to his broker when bought the stock.")
print("He Sold the stock he bought for "+str(sell_amount)+"$.")
print("He paid another "+str(commision2)+"$ to the broker when he sold the stock.")
if (profit > 0) :
    print("After doing his business, Joe has made "+str(profit)+"$ profit.\n")
else :
    print("After doing his business, Joe has lost "+str(profit)+"$ amount of money\n")


# Exercice 2 : INGREDIENT ADJUSTER
print("This program is an ingredient adjuster for making cookies : \n")
sugar = 1.5
butter = 1
flour = 2.75
cookies = 48

cookies_number = int(input("How many cookies do you want? : "))
sugar_needed = cookies_number*sugar/cookies
butter_needed = cookies_number*butter/cookies
flour_needed = cookies_number*flour/cookies

print(f"To make {cookies_number} cookies, you will need : ")
print(f"{sugar_needed} cups of sugar;\n{butter_needed} cups of butter;\nand {flour_needed} cups of flour.\nEnjoy your cookies :)\n")
