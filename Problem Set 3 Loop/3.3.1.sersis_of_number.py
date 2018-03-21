# 1+2+3+4+⋯……+N
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  1+2+3+4+⋯……+N


print("Enter the value of N = ",end="")
n=int(input())
for i in range(1,n+1):
    if i<n:
        print(f"{i} +",end="")
    else:
        print(f"{i}",end="")
    

    


