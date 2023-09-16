
import tkinter as tk
from tkinter import messagebox
from datetime import datetime 
def add_task():
    task = entry.get()
    due_date = due_date_entry.get()
    if task:
        if due_date:
            task_with_due_date = f"{task} (Due: {due_date})"
            listbox.insert(tk.END, task_with_due_date)
            entry.delete(0, tk.END)
            due_date_entry.delete(0, tk.END)
        else:
            listbox.insert(tk.END, task)
            entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")
def show_alert():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        task_due_date = None

        if "(Due:" in selected_task:
            task_due_date = selected_task.split("(Due:")[1].strip(")")

        if task_due_date:
            due_date = datetime.strptime(task_due_date, "%Y-%m-%d")
            current_date = datetime.now()
            if current_date > due_date:
                messagebox.showwarning("Alert", f"The task '{selected_task}' is overdue!")
            else:
                messagebox.showinfo("Alert", f"The task '{selected_task}' is not yet due.")
        else:
            messagebox.showinfo("Alert", f"The task '{selected_task}' has no due date.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to show an alert!")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")

def clear_tasks():
    listbox.delete(0, tk.END)
root = tk.Tk()
frame = tk.Frame(root)
frame.pack(pady=40)
root.configure(bg='pink')

entry = tk.Entry(frame, font=("Helvetica", 14))
entry.grid(row=0, column=0, padx=5)


add_button = tk.Button(frame, text="Add Task", font=("Helvetica", 12), command=add_task)
add_button.grid(row=1, column=2)

due_date_entry = tk.Entry(frame, font=("Helvetica", 10))
due_date_entry.grid(row=0, column=1,padx=3)
due_date_entry.insert(0, "MM-DD")

alert_button = tk.Button(frame, text="Show Alert", font=("Helvetica", 12), command=show_alert)
alert_button.grid(row=2,column=0,padx=5)


delete_button = tk.Button(frame, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_button.grid(row=1, column=0, padx=5)

clear_button = tk.Button(frame, text="Clear All", font=("Helvetica", 12), command=clear_tasks)
clear_button.grid(row=1, column=1)


listbox = tk.Listbox(root, selectbackground="yellow", selectmode=tk.SINGLE, font=("Helvetica", 14))
listbox.pack(pady=10)

root.mainloop()