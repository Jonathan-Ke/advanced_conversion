#Advanced conversion code
#Jonathan Kessler
#10/30/2024
#Version 1.0
#This code will convert dollars into 5 different currencies ranging from pounds to lek.

#This asks for the starting dollar amount
dollar_amount=float(input("Enter dollar amount to be converted : $"))
print("-----------------------------------------------------------")
type_money = input("What would you like to convert it to (type options to see the options) ")

#This shows the user the options if they need them.

while type_money == "options":
     if type_money == "options":
        print("---------------------------------------------------------------------------")
        print("euros, ruppees, afghani, pounds, and lek")
        print("---------------------------------------")
        type_money = input("What would you like to convert it to (type options to see the options) ")

# This sets up the variable for the while loop.
x = 0 

# This is the user dollar amount coverted into each currency
euros = dollar_amount * .94540
ruppees = dollar_amount * 84.04
afghani = dollar_amount * 66.55
lek = dollar_amount * 91.01
pounds = dollar_amount * .77

#The following if statements print the one currency that the user wanted to see
print("---------------------------------------")
if type_money == "ruppees":
        print("Amount of " + type_money +" :"  +str(ruppees))
        print("-------------------------------------------")

if type_money == "euros":
        print("Amount of " + type_money +" :"  +str(euros))
        print("-------------------------------------------")

if type_money == "afghani":
        print("Amount of " + type_money +" :"  +str(afghani))
        print("-------------------------------------------")

if type_money == "pounds":
        print("Amount of " + type_money +" :"  +str(pounds))
        print("-------------------------------------------")

if type_money == "lek":
        print("Amount of " + type_money +" :"  +str(lek))
        print("-------------------------------------------")

# This allows the user to choose whether or no they'd like to convert again
again = input("Would you like to convert again : ")
if again == "Yes" or again == "yes" :
    print("--------------------------------------------------")

   

    x=1
if again == "No" or again == "no" :
        x=2
while x == 1:    
    dollar_amount=float(input("Enter dollar amount to be converted : $"))
    print("-----------------------------------------------------------")
    type_money = input("What would you like to convert it to ")
    print("---------------------------------------")
    if type_money == "ruppees":
        print("Amount of " + type_money +" :"  +str(ruppees))
        print("-------------------------------------------")
        again = input("Would you like to convert again : ")

    if type_money == "euros":
        print("Amount of " + type_money +" :"  +str(euros))
        print("-------------------------------------------")
        again = input("Would you like to convert again : ")

    if type_money == "afghani":
        print("Amount of " + type_money +" :"  +str(afghani))
        print("-------------------------------------------")
        again = input("Would you like to convert again : ")

    if type_money == "pounds":
        print("Amount of " + type_money +" :"  +str(pounds))
        print("-------------------------------------------")
        again = input("Would you like to convert again : ")
        dollar_amount=float(input("Enter dollar amount to be converted : $"))
    if type_money == "lek":
        print("Amount of " + type_money +" :"  +str(lek))
        print("-------------------------------------------")
        again = input("Would you like to convert again : ")

    if again == "Yes" or again == "yes" :
        x=1
    if again == "No" or again == "no" :
        x=2
    print("-----------------------------------------------------------")

# This was helpful to see if the code was running properly
print("Program finished")