# pseudo:
# request there lengths of a triangle from the users
# calculate the area of the triangle using Heron's Formula
# print out the area of the triangle

import math

side1 = float(input("Please input the first side of the triangle: "))
side2 = float(input("Please input the second side of the triangle: "))
side3 = float(input("Please input the third side of the triangle: "))

# First calculate the semi-perimeter
s = (side1 + side2 + side3) / 2

# Calculate the area using Heron's Formula
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))

print(f"The area of the triangle is: {area}")