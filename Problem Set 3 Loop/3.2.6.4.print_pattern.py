# print a pattern of 3.2.6.4
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  print a pattern

n = int(input("enter the value of row = "))
for i in range(n-1,-1,-1):
    for j in range(2*i+1):
        print("*",end="")
    print("")

