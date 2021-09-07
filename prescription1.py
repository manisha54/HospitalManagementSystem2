from tkinter import *
import sqlite3
from tkinter import messagebox
def prescribe1():
    root = Toplevel()
    root.title('Prescription')
    root.geometry('580x750')
    root.resizable(False, False)
    # connecting to  database
    join = sqlite3.connect('prescription1.db')
    # creating the cursor
    j = join.cursor()
    """
    #creating the tables
    j.execute(('''CREATE TABLE prescribeD(
               diagnosed_entry1 text ,
               diagnosed_entry2 text ,
               diagnosed_entry3 text ,
               diagnosed_entry4 text ,
               d1_entry text ,
               d2_entry text ,
               d3_entry text ,
               d4_entry text ,
               d5_entry text ,
               unit1_entry text ,
               unit2_entry text ,
               unit3_entry text ,
               unit4_entry text ,
               unit5_entry text ,
               dose1_entry text ,
               dose2_entry text ,
               dose3_entry text ,
               dose4_entry text ,
               dose5_entry text ,
               diet_entry1 text ,
               diet_entry2 text ,
               diet_entry3 text ,
               history_entry1 text ,
               history_entry2 text ,
               history_entry3 text
               )'''))

    print('TABLE CREATED SUCCESSFULLY')
    """

    def submit():
        j = sqlite3.connect("prescription1.db")
        j1 = j.cursor()
        j.execute(
            "INSERT INTO prescribeD VALUES (:diagnosed_entry1, :diagnosed_entry2, :diagnosed_entry3,:diagnosed_entry4, :d1_entry ,:d2_entry ,:d3_entry ,:d4_entry ,:d5_entry ,:unit1_entry,:unit2_entry, :unit3_entry, :unit4_entry, :unit5_entry, :dose1_entry, :dose2_entry,:dose3_entry ,:dose4_entry,:dose5_entry ,:diet_entry1 , :diet_entry2 ,:diet_entry3 ,:history_entry1 , :history_entry2, :history_entry3 )",
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


