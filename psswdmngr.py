import tkinter as tk
from tkinter import messagebox, simpledialog
from cryptography.fernet import Fernet


def load_key():
    try:
        with open("key.key", "rb") as file:
            return file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "Key file not found! Generate it first.")
        return None


def view_passwords():
    try:
        with open("passwords.txt", "r") as f:
            passwords = f.readlines()
        
        if not passwords:
            messagebox.showinfo("View Passwords", "No stored passwords.")
            return

        decrypted_passwords = []
        for line in passwords:
            user, passw = line.strip().split("|")
            decrypted_passwords.append(f"User: {user} | Password: {fer.decrypt(passw.encode()).decode()}")
        
        messagebox.showinfo("Stored Passwords", "\n".join(decrypted_passwords))
    except FileNotFoundError:
        messagebox.showerror("Error", "Passwords file not found!")


def add_password():
    name = simpledialog.askstring("Input", "Enter Account Name:")
    if not name:
        return
    pwd = simpledialog.askstring("Input", "Enter Password:", show='*')
    if not pwd:
        return

    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")
    
    messagebox.showinfo("Success", "Password added successfully!")


key = load_key()
if key:
    fer = Fernet(key)

    # Create UI
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("300x200")

    tk.Label(root, text="Password Manager", font=("Arial", 14, "bold")).pack(pady=10)

    view_button = tk.Button(root, text="View Passwords", command=view_passwords)
    view_button.pack(pady=5)

    add_button = tk.Button(root, text="Add Password", command=add_password)
    add_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=5)

    root.mainloop()
