from tkinter import *
import sqlite3
from tkinter import messagebox
def prescribe12():
    root = Toplevel()
    root.title('Prescription')
    root.geometry('580x750')
    root.resizable(False, False)
    root.iconbitmap("hos.ico")
    def query():
        # retriving data from 2nd database
        conn = sqlite3.connect("check2.db")
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
        conn2 = sqlite3.connect('prescription1.db')
        c2 = conn2.cursor()
        c2.execute("SELECT * FROM prescribeD where oid=" + ID_entry.get())
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
            unit1_entry.insert(0,records3[9])
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
    def logout():
        response = messagebox.askyesno("Logout Application", "Are you sure want to close this application")
        if response > 0:
            root.destroy()

        return

    mybutton = Button(root, text="EXIT", font=("calibre", 15, "bold"), fg="white", bg="red", command=logout)
    mybutton.place(x=390, y=20)

    label_title = Label(root, text='DOCTORS', font=('san fransisco', 20, 'bold'), bg='light grey', fg="red")
    label_title.place(x=0, y=0)
    label_title2 = Label(root, text='Medical Prescription', font=('san fransisco', 18, 'bold'), bg='light grey',
                         fg='black')
    label_title2.place(x=0, y=40)

    frame1 = Frame(root, bg='#66CDAA')
    frame1.place(x=0, y=70, width=580, height=30)
    frame2 = Frame(root, bg='#EEE9BF')
    frame2.place(x=0, y=100, width=580, height=30)
    frame3 = Frame(root, bg="#66CDAA")
    frame3.place(x=0, y=130, width=580, height=30)

    frame4 = Frame(root, bg='#EEE9BF')
    frame4.place(x=0, y=160, width=580, height=30)
    frame5 = Frame(root, bg='#EEE9BF')
    frame5.place(x=0, y=190, width=580, height=30)
    frame6 = Frame(root, bg='#EEE9BF')
    frame6.place(x=0, y=220, width=580, height=30)

    frame7 = Frame(root, bg='#66CDAA')
    frame7.place(x=0, y=250, width=580, height=30)

    frame8 = Frame(root, bg='#EEE9BF')
    frame8.place(x=0, y=280, width=580, height=30)

    frame9 = Frame(root, bg='#66CDAA')
    frame9.place(x=0, y=310, width=580, height=30)

    frame10 = Frame(root, bg='#EEE9BF')
    frame10.place(x=0, y=340, width=580, height=30)
    frame11 = Frame(root, bg='#66CDAA')
    frame11.place(x=0, y=370, width=580, height=30)
    frame12 = Frame(root, bg='#EEE9BF')
    frame12.place(x=0, y=400, width=580, height=30)
    frame13 = Frame(root, bg='#66CDAA')
    frame13.place(x=0, y=430, width=580, height=30)
    frame14 = Frame(root, bg='#EEE9BF')
    frame14.place(x=0, y=460, width=580, height=30)
    frame15 = Frame(root, bg='#66CDAA')
    frame15.place(x=0, y=490, width=580, height=70)
    frame16 = Frame(root, bg='#EEE9BF')
    frame16.place(x=0, y=520, width=580, height=70)
    frame17 = Frame(root, bg='#66CDAA')
    frame17.place(x=0, y=590, width=580, height=70)
    frame18 = Frame(root, bg='#EEE9BF')
    frame18.place(x=0, y=660, width=580, height=30)

    label1 = Label(root, text='Patients name:', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label1.place(x=0, y=72)
    label2 = Label(root, text='Date:', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label2.place(x=350, y=72)
    label3 = Label(root, text='Patients ID:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label3.place(x=0, y=102)
    label4 = Label(root, text='Age:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label4.place(x=340, y=102)

    label6 = Label(root, text='Gender:', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label6.place(x=0, y=132)

    label11 = Label(root, text='Diagnosed With:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label11.place(x=0, y=162)

    label14 = Label(root, text='Allergies:', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label14.place(x=0, y=252)

    label16 = Label(root, text='Drugs:', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label16.place(x=80, y=312)
    label17 = Label(root, text='Unit(Tablet/Syrup):', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label17.place(x=227, y=312)
    label18 = Label(root, text='Dosage(Per Day):', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label18.place(x=420, y=312)
    label19 = Label(root, text='Diet To Follow:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label19.place(x=0, y=520)
    label20 = Label(root, text='Brief History Of Patient:', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label20.place(x=0, y=592)
    label21 = Label(root, text='Name Of Physician:', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label21.place(x=0, y=662)
    label22 = Label(root, text='1.', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label22.place(x=0, y=342)
    label23 = Label(root, text='2.', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label23.place(x=0, y=372)
    label24 = Label(root, text='3.', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label24.place(x=0, y=402)
    label25 = Label(root, text='4.', bg='#66CDAA', font=('georgia', 11, 'bold'))
    label25.place(x=0, y=432)
    label26 = Label(root, text='5.', bg='#EEE9BF', font=('georgia', 11, 'bold'))
    label26.place(x=0, y=462)
    label27 = Label(root, text="", bg='white', font=('georgia', 115))
    label27.place(x=210, y=312)
    label28 = Label(root, text="", bg='white', font=('georgia', 115))
    label28.place(x=400, y=312)

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
    d1_entry.place(x=29, y=344)
    d2_entry = Entry(root, font=('georgia', 11), width=19)
    d2_entry.place(x=29, y=374)
    d3_entry = Entry(root, font=('georgia', 11), width=19)
    d3_entry.place(x=29, y=404)
    d4_entry = Entry(root, font=('georgia', 11), width=19)
    d4_entry.place(x=29, y=434)
    d5_entry = Entry(root, font=('georgia', 11), width=19)
    d5_entry.place(x=29, y=464)
    unit1_entry = Entry(root, font=('georgia', 11), width=19)
    unit1_entry.place(x=221, y=344)
    unit2_entry = Entry(root, font=('georgia', 11), width=19)
    unit2_entry.place(x=221, y=374)
    unit3_entry = Entry(root, font=('georgia', 11), width=19)
    unit3_entry.place(x=221, y=404)
    unit4_entry = Entry(root, font=('georgia', 11), width=19)
    unit4_entry.place(x=221, y=434)
    unit5_entry = Entry(root, font=('georgia', 11), width=19)
    unit5_entry.place(x=221, y=464)
    dose1_entry = Entry(root, font=('georgia', 11), width=18)
    dose1_entry.place(x=411, y=344)
    dose2_entry = Entry(root, font=('georgia', 11), width=18)
    dose2_entry.place(x=411, y=374)
    dose3_entry = Entry(root, font=('georgia', 11), width=18)
    dose3_entry.place(x=411, y=404)
    dose4_entry = Entry(root, font=('georgia', 11), width=18)
    dose4_entry.place(x=411, y=434)
    dose5_entry = Entry(root, font=('georgia', 11), width=18)
    dose5_entry.place(x=411, y=464)

    diet_entry1 = Entry(root, font=('georgia', 11), width=47)
    diet_entry1.place(x=129, y=524)
    diet_entry2 = Entry(root, font=('georgia', 11), width=47)
    diet_entry2.place(x=129, y=544)
    diet_entry3 = Entry(root, font=('georgia', 11), width=47)
    diet_entry3.place(x=129, y=564)

    history_entry1 = Entry(root, font=('georgia', 11), width=40)
    history_entry1.place(x=200, y=594)
    history_entry2 = Entry(root, font=('georgia', 11), width=40)
    history_entry2.place(x=200, y=614)
    history_entry3 = Entry(root, font=('georgia', 11), width=40)
    history_entry3.place(x=200, y=634)
    doc_name_entry = Entry(root, font=('georgia', 11), width=18)
    doc_name_entry.place(x=200, y=664)

    enter_btn = Button(root, text='ENTER', font=('calibre', 15, 'bold'), bg='red', fg='white',command=query )
    enter_btn.place(x=300, y=20)
    mainloop()