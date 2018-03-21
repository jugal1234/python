# print a pattern of 3.2.6.5
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  print a pattern

n = int(input("enter the value of row = "))
div = n//2

for i in range(n):
    if(i<=div):
        incriment = 1
        initial = 0
        end = i+1
    else:
        incincriment = 1
        initial = i
        end = n
    for j in range(initial,end,incriment):
        print("*",end="")
    print("")
