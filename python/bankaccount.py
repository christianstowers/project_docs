class BankAccount(object):
	balance = 0
	def __init__(self, name):
		self.name = name
	def __repr__(self):
		return "This account belongs to %s. The balance is $%.2f" %(self.name, self.balance)
	def show_balance(self):
		print "The current balance is $%.2f" %(self.balance)
	def deposit(self, amount):
		if amount <= 0:
			print "Deposit amount at or below zero"
			return
		else:
			print "Deposit amount: $%.2f" %(amount)
			self.balance += amount
			self.show_balance()
	def withdraw(self, amount):
		if amount > self.balance:
			print "Withdrawal amount too high"
			return
		else:
			print "Withdrawal amount: $%.2f" %(amount)
			self.balance -= amount
			self.show_balance()
      