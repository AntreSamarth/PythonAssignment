import tkinter as tk

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("350x250")

tk.Label(root, text="Enter Your Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Enter Your Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack()

result = tk.Label(root, text="Eligibility Result:")
result.pack(pady=10)


def check_eligibility():
    name = name_entry.get().strip()

    try:
        age = int(age_entry.get())

        if not name:
            result.config(text="Please enter your name.")
        elif age < 0:
            result.config(text="Age cannot be negative.")
        elif age >= 18:
            result.config(text=f"{name}, you are eligible to vote.")
        else:
            result.config(text=f"{name}, you are not eligible to vote.")
    except ValueError:
        result.config(text="Please enter a valid age.")


tk.Button(
    root, text="Check Eligibility", command=check_eligibility
).pack(pady=5)

root.mainloop()