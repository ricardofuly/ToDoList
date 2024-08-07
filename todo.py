import tkinter as tk
from tkinter import messagebox
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

def add_task():
    #Add a new task to the ToDo list.
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        listbox_tasks.insert(tk.END, task)
        save_tasks()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "You must add a task.")
    
def remove_task():
    #Remove a task from the list.
    try:
        task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(task_index)
        if messagebox.askyesno("Confirm", f"Are you sure you would like to remove '{task}'?"):
            tasks.remove(task)
            listbox_tasks.delete(task_index)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Error", "You must to select a task!")
        
def clear_all_tasks():
    #Remove all task from the list
    if messagebox.askyesno("Confirm", "Are you sure you would like to remove ALL the tasks?"):
        listbox_tasks.delete(0, tk.END)
        tasks.clear()
        save_tasks()

def load_tasks_to_listbox():
    #Load the tasks from the listbox
    for task in tasks:
        listbox_tasks.insert(tk.END, task)
        
#Initial setup
root = tk.Tk()
root.title("ToDo List")

#Frame to hold input of tasks and buttons
frame = tk.Frame(root)
frame.pack(pady=10)

#Listbox to show tasks
listbox_tasks = tk.Listbox(
    frame,
    width=50,
    height=10,
    selectmode=tk.SINGLE
)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

#Scrollbar to the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

#Input of text to add tasks
entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

#Buttons
button_add_task = tk.Button(
    root,
    text="Add Task",
    width=48,
    command=add_task
)
button_add_task.pack(pady=5)

button_remove_task =tk.Button(
    root,
    text="Remove Task",
    width=48,
    command=remove_task
)
button_remove_task.pack(pady=5)

button_clear_all_tasks = tk.Button(
    root,
    text="Remove All Tasks",
    width=48,
    command=clear_all_tasks
)
button_clear_all_tasks.pack(pady=5)

#Load taks at the begining
load_tasks()
load_tasks_to_listbox()

#Main loop of the graphic inteface
root.mainloop()