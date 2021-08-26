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

    # Back-end
    def submit():
        """this function inserts the data in the database."""
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

    # query
    def query():
        """this functions displays the records """
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM addressb")
        records = c.fetchall()
        print(records)


        if (len(records) != 0):
            patient_table.delete(*patient_table.get_children())
            for row in records:
                patient_table.insert('', END, values=row)

        conn.commit()
        conn.close()

    def delete():
        """this function deletes the selected data """
        # Create a databases or connect to one
        conn = sqlite3.connect('Hospitalmanagement.db')
        c = conn.cursor()
        # delete a record
        c.execute("DELETE from addressb WHERE oid = " + delete_box_entry.get())
        messagebox.showinfo('DELETE DATA',
                            'You have successfully deleted the data of ID number ' + delete_box_entry.get())
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
        """this function will update the datas saved in the database."""
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

        conn.commit()
        conn.close()

    def appoint9():
        appoint2()

    def fordoctors():
        prescribe1()