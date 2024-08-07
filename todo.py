import os

tasks = []
    
def load_tasks():
    #Load Tasks the file if it's exists.
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    #Save all tasks in a file.
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    #Add a new task to the ToDo list.
    tasks.append(task)
    print(f'Task "{task}" was successfuly added!')
    
def remove_task(task):
    #Remove a task from the list.
    if task in tasks:
        confirmation = input(f'Are you sure do you would like to remove "{task}" ? (Y / N): ')
        if confirmation.lower() == 'y':
            remove_task(task)
            print("Task Removed!")
        else:
            print("Action Canceled!")
    else:
        print(f'Task "{task}" not found!!')
        
def task_list():
    #Show the list of tasks.
    if tasks:
        print("List of Tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Task List was empty!")
        
def show_menu():
    #Show the options menu to the user.
    print("\n Menu: ")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. List Task")
    print("4. Exit")
    
while True:
    #Main loop for the menu.
    show_menu()
    option = input("Choose the option: ")
    
    match option:
        case "1":
           task = input("Type a task  to be added: ")
           add_task(task)
        case "2":
            task = input("Choose one to remove: ")
            remove_task(task)
        case "3":
            task_list()
        case "4":
            print("Exiting.... See ya!")
            break
        case _:
            print("Invalid option, try again!!")