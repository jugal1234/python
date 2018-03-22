#Find the area of triangle from three sides
#Auther Name : Jugal Kishore Chanda
print("\n\nAuther Name : Jugal Kishore Chanda\n\n")
#This program is for finding the area of a triangle from three sides

a,b,c = float(input("Enter the 1st side triangle ")),float(input("Enter the 2nd side of triangle ")),float(input("Enter the 3rd side of triangle "))

p = (a+b+c)/2
import math
print(f"The area of triangle is {math.sqrt(p*(p-a)*(p-b)*(p-c))}")
