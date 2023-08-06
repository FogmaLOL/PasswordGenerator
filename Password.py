import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def save_password():
    password = password_entry.get()
    if password:
        with open("Passwords100.txt", "a") as f:
            f.write(password + "\n")
        messagebox.showinfo("Success", "Password saved to Passwords100.txt!")
    else:
        messagebox.showerror("Error", "No password to save!")

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")
      
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.configure(bg="black")

password_entry = tk.Entry(root, font=("Arial", 20), bg="blue", fg="white")
password_entry.pack(pady=20)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white")
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save Password", command=save_password, bg="blue", fg="white")
save_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy Password", command=copy_password, bg="blue", fg="white")
copy_button.pack(pady=5)

root.mainloop()
