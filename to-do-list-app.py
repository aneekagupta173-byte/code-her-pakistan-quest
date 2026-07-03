import tkinter as tk


root = tk.Tk()
root.title("TO DO LIST")
root.geometry("500x500")
root.minsize(450, 430)
root.attributes("-topmost", True)

tk.Label(root, text="TO DO LIST", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter your task:", font=("Helvetica", 12)).pack(pady=5)

task_entry = tk.Entry(root, width=40, font=("Helvetica", 11))
task_entry.pack(pady=8, padx=20, fill="x")
task_entry.bind("<Return>", lambda event: add_task())
task_entry.bind("<KP_Enter>", lambda event: add_task())

tk.Label(root, text="Time (optional):", font=("Helvetica", 12)).pack(pady=(0, 2))
time_entry = tk.Entry(root, width=20, font=("Helvetica", 11))
time_entry.pack(padx=20, fill="x")
time_entry.bind("<Return>", lambda event: add_task())
time_entry.bind("<KP_Enter>", lambda event: add_task())

tk.Label(root, text="Your tasks:", font=("Helvetica", 12)).pack(pady=5)
tasks_frame = tk.Frame(root)
tasks_frame.pack(padx=20, pady=10, fill="both", expand=True)

tasks_listbox = tk.Listbox(
    tasks_frame,
    width=50,
    height=12,
    font=("Helvetica", 11),
    activestyle="dotbox",
)
tasks_listbox.pack(fill="both", expand=True)
tasks_listbox.bind("<Delete>", lambda event: delete_task())


def add_task():
    task = task_entry.get().strip()
    task_time = time_entry.get().strip()
    if task:
        if task_time:
            task_text = f"{task}  ({task_time})"
        else:
            task_text = task
        tasks_listbox.insert(tk.END, task_text)
        task_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)


def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=12)
add_button.pack(side="left", padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, width=12)
delete_button.pack(side="left", padx=5)

root.mainloop()