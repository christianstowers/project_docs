'''
Command Line Accessible Calendar
'''

from time import sleep, strftime

USER_FIRST_NAME = "Crisco"

# 7
calendar = {}

def welcome():
	print "Welcome to your calendar, " + USER_FIRST_NAME + "!"
	print "Calendar initializing..."
	sleep(1)
  
  # 11 
	print "Today is " + strftime("%A %B %d, %Y")
  # 12
	print "The Current time is " + strftime("%H:%M:%S")
	sleep(1)
	print "What would you like to do?"
  
# 14
def start_calendar():
	welcome()
	start = True
	while start:
# 17
		user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, or X to Exit: ")
		user_choice = user_choice.upper()
		if user_choice == "V":
# 20
			if len(calendar.keys()) < 1:
				print "The calendar is currently empty."
			else:
				print calendar
		elif user_choice == "U":
			date = raw_input("What date? ")
			update = raw_input("Enter the update: ")
# 24
			calendar[date] = update
			print "Update successful."
		elif user_choice == "A":
			event = raw_input("Enter event: ")
			date = raw_input("Enter date (MM/DD/YYYY): ")
			if (len(date)) > 10 or int(date[6:]) < int(strftime("%Y")):
				print "Hmm..."
				sleep(2)
				print "That date doesn't work."
        # 31
				try_again = raw_input("Try Again? Y for Yes, N for No: ")
				try_again = try_again.upper()
				if try_again == "Y":
					continue
				else:
					start = False
			else:
				print "Processing..."
				sleep(1)
				calendar[date] = event
				print "Event update successful"
		elif user_choice == "D":
			if len(calendar.keys()) < 1:
				print "The Calendar is currently empty."
			else:
				event = raw_input("What event?")
				for date in calendar.keys():
					if event == calendar[date]:
						del calendar[date]
						print "Event deletion successful"
						print calendar
					else:
						print "That's not an event of yours currently."
		elif user_choice == "X":
			start = False
		else:
			print "Invalid command. Exiting Program..."
			sleep(1)
			start = False

#test line
start_calendar()



'''
quick question: 
booleans vs. math: why in step 20 is it better to use 
"if len(calendar.keys()) < 1: ... " 
instead of 
"if calendar.keys(len(0)) == True: ..." ?
Does the second quotation even work?
https://www.codecademy.com/en/courses/python-ext/projects/calendar?user_id=54a1dbf2d3292f41c201565a
2h ago

Hi Christian, I'm Jerry. Let's take a look!
2h ago

So len(calendar.keys()) will return the number of keys calendar has 
The second one would return an error, as you can't take the length of an integer len(0)
'''

'''
      ok. last ridiculous question: why [] instead {} here to pass in date?
2h ago

Because date is the key, and calendar is the dictionary. In order to get the value, we need its key to find it:
calendar[date] -> will get us our value for that date
2h ago
eggsellent. thank you
      '''



        
    