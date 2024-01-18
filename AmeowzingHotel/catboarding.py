import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
def update_record():
    # Fetch the record to update
    selected_record_id = get_selected_record_id()

    if not selected_record_id:
        messagebox.showwarning("Update Record", "Please select a record to update.")
        return

    # Get updated data from widgets
    updated_date_of_entry = cal_a.get_date()
    updated_date_of_release = cal_b.get_date()
    updated_package_type = TOC_combobox.get()
    updated_selected_price = POS_combobox.get()

    # The prices below are to define the value from the user selections
    updated_prices_dict = {
        "Comfy (RM300)": 300,
        "Premium 3 cat (RM300)": 300,
        "Premium 4 cat (RM410)": 410,
        "Premium 5 cat (RM530)": 530,
    }

    # Get the updated price from the dictionary based on the selected option
    updated_price = updated_prices_dict.get(updated_selected_price, 0)

    # Calculate the total price using the provided formula
    total_price = updated_price - (cal_a.get_date() * updated_price)

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="catboarding"
    )
    cursor = connection.cursor()

    # Update data in the table
    update_query = "UPDATE `boarding` SET boarding_doe=%s, boarding_dor=%s, boarding_package=%s, boarding_price=%s WHERE id=%s"
    updated_data = (updated_date_of_entry, updated_date_of_release, updated_package_type, total_price, selected_record_id)
    cursor.execute(update_query, updated_data)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

    messagebox.showinfo("Update Record", "Record updated successfully.")

def delete_record():
    # Fetch the record to delete
    selected_record_id = get_selected_record_id()  # You need to implement this function

    if not selected_record_id:
        messagebox.showwarning("Delete Record", "Please select a record to delete.")
        return

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cathotel"
    )
    cursor = connection.cursor()

    # Delete data from the table
    delete_query = "DELETE FROM `boarding` WHERE id=%s"
    cursor.execute(delete_query, (selected_record_id,))

    # Commit changes and close the connection
    connection.commit()
    connection.close()

    messagebox.showinfo("Delete Record", "Record deleted successfully.")

# Function to get the selected record ID (you need to implement this based on your GUI structure)
def get_selected_record_id():
    pass

# Function to save data to the database (you need to implement this)
def save_data_to_database():
    # Implement the logic to save data to the database
    pass

# Callback function when a date is selected in the calendar
def on_date_selected(selected_date, label_widget):
    label_widget.config(text="Selected Date: " + selected_date)

root = tk.Tk()
root.title("Service_Details")
root.config(bg='#3C565B')
root.geometry('700x600')

# Services Details section A
a = tk.LabelFrame(root, text="Section A: ")
a.grid(row=0, column=0, padx=30, pady=20)

DOE= tk.Label(a, text="Date of Entry (choose your date)", font=("Times New Roman", 12, "bold"))
DOE.grid(row=0, column=0, padx=(0, 10))

# Date Picker A
a = tk.LabelFrame(root, text="Date Picker A: ")
a.grid(row=1, column=0, padx=10, pady=10)

cal_a = Calendar(a)
cal_a.pack(pady=20)

a = tk.Label(a, text="Selected Date: ")
a.pack()

cal_a.bind("<<CalendarSelected>>", lambda e: on_date_selected(cal_a.get_date(), a))

# Services Details section B
b = tk.LabelFrame(root, text="Section B: ")
b.grid(row=0, column=1, padx=30, pady=20)

DOR= tk.Label(b, text="Date of Release (choose your date)", font=("Times New Roman", 12, "bold"))
DOR.grid(row=0, column=0, padx=(0, 10))

# Date Picker B
b = tk.LabelFrame(root, text="Date Picker B: ")
b.grid(row=1, column=1, padx=30, pady=20)

cal_b = Calendar(b)
cal_b.pack(pady=20)

b = tk.Label(b, text="Selected Date: ")
b.pack()

cal_b.bind("<<CalendarSelected>>", lambda e: on_date_selected(cal_b.get_date(), b))

# Services Details section C
package = ttk.LabelFrame(root , text="Section C:")
package.grid(row=2, column=0)

TOC_label = ttk.Label(package, text="Package:")
TOC_label.grid(row=3, column=0)
TOC_combobox = ttk.Combobox(package, values=['Comfy (1/2 cat only)', 'Premium (3-5 cat only)'])
TOC_combobox.grid(row=3, column=1)

POS_label = ttk.Label(package, text="Price")
POS_label.grid(row=4, column=0)
POS_combobox = ttk.Combobox (package, values= ['Comfy (RM300)', 'Premium 3 cat (RM300)', 'Premium 4 cat (RM410)', 'Premium 5 cat (RM530)'])
POS_combobox.grid(row=4, column=1)

# Accept terms
tap = tk.LabelFrame(root, text="Terms & Conditions")
tap.grid(row=2, column=1, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
tap_check = tk.Checkbutton(tap, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
tap_check.grid(row=0, column=0)


# Save button
save_button = tk.Button(root, text="Book", command=save_data_to_database)
save_button.grid(row=3, column=0, columnspan=2, pady=10)


# Button to delete
delete_button = ttk.Button(root, text="Delete", command=delete_record)
delete_button.grid(row=6, column=0)

# Button to update
update_button = ttk.Button(root, text="Update", command=update_record)
update_button.grid(row=6, column= 1)

root.mainloop()
