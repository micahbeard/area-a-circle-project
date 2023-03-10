"""
Project 1 Area of a circle calculator: Create a script that calculates the area of a circle for a user
Allow a user to enter their name in the console
Print the type of what was entered by the user
Greet the user with a nice statement and tell them what this script does
Let the user enter the radius of their circle
Print the type of what they entered
Calculate the area of the circle
Return the area of the circle and thank them for using the script
"""


import time
import math

# Countdown Starting Number
# i = 3

# Input for User's Name
usr_name = input("Enter your name here: ")
print(str(type(usr_name)))

time.sleep(1)

# Welcome Text and Decription
print("Welcome, " + usr_name)
print("I am here to calulate the area of a circle of your choosing")

time.sleep(1)

# Where User Enters Radius of their Circle
r_circle = input("Please enter the radius of your circle: ")
print(str(type(r_circle)))

# Math to Calculate Area
a_circle = math.pi * pow(int(r_circle), 2)
print("Calulating...")

# Countdown

for i in range(3,0,-1):
    print(i)
    time.sleep(.5)

"""
while i >= 1:
    print(i)
    i = i - 1
    time.sleep(.5)
"""
a_circle = round(a_circle, 2)

time.sleep(1)

print("The area of your circle is: "+ str(a_circle))
print("Thank you for using my script. Come again!")