#average of n numbers
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for calculating average of n numbers

print("Input negative value for end of the input")

total_num = 0;
num = float(input())
index=1;
while(num>=0):
    total_num = total_num + num;
    
    num = float(input())
    index+=1
print(f"The average of {index-1} numbers is {total_num/(index-1)}")
    
