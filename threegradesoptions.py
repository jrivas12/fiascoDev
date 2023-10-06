import math

def threeGrades():
  grade = int(input("Enter grade between 1-100: "))
  while grade < 1 or grade > 100:
    grade = int(input("Enter grade between 1-100: "))
  return grade

def averageGrade(grades):
  total = 0
  for grade in grades:
    total += grade
  average = total / len(grades)
  return average

def maxGrade(grades):
  max = grades[0]
  for grade in grades:
    if grade > max:
      max = grade
  return max

def minGrade(grades):
  min = grades[0]
  for grade in grades:
    if grade < min:
      min = grade
  return min

def main():
  grades = []
  menu = """
1. Enter three grades:
2. Show Average
3. Show Highest Grade
4. Show Lowest Grade
5. Exit
"""
  while True:
    print(menu)
    option = int(input("Enter Option: "))
    if option == 1:
      for i in range(3):
        grades.append(threeGrades())
    elif option == 2:
      average = averageGrade(grades)
      print("average = ", average)
      if average >= 90:
        print("The average grade is: A")
      elif average >= 80:
        print("The average grade is: B")
      elif average >= 70:
        print("The average grade is: C")
      elif average >= 60:
        print("The average grade is: D")
      else:
        print("The average grade is: F")
    elif option == 3:
      max = maxGrade(grades)
      print("The Highest Grade is: ", max)
    elif option == 4:
      min = minGrade(grades)
      print("The Lowest Grade is: ", min)
    elif option == 5:
      break
    else:
      print("error: Please Enter a Correct Choice!")
  
if __name__ == "__main__":
  main()
