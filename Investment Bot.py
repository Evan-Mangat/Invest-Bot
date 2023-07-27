#Made by Evan Mangat
import math
from random import randint
import time
import sys
# Imported lirbaries necassary for code
def Rules(): # Function which will be called later to display rules
    print("The Rules I use to calculate go as follows:")
    time.sleep(0.5) # used to make bot wait to say the next line
    print("If you choose to invest for 5 years or less....")
    time.sleep(0.5)
    print("\t you will get a % equal to half the the number of years") # the /t causes tab spaces
    time.sleep(0.5)
    print("If you choose to invest more than 5 years....")
    time.sleep(0.5)
    print("\t you will get 2% + half the number of years as %")
    time.sleep(0.5)
    print("Additionally if you invest for more than 10 years....")
    time.sleep(0.5)
    print("\t you will get a random % between 0 and 2, extremes possibly included")

name = input("Hello what is your name?: ") #Asks user name
print("Hello", name + str("!"))
age = int(input("How old are you?: ")) # Asks user age
passnum = age/7  #number that will be used later to dtermine amount of ! points in password
# ndp stands for No Decimal Password
ndp = math.ceil(passnum) #rounds the passnum to an integer
ndp = int(ndp) #classifies ndp as an integer
print("if you choose to invest with me...") #displays the given msg
time.sleep(0.5)
print("I will provide you a secure password to enter my website")
time.sleep(2)
print("------------------") # line for the sake of visual appeal
Rules()
capinit = int(input("What is your initial capital?:")) # asks for the initial capital
years = int(input("How many years will you invest with me?:")) #asks for the years invested
roundedperc = math.floor(years * 0.5)
perc = 0.01 * (roundedperc)  #All calculations related to percentages
randnum = randint(0,2)
randperc = randnum * 0.01
letter = 0 #letter definiton as a number
#Money calculations for less then 5 years
if years <= 5:
    newcap = capinit * (1 + perc)
    print("**Trace --> reminder percentage is", perc)
    c = round(newcap, 2)
    print("The money you will recieve back is:", c) #prints investment returns
# Money calculations for more than 5 years
if years > 5: 
    if years > 10:
        newcap2 = capinit * ((1.02 + perc) + randperc)
        print("**Trace --> reminder percentage is 2 +", roundedperc, "+ a random percentage of", randnum)
        c = round(newcap2, 2)
        print("The money you will recieve back is:", c)  #prints investment returns
    else:
        newcap2 = capinit * (1.02 + perc)
        c = round(newcap2, 2)
        print("**Trace --> reminder percentage is 2 +", perc)
        print("The money you will recieve back is:", c) #prints investment returns

print("Now that you see what you'll get back, do you want to invest with me?")
answer = input("Please answer Yes/No:") # Asks user if they want to sign up
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y": #if user says yes
    print("Great! Your secret password is as follows:") #password calculations
    for i in range (ndp): #counts characters in name
        letter = letter + 1
        lettercount = int(letter)
    if (lettercount + 1) % 2 == 0: #if it is even
        print(str(name[0]) * ndp + str(name[-1]) + "!") #gives password
    if (lettercount + 1) % 2 != 0: #if it is odd
        print(str(name[0]) * ndp + str(name[-1]) + "!!") #gives password
            
if answer == "No" or answer == "no" or answer == "n" or answer == "N": # if user says no
    print("Alright! Please come back if you reconsider. Have a nice day!")
    sys.exit() # ends code
    
    
    
     
