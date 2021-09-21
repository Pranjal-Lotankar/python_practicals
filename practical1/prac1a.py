#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
name = input("Hello! Please enter your name:")
print ("Hello "+  name)
age= int(input("Enter your age:"))
year_now= datetime.datetime.now()
print (year_now.year)
print("You will turn 100 in" + str(int(100-age)+ int(year_now.year)))
