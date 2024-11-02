tasks = []
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
