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
        #displaying records in frame
        global print_record
        global print_record1
        print_record = ''
        print_record1 = ''
        for records in recordI:
            print_record += str(records[0]) + "\t" + str(records[1]) + str(records[2]) + str(
                records[3]) + " " + "\n"
        query_label = Label(records_frame, text=print_record, bg="powder blue",font = ('calibri', 14 , 'bold'))
        query_label.pack()
        for records1 in recordB:
            print_record1 += str(records1[0]) + "\t" + str(records1[1]) + str(records1[2]) + str(records1[3]) + str(
                records1[4]) + str(records1[5])

        query_label1 = Label(records_frame, text=print_record1, bg="powder blue",font = ('calibri', 14 , 'bold'))
        query_label1.pack()


    def delete():
        # Create a databases or connect to one
        conn3 = sqlite3.connect('prescription1.db')
        c3 = conn3.cursor()
        # delete a record
        c3.execute("DELETE from prescribeD WHERE oid = " + ID_entry.get())
        print('Deleted Successfully')
        # query of the database
        c3.execute("SELECT *, oid FROM prescribeD")
        records = c3.fetchall()
        # print(records)
        # Loop through the results
        print_record3 = ''
        for record in records:
            print_record3 += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t'  + "\n"
        query_label = Label(records_frame, text=print_record3,font = ('calibri', 14 , 'bold'))
        query_label.place(x=0, y=0)
        conn3.commit()
        conn3.close()

    def clear():
        """this function clears the data shown in the entry"""
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


