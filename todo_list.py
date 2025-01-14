# todo_list.py
import os

tasks = []

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")
    print("===========================")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def view_tasks():
    if not tasks:
        print("\nNo tasks to display.")
    else:
        print("\n===== Your Tasks =====")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")
        print("======================")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
