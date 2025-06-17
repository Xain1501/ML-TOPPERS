# MIni PROJECT 1
# requirements:
# • Take Input from the User (name and age)
# • Take Input For 3 Subjects in a dictionary subject:marks (english, math, urdu)
# • Define a Function to Calculate Average of all subjects together
# • Grade Assignment using if/elif/else
# Average Score Grade
# 80 or above A
# 60 to 79 B
# 40 to 59 C
# Below 40 F
# • Bonus give using lambda function (Ask the user: Add 5 bonus marks to all subjects? (yes/no))
# • Write the Report to a File
# Name: Ali
# Age: 20
# Math: 90
# English: 83
# Urdu: 95
# Average: 89.33
# Grade: A
# • Read and Display the Report Card


def CalAvg(marks):
  Total=0
  for i in marks.values():
    Total+= i
  
  Avg= Total/len(marks)
  return Avg

def CalGrade():
  if Avg>=80:
    Grade='A'
  elif Avg>=60:
    Grade='B'
  elif Avg>=40:
    Grade='C'
  else:
    Grade ='F'
  return Grade


def WriteReport(name,age,Grade,Avg,marks):
  fd=open("report.txt","a")
  fd.write("Name:" + name)
  fd.write("Age" + str(age))
  fd.write("Grade" + Grade)
  fd.write("Average" + str(Avg))
  for sub, mark in marks.items:
   fd.write(f"{sub}: {mark}\n")

  fd.write("\n\n")

  

def ReadReport():
  fd= open("report.txt","r")
  for line in fd:
    print(line.strip())
    fd.close()


name= input("Enter Your Name: ")
age= int(input("Enter Your Age: "))
marks={}
subs=["English","Math","Urdu"]

for key in subs:
  mark=float(input("Enter marks: "))
  marks[key]= mark

Avg= CalAvg(marks)
Grade =CalGrade(Avg)
WriteReport(name,age,Grade,Avg,marks)
ReadReport()


ask= lambda: input("Do you want to give bonus marks? (y/n): ")
Bonus=ask()

if Bonus=='y':
  for key,val in marks:
    marks[key]= val+5




Avg= CalAvg(marks)
Grade =CalGrade(Avg)

