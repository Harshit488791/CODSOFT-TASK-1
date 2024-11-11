import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful To-Do List")
        self.root.geometry("500x500")
        
        # List to store tasks
        self.tasks = []
        
        # Colors for UI
        self.bg_color = "#f1f1f1"
        self.button_color = "#4CAF50"
        self.active_button_color = "#45a049"
        self.completed_color = "#d3ffd3"
        
        # Set background color
        self.root.config(bg=self.bg_color)

        # Label for the title
        self.title_label = tk.Label(self.root, text="My To-Do List", font=("Arial", 20, "bold"), bg=self.bg_color)
        self.title_label.pack(pady=10)

        # Frame for the task input section
        self.input_frame = tk.Frame(self.root, bg=self.bg_color)
        self.input_frame.pack(pady=10)

        # Task input
        self.task_input = tk.Entry(self.input_frame, font=("Arial", 14), width=30)
        self.task_input.grid(row=0, column=0, padx=5)
        
        # Add task button
        self.add_task_button = tk.Button(self.input_frame, text="Add Task", font=("Arial", 12), bg=self.button_color, fg="white", command=self.add_task)
        self.add_task_button.grid(row=0, column=1)

        # Listbox for displaying tasks
        self.task_listbox = tk.Listbox(self.root, width=50, height=15, font=("Arial", 12), bg="#ffffff", selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Buttons for updating and deleting tasks
        self.update_task_button = tk.Button(self.root, text="Update Task", font=("Arial", 12), bg=self.button_color, fg="white", command=self.update_task)
        self.update_task_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", font=("Arial", 12), bg="#f44336", fg="white", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.complete_task_button = tk.Button(self.root, text="Mark as Complete", font=("Arial", 12), bg="#2196F3", fg="white", command=self.complete_task)
        self.complete_task_button.pack(side=tk.LEFT, padx=10, pady=10)
        
    def add_task(self):
        task = self.task_input.get()
        if task != "":
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task_info in enumerate(self.tasks):
            display_text = task_info["task"]
            if task_info["completed"]:
                display_text = f"✓ {display_text}"
            self.task_listbox.insert(tk.END, display_text)

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_input.get()
            if new_task != "":
                self.tasks[selected_index]["task"] = new_task
                self.update_task_listbox()
                self.task_input.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task!")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete!")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as complete!")

# Create the main window (root)
root = tk.Tk()
todo_app = ToDoApp(root)

# Start the Tkinter event loop
root.mainloop()
