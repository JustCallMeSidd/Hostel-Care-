import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def empdone():
    subprocess.Popen(["python", "emptaskdone5.py"])

def hostable():
    subprocess.Popen(["python", "emphostable.py"])

app = tk.Tk()
app.title("File Dialog Example")

hostel_req_button = tk.Button(app, text="Request Complete ", command=empdone)
hostel_req_button.pack(padx=20, pady=10)

req_complete_button = tk.Button(app, text="Hostel Complete", command=hostable)
req_complete_button.pack(padx=20, pady=10)

app.mainloop()
