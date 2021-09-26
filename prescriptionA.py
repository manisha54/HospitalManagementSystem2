from tkinter import *
from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
def prescribe1():
    root = Toplevel()
    root.title('Prescription')
    root.geometry('580x750')
    root.resizable(False, False)
    # root.iconbitmap('C:/Users/RUPA/Downloads/iconn.png')
    # connecting to  database
    join = sqlite3.connect('prescription.db')
    # creating the cursor
    j = join.cursor()

    #creating the tables
    #j.execute(('''CREATE TABLE prescribeC(
    #          diagnosed_entry1 text ,
    #          diagnosed_entry2 text ,
    #           diagnosed_entry3 text ,
    #           diagnosed_entry4 text ,
    #           d1_entry text ,
    #           d2_entry text ,
    #           d3_entry text ,
    #           d4_entry text ,
    #          d5_entry text ,
    #           unit1_entry text ,
    #           unit2_entry text ,
    #           unit3_entry text ,
    #          unit4_entry text ,
     #          unit5_entry text ,
     #          dose1_entry text ,
     #          dose2_entry text ,
     #          dose3_entry text ,
     #          dose4_entry text ,
     #          dose5_entry text ,
     #          diet_entry1 text ,
    #           diet_entry2 text ,
    #           diet_entry3 text ,
    #           history_entry1 text ,
    #          history_entry2 text ,
     #          history_entry3 text
      #         )'''))
    #print('TABLE CREATED SUCCESSFULLY')

    def submit():
        j = sqlite3.connect("prescription.db")
        j1 = j.cursor()
        j.execute(
            "INSERT INTO prescribeC VALUES (:diagnosed_entry1, :diagnosed_entry2, :diagnosed_entry3,:diagnosed_entry4, :d1_entry ,:d2_entry ,:d3_entry ,:d4_entry ,:d5_entry ,:unit1_entry,:unit2_entry, :unit3_entry, :unit4_entry, :unit5_entry, :dose1_entry, :dose2_entry,:dose3_entry ,:dose4_entry,:dose5_entry ,:diet_entry1 , :diet_entry2 ,:diet_entry3 ,:history_entry1 , :history_entry2, :history_entry3 )",
            {
                'diagnosed_entry1': diagnosed_entry1.get(),
                'diagnosed_entry2': diagnosed_entry2.get(),
                'diagnosed_entry3': diagnosed_entry3.get(),
                'diagnosed_entry4': diagnosed_entry4.get(),
                'd1_entry': d1_entry.get(),
                'd2_entry': d2_entry.get(),
                'd3_entry': d3_entry.get(),
                'd4_entry': d4_entry.get(),
                'd5_entry': d5_entry.get(),
                'unit1_entry': unit1_entry.get(),
                'unit2_entry': unit2_entry.get(),
                'unit3_entry': unit3_entry.get(),
                'unit4_entry': unit4_entry.get(),
                'unit5_entry': unit5_entry.get(),
                'dose1_entry': dose1_entry.get(),
                'dose2_entry': dose2_entry.get(),
                'dose3_entry': dose3_entry.get(),
                'dose4_entry': dose4_entry.get(),
                'dose5_entry': dose5_entry.get(),
                'diet_entry1': diet_entry1.get(),
                'diet_entry2': diet_entry2.get(),
                'diet_entry3': diet_entry3.get(),
                'history_entry1': history_entry1.get(),
                'history_entry2' : history_entry2.get(),
                'history_entry3': history_entry3.get()
            })
        messagebox.showinfo('Success.' , 'YOUR DATA HAS BEEN INSERTED.')
        j.commit()
        j.close()

    def query():
        # retriving data from 2nd database
        conn = sqlite3.connect("check.db")
        c = conn.cursor()
        c.execute("SELECT * FROM appointment_test5 WHERE oid=" + ID_entry.get())
        recordI = c.fetchall()
        print(recordI)

        for recordsA in recordI:
            date_entry.insert(0, recordsA[3])
            allergies_entry.insert(0, recordsA[4])
            history_entry1.insert(0, recordsA[0])
            history_entry2.insert(0, recordsA[1])
            doc_name_entry.insert(0, recordsA[5])

        # retriving data from 1st database
        conn1 = sqlite3.connect("Hospitalmanagement.db")
        c1 = conn1.cursor()
        c1.execute(
            "SELECT *FROM addressb WHERE oid=" + ID_entry.get())
        recordB = c1.fetchall()
        print(recordB)

        for records in recordB:
            name_entry.insert(0, records[1])
            name_entry.insert(0, records[0])
            age_entry.insert(0, records[2])
            gender_entry.insert(0, records[5])

        # retriving data from 3rd database
        conn2 = sqlite3.connect('prescription.db')
        c2 = conn2.cursor()
        c2.execute("SELECT * FROM prescribeC where oid=" + ID_entry.get())
        record3 = c2.fetchall()
        print(record3)
        for records3 in record3:
            diagnosed_entry1.insert(0, records3[0])
            diagnosed_entry2.insert(0, records3[1])
            diagnosed_entry3.insert(0, records3[2])
            diagnosed_entry4.insert(0, records3[3])
            d1_entry.insert(0, records3[4])
            d2_entry.insert(0, records3[5])
            d3_entry.insert(0, records3[6])
            d4_entry.insert(0, records3[7])
            unit1_entry.insert(0, records3[9])
            unit2_entry.insert(0, records3[10])
            unit3_entry.insert(0, records3[11])
            unit4_entry.insert(0, records3[12])
            unit5_entry.insert(0, records3[13])
            dose1_entry.insert(0, records3[14])
            dose2_entry.insert(0, records3[15])
            dose3_entry.insert(0, records3[16])
            dose4_entry.insert(0, records3[17])
            dose5_entry.insert(0, records3[18])
            diet_entry1.insert(0, records3[19])
            diet_entry2.insert(0, records3[20])
            diet_entry3.insert(0, records3[21])
            history_entry1.insert(0, records3[22])
            history_entry2.insert(0, records3[23])
            history_entry3.insert(0, records3[24])
            # displaying records in frame
            global print_record
            global print_record1
            print_record = ''
            print_record1 = ''
            for records in recordI:
                print_record += str(records[0]) + "\t" + str(records[1]) + str(records[2]) + str(
                    records[3]) + " " + "\n"
            query_label = Label(records_frame, text=print_record, bg="powder blue")
            query_label.pack()
            for records1 in recordB:
                print_record1 += str(records1[0]) + "\t" + str(records1[1]) + str(records1[2]) + str(records1[3]) + str(
                    records1[4]) + str(records1[5])

            query_label1 = Label(records_frame, text=print_record1, bg="powder blue")
            query_label1.pack()
    def delete():
        # Create a databases or connect to one
        conn3 = sqlite3.connect('prescription.db')
        c3 = conn3.cursor()
        # delete a record
        c3.execute("DELETE from prescribeC WHERE oid = " + ID_entry.get())
        print('Deleted Successfully')
        # query of the database
        c3.execute("SELECT *, oid FROM prescribeC")
        records = c3.fetchall()
        # print(records)
        # Loop through the results
        print_record3 = ''
        for record in records:
            print_record3 += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t'  + "\n"
        query_label = Label(records_frame, text=print_record3)
        query_label.place(x=0, y=0)
        conn3.commit()
        conn3.close()
    def clear():
        name_entry.delete(0,END)
        allergies_entry.delete(0, END)
        age_entry.delete(0, END)
        gender_entry.delete(0, END)
        doc_name_entry.delete(0, END)
        date_entry.delete(0, END)
        d1_entry.delete(0, END)
        d2_entry.delete(0, END)
        d3_entry.delete(0, END)
        d4_entry.delete(0, END)
        d5_entry.delete(0, END)
        dose1_entry.delete(0, END)
        dose2_entry.delete(0, END)
        dose3_entry.delete(0, END)
        dose4_entry.delete(0, END)
        dose5_entry.delete(0, END)
        unit1_entry.delete(0, END)
        unit2_entry.delete(0, END)
        unit3_entry.delete(0, END)
        unit4_entry.delete(0, END)
        unit5_entry.delete(0, END)
        diet_entry1.delete(0, END)
        diet_entry2.delete(0, END)
        diet_entry3.delete(0, END)
        diagnosed_entry1.delete(0, END)
        diagnosed_entry2.delete(0, END)
        diagnosed_entry3.delete(0, END)
        diagnosed_entry4.delete(0, END)
        history_entry1.delete(0, END)
        history_entry2.delete(0, END)
        history_entry3.delete(0, END)


    label_title = Label(root, text='DOCTORS', font=('san fransisco', 20, 'bold'), bg='light grey', fg="red")
    label_title.place(x=0, y=0)
    label_title2 = Label(root, text='Medical Prescription', font=('san fransisco', 18, 'bold'), bg='light grey',
                         fg='black')
    label_title2.place(x=0, y=40)

    frame1 = Frame(root, bg='#FFA07A')
    frame1.place(x=0, y=70, width=580, height=30)
    frame2 = Frame(root, bg='#FFDAB9')
    frame2.place(x=0, y=100, width=580, height=30)
    frame3 = Frame(root, bg="#FFA07A")
    frame3.place(x=0, y=130, width=580, height=30)

    frame4 = Frame(root, bg='#FFDAB9')
    frame4.place(x=0, y=160, width=580, height=30)
    frame5 = Frame(root, bg='#FFDAB9')
    frame5.place(x=0, y=190, width=580, height=30)
    frame6 = Frame(root, bg='#FFDAB9')
    frame6.place(x=0, y=220, width=580, height=30)

    frame7 = Frame(root, bg='#FFA07A')
    frame7.place(x=0, y=250, width=580, height=30)

    frame8 = Frame(root, bg='#FFDAB9')
    frame8.place(x=0, y=290, width=580, height=30)

    frame9 = Frame(root, bg='#FFA07A')
    frame9.place(x=0, y=400, width=580, height=30)

    frame10 = Frame(root, bg='#FFDAB9')
    frame10.place(x=0, y=430, width=580, height=30)
    frame11 = Frame(root, bg='#FFA07A')
    frame11.place(x=0, y=460, width=580, height=30)
    frame12 = Frame(root, bg='#FFDAB9')
    frame12.place(x=0, y=490, width=580, height=30)
    frame13 = Frame(root, bg='#FFA07A')
    frame13.place(x=0, y=520, width=580, height=30)
    frame14 = Frame(root, bg='#FFDAB9')
    frame14.place(x=0, y=550, width=580, height=30)
    frame15 = Frame(root, bg='#FFA07A')
    frame15.place(x=0, y=580, width=580, height=70)
    frame16 = Frame(root, bg='#FFDAB9')
    frame16.place(x=0, y=650, width=580, height=70)
    frame17 = Frame(root, bg='#FFA07A')
    frame17.place(x=0, y=720, width=580, height=30)

    records_frame = Frame(root, bg='white')
    records_frame.place(x=0, y=280, width=580, height=120)
    frame_rec = LabelFrame(records_frame, text='records', font=('georgia', 12, 'bold'), relief=RIDGE, bd=5, fg="black",
                           bg="white")
    frame_rec.place(x=3, y=1, width=570, height=110)
    label1 = Label(root, text='Patients name:', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label1.place(x=0, y=72)
    label2 = Label(root, text='Date:', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label2.place(x=350, y=72)
    label3 = Label(root, text='Patients ID:', bg='#FFDAB9', font=('georgia', 11, 'bold'))
    label3.place(x=0, y=102)
    label4 = Label(root, text='Age:', bg='#FFDAB9', font=('georgia', 11, 'bold'))
    label4.place(x=340, y=102)

    label6 = Label(root, text='Gender:', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label6.place(x=0, y=132)

    label11 = Label(root, text='Diagnosed With:', bg='#FFDAB9', font=('georgia', 11, 'bold'))
    label11.place(x=0, y=162)

    label14 = Label(root, text='Allergies:', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label14.place(x=0, y=252)

    label16 = Label(root, text='Drugs:', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label16.place(x=80, y=402)
    label17 = Label(root, text='Unit(Tablet/Syrup):', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label17.place(x=227, y=402)
    label18 = Label(root, text='Dosage(Per Day):', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label18.place(x=420, y=402)
    label19 = Label(root, text='Diet To Follow:', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label19.place(x=0, y=580)
    label20 = Label(root, text='Brief History Of Patient:', bg='#FFDAB9', font=('georgia', 11, 'bold'))
    label20.place(x=0, y=650)
    label21 = Label(root, text='Name Of Physician:', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label21.place(x=0, y=720)
    label22 = Label(root, text='1.', bg='#FFDAB9', font=('georgia', 11, 'bold'))
    label22.place(x=0, y=432)
    label23 = Label(root, text='2.', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label23.place(x=0, y=462)
    label24 = Label(root, text='3.', bg='#FFDAB9', font=('georgia', 11, 'bold'))
    label24.place(x=0, y=492)
    label25 = Label(root, text='4.', bg='#FFA07A', font=('georgia', 11, 'bold'))
    label25.place(x=0, y=522)
    label26 = Label(root, text='5.', bg='#FFDAB9', font=('georgia', 11, 'bold'))
    label26.place(x=0, y=552)
    label27 = Label(root, text="", bg='white', font=('georgia', 115))
    label27.place(x=210, y=400)
    label28 = Label(root, text="", bg='white', font=('georgia', 115))
    label28.place(x=400, y=400)

    name_entry = Entry(root, font=('georgia', 11,))
    name_entry.place(x=130, y=73)
    date_entry = Entry(root, font=('georgia', 11), width=18)
    date_entry.place(x=400, y=73)
    ID_entry = Entry(root, font=('georgia', 11), width=18)
    ID_entry.place(x=130, y=103)
    age_entry = Entry(root, font=('georgia', 11), width=10)
    age_entry.place(x=400, y=103)
    gender_entry = Entry(root, font=('georgia', 11), width=10)
    gender_entry.place(x=130, y=133)

    diagnosed_entry1 = Entry(root, font=('georgia', 11), width=47)
    diagnosed_entry1.place(x=140, y=162)
    diagnosed_entry2 = Entry(root, font=('georgia', 11), width=47)
    diagnosed_entry2.place(x=140, y=182)
    diagnosed_entry3 = Entry(root, font=('georgia', 11), width=47)
    diagnosed_entry3.place(x=140, y=202)
    diagnosed_entry4 = Entry(root, font=('georgia', 11), width=47)
    diagnosed_entry4.place(x=140, y=222)

    allergies_entry = Entry(root, font=('georgia', 11), width=48)
    allergies_entry.place(x=130, y=253)
    d1_entry = Entry(root, font=('georgia', 11), width=19)
    d1_entry.place(x=29, y=434)
    d2_entry = Entry(root, font=('georgia', 11), width=19)
    d2_entry.place(x=29, y=464)
    d3_entry = Entry(root, font=('georgia', 11), width=19)
    d3_entry.place(x=29, y=494)
    d4_entry = Entry(root, font=('georgia', 11), width=19)
    d4_entry.place(x=29, y=524)
    d5_entry = Entry(root, font=('georgia', 11), width=19)
    d5_entry.place(x=29, y=554)
    unit1_entry = Entry(root, font=('georgia', 11), width=19)
    unit1_entry.place(x=221, y=434)
    unit2_entry = Entry(root, font=('georgia', 11), width=19)
    unit2_entry.place(x=221, y=464)
    unit3_entry = Entry(root, font=('georgia', 11), width=19)
    unit3_entry.place(x=221, y=494)
    unit4_entry = Entry(root, font=('georgia', 11), width=19)
    unit4_entry.place(x=221, y=524)
    unit5_entry = Entry(root, font=('georgia', 11), width=19)
    unit5_entry.place(x=221, y=554)
    dose1_entry = Entry(root, font=('georgia', 11), width=18)
    dose1_entry.place(x=411, y=434)
    dose2_entry = Entry(root, font=('georgia', 11), width=18)
    dose2_entry.place(x=411, y=464)
    dose3_entry = Entry(root, font=('georgia', 11), width=18)
    dose3_entry.place(x=411, y=494)
    dose4_entry = Entry(root, font=('georgia', 11), width=18)
    dose4_entry.place(x=411, y=524)
    dose5_entry = Entry(root, font=('georgia', 11), width=18)
    dose5_entry.place(x=411, y=554)

    diet_entry1 = Entry(root, font=('georgia', 11), width=47)
    diet_entry1.place(x=129, y=584)
    diet_entry2 = Entry(root, font=('georgia', 11), width=47)
    diet_entry2.place(x=129, y=604)
    diet_entry3 = Entry(root, font=('georgia', 11), width=47)
    diet_entry3.place(x=129, y=624)

    history_entry1 = Entry(root, font=('georgia', 11), width=40)
    history_entry1.place(x=200, y=654)
    history_entry2 = Entry(root, font=('georgia', 11), width=40)
    history_entry2.place(x=200, y=674)
    history_entry3 = Entry(root, font=('georgia', 11), width=40)
    history_entry3.place(x=200, y=694)
    doc_name_entry = Entry(root, font=('georgia', 11), width=18)
    doc_name_entry.place(x=200, y=724)

    # buttons
    enter_btn = Button(root, text='Enter', font=('calibre', 15, 'bold'), bg='red', fg='white',command=query)
    enter_btn.place(x=255, y=25)
    submit_btn = Button(root, text='Submit', font=('calibre', 16, 'bold'), bg='red', fg='white',command=submit)
    submit_btn.place(x=325, y=25)
    entry_btn = Button(root, text='Clear', font=('calibre', 16, 'bold'), bg='red', fg='white',command=clear)
    entry_btn.place(x=417, y=25)
    delete_btn = Button(root, text='Delete', font=('calibre', 16, 'bold'), bg='red', fg='white',command=delete)
    delete_btn.place(x=490, y=25)

    mainloop()