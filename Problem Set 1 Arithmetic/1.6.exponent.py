#Fina a^b
#Author Name:Jugal Kishore Chanda
print("\n\nAuthor Name:Jugal Kishore Chanda\n\n")
#this prgoam is forinput two number and find a^b

a,b = int(input("a = ")),int(input("b = "))
print(f"{a}^{b} = {a**b} (using **)")
print(f"{a}^{b} = {pow(a,b)} (using pow())")
import math
print(f"{a}^{b} = {math.pow(a,b)} (using math.pow())")

