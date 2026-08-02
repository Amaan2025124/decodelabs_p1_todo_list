# ==========================================
# DecodeLabs Project 1 - To-Do List Manager
# ==========================================

tasks = []


def add_task():
    task_name = input("Enter task: ").strip()

    if task_name == "":
        print("Task cannot be empty!")
        return

    task = {
        "id": len(tasks) + 1,
        "task": task_name
    }

    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
        return

    print("\n===== TO-DO LIST =====")
    for task in tasks:
        print(f"{task['id']}. {task['task']}")
    print()


def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    view_tasks()

    try:
        task_id = int(input("Enter Task ID to delete: "))

        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)

                # Reassign IDs
                for i, t in enumerate(tasks, start=1):
                    t["id"] = i

                print("Task deleted successfully!")
                return

        print("Task ID not found.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Thank you for using the To-Do List App!")
            break

        else:
            print("Invalid choice. Try again.")


main()