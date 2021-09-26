
def prescribe2():
    root = Toplevel()
    root.title('Prescription')
    root.geometry('580x750')
    root.resizable(False, False)
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

