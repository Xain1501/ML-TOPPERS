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







lambda_func = lambda x: x + 5

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
  
  def AddGrade(self, subject, marks):
      self.marks[subject] = marks
  
  def ApplyBonus(self, lambda_func):
    
    for subject in self.marks:
      self.marks[subject] = min(100, lambda_func(self.marks[subject]))

  def GenRep(self):
    report = "Name: {self.name} Age: {self.age}\n"
    
    for subject, marks in self.marks.items():
      report += f"{subject}: {marks}\n"
   
    avg = self.CalAvg()
   
    report += f"Average: {avg:}\nGrade: {self.
    CalGrade(avg)}"
    return report

  def SaveToFile(self, filename):
    
    with open(filename, 'w') as file:
      
      file.write(self.GenRep())
  
  @staticmethod
  def LoadFromFile(filename):
    
    with open(filename, 'r') as file:
      report = file.read()
      
      print(report) 









name= input(" Enter Your Name: ")
age= int(input(" Enter Your Age: "))

subs=["English","maths","urdu"]
student = Student(name, age)

for i in subs:
 subject = input(f" Enter marks for {i}: ")
 marks = int(input(f" Enter marks for {i}: "))

 student.add_grade(subject, marks)

avg = student.CalAvg()
print(f"Average marks: {avg:.2f}")

apply_bonus = input("do you want to apply bonus (yes/no): ").strip().lower()

if apply_bonus == 'yes':
   
    student.ApplyBonus(lambda_func)

filename = f"{ name}_report.txt"

student.SaveToFile(filename)  
Student.LoadFromFile(filename)
