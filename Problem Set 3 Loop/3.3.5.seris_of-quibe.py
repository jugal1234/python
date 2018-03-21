# 2^3+4^3+6^3+8^3+⋯+N^3
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  2^3+4^3+6^3+8^3+⋯+N^3


print("Enter the value of N = ",end="")
n=int(input())
sum=0;
for i in range(2,n+1):
    sum=sum+pow(i,3)
    if(i<n):
        print(f"{i}^3 + ",end="")
    else:
        print(f"{i}^3 = ",end="")
print(f"{sum}")
    
