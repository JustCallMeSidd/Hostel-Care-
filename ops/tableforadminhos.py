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

def fetch_hosteler():
    tree.delete(*tree.get_children())  
    
    query = "SELECT * FROM hosteler"
    cursor.execute(query)
    hosteler = cursor.fetchall()

    for idx, hosteler in enumerate(hosteler):
        tree.insert("", "end", values=(idx + 1, *hosteler))

root = tk.Tk()
root.title("hosteler Display")

tree = ttk.Treeview(root, columns=("#","username", "password"), show="headings")
tree.heading("#", text="Index")
tree.heading("username", text="username")
tree.heading("password", text="password")

tree.column("#", width=50)
tree.column("username", width=150)
tree.column("password", width=150)


tree.pack()

fetch_button = tk.Button(root, text="Fetch hosteler", command=fetch_hosteler)
fetch_button.pack()

root.mainloop()
