import math

class Class:
  def __init__(self, subject, grades):
    self.subject = subject
    self.grades = grades

def main():
  # Create an empty list to store the subjects.
  subjects = []

  # Read the grades from the file.
  with open("grades.txt", "r") as f:
    grades = f.readlines()

  # Print the menu.
  print("Welcome to your Grade Calculator")
  print("1. New Entry")
  print("2. Highest Course Average")
  print("3. Lowest Course Average")
  print("4. Calculate your Average")
  print("5. Exit")

  # Get the user's choice.
  choice = int(input("Enter your choice: "))

  # Process the user's choice.
  while choice != 5:
    if choice == 1:
      # Add a new class.
      subject = input("Enter the name of the new subject: ")
      subjects.append([])
      for i in range(5):
        grade = float(input("Enter the grade for {}: ".format(subject)))
        subjects[-1].append(grade)
      with open("grades.txt", "a") as f:
        f.write("{}: {}\n".format(subject, subjects[-1]))
    elif choice == 2:
      # Find the class with the highest average grade.
      max_sort = -1
      max_avg_grade = -1.0
      for i in range(len(subjects)):
        sum = 0.0
        for j in range(len(subjects[i])):
          sum += subjects[i][j]
        avg_grade = sum / len(subjects[i])
        if avg_grade > max_avg_grade:
          max_sort = i
          max_avg_grade = avg_grade
      if max_sort == -1:
        print("No classes found.")
      else:
        print("Class with highest average grade: " + subjects[max_sort])
    elif choice == 3:
      # Find the class with the lowest average grade.
      min_sort = -1
      min_avg_grade = 101.0
      for i in range(len(subjects)):
        sum = 0.0
        for j in range(len(subjects[i])):
          sum += subjects[i][j]
        avg_grade = sum / len(subjects[i])
        if avg_grade < min_avg_grade:
          min_sort = i
          min_avg_grade = avg_grade
      if min_sort == -1:
        print("No classes found.")
      else:
        print("Class with lowest average grade: " + subjects[min_sort])
    elif choice == 4:
      # Calculate the average grades for each subject.
      for i in range(len(subjects)):
        sum_of_grades = sum(subjects[i])
        average_grade = sum_of_grades / len(subjects[i])
        print("The average grade for {} is {}".format(subjects[i], average_grade))
    else:
      print("Invalid choice.")

    print("Welcome to your Grade Calculator")
    print("1. New Entry")
    print("2. Highest Course Average")
    print("3. Lowest Course Average")
    print("4. Calculate your Average")
    print("5. Exit")

    # Get the user's choice.
    choice = int(input("Enter your choice: "))

if __name__ == "__main__":
  main()
