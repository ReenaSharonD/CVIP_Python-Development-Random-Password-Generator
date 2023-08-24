import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 5:
        password_label.config(text="Password length should be at least 5 characters")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack()

# Start the GUI event loop
root.mainloop()
