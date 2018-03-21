# 1^2+3^2+5^2+7^2+⋯+101^2
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for  1^2+3^2+5^2+7^2+⋯+101^2


print("Enter the value of N = ",end="")
n=int(input())
sum=0;
for i in range(1,n+1):
    sum=sum+pow(i,2)
    if(i<n):
        print(f"{i}^2 + ",end="")
    else:
        print(f"{i}^2 = ",end="")
print(f"{sum}")
    
