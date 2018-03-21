# print a pattern of 3.2.6.8
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  print a pattern

n = int(input("enter the value of row = "))

div = n//2
div = div+1; 
for i in range(div):
    for j in range(div-1,i,-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print("")


for i in range(div-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(2*(div-1)-1,2*i,-1):
        print("*",end="")
    print("")

