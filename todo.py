def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == "3":
            show_tasks(tasks)
            try:
                task_no = int(input("Enter task number to delete: "))
                tasks.pop(task_no - 1)
                save_tasks(tasks)
                print("Task deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

main()
