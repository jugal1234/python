# 2+4+6+8+⋯……+N
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  2+4+6+8+⋯……+N


print("Enter the value of N = ",end="")
n=int(input())
for i in range(2,n+1,2):
    if i<n-1:
        print(f"{i} +",end="")
    else:
        print(f"{i}",end="")
    

    
