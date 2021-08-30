
def appoint2():
    root = Toplevel()
    root.title('Appointment')
    root.geometry('1100x800')
    title = Label(root, text='PATIENTS DETAILS', bg='powder blue', fg='green', bd=10, relief=RIDGE,
                  font=("times new roman", 25, "bold"), padx=2, pady=6)
    title.pack(side=TOP, fill=X)

    # creating to database
    conn = sqlite3.connect('check2.db')
    # Creating the cursor
    c = conn.cursor()
    # creating tables
    """
    c.execute(('''CREATE TABLE appointment_test5 (
             p_conditions text ,
             medication text ,
           symptoms text ,
           cal_check text ,
           allergy text ,
           doctors text
         )'''))
    print('TABLE CREATED SUCCESSFULLY ')
    """




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

        for records in record1:
            name.insert(0, records[1])
            name.insert(0, records[0])
            age.insert(0, records[2])
            gender.insert(0, records[5])

        conn1 = sqlite3.connect('check2.db')
        c1 = conn1.cursor()
        c1.execute("SELECT * FROM appointment_test5 where oid=" + ID_e.get())
        record2 = c1.fetchall()
        print(record2)

        for recordss in record2:
            condition.insert(0, recordss[0])
            medications.insert(0, recordss[1])
            symptoms.insert(0, recordss[2])
            cale_entry.insert(0, recordss[3])
            symptom2.insert(0, recordss[4])
            doc_entry.insert(0, recordss[5])

        global print_record
        global print_record1
        print_record = ''
        print_record1 = ''
        for records in record1:
            print_record += str(records[0]) + "\t" + str(records[1]) + str(records[2]) + str(
                records[3]) + " " + "\n"
        query_label = Label(framedetails, text=print_record, bg="powder blue", font=('calibri', 14, 'bold'))
        query_label.place(x=50, y=20)
        for records1 in record2:
            print_record1 += str(records1[0]) + "\t" + str(records1[1]) + str(records1[2]) + str(records1[3]) + str(
                records1[4]) + str(records1[5])

        query_label1 = Label(framedetails, text=print_record1, bg="powder blue", font=('calibri', 14, 'bold'))
        query_label1.place(x=100, y=20)

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
        name.delete(0, END)
        age.delete(0, END)
        gender.delete(0, END)
        condition.delete(0, END)
        symptoms.delete(0, END)
        symptom2.delete(0, END)
        doc_entry.delete(0, END)
        cale_entry.delete(0, END)
        medications.delete(0, END)

    def list_doctors():
        lod()

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
