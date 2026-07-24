# Practice of Python Basic Concepts: Variables, Data Types, Operators, Functions & Loops

# Variables
name = "Momina Javaid"
age = 20
city = "Lahore"
course = "Python Programming"
cgpa = 3.77

print(name)
print(age)
print(city)
print(course)
print(cgpa)

# Data Types
employee_name = "Ali Ahmed"
emp_age = 36
emp_id = 23476
isPermanent_emp = True

print(type(employee_name))
print(type(emp_age))
print(type(emp_id))
print(type(isPermanent_emp))

# Arithmetic Operators
num1 = 20
num2 = 10

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 % num2)
print(num1 / num2)

# Comparison Operators
var1 = 24
var2 = 12

print(var1 > var2)
print(var1 >= var2)
print(var1 < var2)
print(var1 <= var2)
print(var1 == var2)
print(var1 != var2)

# Logical Operators
is_student = True
has_id = False

print(is_student and has_id)
print(is_student or has_id)
print(not is_student)
print(not has_id)

# Conditional Statements (if-elif-else)
number = 58

if number > 0:
    print("Number is Positive.")
elif number < 0:
    print("Number is Negative.")
else:
    print("Number is Zero.")

# For Loop
n = 5

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# While Loop
nbr = 2

while nbr <= 20:
    print(nbr)
    nbr += 2

# Functions

def greetUser(name):
    print("Hello", name)

greetUser("Zoya Iqbal")


def sumNumbers(c, d):
    total = c + d
    print("Sum =", total)

sumNumbers(33, 45)


def isEven(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

isEven(25)


def squareNum(number):
    print("Square =", number * number)

squareNum(5)

# Mini Task by using all basic concepts 

std_id = 3457836
std_name = "Fakhra Khanum"
std_age = 19


def eligible_for_Scholarship(marks, attendance):
    print("Student ID:", std_id)
    print("Student Name:", std_name)
    print("Student Age:", std_age)

    if marks >= 80 and attendance >= 75:
        print("Eligible for Scholarship")
    else:
        print("Not Eligible for Scholarship")


eligible_for_Scholarship(89, 79)

print(type(std_id))
print(type(std_name))
print(type(std_age))

# Mini Task 1 - Employee Bonus Eligibility

emp_id = 1023
emp_name = "Ali Ahmed"
salary = 65000
years_of_service = 5

def check_bonus(salary, years_of_service):
    print("Employee ID:", emp_id)
    print("Employee Name:", emp_name)
    print("Salary:", salary)
    print("Years of Service:", years_of_service)

    if salary >= 50000 and years_of_service >= 3:
        print("Eligible for Bonus")
    else:
        print("Not Eligible for Bonus")

check_bonus(salary, years_of_service)

print(type(emp_id))
print(type(emp_name))
print(type(salary))
print(type(years_of_service))

# Mini Task 3 - Product Discount Calculator

product_name = "Laptop"
price = 70000
quantity = 2

def calculate_bill(price, quantity):
    total = price * quantity

    print("Product:", product_name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total Bill:", total)

    if total >= 100000:
        discount = total * 0.10
        final_bill = total - discount
        print("Discount:", discount)
        print("Final Bill:", final_bill)
    else:
        print("No Discount")

calculate_bill(price, quantity)

print(type(product_name))
print(type(price))
print(type(quantity))