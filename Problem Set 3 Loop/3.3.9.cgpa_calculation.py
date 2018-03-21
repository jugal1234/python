#calculate cgpa
#Author Name : Jugal Kishore Chanda
print("\nAuthor Name : Jugal Kishore Chanda\n\n")
# this program is for calculating cgpa

print("What is your name? ",end="")
name = input();
print(f"{name}, how many semister you have passed? ",end="")
semister = int(input())
total_credit = 0
total_gpa = 0;
for i in range(1,semister+1):
    print(f"Enter the GPA of semister{i}__  ",end="")
    gpa = float(input())
    print(f"Enter the completed credit of semister{i}__  ",end="")
    credit = float(input())
    total_gpa =total_gpa + credit*gpa
    total_credit = total_credit + credit
print(f"Your cgpa is {total_gpa/total_credit}")
    
