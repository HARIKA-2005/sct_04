import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

# Initialize the root window
root = tk.Tk()
root.title("To-Do App")
root.geometry("500x500")

# Global list to store tasks
tasks = []

# Function to add a task
def add_task():
    task_name = entry_task.get()
    if task_name:
        task_date = cal.get_date()
        task_time = entry_time.get()
        tasks.append({"name": task_name, "date": task_date, "time": task_time, "completed": False})
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task name.")

# Function to mark a task as completed
def mark_completed():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Function to edit a task
def edit_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task = tasks[selected_task_index[0]]
        entry_task.delete(0, tk.END)
        entry_task.insert(0, task["name"])
        entry_time.delete(0, tk.END)
        entry_time.insert(0, task["time"])
    else:
        messagebox.showwarning("Selection Error", "Please select a task.")

# Function to update the task list
def update_task_list():
    task_list.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        task_list.insert(tk.END, f"{i+1}. {task['name']} - {task['date']} - {task['time']} - {status}")

# Task Entry Fields
tk.Label(root, text="Task:").pack(pady=5)
entry_task = tk.Entry(root)
entry_task.pack(pady=5)

# Calendar widget to select the date
cal = Calendar(root, selectmode='day', year=2024, month=9, day=23)
cal.pack(pady=5)

# Task Time Entry
tk.Label(root, text="Time (HH:MM):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Task List
task_list = tk.Listbox(root)
task_list.pack(pady=10, fill=tk.BOTH, expand=True)

# Mark completed button
mark_button = tk.Button(root, text="Mark as Completed", command=mark_completed)
mark_button.pack(pady=5)

# Edit task button
edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack(pady=5)

# Main loop to run the application
root.mainloop()
