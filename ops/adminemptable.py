import tkinter as tk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amitshap19",
    database="ops"
)
cursor = db.cursor()

def fetch_employee():
    tree.delete(*tree.get_children()) 
    
    query = "SELECT * FROM employee"
    cursor.execute(query)
    employee = cursor.fetchall()

    for idx, employee in enumerate(employee):
        tree.insert("", "end", values=(idx + 1, *employee))


root = tk.Tk()
root.title("employee Display")

tree = ttk.Treeview(root, columns=("#","username", "password"), show="headings")
tree.heading("#", text="Index")
tree.heading("username", text="username")
tree.heading("password", text="password")

tree.column("#", width=50)
tree.column("username", width=50)
tree.column("password", width=300)


tree.pack()

fetch_button = tk.Button(root, text="Fetch employee", command=fetch_employee)
fetch_button.pack()

root.mainloop()
