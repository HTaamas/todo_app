import tkinter as tk
from tkinter import messagebox
import json

root = tk.Tk()
root.title("ToDo App")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#2E2E2E")

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, f"{task} - Completed")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

header_frame = tk.Frame(root, bg="#2E2E2E")
header_frame.pack(pady=10)

title_label = tk.Label(header_frame, text="To-Do List 📝", font=('Arial', 18, 'bold'), bg="#2E2E2E", fg="white")
title_label.pack()

input_frame = tk.Frame(root, bg="#2E2E2E")
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=22, font=('Arial', 14), bg="#4D4D4D", fg="white", insertbackground="white")
task_entry.pack(side=tk.LEFT, padx=5)

add_task_button = tk.Button(input_frame, text="ADD", width=8, command=add_task, bg="#FF6347", fg="white", font=('Arial', 12, 'bold'), relief=tk.FLAT)
add_task_button.pack(side=tk.LEFT)

tasks_frame = tk.Frame(root, bg="#2E2E2E")
tasks_frame.pack(pady=10)

tasks_listbox = tk.Listbox(tasks_frame, width=40, height=10, font=('Arial', 12), bg="#4D4D4D", fg="white", selectbackground="#616161", relief=tk.FLAT, bd=0, highlightthickness=0)
tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(tasks_frame, bg="#2E2E2E", activebackground="#2E2E2E", troughcolor="#2E2E2E")
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

tasks_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks_listbox.yview)

action_frame = tk.Frame(root, bg="#2E2E2E")
action_frame.pack(pady=10)

mark_completed_button = tk.Button(action_frame, text="Mark Completed", width=15, command=mark_completed, bg="#2196F3", fg="white", font=('Arial', 12), relief=tk.FLAT)
mark_completed_button.pack(side=tk.LEFT, padx=10)

delete_task_button = tk.Button(action_frame, text="Delete Task", width=15, command=delete_task, bg="#f44336", fg="white", font=('Arial', 12), relief=tk.FLAT)
delete_task_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
