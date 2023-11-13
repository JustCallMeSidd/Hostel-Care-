import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

class RequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Request Form")

        self.label = tk.Label(root, text="Enter Room Number:")
        self.label.pack()

        self.room_entry = tk.Entry(root)
        self.room_entry.pack()

        self.label = tk.Label(root, text="Enter Request:")
        self.label.pack()

        self.request_entry = tk.Entry(root)
        self.request_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_request)
        self.submit_button.pack()

    def submit_request(self):
        room_no = self.room_entry.get()
        request = self.request_entry.get()

        if not room_no or not request:
            messagebox.showwarning("Warning", "Both Room Number and Request are required!")
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

                update_query = f"UPDATE request SET Yes = %s WHERE roomNo = %s"
                values = (request, room_no)

                cursor.execute(update_query, values)
                connection.commit()

                messagebox.showinfo("Success", "Request submitted successfully!")

        except Error as e:
            print("Error:", e)
            messagebox.showerror("Error", "An error occurred while processing the request.")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = RequestApp(root)
    root.mainloop()
