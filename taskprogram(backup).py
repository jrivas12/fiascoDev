import os

class Task:
    def __init__(self, id, category, description, completed):
        self.id = id
        self.category = category
        self.description = description
        self.completed = completed

def add_task(tasks):
    task_id = len(tasks) + 1
    print("Categories:")
    print("1. Home")
    print("2. School")
    print("3. Personal")
    print("4. Payments")
    print("5. Other")
    category_choice = int(input("Enter the category number: "))
    category_map = {
        1: "Home",
        2: "School",
        3: "Personal",
        4: "Payments",
        5: "Other"
    }
    category = category_map.get(category_choice, "Other")
    description = input("Enter task description: ")
    completed = False
    task = Task(task_id, category, description, completed)
    tasks.append(task)
    print("Task added successfully!")

    # Write the task to the output file
    with open("tasks.txt", "a") as file:
        file.write(f"{task.id}\n")
        file.write(f"{task.category}\n")
        file.write(f"{task.description}\n")
        file.write(f"{task.completed}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for task in tasks:
        print("ID:", task.id)
        print("Category:", task.category)
        print("Description:", task.description)
        print("Status:", "Completed" if task.completed else "Incomplete")
        print()

def load_tasks_from_file():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for i in range(0, len(lines), 4):
                task_id = int(lines[i].strip())
                category = lines[i + 1].strip()
                description = lines[i + 2].strip()
                completed = lines[i + 3].strip() == "True"
                task = Task(task_id, category, description, completed)
                tasks.append(task)
    else:
        print("No tasks file found. Creating a new one.")

    return tasks

def mark_task_complete(tasks):
    if not tasks:
        print("No tasks found.")
        return

    task_id = int(input("Choose a task to mark as complete (Enter the ID): "))

    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print("Task marked as complete!")

            # Update the task completion status in the output file
            with open("tasks.txt", "w") as file:
                for t in tasks:
                    file.write(f"{t.id}\n")
                    file.write(f"{t.category}\n")
                    file.write(f"{t.description}\n")
                    file.write(f"{t.completed}\n")
            return

    print("Invalid task ID.")

def delete_task(tasks):
    if not tasks:
        print("No tasks found.")
        return

    task_id = int(input("Choose a task to delete (Enter the ID): "))

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            print("Task deleted successfully!")

            # Update the tasks in the output file
            with open("tasks.txt", "w") as file:
                for t in tasks:
                    file.write(f"{t.id}\n")
                    file.write(f"{t.category}\n")
                    file.write(f"{t.description}\n")
                    file.write(f"{t.completed}\n")

            return

    print("Invalid task ID.")

def main():
    tasks = load_tasks_from_file()

    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

        print()

if __name__ == "__main__":
    main()
