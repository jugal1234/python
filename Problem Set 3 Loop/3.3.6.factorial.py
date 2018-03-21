#find the factorial of a number
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for finding factorial of a number

print("please input a number for factorial ",end="")
x = int(input())
fact = 1;
for i in range(2,x+1):
    fact=fact*i
print(f"The factorial of {x} is {fact}")
