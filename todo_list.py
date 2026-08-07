tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task_name = input("Enter task: ")

        task = {
            "id": len(tasks) + 1,
            "name": task_name
        }

        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print(f"{task['id']}. {task['name']}")

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")
