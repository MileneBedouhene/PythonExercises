import re

name = input("Please enter your name : ")
nb_ticket = int(input("How many tickets would you like to buy? "))
price_ticket = int(15.50)
vip = "VIP"

if re.search(name,vip):
    print("Enjoy the show for free!")

else :
    price = nb_ticket * price_ticket
    print(f"The total cost is : {price}")