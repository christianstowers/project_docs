'''
The Roll of the Dice
'''
from random import randint
from time import sleep

def get_user_guess():
	user_guess = int(raw_input("Guess the number: "))
	return user_guess

def roll_dice(number_of_sides):
	#number_of_sides = int(raw_input("How many sides to the dice: "))
	first_roll = randint(1, number_of_sides)
  	second_roll = randint(1, number_of_sides)
  	#why is this next line necessary?
  	max_val = number_of_sides * 2
  	print "The maximum dice roll is " + str(max_val)
  	sleep(1)
  	#next line inside/outside the function?
  	user_guess = get_user_guess()
  
	if user_guess > max_val:
  		print "That guess is too damn high!"
    	return
    else:
  		print "Rolling..."
  		sleep(2)
    	# %s : used to format string variables
    	# %d : used to format integers
    	print "Roll 1 is %d" % (first_roll)
    	sleep(1)
    	print "Roll 2 is %d" % (second_roll)
    	sleep(1)
    	total_roll = first_roll + second_roll
    	print total_roll
    	print "Result..."
    	sleep(1)
    	if user_guess > total_roll:
      		print "By Jove, you won!"
      		return
    	else:
      		print "You lose."
      		return
    
roll_dice(6)
    
    

    
    