import os

class Class:
  def __init__(self, subject, grades):
    self.subject = subject
    self.grades = grades

def main():
  # Get the subject.
  subject = input("Enter the name of the new subject: ")

  # Get the number of grades.
  num_grades = int(input("Enter the number of grades: "))

  # Create a new class.
  new_class = Class(subject, [])

  # Get the grades for the new class.
  for i in range(num_grades):
    new_class.grades.append(float(input("Enter the grade for the new subject: ")))

  # Write the new class and grades to the file grades.txt.
  with open("grades.txt", "a") as f:
    f.write(subject + ": " + " ".join([str(grade) for grade in new_class.grades]) + "\n")

  # Prompt the user if he/she would like to calculate the average of the grades.
  calculate_average = input("Would you like to calculate the average of the grades? (Y/N): ")

  if calculate_average == "Y":
    # Calculate the average of the grades.
    average = sum(new_class.grades) / len(new_class.grades)

    # Print the average of the grades.
    print("The average grade for", subject, "is", average)

if __name__ == "__main__":
  main()