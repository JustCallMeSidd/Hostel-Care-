import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

class RequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Employee Form")

        self.label = tk.Label(root, text="Name of employee:")
        self.label.pack()

        self.emp_entry = tk.Entry(root)
        self.emp_entry.pack()

        self.label = tk.Label(root, text="Enter password:")
        self.label.pack()

        self.pass_entry = tk.Entry(root)
        self.pass_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_request)
        self.submit_button.pack()

    def submit_request(self):
        emp_ = self.emp_entry.get()
        pass_ = self.pass_entry.get()

        if not emp_ or not pass_:
            messagebox.showwarning("Warning", "username and password are required for form")
            return

        try:
            connection = mysql.connector.connect(
                host="localhost",
                database="ops",
                user="root",
                password="amitshap19"
            )

            if connection.is_connected():
                cursor = connection.cursor()

                update_query = f"INSERT INTO employee (username, password) VALUES (%s, %s)"
                values = (emp_, pass_)

                cursor.execute(update_query, values)
                connection.commit()

                messagebox.showinfo("Success", "Form submitted successfully!")

        except Error as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while processing the Form.")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = RequestApp(root)
    root.mainloop()
