#Evan Mangat
from random import choice
initLists = input("Execute with new lists (n) or original lists (o)? ==> ") #Question to the user as to whether or not to use their own list or prebuilt
print() #Prints a blank line

if initLists == "n": #Used to initalize the lists

    print("\nTo start please input the lists exactly using the list format")
    print("Lists should have at least 1 dish and not more than 10 dishes")
    print("Lists with prices correspond exactly to lists with dishes\n")

    vietnamese_dishes = eval(input("List of Vietnamese dishes ==> "))
    vietnamese_dish_prices = eval(input("List of Vietnamese dishes prices ==> "))
    print()
    italian_dishes = eval(input("List of Italian dishes ==> "))
    italian_dish_prices = eval(input("List of Italian dishes prices ==> "))

else: #if user chooses prebuilt

    print("Now lists are initialized in the program ")

    vietnamese_dishes = ["Pho", "Fried rice", "Pancake", "Steamed sticky rice"]
    vietnamese_dish_prices = [7.5, 6.75, 5.15, 8.25]

    italian_dishes = ["Pizza", "Meatball spaghetti", "Pasta"]
    italian_dish_prices = [7.15, 6.25, 5.0]

#Variables used later given inital definition
vcount = 1
ncount = 0
icount = 1
pcount = 0
ilist = ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10"] #food lists which can store up to 10 items
vlist = ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10"] #Both used during dish 2 selection
# TRACE PRINTING IN ANY CASE
print ("\n*** TRACE Vietnamese ", vietnamese_dishes, vietnamese_dish_prices)
print ("\n*** TRACE Italian ", italian_dishes, italian_dish_prices)
vietnamese_dishes = [item.capitalize() for item in vietnamese_dishes] #Capitalizes lists essential so the variables match later
italian_dishes = [item.capitalize() for item in italian_dishes]
print("Welcome to the Food Ordering Bot!!")
def namefunc(): #Name function which hosts the variable which is called back later
    global name
    name = input("What is your name?: ")
suggestswitch = False   #Level 3 switch
namefunc() #Asks user their name
print("Hello dear", name + "!") #calls on name variable from previous function and prints a hello to the user
print("We specialize in Vietnamese and Italian food. \n You will be able to order two dishes \n If you are not sure what to ask we will choose for you!")
dish1 = input("What specific dish do you want to order? ---> ") #Asks user for their first order
Capscheck1 = dish1.capitalize() #Checks if the users input was a capitalized version of the word
if dish1 in vietnamese_dishes or Capscheck1 in vietnamese_dishes: #if the users input for their first dish is a vietnamese dish
    dish1 = dish1.capitalize() #capitalizes order
    pricelistnum = vietnamese_dishes.index(dish1) #links item cost to list item
    dish1cost = vietnamese_dish_prices[pricelistnum]
    print("It seems that you like Vietnamese style of food") #prints the users apparent food style preference
    print("**TRACE dish", dish1, "costs", dish1cost) # Trace print for dish and dish cost
if dish1 in italian_dishes or Capscheck1 in italian_dishes: # if the user input a food in the italian list
    dish1 = dish1.capitalize() #all the same refer to above comments
    pricelistnum = italian_dishes.index(dish1)# ^
    dish1cost = italian_dish_prices[pricelistnum]# ^
    print("It seems that you like Italian style of food ") # ^
    print("**TRACE dish", dish1, "costs", dish1cost) # ^

if dish1 not in italian_dishes and dish1 not in vietnamese_dishes and Capscheck1 not in vietnamese_dishes and Capscheck1 not in italian_dishes: #if the dish is in neither list
    dish1choice = choice(vietnamese_dishes + italian_dishes) # makes a random dish choice for the user
    print("Since you indicated a dish not available, we are choosing one for you") # prints the given msg
    suggest = input("But also, would you like to request that this dish is considered for the future? \ny/n ==> ") # input for level 3 user based menu suggestion
    if suggest == "y" or suggest == "Y": # if the user says yes
        print("**Trace suggested dish", dish1) # affirms to the user their requested dish was suggested
        suggestswitch = True # flips switch from earlier
    print("The dish we chose for you is", dish1choice) # tells the user what dish they will instead recieve
    if dish1choice in vietnamese_dishes: # if the randomly selected dish is in vietnam list
        pricelistnum = vietnamese_dishes.index(dish1choice) # From here same as previous if statements just item-cost linking
        dish1cost = vietnamese_dish_prices[pricelistnum]
        print("**Trace dish", dish1choice, "costs", dish1cost)
    if dish1choice in italian_dishes: # if item is in italian list
        pricelistnum = italian_dishes.index(dish1choice) # refer to above comments
        dish1cost = italian_dish_prices[pricelistnum]
        print("**Trace dish", dish1choice, "costs", dish1cost)

def breaker_line(): # defines the break line function to fufill the print function criteria
    print("========================")
    
userYN = input("Do you want to order another dish? y/n ==>") #Asks the user if they want to order another dish
if userYN == "y" or userYN == "Y": #if they agree
    print("All available dishes are") #displays available dishes
    breaker_line()
    for item in vietnamese_dishes:  #lists coded variables next to dish options, lasts until the list is completly run through
        print("v" + str(vcount), "-", vietnamese_dishes[ncount]) # prints for example v1 - Pho
        ncount = ncount + 1 # counters to make the list continue forward
        vcount = vcount + 1
    breaker_line()
    for item in italian_dishes: # same as above code but for italian list
        print("i" + str(icount), "-", italian_dishes[pcount])
        pcount = pcount + 1
        icount = icount + 1
    print("Please choose another dish by indicating the code that we provide \nYou may order the same dish as before, if you want \nIf you do not choose an existing dish we will choose one for you")
    dish2 = input("Provide the dish code here (MUST BE a letter and a number) ==>") #User inputs food code for dish 2
    vtrim = vcount - 1 # gives index number to cut from
    itrim = icount - 1
    del vlist[vtrim:] #deletes all items from the vlist and ilist that aren't given a food to associate with
    del ilist[itrim:]
    if dish2 in vlist: #if the user chose a v# related code
        dish2cost = vietnamese_dish_prices[int(dish2[1])-1]
        print("**Trace", vietnamese_dishes[int(dish2[1])-1], "costs", dish2cost) #linking cost to dish again
        totalcost = float(dish1cost) + float(dish2cost) # calculates total cost of order
        print("Please dear", name + ",","pay the delivery person the total", "$" + str(totalcost), "and a nice tip :) \nNice doing buisness with you!")#closing lines of interaction informs user of the total cost and bids them farewell
        if suggestswitch == True: # if the user answered yes to the earlier question about their suggestion
            print("And thank you for your suggestion of", dish1) #thanks user for suggesting a dish not on menu and calls that dish
    if dish2 in ilist: #same as comments from lines 96-102  just replace vietnamese with italian
        dish2cost = italian_dish_prices[int(dish2[1])-1]
        print("**Trace", italian_dishes[int(dish2[1])-1], "costs", dish2cost)
        totalcost = float(dish1cost) + float(dish2cost)
        print("Please dear", name + ",","pay the delivery person the total", "$" + str(totalcost), "and a nice tip :) \nNice doing buisness with you!")
        if suggestswitch == True:
            print("And thank you for your suggestion of", dish1)
    if dish2 not in ilist and dish2 not in vlist: # if the user inputted a code not found in either list
        print("Since you indicated a code dish not available, we are choosing one for you") # tells the user what they did
        dish2choice = choice(italian_dishes + vietnamese_dishes) #randomizes 2nd food choice
        print("Your dish will be:", dish2choice) #informs user of their 2nd meal
        if dish2choice in vietnamese_dishes: #if it was a vietnamese dish
            pricelistnum2 = vietnamese_dishes.index(dish2choice) #refer to lines 96-102
            dish2cost = vietnamese_dish_prices[pricelistnum2]
            print("**Trace: dish", dish2choice, "costs", dish2cost)
            totalcost = float(dish1cost) + float(dish2cost)
            print("Please dear", name + ",","pay the delivery person the total", "$" + str(totalcost), "and a nice tip :) \nNice doing buisness with you!")
            if suggestswitch == True:
                print("And thank you for your suggestion of", dish1)
        if dish2choice in italian_dishes: # if it was italian
            pricelistnum2 = italian_dishes.index(dish2choice) #refer to lines 96-102 for the following lines
            dish2cost = italian_dish_prices[pricelistnum2]
            print("**Trace dish", dish2choice, "costs", dish2cost)
            totalcost = float(dish1cost) + float(dish2cost)
            print("Please dear", name + ",","pay the delivery person the total", "$" + str(totalcost), "and a nice tip :) \nNice doing buisness with you!")
            if suggestswitch == True:
                print("And thank you for your suggestion of", dish1)
        
if userYN == "n" or userYN == "N": #if user only wants one meal
    print("OK! No more dishes for you \n") #prints the msg
    print("Please dear", name + ",","pay the delivery person the total", "$" + str(dish1cost), "and a nice tip :) \nNice doing buisness with you!") #closing msg tells the total cash spent witha goodbye msg
    if suggestswitch == True: # if the user answered yes to the first meal suggestion question
        print("And thank you for your suggestion of", dish1) #prints the suggestion made earlier
    

# Reflection: Fun little assignment to work on. Most of that time was
#             was spent pondering how to go about linking price and menu items but it was less problem solving and more
#             picking a route to go with, other routes I thought of included using hashing or using dictionary function {}
#             Overall between debugging/working it took about 2 hours of on and off work.
#             Made by Evan Mangat 
          
    
    
