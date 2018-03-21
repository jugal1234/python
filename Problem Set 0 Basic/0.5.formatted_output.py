#input a float number a print this and this type
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# This is input your name and age and cgpa

#solution 1
print("For first solution")
name = input("What is your name? ")
print(f"Hello {name}, How old you are? ",end="")
age = input()
print(f"{name},Please tell us your versity cgpa.  ",end="")
cgpa = input()
print(f"Hello {name} your age is {age} years old and your cgpa is {cgpa}")


print(f"cgpa is a {type(cgpa)}")
cgpa = float(cgpa)
print(f"After type convertion cgpa is a {type(age)}")

#solution 2
print("\n\nFor second solution")
name = input("What is your name? ")
print(f"Hello {name}, How old you are? ",end="")
age = int(input())
print(f"{name},Please tell us your versity cgpa.  ",end="")
cgpa = float(input())
print(f"Hello {name} your age is {age} years old and your cgpa is {cgpa}")

print(f"cgpa is a {type(cgpa)}")

print("\n\nThanks for showing my program\n\n")
