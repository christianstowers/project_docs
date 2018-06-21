#make a list into a not stupid looking sentence.

groceries = ['apples', 'bananas', 'outrage cheese', 'eggs', 'coffee']

def shop(value):
	print(len(value))
	for i in value:
		if value.index(i) == len(value) - 1:
			print('and %s.' %(i))
		else:
			print('%s, ' %(i), end="")

shop(groceries)