# print a pattern of 3.2.6.6
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  print a pattern

n = int(input("enter the value of row = "))
index=1
for i in range(n):
    for j in range(i+1):
        print(f"{index} ",end="")
        index=index+1
    print("")
