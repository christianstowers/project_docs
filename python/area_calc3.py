'''
Python 3
This is a calculator that will be able to determine the area of circles and triangles.
The user will select a shape and the calculator will calculate the area of the shape selected.
'''
from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print ("The calculator is starting up...")

print ('%s/%s/%s %s:%s' % (now.month, now.day, now.year, now.hour, now.minute))
sleep(1)

hint = "Don't forget to include the correct units! \nExiting... "
  
option = input("Enter C for Circle or T for Triangle: ")

option = option.upper()

if option == 'C':
    radius = float(input("Enter the radius: "))
    area = pi * radius**2
    print ("The pie is baking...")
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
elif option == 'T':
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = (0.5)*base*height
    print ("Computing...")
    sleep(1)
    print ("Area: %.2f. \n%s" % (area, hint))
else:
	print ("DOES NOT COMPUTE \nShutting down...")