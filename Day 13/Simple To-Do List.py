todo_list = []

def show_menu():
    print("\n📝 TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Remove Task")
    print("5. Exit")

def add_task():
    task = input("Enter task to add: ")
    todo_list.append({"task": task, "done": False})
    print("✅ Task added!")

def view_tasks():
    if not todo_list:
        print("📭 No tasks yet!")
        return
    print("\n📋 Your Tasks:")
    for i, item in enumerate(todo_list, start=1):
        status = "✔️ Done" if item["done"] else "❌ Not Done"
        print(f"{i}. {item['task']} - {status}")

def mark_done():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(todo_list):
                todo_list[task_num - 1]["done"] = True
                print("✅ Task marked as done!")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"🗑️ Task '{removed['task']}' removed!")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("👋 Goodbye, Aysha!")
        break
    else:
        print("❌ Invalid choice. Please select 1 to 5.")
"""
Output:
📝 TO-DO LIST MENU
1. Add Task
2. View Tasks
3. Mark Task as Done
4. Remove Task
5. Exit
Choose an option (1-5): 1
Enter task to add: Complete Python project
✅ Task added!

Choose an option (1-5): 2
📋 Your Tasks:
1. Complete Python project - ❌ Not Done

Choose an option (1-5): 3
Enter task number to mark as done: 1
✅ Task marked as done!

Choose an option (1-5): 5
👋 Goodbye, Aysha!
"""
