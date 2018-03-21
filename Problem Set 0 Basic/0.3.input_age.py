#input a integer number a print this and this type
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# This is input your name and age

#solution 1
print("For first solution")
name = input("What is your name? ")
print(f"Hello {name}, How old you are? ",end="")
age = input()
print(f"Hello {name} your age is {age} years old.")

print(f"Age is a {type(age)}")
age = int(age)
print(f"After type convertion age is a {type(age)}")

#solution 2
print("\n\nFor second solution")
name = input("What is your name? ")
print(f"Hello {name}, How old you are? ",end="")
age = int(input())
print(f"Hello {name} your age is {age} years old.")

print(f"Age is a {type(age)}")
