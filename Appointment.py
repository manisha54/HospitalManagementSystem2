from tkinter import *
from prescriptionB import *
from list_of_doctors import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview

def appoint2():
    root = Toplevel()
    root.title('Appointment')
    root.geometry('1100x750')
    root.resizable(False,False)
    # root.iconbitmap('C:/Users/RUPA/Downloads/iconn.png')
    title = Label(root, text='PATIENTS DETAILS', bg='powder blue', fg='green', bd=10, relief=RIDGE,
                  font=("times new roman", 25, "bold"), padx=2, pady=6)
    title.pack(side=TOP, fill=X)
    # creating to database
    conn = sqlite3.connect('check2.db')
    # Creating the cursor
    c = conn.cursor()
    # creating tables

    # c.execute(('''CREATE TABLE appointment_test5 (
    #          p_conditions text ,
    #          medication text ,
    #        symptoms text ,
    #        cal_check text ,
    #        allergy text ,
    #        doctors text
    #      )'''))
    # print('TABLE CREATED SUCCESSFULLY ')
    #

    def submit():
        conn = sqlite3.connect('check2.db')
        c = conn.cursor()
        c.execute(
            "INSERT INTO appointment_test5 VALUES (:p_conditions, :medication, :symptom, :cal_check , :allergy , :doctors )",
            {
                'p_conditions': condition.get(),
                'medication': medications.get(),
                'symptom': symptoms.get(),
                'cal_check': cale_entry.get(),
                'allergy': symptom2.get(),
                'doctors': doc_entry.get()
            })
        messagebox.showinfo('Success', 'Data inserted succefully')
        conn.commit()
        conn.close()

    def query():
        conn = sqlite3.connect("Hospitalmanagement.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM addressb  WHERE oid=" + ID_e.get())
        record1 = c.fetchall()
        print(record1)


        if (len(record1) != 0):
            patient_table.delete(*patient_table.get_children())
            for row in record1:
                patient_table.insert('', END, values=row)

    def update():
        conn = sqlite3.connect("Hospitalmanagement.db")
        c = conn.cursor()
        c.execute(
            "SELECT * FROM addressb  WHERE oid=" + ID_e.get())
        record1 = c.fetchall()
        print(record1)
        for records in record1:
            name.insert(0, records[0])
            age.insert(0, records[2])
            gender.insert(0, records[5])
        conn1 = sqlite3.connect('check2.db')
        c1 = conn1.cursor()
        c1.execute("SELECT  * FROM appointment_test5 WHERE oid=" + ID_e.get())
        record2 = c1.fetchall()
        for records in record2:
            condition.insert(0, records[0])
            medications.insert(0, records[1])
            symptoms.insert(0, records[2])
            cale_entry.insert(0, records[3])
            symptom2.insert(0, records[4])
            doc_entry.insert(0, records[5])


    def editor():
        conn = sqlite3.connect('check2.db')
        c = conn.cursor()
        record_id1 = ID_e.get()
        c.execute("""UPDATE appointment_test5 SET
                      p_conditions = :condition ,
                 medication = :medicine ,
               symptoms = :symptom ,
               cal_check = :date,
               allergy = :allergies ,
               doctors = :doc
               WHERE oid = :oid""",
                  {'condition': condition.get(),
                   'medicine': medications.get(),
                   'symptom': symptoms.get(),
                   'date': cale_entry.get(),
                   'allergies': symptom2.get(),
                   'doc': doc_entry.get(),
                   'oid': record_id1
                   })
        conn.commit()
        conn.close()
        messagebox.showinfo('SUCCESS ', 'DATA HAS BEEN UPDATED SUCCESFULLY!!!')

    def clear():
        """this function clears the data shown in the entry"""
        name.delete(0, END)
        age.delete(0, END)
        gender.delete(0, END)
        condition.delete(0, END)
        symptoms.delete(0, END)
        symptom2.delete(0, END)
        doc_entry.delete(0, END)
        cale_entry.delete(0, END)
        medications.delete(0, END)

    def delete():
        # Create a databases or connect to one
        conn3 = sqlite3.connect('check2.db')
        c3 = conn3.cursor()
        # delete a record
        c3.execute("DELETE from appointment_test5 WHERE oid = " + ID_e.get())
        print('Deleted Successfully')
        # query of the database
        c3.execute("SELECT *, oid FROM appointment_test5")
        records = c3.fetchall()
        # print(records)
        # Loop through the results
        print_record3 = ''
        for record in records:
            print_record3 += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[2]) + '' + str(record[3]) + str(
                record[4]) + str(record[5]) + '\t' + "\n"
        query_label = Label(framedetails, text=print_record3, bg='powder blue', font=('calibri', 14, 'bold'))
        query_label.place(x=100, y=20)
        conn3.commit()
        conn3.close()

    def prescription():
        prescribe2()

    def doctors():
            lod()

    global patient_table
    global framedetails
    style = ttk.Style()
    style.configure('Treeview.Heading', font=('Cambria 15 italic', 12, 'bold'))
    framedetails = Frame(root, bd=10, relief=RIDGE, padx=20, bg='#ACB5AF')
    framedetails.place(x=0, y=560, width=1100, height=200)
    scroll_x = Scrollbar(framedetails, orient=HORIZONTAL)
    scroll_y = Scrollbar(framedetails, orient=VERTICAL)
    patient_table = Treeview(framedetails, column=(
        'first_name', 'last_name', 'age', 'address', 'date_of_birth', 'gender', 'father_name', 'mother_name',
        'blood_group',
        'contact_number', 'email_address', 'marital_status'),
                             yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=patient_table.xview)
    scroll_y.config(command=patient_table.yview)
    patient_table.heading('first_name', text='First Name')
    patient_table.heading('last_name', text='Last Name')
    patient_table.heading('age', text='Age')
    patient_table.heading('address', text='Address')
    patient_table.heading('date_of_birth', text='Date Of Birth')
    patient_table.heading('gender', text='Gender')
    patient_table.heading('father_name', text='Fathers Name')
    patient_table.heading('mother_name', text='Mothers Name')
    patient_table.heading('blood_group', text='Blood Group')
    patient_table.heading('email_address', text='E-mail Address')
    patient_table.heading('contact_number', text='Contact')
    patient_table.heading('marital_status', text='Marital Status')
    patient_table['show'] = 'headings'
    patient_table.column('first_name', width=150)
    patient_table.column('last_name', width=140)
    patient_table.column('age', width=65)
    patient_table.column('address', width=140)
    patient_table.column('date_of_birth', width=140)
    patient_table.column('gender', width=120)
    patient_table.column('father_name', width=140)
    patient_table.column('mother_name', width=140)
    patient_table.column('blood_group', width=140)
    patient_table.column('email_address', width=230)
    patient_table.column('contact_number', width=120)
    patient_table.column('marital_status', width=120)
    patient_table.pack(fill=BOTH, expand=YES)

    title = Label(root, text='PATIENTS DETAILS', bg='#D8D3CD', fg='#8B4789', bd=10, relief=RIDGE,
                  font=("times new roman", 25, "bold"), padx=2, pady=6)
    title.place(x=0, y=0, height=70, width=1100)

    frame = Frame(root, bd=10, relief=RIDGE, padx=20, bg='#ACB5AF')
    frame.place(x=0, y=69, width=1100, height=430)
    Dataframeleft = LabelFrame(frame, text='Patient Information', bg='#FFE1FF', fg='#8B4789', bd=10, relief=RIDGE,
                               font=("times new roman", 12, "bold"))
    Dataframeleft.place(x=0, y=10, width=280, height=380)
    Dataframeright1 = LabelFrame(frame, bg='#FFE4E1', bd=10, relief=RIDGE, font=("times new roman", 12, "bold"))
    Dataframeright1.place(x=300, y=10, width=600, height=380)
    Dataframeright2 = LabelFrame(frame, text="Calendar", fg='#8B4789', bg='#FFE1FF', bd=10, relief=RIDGE,
                                 font=("times new roman", 12, "bold"))
    Dataframeright2.place(x=750, y=9, width=300, height=380)
    # calendar
    cale = Label(Dataframeright2, text='Enter the date for your appointment : ', bg='#FFE1FF',
                 font=("times new roman", 12, "bold"))
    cale.place(x=10, y=0)
    cale_entry = Entry(Dataframeright2, font=("times new roman", 12, "bold"))
    cale_entry.place(x=20, y=25)

    # framedetails1 = LabelFrame(framedetails, text="Records", bg='#FFE1FF', fg='#8B4789', bd=10, relief=RIDGE,
    #                            font=("times new roman", 12, "bold"))
    # framedetails1.place(x=0, y=10, width=1050, height=160)
    FrameButton = Frame(root, bd=10, relief=RIDGE, padx=20, bg='#D8BFD8')
    FrameButton.place(x=0, y=500, width=1100, height=60)

    # doctors
    doc_label = Label(FrameButton, text="Please enter the doctor's name", bg='#D8BFD8', font=('calibri', 12, 'bold'))
    doc_label.place(x=580, y=5)
    doc_entry = Entry(FrameButton, font=('calibri', 14,), width=15, relief=SUNKEN)
    doc_entry.place(x=800, y=5)

    name_label = Label(Dataframeright1, text='Name:', bg="#FFE4E1", font=('times new roman', 14, 'bold'))
    name_label.place(x=10, y=10)
    age_label = Label(Dataframeright1, text='Age:', bg="#FFE4E1", font=('times new roman', 14, 'bold'))
    age_label.place(x=10, y=60)
    gender_label = Label(Dataframeright1, text='Gender:', bg="#FFE4E1", font=('times new roman', 14, 'bold'))
    gender_label.place(x=10, y=110)
    condition_label = Label(Dataframeright1, text='Previous Conditions: ', bg="#FFE4E1",
                            font=('times new roman', 14, 'bold'))
    condition_label.place(x=10, y=160)
    mediation_label = Label(Dataframeright1, text='Medication you are on:', bg="#FFE4E1",
                            font=('times new roman', 14, 'bold'))
    mediation_label.place(x=10, y=210)
    symptom1_label = Label(Dataframeright1, text='Symptoms you are having:', bg="#FFE4E1",
                           font=('times new roman', 14, 'bold'))
    symptom1_label.place(x=10, y=260)
    symptom2_label = Label(Dataframeright1, text='Any Allergies:', bg="#FFE4E1", font=('times new roman', 14, 'bold'))
    symptom2_label.place(x=10, y=310)
    global name
    global age
    global gender
    global condition
    global medications
    global symptoms
    global ID_e
    name = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    name.place(x=230, y=10)
    age = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    age.place(x=230, y=60)
    gender = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    gender.place(x=230, y=110)
    condition = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    condition.place(x=230, y=160)
    medications = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    medications.place(x=230, y=210)
    symptoms = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    symptoms.place(x=230, y=260)
    symptom2 = Entry(Dataframeright1, font=('calibri', 14,), width=15, relief=SUNKEN)
    symptom2.place(x=230, y=310)
    # forID
    ID_label = Label(Dataframeleft, text='ENTER PATIENT ID', font=('calibri', 14, 'bold'), bg='#FFE1FF', fg="#8B4789")
    ID_label.place(x=0, y=0)
    ID_e = Entry(Dataframeleft, font=('calibri', 14,), width=10)
    ID_e.place(x=10, y=30)
    # buttons

    global bg1
    bg1 = PhotoImage(file="submit .png")
    submit_btn = Button(frame, image=bg1, borderwidth=0, command=submit )
    submit_btn.place(x=15, y=90, height=44, width=250)
    global bg2
    bg2 = PhotoImage(file="dis.png")
    display_btn = Button(frame, image=bg2, borderwidth=0, height=40, width=250, command=query)
    display_btn.place(x=15, y=140, )
    global bg3
    bg3 = PhotoImage(file="updatee.png")
    update_btn = Button(frame, image=bg3, borderwidth=0, height=40, width=250, command=update)
    update_btn.place(x=15, y=188)
    global bg4
    bg4 = PhotoImage(file="save .png")
    save_btn = Button(frame, image=bg4, borderwidth=0, height=40, width=250,command=editor)
    save_btn.place(x=15, y=236)
    global bg5
    bg5 = PhotoImage(file="clearr.png")
    clear_btn = Button(frame, image=bg5, borderwidth=0, height=40, width=250, command=clear)
    clear_btn.place(x=15, y=285, )
    global bg6
    bg6 = PhotoImage(file="dele.png")
    delete_btn = Button(frame, image=bg6, borderwidth=0, height=40, width=250, command=delete)
    delete_btn.place(x=15, y=334)
    global bg7
    bg7 = PhotoImage(file="ourdoc.png")
    ourdoc_btn = Button(FrameButton, image=bg7, borderwidth=0, height=30, width=330, command=doctors)
    ourdoc_btn.place(x=5, y=3)
    global bg8
    bg8 = PhotoImage(file="enter.png")
    entry_btn = Button(frame, image=bg8, borderwidth=0, height=30, width=100, command=query)
    entry_btn.place(x=130, y=55, )
    global bg9
    bg9 = PhotoImage(file="pres.png")
    entry_btn = Button(Dataframeright2, image=bg9, borderwidth=0, height=85, width=250, command=prescription)
    entry_btn.place(x=10, y=270, )
    global bg10
    bg10 = PhotoImage(file="calender.png")
    label1 = Label(Dataframeright2, image=bg10)
    label1.place(x=3, y=45)
    mainloop()

