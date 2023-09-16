import tkinter as tk

def evaluate():
    try:
        result.set(eval(entry.get()))
    except:
        result.set("Error")

def button_click(value):
    current_expression = entry.get()
    if current_expression == "Error":
        entry.delete(0, tk.END)
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.config(bg="purple")

entry = tk.Entry(window, font=("Helvetica", 24))
entry.pack(fill=tk.BOTH, expand=True)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, font=("Helvetica", 24))
result_label.pack(fill=tk.BOTH, expand=True)

button_frame = tk.Frame(window)
button_frame.pack(fill=tk.BOTH, expand=True)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "", "+"
]

row, col = 1, 0
for button in buttons:
    tk.Button(
        button_frame,
        text=button,
        font=("Helvetica", 18),
        padx=20,
        pady=20,
        command=lambda b=button: button_click(b)
    ).grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(
    button_frame,
    text="Clear",
    font=("Helvetica", 18),
    padx=20,
    pady=20,
    command=clear
).grid(row=5, column=0, columnspan=2, sticky="nsew")

tk.Button(
    button_frame,
    text="=",
    font=("Helvetica", 18),
    padx=20,
    pady=20,
    command=evaluate
).grid(row=5, column=2, columnspan=2, sticky="nsew")

for i in range(6):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

window.mainloop()


