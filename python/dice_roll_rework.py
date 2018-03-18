#03122018_dice_roll_blind
from time import sleep
from random import randint

#number of sides, user guess, die total, condition

num_dice = int(input("How many dice: "))
num_sides = int(input("How many sides each: "))
totes_sides = num_dice * num_sides
sleep(.5)
print("The highest possible roll is %s." % (totes_sides))
sleep(.5)
guess = int(input("Make a guess: "))

#needs a for loop here. if given 1 die, this logic doesn't work.
first_roll = randint(1, num_sides)
second_roll = randint(1, num_sides)
totes_rolls = first_roll+ second_roll
print("Your guess: %s" % (guess))
sleep(.5)
print("Rolling.....")
sleep(2)
if(guess == totes_rolls):
	print("By jove, muhboi! You've won! So shines a good deed.")
else:
	print("WRONG. It was %s. You lose. Good day, sir!" % (totes_rolls))