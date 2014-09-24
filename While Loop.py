#Project 5: Indefinite Iteration

#1: Number Guessing Game

import random

print ('Choose a number between 1 to 100 and the Number Genie will find it for you!'
       'All you have to do is type Up for a higher number or down for a lower number.'
       'If I get it correct just type in yes!')
high = 100
low = 0
answer = ''
number = random.randint(low, high)

while answer != 'yes':
    print ("Is the number", number,"?")
    answer = input()
    if answer.lower() == "up":
        low = number + 1
        number = random.randint(low, high)
    elif answer.lower() == "down":
        high = number - 1
        number = random.randint(low, high)
    elif answer.lower() == "yes":
        print ("Well you have two more wishes, so get thinking!")
    else:
        print ("That is an invalid answer. Try up, down or yes")



