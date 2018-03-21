#Multiplication Table Of given number
#Auther Name:Jugal Kishore Chanda
print("Auther Name:Jugal Kishore Chanda")
#this program is for print a multiplication table

n = int(input("Please input a number.. "))

for i in range(1,11,1):
    print(f"{n:2} x {i:2} = {n*i:3}")
