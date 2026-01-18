#Using if else statements in Python
#If-Else example
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number")    

#If-Elif-Else example
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: F")

#Logical operators with If statements
age = int(input("Enter your age: "))
if age >= 18 and age < 65:
    print("You are eligible to work")
else:
    print("You are not eligible to work")

if age < 18 or age >= 65:
    print("You are either a minor or a senior citizen")
else:
    print("You are an adult")

if not(age < 18):
    print("You are an adult")
else:
    print("You are a minor")