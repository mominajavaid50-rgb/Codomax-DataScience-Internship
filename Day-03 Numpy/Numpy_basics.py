# Day 3 Task - NumPy Basics

# Import NumPy Library
import numpy as np

# 1D Array - Employee Salaries
emp_salaries_1D = np.array([30000, 35000, 40000, 45000, 50000])

print("Employee Salaries")
print(emp_salaries_1D)
print("Type:", type(emp_salaries_1D))
print("Shape:", emp_salaries_1D.shape)
print("Size:", emp_salaries_1D.size)
print("Data Type:", emp_salaries_1D.dtype)
print("Dimensions:", emp_salaries_1D.ndim)

# 2D Array - Student Marks
std_marks_2D = np.array([
    [56, 67, 65],
    [78, 67, 98],
    [69, 88, 59]
])

print("\nStudent Marks")
print(std_marks_2D)
print("Type:", type(std_marks_2D))
print("Shape:", std_marks_2D.shape)
print("Size:", std_marks_2D.size)
print("Data Type:", std_marks_2D.dtype)
print("Dimensions:", std_marks_2D.ndim)

# Mathematical Operations
phone_price = np.array([45000, 78000, 65000, 34000])
iron_price = np.array([5600, 7600, 8900, 4900])

print("\nAddition")
print(phone_price + iron_price)

print("Subtraction")
print(phone_price - iron_price)

print("Division")
print(phone_price / iron_price)

print("Multiplication")
print(phone_price * iron_price)

# Statistical Functions
print("\nEmployee Salary Analysis")
print("Total Salary:", np.sum(emp_salaries_1D))
print("Average Salary:", np.mean(emp_salaries_1D))
print("Highest Salary:", np.max(emp_salaries_1D))
print("Lowest Salary:", np.min(emp_salaries_1D))

# Array Slicing
product_id = np.array([75343, 84344, 83037, 87473, 73982])

print("\nArray Slicing")
print("First Three IDs:", product_id[0:3])
print("Last Two IDs:", product_id[-2:])
print("Middle IDs:", product_id[1:4])

# Array Indexing
movies_name = np.array(["3 Idiots", "1920", "Alone", "Load Wedding", "The Legend of Maula Jatt"])

print("\nMovie Names")
print("First Movie:", movies_name[0])
print("Third Movie:", movies_name[2])
print("Last Movie:", movies_name[4])

std_marks = np.array([65, 78, 56, 98, 69, 87, 76, 49])

print("\nStudent Marks")
print("Second Student:", std_marks[1])
print("Fourth Student:", std_marks[3])
print("Sixth Student:", std_marks[5])
print("Last Student:", std_marks[7])

# Mini Task - Weather Temperature Analysis
city_temperature = np.array([34, 40, 35, 38, 41, 42])

print("\nCity Temperature")
print(city_temperature)

print("Total Temperature:", np.sum(city_temperature))
print("Average Temperature:", np.mean(city_temperature))
print("Highest Temperature:", np.max(city_temperature))
print("Lowest Temperature:", np.min(city_temperature))

print("First Two Days:", city_temperature[0:2])
print("Last Two Days:", city_temperature[4:6])