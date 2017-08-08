# This program is about guessing the random number.
#If we guess bigger number then the program will say down.
#If we guess smaller number then the program will say up.
#Soonyoung Jeoung

#Import random module
import random

#variable declearation 
play = True
x= random.randint(0,10) #generate random number

#guessing number with loop
while (play == True): #while start
    
    user = int(input("enter your integer btw 0 and 10--")) #user input

    #conditonal_statement
    if (user < x):
	    print("up") #when user guesses less than actual number.
    elif (user > x):
	    print("down") #when user guesses greater than actual number.
    elif (user == x):
	    print("you won! good job") # Correct.
	    play = False
	    
#end loop

input() # stay in console.
