# Importing necessary modules
import os

# Define the filename for the to-do list
todo_file = "todo_list.txt"

# Check if the to-do list file exists; if not, create it
if not os.path.exists(todo_file):
    with open(todo_file, "w"):
        pass

# Function to add a task to the to-do list
def add_task(task):
    with open(todo_file, "a") as file:
        file.write(task + "\n")

# Function to view the entire to-do list
def view_tasks():
    with open(todo_file, "r") as file:
        tasks = file.readlines()
        if not tasks:
            print("The to-do list is empty. Add your tasks using option 1.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

# Function to delete a task
def delete_task(task_number):
    tasks = []
    with open(todo_file, "r") as file:
        tasks = file.readlines()

    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)

        with open(todo_file, "w") as file:
            file.writelines(tasks)

        print(f"Deleted task: {deleted_task.strip()}")

# Function to update a task
def update_task(task_number):
    new_task = input("Enter the updated task: ")

    tasks = []
    with open(todo_file, "r") as file:
        tasks = file.readlines()

    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = new_task + "\n"

        with open(todo_file, "w") as file:
            file.writelines(tasks)

        print("Task updated successfully!")

# Main program loop
while True:
    print("\nTo-Do List Manager\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        task = input("Enter the task to add: ")
        add_task(task)
        print("Task added successfully!")

    elif choice == "2":
        print("To-Do List:")
        view_tasks()

    elif choice == "3":
        task_number = int(input("Enter the task number to update: "))
        update_task(task_number)

    elif choice == "4":
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
