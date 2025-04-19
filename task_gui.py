# task_gui.py

import tkinter as tk
from task_manager import TaskManager

tm = TaskManager()

def add_task():
    task = task_input.get()
    if task:
        tm.add_task(task)
        task_input.delete(0, tk.END)
        update_tasks()

def complete_selected_task():
    selected = task_listbox.curselection()
    if selected:
        tm.complete_task(selected[0])
        update_tasks()

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tm.get_tasks():
        task_listbox.insert(tk.END, task)

# Setup GUI
root = tk.Tk()
root.title("To-Do Task Manager")

frame = tk.Frame(root)
frame.pack(pady=10)

task_input = tk.Entry(frame, width=40)
task_input.pack(side=tk.LEFT)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Complete Selected Task", command=complete_selected_task)
complete_button.pack()

root.mainloop()
