"""
eventually make this searchable by month, returning all birthdays within
the given month.
"""
birthdays = {'Rick': 'December 20th', 'Melanie': 'June 20th'}

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
