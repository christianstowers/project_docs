"""
eventually make this searchable by month, returning all birthdays within
the given month.
"""
birthdays = {'Dad': 'December 21st', 'Mum': 'July 20th', 'Sis': 'March 13th', 'Bruv': 'November 27th'}

while True:
	print('Enter a name: (black to quit)')
	name = input()
	if name == '':
		break

	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('No birthday information for ' + name)
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('Birthday database updated.')


	print('Enter a month: (blank to quit)')
	month = input()
	if month == '':
		break

#currently only returns month if directly associated with given name
	if month in birthdays[name]:
		print(name)
	else:
		print('no birthdays')
