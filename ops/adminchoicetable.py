import tkinter as tk
import subprocess

def emptable():
    subprocess.Popen(["python", "adminemptable.py"])
def hostable():
    subprocess.Popen(["python", "tableforadminhos.py"])
def reqtable():
    subprocess.Popen(["python", "adminrequestadmin.py"])
def Addemp():
    subprocess.Popen(["python", "addEMP.py"])

root = tk.Tk()
root.title("Employee and Hosteler Page")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

employee_button = tk.Button(root, text="Employee", command=emptable)
employee_button.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.2)

hosteler_button = tk.Button(root, text="Hosteler", command=hostable)
hosteler_button.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.2)

employee_admin = tk.Button(root, text="Request", command=reqtable)
employee_admin.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.2)

employee_admin = tk.Button(root, text="Request", command=Addemp)
employee_admin.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.2)

root.mainloop()
