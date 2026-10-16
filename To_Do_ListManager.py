
import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                tasks = json.load(file)

            if isinstance(tasks, list):
                return tasks

        except (json.JSONDecodeError, OSError):
            print("Could not read saved tasks. Starting with an empty list.")

    return []


def save_tasks(tasks):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)
    except OSError:
        print("Error: Tasks could not be saved.")


def add_task(tasks):
    name = input("Enter your new task: ").strip()

    if not name:
        print("Task cannot be empty.")
        return

    tasks.append({"name": name, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    print("\n===== YOUR TASKS =====")

    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i}. {task['name']} - {status}")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print("Deleted task:", removed["name"])
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def mark_completed(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to mark completed: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            mark_completed(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
