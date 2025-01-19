from datetime import datetime

# Task class to represent each task
class Task:
    def __init__(self, name, description, due_date=None):
        self.name = name
        self.description = description
        self.due_date = due_date

    def __str__(self):
        due_date_str = self.due_date.strftime('%Y-%m-%d') if self.due_date else 'No due date'
        return f"Task: {self.name}, Description: {self.description}, Due Date: {due_date_str}"

    # Set due date for a task
    def set_due_date(self, due_date):
        try:
            self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format! Please use YYYY-MM-DD.")

# Function to create a task
def create_task():
    while True:
        try:
            name = input("Enter task name: ").strip()
            if not name:
                raise ValueError("Task name cannot be empty.")

            description = input("Enter task description: ").strip()
            if not description:
                raise ValueError("Task description cannot be empty.")

            due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()

            task = Task(name, description)
            if due_date:
                task.set_due_date(due_date)

            return task
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.\n")

# Function to display all tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Main function to run the task manager
def main():
    tasks = []  # List to store tasks

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Display Tasks")
        print("3. Exit")
        try:
            choice = input("Enter your choice: ").strip()
            if choice not in {'1', '2', '3'}:
                raise ValueError("Invalid choice. Please select a valid option (1, 2, or 3).")

            if choice == '1':
                task = create_task()
                tasks.append(task)
                print("Task added successfully!")
            elif choice == '2':
                display_tasks(tasks)
            elif choice == '3':
                print("Exiting Task Manager.")
                break
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
