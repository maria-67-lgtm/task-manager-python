import json


def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
                return json.load(file)
    except FileNotFoundError:
        return []
    
tasks = load_tasks()

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    new_task = {'title': task,
                'done': False}
    if not new_task['title']:
        print("Task cannot be empty.")
        return
    if new_task['title'].isspace():
        print("Task cannot be empty.")
        return
    new_title = new_task['title']
    new_title = new_title.strip().lower()
    for t in tasks:
        title = t['title']
        title = title.strip().lower()
        
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



def menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Check Task")
        print("5. Delete All Tasks")
        print("6. Exit")

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
            index = (input("Enter the task number to delete: "))
            if index < 1 or index > len(tasks) or index.isdigit() == False:
                print("Invalid task number.")
            else:
                delete_task(index)
        elif choice == '4':
            show_tasks()
            index = (input("Enter the task number to check: "))
            if index < 1 or index > len(tasks) or index.isdigit() == False:
                print("Invalid task number.")
            else:
                check_task(index)
        elif choice == '5':
            delete_all_tasks()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
