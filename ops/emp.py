import tkinter as tk
import mysql.connector
from tkinter import messagebox
import subprocess
import os

def empcheck():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    emphostable_path = os.path.join(script_directory, "empcheck1.py")
    subprocess.Popen(["python", emphostable_path])

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

    query = "SELECT * FROM employee WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
       employee_button = tk.Button(root, text="Employee", command=empcheck)
       employee_button.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.2)
    else:
        messagebox.showerror("Login Failed", "Invalid Credentials")

root = tk.Tk()
root.title("Employee Login")

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
