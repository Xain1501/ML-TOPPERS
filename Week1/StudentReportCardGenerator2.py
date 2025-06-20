# You are required to implement a in Python using Object-Oriented
# Programming (OOP) principles.

# Student Report Card Generator

# Problem:
# Write a Python program using a class called to manage a student's academic
# performance. The program must:

# Student

# Part A — Class Implementation
# 1. Create a class Student with the following:
# • Attributes: name , age , and grades (a dictionary to store subject → marks)
# • Method add_grade(subject, marks) to add a subject and its marks to the dictionary
# • Method calculate_average() to compute the average of all subject marks
# • Method assign_grade() to return the letter grade based on average:
# Average Score Grade
# 80 and above A
# 60 to 79 B
# 40 to 59 C
# Below 40 F

# 2. Add a method that applies a lambda function to increase all subject
# marks (max 100).

# apply_bonus(lambda_func)

# 3. Add methods to:
# • generate_report() to return a formatted report string.
# • save_to_file(filename) to save the report to a .txt file.
# • A @staticmethod load_from_file(filename) to read and display the report.
# Part B — Program Flow
# 1. Prompt the user to enter the student’s name and age .
# 2. Take marks input for 3 subjects: Math, English, and Urdu.
# 3. Ask the user:
# Do you want to apply 5 bonus marks to all subjects? (yes/no)
# If yes, use a lambda function to apply the bonus

# Part C — File Handling & Output
# 1. Save the report to a file named <name>_report.txt
# 2. Read from the file and display the report in the console.
# Example Output:

# Enter student's name: Ali Enter age: 20 Enter marks for Math: 90 Enter marks for English:
# 83 Enter marks for Urdu: 95 Add 5 bonus marks to all subjects? yes Report saved successfu
# lly! Report Card: Name: Ali Age: 20 Math: 95 English: 88 Urdu: 100 Average: 94.33 Grade:



# You are required to implement a in Python using Object-Oriented
# Programming (OOP) principles.

# Student Report Card Generator

# Problem:
# Write a Python program using a class called to manage a student's academic
# performance. The program must:

# Student

# Part A — Class Implementation
# 1. Create a class Student with the following:
# • Attributes: name , age , and grades (a dictionary to store subject → marks)
# • Method add_grade(subject, marks) to add a subject and its marks to the dictionary
# • Method calculate_average() to compute the average of all subject marks
# • Method assign_grade() to return the letter grade based on average:
# Average Score Grade
# 80 and above A
# 60 to 79 B
# 40 to 59 C
# Below 40 F

# 2. Add a method that applies a lambda function to increase all subject
# marks (max 100).

# apply_bonus(lambda_func)

# 3. Add methods to:
# • generate_report() to return a formatted report string.
# • save_to_file(filename) to save the report to a .txt file.
# • A @staticmethod load_from_file(filename) to read and display the report.
# Part B — Program Flow
# 1. Prompt the user to enter the student’s name and age .
# 2. Take marks input for 3 subjects: Math, English, and Urdu.
# 3. Ask the user:
# Do you want to apply 5 bonus marks to all subjects? (yes/no)
# If yes, use a lambda function to apply the bonus

# Part C — File Handling & Output
# 1. Save the report to a file named <name>_report.txt
# 2. Read from the file and display the report in the console.
# Example Output:

# Enter student's name: Ali Enter age: 20 Enter marks for Math: 90 Enter marks for English:
# 83 Enter marks for Urdu: 95 Add 5 bonus marks to all subjects? yes Report saved successfu
# lly! Report Card: Name: Ali Age: 20 Math: 95 English: 88 Urdu: 100 Average: 94.33 Grade:

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.marks = {}

  def CalAvg(self):
    Total=0
    for i in self.marks.values():
      Total+= i
    
    Avg= Total/len(self.marks)
    return Avg
  
  def CalGrade(Avg):
    if Avg>=80:
      Grade='A'
    elif Avg>=60:
      Grade='B'
    elif Avg>=40:
      Grade='C'
    else:
      Grade ='F'
    return Grade
  
  def add_grade(self, subject, marks):
      self.marks[subject] = marks
  
