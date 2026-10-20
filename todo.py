def add_item(tasks, item):
    tasks.append(item)
    print("Task added!")

def remove_item(tasks, item):
    found = False
    for t in tasks:
        if t == item:
            tasks.remove(t)
            found = True
    if found:
        print("Task Removed!")
    else:
        print("Task not found!")

def view_items(tasks):
    for index, item in enumerate(tasks, start=1):
                print(index, item)

def form():
    print("Enter a To-do:")
    print("1. Add Task.")
    print("2. Remove Task.")
    print("3. View Task.")
    print("4. Quit.")

def main():
    task = []

    while True:
        form()
        toDo = int(input("Enter a number from the list: "))
        if toDo == 1:
            newTask = input("Enter task to add: ")
            add_item(task, newTask)
        elif toDo == 2:
            newTask = input("Enter task to remove: ")
            remove_item(task, newTask)
        elif toDo == 3:
            view_items(task)
            
        elif toDo == 4:
            print("Goodbye")
            break
        else:
            print("Invalid Option, select an option between 1-4")

main()