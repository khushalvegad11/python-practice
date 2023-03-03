#1.
# Write a Python program to print the following string in a specific format (see the output). Go to the editor
#Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
"""
Twinkle, twinkle, little star,
        How I wonder what you are!
                Up above the world so high,
                Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are!
        
        
"""
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#2.
# Write a Python program to find out what version of Python you are using.

import sys

print("python version")
print(sys.version)
print("sys version")
print(sys.version_info)

#3.
#Write a Python program to display the current date and time.

from datetime import datetime

print(datetime.now())

#4
# Write a Python program that calculates the area of a circle based on the radius entered by the user. 

from math import pi

r = float(input(" radius entered by the user:"))
print(' radius entered by the user:'+ str(r) + "is" + str(pi*r**2))