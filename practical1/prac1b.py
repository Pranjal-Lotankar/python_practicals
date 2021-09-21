#Python program to check if the input number is odd or even. A number is even if division by 2 give a reminder of 0. If reminder is 1, it is odd number.
num= int(input("Enter a number:"))
if (num%2)==0:
    print("{} is Even",format(num))
else:
    print("{} is odd",format(num))
