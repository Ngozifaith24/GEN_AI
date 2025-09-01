# no 2 **Hands-On Exercise**

# Try improving the to-do list application
# with these additional features:

# 1. Save tasks to a file so that they persist after
# restarting the program.
# 2. Mark tasks as completed and display
# completed tasks separately.
# 3. Allow editing tasks instead of just adding and
# removing them.
# 4. Improve the user interface with better
# formatting and menu options.
# 5. Add a priority system to sort tasks by urgency.

# Simple To-Do List Application

# List to store tasks
tasks = []
completed_tasks = []
# Function to add a task to the list
def add_task(task):
    # return( tasks)
    tasks.append(task)
    print(f'Task "{task}" added!')

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed!')
    else:
        print("Task not found!")

# Function to mark completed tasks     
def add_task(completed_task):
    # return( tasks)
    completed_tasks.append(completed_task)
    print(f'Task "{completed_task}" Completed!')
# Function to display all tasks
def view_tasks():
    if tasks:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, 1):  # Start numbering from 1
            print(f'{idx}. {task}')
    else:
        print("No tasks in your list!")
# Function to display all completed tasks
def completed_task():
    if completed_tasks:
        print("Your completeded task includes: ")
        for idx, completed_task in enumerate(completed_tasks, 1):
            print(f'{idx}. {completed_task}')

# Infinite loop to keep the program running until user exits
while True:
    print("\nOptions: 1. Add Task  2. Remove Task  3. View Tasks  4. completed task 5. Exit")

    # Ask user for their choice
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        completed_task(completed_tasks)

    elif choice == '5':
        print("Exiting program. Have a productive day!")
        break
    else:
        print("Invalid choice! Please select a valid option.")

print("=================\nNGOZI TO DO LIST TRACKER\n==============")
print(f"{tasks}\n{completed_tasks}")


f = open(tasks, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()

