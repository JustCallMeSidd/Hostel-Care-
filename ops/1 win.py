import tkinter as tk
import subprocess

def emp():
    subprocess.Popen(["python", "emp.py"])
def hos():
    subprocess.Popen(["python", "hos.py"])
def adm():
    subprocess.Popen(["python", "Admin.py"])


root = tk.Tk()
root.title("LOG-in panel")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

employee_button = tk.Button(root, text="Employee", command=emp)
employee_button.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.2)

hosteler_button = tk.Button(root, text="Hosteler", command=hos)
hosteler_button.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)

employee_admin = tk.Button(root, text="Admin", command=adm)
employee_admin.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)

root.mainloop()