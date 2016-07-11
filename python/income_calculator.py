from time import sleep
# ask the hourly rate of the user
# convert hourly rate to float
hourly_rate = float(input("What is your hourly rate?: "))

# ask the number of hours that the user has worked
# convert hours worked to float
hours_worked = float(input("How many hours did you work?: "))
sleep(1)
# multiply the hourly rate and the number of hours worked
gross_income = hours_worked * hourly_rate
print ("gross income: %.2f." % (gross_income))
sleep(1)
# get the 10% of the gross income
deduction = gross_income / 10
print ("deduction: %s" % (deduction))
sleep(1)

# add 1 to the deduction
total_deductions = deduction + 1

# subtract the deductions to the gross income
net_income = gross_income - total_deductions
print "drum roll please..."
sleep(1)
print ("take home pay: %.2f." % (net_income))

# show the gross income, net income and deduction