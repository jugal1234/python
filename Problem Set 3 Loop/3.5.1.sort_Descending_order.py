#sort an array in dscending order
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for sorting an array in dscending order 


#for integer number
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

for i in range(n):
    for j in range(i+1,n,1):
        if array[j]>array[i]:
            temp = array[j]
            array[j]=array[i]
            array[i]=temp

print(f"1. The descending order is  {array}")


