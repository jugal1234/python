#find the minimum number of N numbers
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for finding minimum number


#solution1
#for integer number
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

for i in range(n):
    for j in range(i+1,n,1):
        if array[j]<array[i]:
            temp = array[j]
            array[j]=array[i]
            array[i]=temp

print(f"1. The Minimum number is {array[0]} from {array}")

min = array[0]
for i in range(n):
    if(array[i]<min):
        min=array[i]

print(f"2. The Minimum number is {min} from {array}")

