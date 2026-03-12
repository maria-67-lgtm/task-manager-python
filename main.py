tasks = []

def add_task(task):
    new_task = {'title': task,
                'done': False}
    tasks.append(new_task)
    print(f"Task '{new_task['title']}' added.")


def show_tasks():
    number = 1
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(f"{number}. {task['title']}, Done: {task['done']}")
            number += 1


def delete_task( index):
    index = index - 1
    if not tasks:
        print("No tasks available.")
    elif index < 0 or index >= len(tasks):
        print("Invalid task index.")
    else:
        eliminada = tasks.pop(index)
        print(f"Task '{eliminada['title']}' deleted.")

def check_task(index):
    index = index - 1
    if not tasks:
        print("No tasks available.")
    elif index < 0 or index >= len(tasks):
        print("Invalid task index.")
    else:
        tasks[index]['done'] = True
        print(f"Task '{tasks[index]['title']}' marked as done.")
def menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Delete Task")
        print("4. Check Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            index = int(input("Enter the task number to delete: "))
            delete_task(index)
        elif choice == '4':
            show_tasks()
            index = int(input("Enter the task number to check: "))
            check_task(index)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
