from tkinter import *
import sqlite3
from tkinter import messagebox
from prescriptionA import *
from appointment import *


def registrationform():
    root = Toplevel()
    root.title('Registration')
    root.geometry('1500x750')
    # connect to database
    conn = sqlite3.connect('Hospitalmanagement.db')
    # create a cursor
    c = conn.cursor()
    """ 
    c.execute(('''CREATE TABLE addressb( 
            first_name  text , 
            last_name text , 
            age integer , 
            address text , 
            date_of_birth integer , 
            gender text , 
            father_name text , 
            mother_name text , 
            blood_group text , 
            contact_number integer , 
            email_address text, 
          marital_status text 
        )''')) 
    """

    def submit():
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO addressb VALUES (:first_name, :last_name, :age, :address, :date_of_birth, :gender, :father_name, :mother_name, :blood_group, :contact_number, :email_address, :marital_status)",
            {
                'first_name': first_name.get(),
                'last_name': last_name.get(),
                'age': age.get(),
                'address': address.get(),
                'date_of_birth': date_of_birth.get(),
                'gender': gender_dropdown.get(),
                'father_name': father_name.get(),
                'mother_name': mother_name.get(),
                'blood_group': btype_dropdown.get(),
                'contact_number': Contact_number.get(),
                'email_address': Email_address.get(),
                'marital_status': marital_dropdown.get()
            })
        messagebox.showinfo('success')
        conn.commit()
        conn.close()
        first_name.delete(0, END)
        last_name.delete(0, END)
        age.delete(0, END)
        address.delete(0, END)
        date_of_birth.delete(0, END)
        father_name.delete(0, END)
        mother_name.delete(0, END)
        Contact_number.delete(0, END)
        Email_address.delete(0, END)

    def query():
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM addressb")
        records = c.fetchall()
        print(records)
        print_record = ''
        for record in records:
            print_record += str(record[12]) + ' ' + str(record[0]) + ' ' + str(record[1]) + ' ' + str(
                record[2]) + ' ' + str(record[3]) + ' ' + str(record[4]) + ' ' + str(record[5]) + ' ' + str(
                record[6]) + ' ' + str(record[7]) + ' ' + str(record[8]) + ' ' + str(record[9]) + ' ' + str(
                record[10]) + ' ' + str(record[11]) + '\t' + "\n"
        query_label = Label(Bottom_frame_details, text=print_record, font=('calibri', 14, 'bold'))
        query_label.place(x=-20, y=5)
        conn.commit()
        conn.close()

    def delete():
        # Create a databases or connect to one
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        # delete a record
        c.execute("DELETE from addressb WHERE oid = " + delete_box_entry.get())
        messagebox.showinfo('DELETE DATA',
                            'You have succesfully deleted the data of ID number ' + delete_box_entry.get())
        # query of the database
        c.execute("SELECT *, oid FROM addressb")
        records = c.fetchall()
        # print(records)
        # Loop through the results
        print_record = ''
        for record in records:
            # str(record[12]) added for displaying the id
            print_record += str(record[12]) + ' ' + str(record[0]) + ' ' + str(record[1]) + ' ' + str(
                record[2]) + ' ' + str(record[3]) + ' ' + str(record[4]) + ' ' + str(record[5]) + ' ' + str(
                record[6]) + ' ' + str(record[7]) + ' ' + str(record[8]) + ' ' + str(record[9]) + ' ' + str(
                record[10]) + ' ' + str(record[11]) + '\t' + "\n"
        query_label = Label(Bottom_frame_details, text=print_record, font=('calibri', 14, 'bold'))
        query_label.place(x=-30, y=5)
        conn.commit()
        conn.close()

    def update():
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        record_id = delete_box_entry.get()
        c.execute("SELECT *FROM addressb WHERE oid=" + record_id)
        record = c.fetchall()
        for records in record:
            first_name.insert(0, records[0])
            last_name.insert(0, records[1])
            age.insert(0, records[2])
            address.insert(0, records[3])
            date_of_birth.insert(0, records[4])
            father_name.insert(0, records[6])
            mother_name.insert(0, records[7])
            Contact_number.insert(0, records[9])
            Email_address.insert(0, records[10])

    def editor():
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        record_id = delete_box_entry.get()
        c.execute("""UPDATE addressb SET 
             first_name = :first, 
             last_name = :last, 
             age= :age, 
             address = :address, 
             date_of_birth= :dob, 
             father_name = :father, 
             mother_name = :mother, 
             Contact_number = :contact, 
             Email_address = :email 
             WHERE oid = :oid""",
                  {'first': first_name.get(),
                   'last': last_name.get(),
                   'age': age.get(),
                   'address': address.get(),
                   'dob': date_of_birth.get(),
                   'father': father_name.get(),
                   'mother': mother_name.get(),
                   'contact': Contact_number.get(),
                   'email': Email_address.get(),
                   'oid': record_id
                   })
        messagebox.showinfo('Updated Data',
                            'You have successfully updated the data of ID number ' + delete_box_entry.get())
        conn.commit()
        conn.close()

    def appoint9():
        appoint2()

    def fordoctors():
        prescribe1()

    Title_frame_label = Label(root, font=('calibri', 30, 'bold'), fg='#528B8B', bg='#D1EEEE',
                              text='HOSPITAL MANAGEMENT SYSTEM', bd=10, relief=RIDGE, padx=2, pady=6)
    Title_frame_label.pack(side=TOP, fill=X)
    frame = Frame(root, bd=12, relief=RIDGE, padx=20, bg='#293242')
    frame.place(x=0, y=80, width=1499, height=500)
    Entry_frame_details = LabelFrame(frame, bd=10, bg='#FAEBD7', padx=250, relief=RIDGE)
    Entry_frame_details.place(x=0, y=13, width=1150, height=450)
    Button_frame_rights = LabelFrame(frame, bd=10, bg='#FFEBCD', padx=250, relief=RIDGE)
    Button_frame_rights.place(x=1150, y=13, width=290, height=450)
    Bottom_frame_details = Frame(root, bd=10, bg='#293242', padx=25, relief=RIDGE)
    Bottom_frame_details.place(x=0, y=580, width=1499, height=200)
    Recordframedetails = LabelFrame(Bottom_frame_details, text='Records', bd=7, bg='#D1EEEE',
                                    font=("times new roman", 12, "bold"), relief=RIDGE)
    Recordframedetails.place(x=0, y=5, width=1440, height=170)
    first_name_label = Label(Entry_frame_details, text='First Name', bg='#FAEBD7', font=('calibri', 16, 'bold'))
    first_name_label.place(x=-220, y=40)
    last_name_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 16, 'bold'), text='Last Name',
                            anchor='e')
    last_name_label.place(x=250, y=40)
    age_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 16, 'bold'), text='Age')
    age_label.place(x=-220, y=100)
    address_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'), text='Address')
    address_label.place(x=250, y=100)
    date_of_birth_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'),
                                text='Date Of Birth ')
    date_of_birth_label.place(x=-220, y=220)
    gender_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'), text='Gender')
    gender_label.place(x=-220, y=160)
    father_name_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'),
                              text="Father's name ")
    father_name_label.place(x=250, y=160)
    mother_name_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'),
                              text="Mother's name ")
    mother_name_label.place(x=250, y=220)
    Blood_group_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'), text='Blood Group')
    Blood_group_label.place(x=250, y=340)
    Contact_number_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'),
                                 text='Contact Number')
    Contact_number_label.place(x=-220, y=280)
    marital_status_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'),
                                 text='Marital status')
    marital_status_label.place(x=-220, y=340)
    Email_label = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'), text='Email address')
    Email_label.place(x=250, y=280)
    delete_box = Label(Entry_frame_details, bg='#FAEBD7', font=('calibri', 14, 'bold'), text='Delete/Update ID')
    delete_box.place(x=-220, y=390)
    # create textboxes
    first_name = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    first_name.place(x=-80, y=40)
    last_name = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    last_name.place(x=380, y=40)
    age = Entry(Entry_frame_details, font=('calibri', 14,), width=5, borderwidth=5)
    age.place(x=-80, y=100)
    address = Entry(Entry_frame_details, font=('calibri', 14,), width=40, borderwidth=5)
    address.place(x=380, y=100)
    date_of_birth = Entry(Entry_frame_details, font=('calibri', 14,), width=20, borderwidth=5)
    date_of_birth.place(x=-80, y=220)
    # gender = Entry(Entry_frame_details, font = ('calibri', 14 , ), width = 15, borderwidth = 5)
    # gender.place(x =-80 , y = 160)
    father_name = Entry(Entry_frame_details, font=('calibri', 14,), width=40, borderwidth=5)
    father_name.place(x=380, y=160)
    mother_name = Entry(Entry_frame_details, font=('calibri', 14,), width=40, borderwidth=5)
    mother_name.place(x=380, y=220)
    Contact_number = Entry(Entry_frame_details, font=('calibri', 14,), width=17, borderwidth=5)
    Contact_number.place(x=-80, y=280)
    Email_address = Entry(Entry_frame_details, font=('calibri', 14,), width=30, borderwidth=5)
    Email_address.place(x=380, y=280)
    delete_box_entry = Entry(Entry_frame_details, text="Delete ID", font=('calibri', 14,), width=5, borderwidth=5)
    delete_box_entry.place(x=-60, y=390)
    # dropdown
    # drop down menu for gender
    gender = ["Male", "Female", "Other", "Prefer not to say"]
    gender_dropdown = StringVar()
    gender_dropdown.set("Prefer not to say")
    drop1 = OptionMenu(Entry_frame_details, gender_dropdown, *gender)
    drop1.place(x=-80, y=160)
    # drop down menu for marital status
    marital = ["Married", "Unmarried"]
    marital_dropdown = StringVar()
    marital_dropdown.set("Unmarried")
    drop2 = OptionMenu(Entry_frame_details, marital_dropdown, *marital)
    drop2.place(x=-80, y=340)
    # drop down menu for blood group
    blood_type = ["O+", "O-", "A+", "A-", "AB+", "AB-", "B+", "B-"]
    btype_dropdown = StringVar()
    btype_dropdown.set("0+")
    drop3 = OptionMenu(Entry_frame_details, btype_dropdown, *blood_type)
    drop3.place(x=380, y=340)
    global bg1
    bg1 = PhotoImage(file="C:/Users/gurun/Desktop/Submit.png")
    submit_btn = Button(Button_frame_rights, image=bg1, borderwidth=0, command=submit)
    submit_btn.place(x=-240, y=20, height=44, width=250)
    global bg2
    bg2 = PhotoImage(file="C:/Users/gurun/Desktop/Display.png")
    update_btn = Button(Button_frame_rights, image=bg2, borderwidth=0, height=40, width=250, command=query)
    update_btn.place(x=-240, y=80, )
    global bg3
    bg3 = PhotoImage(file="C:/Users/gurun/Desktop/Update.png")
    record_btn = Button(Button_frame_rights, image=bg3, borderwidth=0, height=40, width=250, command=update)
    record_btn.place(x=-240, y=140, )
    global bg4
    bg4 = PhotoImage(file="C:/Users/gurun/Desktop/save.png")
    enrty_btn = Button(Button_frame_rights, image=bg4, borderwidth=0, height=40, width=250, command=editor)
    enrty_btn.place(x=-240, y=200, )
    global bg5
    bg5 = PhotoImage(file="C:/Users/gurun/Desktop/Delete.png")
    sad_btn = Button(Button_frame_rights, image=bg5, borderwidth=0, height=40, width=250, command=delete)
    sad_btn.place(x=-240, y=260, )
    global bg6
    bg6 = PhotoImage(file="C:/Users/gurun/Desktop/Appointment.png")
    sadd_btn = Button(Button_frame_rights, image=bg6, borderwidth=0, height=40, width=250, command=appoint9)
    sadd_btn.place(x=-240, y=320, )
    global bg7
    bg7 = PhotoImage(file="C:/Users/gurun/Desktop/Doctorsuseonly.png")
    lad_btn = Button(Button_frame_rights, image=bg7, borderwidth=0, height=40, width=250, command=fordoctors)
    lad_btn.place(x=-240, y=380, )

    mainloop()

