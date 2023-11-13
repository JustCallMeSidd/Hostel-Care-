import tkinter as tk
import mysql.connector
from tkinter import messagebox

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="amitshap19",
    database="ops"
)
cursor = db.cursor()

def submit_request():
    request_text = request_entry.get()
    room_text = room_entry.get()
    
    query = "INSERT INTO request (request, roomNO) VALUES (%s, %s)"
    cursor.execute(query, (request_text, room_text))
    db.commit()
    
    messagebox.showinfo("Request Submitted", "Your request has been submitted successfully!")

root = tk.Tk()
root.title("Request Submission")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

request_label = tk.Label(root, text="Enter your request:")
request_label.pack()

request_entry = tk.Entry(root)
request_entry.pack()

room_label = tk.Label(root, text="Enter your room number:")
room_label.pack()

room_entry = tk.Entry(root)
room_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_request)
submit_button.pack()

root.mainloop()
