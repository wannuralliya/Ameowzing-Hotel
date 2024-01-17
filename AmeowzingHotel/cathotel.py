import tkinter as tk
from tkcalendar import Calendar
from tkinter import CENTER, Label, messagebox
import mysql.connector

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Ameowzing Hotel Main Window")
        self.master.geometry('500x600')
        self.master.config(bg='#3C565B')

        #Main window title
        self.label = tk.Label(master, text="Welcome to AMEOWZING HOTEL! ", fg='#F0FFFF', font=("Times New Roman", 16, "bold"))
        self.label.config(bg='#3C565B')
        self.label.pack(pady=10)

        # for the information of the cat hotel
        info_text = tk.Text(master, height=10, width=45, font=("Times New Roman", 13))
        info_text.config(bg= '#B0CFDE')
        info_text.pack(pady=20)

        # Defining the information about our cat hotel
        info_text.insert(tk.END, "\n")
        info_text.insert(tk.END, "\n")
        info_text.insert(tk.END, " WE PROVIDE THE BEST SERVICE FOR YOUR CAT !\n\n")
        info_text.insert(tk.END, " Operating hours: 10 am - 10 pm \n\n")
        info_text.insert(tk.END, " Open every day. \n\n")
        info_text.insert(tk.END, " For more information, contact us : 03-12345678")
        info_text.tag_configure ("center", justify = 'center')

        def center_text (text_widget):
            text_widget.tag_add ("center", "1.0", "end")

        center_text (info_text)
        info_text.configure(state='disabled')

        # Patron registration label 
        self.patron_label = tk.Label(master, text="To proceed, please register as a patron first.", fg='#F0FFFF', font=("Times New Roman", 12, "bold"))
        self.patron_label.config(bg='#3C565B')
        self.patron_label.pack()

        # Patron registration button
        self.patron_button = tk.Button(master, text="Patron Registration", command=self.open_patron_registration)
        self.patron_button.pack(pady=10)

        # Appointment booking (label)
        appointment_label = tk.Label(master, text="Book your appointment.", fg='#F0FFFF', font=("Times New Roman", 12, "bold"))
        appointment_label.config(bg='#3C565B')
        appointment_label.pack()

        # grooming booking button
        self.grooming_button = tk.Button(master, text="Cat Grooming", command=self.open_grooming_book)
        self.grooming_button.pack(pady=5)

        # boarding booking button 
        self.boarding_button = tk.Button(master, text="Cat Boarding")
        self.boarding_button.pack(pady=5)

    def open_patron_registration(self):
        # Create a new window for patron registration
        patron_window = tk.Toplevel(self.master)
        patron_window.title ("Cat Hotel Patron Registration")
        patron_window.geometry ('280x300')
        patron_window.config (bg='#3C565B')

        # Create labels and entry fields in the new window
        label_name = tk.Label(patron_window, text="Name:", fg='#F0FFFF', font=("Times New Roman", 12, "bold"))
        label_name.config (bg = '#3C565B')
        label_name.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = tk.Entry(patron_window)
        self.entry_name.grid(row=1, column=1, padx=10, pady=10)

        label_email = tk.Label(patron_window, text="Email:", fg='#F0FFFF', font=("Times New Roman", 12, "bold"))
        label_email.config (bg = '#3C565B')
        label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_email = tk.Entry(patron_window)
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        label_phone = tk.Label(patron_window, text="Phone:", fg='#F0FFFF', font=("Times New Roman", 12, "bold"))
        label_phone.config (bg = '#3C565B')
        label_phone.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_phone = tk.Entry(patron_window)
        self.entry_phone.grid(row=3, column=1, padx=10, pady=10)

        label_address = tk.Label(patron_window, text="Home Address:", fg='#F0FFFF', font=("Times New Roman", 12, "bold"))
        label_address.config (bg = '#3C565B')
        label_address.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entry_address = tk.Entry(patron_window)
        self.entry_address.grid(row=4, column=1, padx=10, pady=10)

        # Create register button
        register_button = tk.Button(patron_window, text="Register", command=self.register_patron)
        register_button.grid(row=5, column=0, columnspan=2, pady=50)

        #delete button 
        delete_button = tk.Button(patron_window, text="Delete Record" , bg='#FF6347', fg='white')  
        delete_button.grid(row=5, column=0, pady=10)

        # Create update button
        update_button = tk.Button(patron_window, text="Update", command= self.update_patron)
        update_button.grid(row=5, column=1, pady=10)
        

    def register_patron(self):
        # Access entry fields using class attributes
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        address = self.entry_address.get()

        if not name or not email or not phone or not address:
            messagebox.showwarning("Error", "Please fill in all fields.")
        else:
            # Connect to MySQL
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="cathotel"
            )

             # Create a cursor object to interact with the database
            cursor = mydb.cursor()

            # Insert patron information into the database
            sql = "INSERT INTO patron (patron_name, patron_email, patron_phone, patron_address) VALUES (%s, %s, %s, %s)"
            data = (name, email, phone, address)



            try:
                cursor.execute(sql, data)
                mydb.commit()
                messagebox.showinfo("Patron Registration", "Registration successful!")
            except Exception as e:
                messagebox.showerror("Error", f"Error during registration: {str(e)}")
            finally:
                # Close the cursor and database connection
                cursor.close()
                mydb.close()

    def update_patron(self):
                 # Get the name, email, phone, and address from the entry fields
            try:
                new_name = self.entry_name.get()
                new_email = self.entry_email.get()
                new_phone = self.entry_phone.get()
                new_address = self.entry_address.get()
                
                sql = "UPDATE patron SET patron_email = %s, patron_phone = %s, patron_address = %s WHERE patron_name = %s"
                val = (new_name, new_email, new_phone, new_address)

                # Connect to MySQL
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="cathotel"
                )

                cursor=mydb.cursor()

                cursor.execute(sql, val)
                mydb.commit()
                
                messagebox.showinfo ("Success", "Data updated succesfully")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                mydb.rollback
                messagebox.showerror("Error", f"Error updating data: {err}")
                
            finally:
                cursor.close()

    def open_grooming_book(self):
        # Create a new window for patron registration
        grooming_window = tk.Toplevel(self.master)
        grooming_window.title ("Cat Hotel Grooming Appointment")
        grooming_window.geometry ('800x700')
        grooming_window.config (bg='#3C565B')

 # Connect to my MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cathotel"
        )

            # creating cursor object to execute SQL queries
        mycursor = mydb.cursor()

            # Function to handle the calculation and database saving
        def Insert():
            grooming_type = package_var.get()
            quantity = int(period_spinbox.get())
            appointment_date= my_label.cget("text")

            if not (grooming_type == "" or quantity =="" or appointment_date ==""):
                messagebox.showinfo("ALERT", "Please enter all fields")
            else:
                mydb= mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="", 
                    database="cathotel")
                cursor= mydb.cursor()
                
                sql= "INSERT INTO grooming (grooming_type, quantity_cat, date_appointment) VALUES (%s, %s, %s)"
                data = (grooming_type, quantity, appointment_date)

                try: 
                    cursor.execute(sql, data)
                    mydb.commit ()
                    messagebox.showinfo("Status", "Succesfully Inserted")
                except Exception as e:
                    messagebox.showerroe ("Error", f"Error during registration: {str(e)}")
                finally:
                    cursor.close()
                    mydb.close()

            #  Defining the prices from the User selections
            prices = {
                    "Aromatic salt Bath": 139,
                    "Oatmeal Scrub": 129,
                    "Collagen Essence Bath": 98,
                    "Royal Splash": 129
  
                    }
    
            # Calculating the total price. Which derived from the selection (Type, Period).
            total_price = (prices[grooming_type] * quantity)



        # Page Title
        label = tk.Label(grooming_window, text='Grooming Your Cat ^_^', font=("Times New Roman", 18, "bold"), bg='#3C565B', fg='white')
        label.grid(row=0, column= 3, pady=20)

        # Prices List by using textbox
        prices_text1 = tk.Text(grooming_window, height=8, width=20, font= ("Georgia", 12), borderwidth=2, relief="sunken", bg= '#B0CFDE')
        prices_text1.grid(row=1, column=1, padx=8, pady=(20, 20))

        prices_text2 = tk.Text(grooming_window, height=8, width=20, font=("Georgia", 12), borderwidth=2, relief="sunken", bg= '#B0CFDE')
        prices_text2.grid(row=2, column=1, padx=8, pady=(20, 20))


        # The defined list by using pricebox

        prices_text1.insert(tk.END,"\n")
        prices_text2.insert(tk.END,"\n")
        prices_text1.insert(tk.END, "Wellness Cat Spa :\n")
        prices_text1.insert(tk.END, "Aromatic Salt Bath \nPrice: RM 139\n\n")
        prices_text1.insert(tk.END, "Oatmeal Scrub \nPrice: RM129\n\n")

        prices_text2.insert(tk.END, "Beauty Cat Spa :\n")
        prices_text2.insert(tk.END, "Collagen Essence Bath \nPrice: RM 98\n\n")
        prices_text2.insert(tk.END, "Royal Splash \nPrice: RM128\n\n")

        # Configure tags for center alignment
        prices_text1.tag_configure("center", justify='center')
        prices_text2.tag_configure("center", justify='center')

        # Center the text in the Text widgets
        def center_text(text_widget):
            text_widget.tag_add("center", "1.0", "end")

        center_text(prices_text1)
        center_text(prices_text2)

        prices_text1.configure(state='disabled')
        prices_text2.configure(state='disabled')

        choose_frame = tk.Frame(grooming_window)
        choose_frame.grid(row=1, column=4, padx=20)
        choose_frame.configure(bg='#3C565B')

        # Trip Type Dropdown (Label)
        period_label = tk.Label(choose_frame, text="Choose Your Grooming Type")
        period_label.grid(pady=10)

        # Trip Type Dropdown
        package_var = tk.StringVar(choose_frame)
        package_var.set("Select Your Grooming Type")  # Default value before your selection
        trip_dropdown = tk.OptionMenu(choose_frame, package_var, "Aromatic Salt Bath", " Oatmeal Scrub", "Collagen Essence Bath", "Royal Splash" )
        trip_dropdown.grid(pady=10)


        # Packs Entry. Label and user can insert data thru entry
        quantity_label = tk.Label(choose_frame, text="Enter Quantity:")
        quantity_label.grid()
        period_spinbox = tk.Spinbox(choose_frame, from_=1, to=4)  
        period_spinbox.grid()

        choose_frame1 = tk.Frame(grooming_window)
        choose_frame1.grid(row=2, column=4, padx=20)

        def grab_date():
            my_label.config(text=cal.get.date())

        my_button = tk.Label (choose_frame1, text="Choose your Appointment Date")
        my_button.grid(row=1, column=4, pady=10)

        my_label= Label(grooming_window, text="")
        my_label.grid(pady=10)


        cal = Calendar(choose_frame1, selectmode="day", year=2024, month=1, day=15 )
        cal.grid(row=2, column=4)

        def update_grooming(self):
                 # Get the name, email, phone, and address from the entry fields
            try:
                new_grooming_type = self.entry_grooming_type.get()
                new_quantity = self.entry_quantity.get()
                new_appointment_date = self.entry_appointment_date.get()
                
                sql = "UPDATE patron SET patron_email = %s, patron_phone = %s, patron_address = %s WHERE patron_name = %s"
                val = (new_grooming_type, new_quantity, new_appointment_date)

                # Connect to MySQL
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="cathotel"
                )

                cursor=mydb.cursor()

                cursor.execute(sql, val)
                mydb.commit()
                
                messagebox.showinfo ("Success", "Data updated succesfully")
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                mydb.rollback
                messagebox.showerror("Error", f"Error updating data: {err}")
                
            finally:
                cursor.close()


        #Save button
        save_button = tk.Button(grooming_window,text='BOOK', font=("Times New Romans",10), relief="raised", command = Insert)
        save_button.grid(row=3, column=3, ipadx=10, ipady=10)


        #delete button 
        delete_button = tk.Button(grooming_window, text="Delete Record" , bg='#FF6347', fg='white')  
        delete_button.grid(row=6, column=3, pady=10)


    # Create update button
        update_button = tk.Button(grooming_window, text="Update")
        update_button.grid(row=5, column=3, pady=10)


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
