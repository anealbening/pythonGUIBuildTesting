import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World: By Aneal")

# Set the window size
root.geometry("300x200")

# Create a label with the text "Hello World"
label = tk.Label(root, text="Hello World", font=("Arial", 24))
label.pack(pady=20)

# Run the application
root.mainloop()
