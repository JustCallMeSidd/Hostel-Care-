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

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if data[j][1] > data[j + 1][1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def display_table():
    query = "SELECT * FROM request"
    cursor.execute(query)
    result = cursor.fetchall()

    bubble_sort(result) 

   
    if hasattr(display_table, 'tree'):
        display_table.tree.destroy()


    tree = ttk.Treeview(main_window)
    tree["columns"] = ("Request", "RoomNO", "Yes")
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("Request", anchor=tk.W, width=200)
    tree.column("RoomNO", anchor=tk.W, width=100)
    tree.column("Yes", anchor=tk.W, width=50)

    tree.heading("#0", text="", anchor=tk.W)
    tree.heading("Request", text="Request", anchor=tk.W)
    tree.heading("RoomNO", text="RoomNO", anchor=tk.W)
    tree.heading("Yes", text="Yes", anchor=tk.W)

    for row in result:
        tree.insert("", tk.END, values=(row[0], row[1], row[2]))

    tree.pack(padx=10, pady=10)


    display_table.tree = tree

def fetch_data():
    display_table()

main_window = tk.Tk()
main_window.title("Fetch Data Example")

fetch_button = tk.Button(main_window, text="Fetch Data", command=fetch_data)
fetch_button.pack(pady=10)

main_window.mainloop()

cursor.close()
db.close()
