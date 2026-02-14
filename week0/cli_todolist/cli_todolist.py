import json
import os

FILENAME = 'tasks.json'

tasks = []
current_task_num = 0

def load_tasks():
    global tasks, current_task_num
    # Check if the file exists so we don't get an error on the first run
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as f:
            tasks = json.load(f)
            if tasks:
                current_task_num = max(t['id'] for t in tasks)
            else:
                current_task_num = 0
        print("Data loaded successfully.")
    else:
        tasks = []
        current_task_num = 0

def save_tasks():
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)
    print("Data saved. Goodbye!")

def display_menu():
    print("\n" + "-"*30)
    print("1. Add a Task")
    print("2. Delete a Task")
    print("3. Mark as Completed")
    print("4. Display all Tasks")
    print("0. Quit")
    print("-"*30)

def handle_add_task():
    global current_task_num
    txt = input("Enter the task: ")
    current_task_num += 1
    task = {'id': current_task_num, 'task': txt, 'is_completed': False}
    tasks.append(task)
    print("Task added!")

def handle_delete_task():
    global tasks
    display_all_task()
    print('Options: 0=All, 99=All Completed')
    try:
        id_to_del = int(input('Enter ID to delete: '))
        
        if id_to_del == 0:
            if input('Delete everything? (y/n): ').lower() == 'y':
                tasks = []
        elif id_to_del == 99:
            tasks = [t for t in tasks if not t['is_completed']]
        else:
            # Rebuild list excluding the specific ID
            tasks = [t for t in tasks if t['id'] != id_to_del]
    except ValueError:
        print("Invalid input. Please enter a number.")

def handle_task_completion():
    display_all_task()
    try:
        id_to_mark = int(input('Enter ID to complete (0 for all): '))
        for task in tasks:
            if id_to_mark == 0 or task['id'] == id_to_mark:
                task['is_completed'] = True
    except ValueError:
        print("Invalid input.")

def display_all_task():
    print(f"\nID\tStatus\t\tTask")
    print("-" * 40)
    for t in tasks:
        status = "✓" if t['is_completed'] else " "
        print(f"{t['id']}\t[{status}]\t\t{t['task']}")

# Main Loop
load_tasks()
while True:
    display_menu()
    try:
        choice = int(input("Choice: "))
        if choice == 0: 
            save_tasks()
            break
        elif choice == 1: handle_add_task()
        elif choice == 2: handle_delete_task()
        elif choice == 3: handle_task_completion()
        elif choice == 4: display_all_task()
    except ValueError:
        print("Please enter a number.")