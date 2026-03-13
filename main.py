import json


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
                return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error loading tasks. Starting with an empty task list.")
        return []
    
tasks = load_tasks()

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    new_task = {'title': task,
                'done': False}
    if not new_task['title'] or new_task['title'].isspace():
        print("Task cannot be empty.")
        return
    new_title = new_task['title'].strip().lower()
    for t in tasks:
        title = t['title'].strip().lower()
        if title == new_title:
            if not t['done']:
                print("Task already exists.")
                return
    new_task['title'] = new_task['title'].strip()
    tasks.append(new_task)
    save_tasks()
    print(f"Task '{new_task['title']}' added.")


def show_tasks():
    number = 1
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            if task['done']:
                status = '✅'
            else:
                status = '❌'
            print(f"{number}. {task['title']} - {status}")
            number += 1


def delete_task( index):
    index = index - 1
    if not tasks:
        print("No tasks available.")
    elif index < 0 or index >= len(tasks):
        print("Invalid task index.")
    else:
        eliminada = tasks.pop(index)
        save_tasks()
        print(f"Task '{eliminada['title']}' deleted.")

def check_task(index):
    index = index - 1
    if not tasks:
        print("No tasks available.")
    elif index < 0 or index >= len(tasks):
        print("Invalid task index.")
    else:
        tasks[index]['done'] = True
        save_tasks()
        print(f"Task '{tasks[index]['title']}' marked as done.")

def delete_all_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Are you sure you want to delete all tasks? (yes/no)")
        confirmation = input().lower()
        if confirmation != 'yes':
            print("Operation cancelled.")
            return
        tasks.clear()
        save_tasks()
        print("All tasks deleted.")

def get_task_number():
    while True:
        index = input("Enter the task number: ")
        if not index.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        return int(index)

def show_summary():
    total_tasks = len(tasks)
    completed_tasks = 0
    pending_tasks= 0
    for t in tasks:
        if t['done']:
            completed_tasks += 1
        else:
            pending_tasks += 1
    return total_tasks, completed_tasks, pending_tasks

def menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Check Task")
        print("5. Delete All Tasks")
        print("6. Show Summary")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            show_tasks()
            index = get_task_number()
            delete_task(index)
        elif choice == '4':
            show_tasks()
            index = get_task_number()
            check_task(index)
        elif choice == '5':
            delete_all_tasks()
        elif choice == '6':
            total_tasks, completed_tasks, pending_tasks = show_summary()
            print(f"Total tasks: {total_tasks}")
            print(f"Completed tasks: {completed_tasks}")
            print(f"Pending tasks: {pending_tasks}")
        elif choice == '7':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
