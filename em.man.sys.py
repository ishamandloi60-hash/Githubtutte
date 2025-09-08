import mysql.connector
import tkinter as tik
from tkinter import messagebox
from tkinter import ttk


conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mandloi@123"
)
if conn.is_connected():
    print("connected to mysql is successfull !")
else:
    print("connectio failed")   

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")

print("Database created or already exists !")

conn.database = "employee_db"

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL
)
""")
print("Table Create Sucessfully !")

def add_employee(name, position, salary):
    if name == "" or position == "" or salary == "":
        print("All Fields Required !")
        return
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)", (name, position, salary))
    conn.commit()
    print(f"Employee '{name}' added Sucessfully !") 


def display_employees_in_table():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

 
 
def remove_employee(emp_id):
    if emp_id == "":
        print("Empoyee id required !")
        return
    cursor.execute("DELETE FROM employees WHERE ID=%s", (emp_id,))
    conn.commit()
    print(f"Employee with ID {emp_id} removed Sucessfully !")


def promote_employee(emp_id, new_position, new_salary):
    if emp_id == "" or new_position == "" or new_salary == "":
        print("Id, position, salary required !")
        return
    cursor.execute(
        "UPDATE employees SET position=%s, salary=%s WHERE id=%s",
        (new_position, new_salary, emp_id)
    )
    conn.commit()
    print(f"Employee with ID {emp_id} Promoted Sucessfully !")


def display_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

add_employee("shreee", "Developer", 50000)
add_employee("mr.avvi", "Manager", 70000)
display_employees()
promote_employee(1, "Senior Developer", 60000)
remove_employee(2)
display_employees()

root = tik.Tk()
root.title("Employee Management System")
root.geometry("600x400")


tik.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tik.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tik.Label(root, text="Position:").grid(row=1, column=0, padx=10, pady=5)
entry_position = tik.Entry(root)
entry_position.grid(row=1, column=1, padx=10, pady=5)

tik.Label(root, text="Salary:").grid(row=2, column=0, padx=10, pady=5)
entry_salary = tik.Entry(root)
entry_salary.grid(row=2, column=1, padx=10, pady=5)

tik.Label(root, text="Employee ID:").grid(row=3, column=0, padx=10, pady=5)
entry_id = tik.Entry(root)
entry_id.grid(row=3, column=1, padx=10, pady=5)



def handle_add():
    name = entry_name.get()
    position = entry_position.get()
    try:
        salary = float(entry_salary.get())  # salary ko float/int me convert
    except ValueError:
        messagebox.showerror("Error", "Salary must be a number!")
        return
    
    add_employee(name, position, salary)
    messagebox.showinfo("Success", f"Employee '{name}' added successfully!")
    entry_name.delete(0, 'end')
    entry_position.delete(0, 'end')
    entry_salary.delete(0, 'end')
    display_employees_in_table()

def handle_remove():
    emp_id = entry_id.get()
    if emp_id == "":
        messagebox.showerror("Error", "Employee ID required!")
        return
    
    remove_employee(emp_id)
    messagebox.showinfo("Success", f"Employee with ID {emp_id} removed successfully!")
    entry_id.delete(0, 'end')
    display_employees_in_table()

def handle_promote():
    emp_id = entry_id.get()
    new_position = entry_position.get()
    try:
        new_salary = float(entry_salary.get())
    except ValueError:
        messagebox.showerror("Error", "Salary must be a number!")
        return
    
    promote_employee(emp_id, new_position, new_salary)
    messagebox.showinfo("Success", f"Employee with ID {emp_id} promoted successfully!")
    entry_id.delete(0, 'end')
    entry_position.delete(0, 'end')
    entry_salary.delete(0, 'end')
    display_employees_in_table()


tik.Button(root, text="Add Employee", command=handle_add, bg="lightgreen").grid(row=4, column=0, pady=10)


tik.Button(root, text="Remove Employee", command=handle_remove, bg="red").grid(row=4, column=1, pady=10)


tik.Button(root, text="Promote Employee", command=handle_promote, bg="lightblue").grid(row=5, column=0, pady=10)


tik.Button(root, text="Display Employees", command=display_employees_in_table, bg="orange").grid(row=5, column=1, pady=10)


from tkinter import ttk


tree = ttk.Treeview(root, columns=("ID", "Name", "Position", "Salary"), show="headings")


tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Position", text="Position")
tree.heading("Salary", text="Salary")


tree.column("ID", width=100)
tree.column("Name", width=150)
tree.column("Position", width=150)
tree.column("Salary", width=100)


tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10)


def display_employees_in_table():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)
        
def handle_add():
    name = entry_name.get()
    position = entry_position.get()
    try:
        salary = float(entry_salary.get())  # salary ko float/int me convert
    except ValueError:
        messagebox.showerror("Error", "Salary must be a number!")
        return
    
    add_employee(name, position, salary)
    messagebox.showinfo("Success", f"Employee '{name}' added successfully!")
    entry_name.delete(0, 'end')
    entry_position.delete(0, 'end')
    entry_salary.delete(0, 'end')
    display_employees_in_table()

def handle_remove():
    emp_id = entry_id.get()
    if emp_id == "":
        messagebox.showerror("Error", "Employee ID required!")
        return
    
    remove_employee(emp_id)
    messagebox.showinfo("Success", f"Employee with ID {emp_id} removed successfully!")
    entry_id.delete(0, 'end')
    display_employees_in_table()

def handle_promote():
    emp_id = entry_id.get()
    new_position = entry_position.get()
    try:
        new_salary = float(entry_salary.get())
    except ValueError:
        messagebox.showerror("Error", "Salary must be a number!")
        return
    
    promote_employee(emp_id, new_position, new_salary)
    messagebox.showinfo("Success", f"Employee with ID {emp_id} promoted successfully!")
    entry_id.delete(0, 'end')
    entry_position.delete(0, 'end')
    entry_salary.delete(0, 'end')
    display_employees_in_table()    

    


tik.Button(root, text="Display Employees", command=display_employees_in_table, bg="orange").grid(row=5, column=1, pady=10)



root.mainloop()

conn.close()







                                                                                         
                                                                                                                                                                                  
                                                                                                