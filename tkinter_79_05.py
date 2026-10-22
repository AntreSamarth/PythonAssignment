import tkinter as tk

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("350x250")

# Predefined credentials
USERNAME = "admin"
PASSWORD = "1234"

tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

result = tk.Label(root, text="Please log in.")
result.pack(pady=10)


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == USERNAME and password == PASSWORD:
        result.config(text="Login Successful!")
    else:
        result.config(text="Invalid username or password.")


tk.Button(root, text="Login", command=login).pack(pady=5)

root.mainloop()