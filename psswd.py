import tkinter as tk
import string
import random


def generate_password():
    password = []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
        passwords = " ".join(str(x)for x in password)
        label.config(text=passwords)


root = tk.Tk()
root.geometry("500x400")
button = tk.Button(root, text="Generate Password", command=generate_password)
button.place(relx=0.5, rely=0.4, anchor='center')
label = tk.Label(root, font=("arial", 15, "bold"))
label.place(relx=0.5, rely=0.5, anchor='center')
root.mainloop()
