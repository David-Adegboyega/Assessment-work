def add_item(tasks, item):
    if not item.strip():
        print("Task cannot be empty.")
        return

    tasks.append({"text": item.strip(), "done": False})
    print("Task added!")


def view_items(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for number, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f'{number}. {status} {task["text"]}')


def get_task_index(tasks):
    if not tasks:
        print("No tasks yet.")
        return None

    try:
        number = int(input("Enter task number: "))
    except ValueError:
        print("Please enter a whole number.")
        return None

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return None

    return number - 1


def remove_item(tasks):
    index = get_task_index(tasks)

    if index is not None:
        tasks.pop(index)
        print("Task removed!")


def mark_done(tasks):
    index = get_task_index(tasks)

    if index is not None:
        tasks[index]["done"] = True
        print(f"Task {index + 1} marked as done.")


def form():
    print("\nTo-Do Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task as Done")
    print("5. Quit")


def main():
    tasks = []

    while True:
        form()
        choice = input("Choose an option from 1-5: ").strip()

        if choice == "1":
            new_task = input("Enter task to add: ")
            add_item(tasks, new_task)

        elif choice == "2":
            remove_item(tasks)

        elif choice == "3":
            view_items(tasks)

        elif choice == "4":
            mark_done(tasks)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose from 1-5.")


main()