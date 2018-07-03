#printing an inventory list and item total

stuff = {
	'rope': 2,
	'pants': 0,
	'wooden sword': 1,
	'tent': 10,
	'bundle of sticks': 3,
	'national bird of Paraguay': 6,
	'jar of nutella': 1
}

def invList(inv):
	item_total = 0
	print('Inventory:')
	for k, v in inv.items():
		print(v, k)
		item_total += v
	print('Item total: ' + str(item_total))
	if item_total > 20:
		print('Only trash humans hoard useless crap. Get rid of ' + str(item_total - 20) + ' items.')
	else:
		print('You still have space for ' + str(abs(item_total - 20)) + ' more items.')
invList(stuff)