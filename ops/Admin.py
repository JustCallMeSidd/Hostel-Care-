import tkinter as tk
import mysql.connector
from tkinter import messagebox
import subprocess
import os

def empdone():
    subprocess.Popen(["python", "adminchoicetable.py"])

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amitshap19",
    database="ops"
)
cursor = db.cursor()

def login():
    username = username_entry.get()
    password = password_entry.get()

    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        employee_button = tk.Button(root, text="choosing", command=empdone)
        employee_button.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.2)
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials")

root = tk.Tk()
root.title("Admin")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
