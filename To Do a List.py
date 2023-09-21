import tkinter as tk
from tkinter import filedialog

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def save_tasks():
    tasks_to_save = listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    if file_path:
        with open(file_path, "w") as file:
            file.write("\n".join(tasks_to_save))
            file.close()

def view_tasks():
    listbox.delete(0, tk.END)
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    if file_path:
        with open(file_path, "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                listbox.insert(tk.END, task)
            file.close()

app = tk.Tk()
app.title("Task List")

# Customize colors
listbox_bg_color = "white"
listbox_fg_color = "black"

button_bg_color = "red"
button_fg_color = "white"

entry_bg_color = "light blue"
entry_fg_color = "black"

# Calculate the centered position
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app_width = 800  # Set your desired application width
app_height = 600  # Set your desired application height
x_pos = (screen_width - app_width) // 2
y_pos = (screen_height - app_height) // 2

# Set the application window size and position
app.geometry(f"{app_width}x{app_height}+{x_pos}+{y_pos}")

frame = tk.Frame(app)
frame.pack(expand=True, fill=tk.BOTH)

listbox = tk.Listbox(frame, selectmode=tk.SINGLE, font=("Helvetica", 12), bg=listbox_bg_color, fg=listbox_fg_color)
listbox.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

entry = tk.Entry(frame, font=("Helvetica", 14), bg=entry_bg_color, fg=entry_fg_color)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

add_button = tk.Button(frame, text="Add Task", font=("Helvetica", 12), command=add_task, bg=button_bg_color, fg=button_fg_color)
add_button.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")

delete_button = tk.Button(frame, text="Delete Task", font=("Helvetica", 12), command=delete_task, bg=button_bg_color, fg=button_fg_color)
delete_button.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

view_button = tk.Button(frame, text="View Tasks", font=("Helvetica", 12), command=view_tasks, bg=button_bg_color, fg=button_fg_color)
view_button.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

save_button = tk.Button(frame, text="Save Tasks", font=("Helvetica", 12), command=save_tasks, bg=button_bg_color, fg=button_fg_color)
save_button.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

# Configure row and column weights to center the widgets
frame.grid_rowconfigure(1, weight=0)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

app.mainloop()
