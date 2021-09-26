from tkinter import *
from tkinter import messagebox
import os
#from registration import registrationform
def login_success():
    messagebox.showinfo(screen, "Login Successful")
    screen2.destroy()
    #registrationform()
def password_not_recognised():
    messagebox.showwarning('ALERT', 'INCORRECT PASSWORD.')
def user_not_found():
    messagebox.showwarning('ALERT','USER NOT FOUND!!!')
def register_user():
    a = ''
    if username_entry.get() == a and password_entry.get() == a and password_entry2.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE FILL ALL THE BOXES.')
    elif username_entry.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE FILL THE BOX.')
    elif password_entry.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE WRITE THE PASSWORD.')
    elif password_entry2.get() == a :
        messagebox.showwarning('ALERT' , 'PLEASE CONFIRM YOUR PASSWORD TO CONTINUE.')
    elif password_entry.get()  != password_entry2.get() :
        messagebox.showwarning('ALERT', "SORRY !!! PASSWORD DOESNOT MATCH.")
    else :
        username_info = username.get()
        password_info = password.get()
        file = open(username_info, "a+")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        screen1.destroy()
        screen.destroy()
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    # os returns the list containing name of entries in the directory in the path
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("800x450")
    #image
    global bg5
    bg5=PhotoImage(file="C:/Users/gurun/Desktop/regim.png")
    img_label2=Label(screen1, image=bg5)
    img_label2.place(x=0, y=0, height=450, width=400)
    #register frame
    register_frame=Frame(screen1, bg='white')
    register_frame.place(x=400, y=0, height=450, width=400)
    id_label= Label(screen1, text="Create Your ID", fg="#FF7F00", bg='white', font=("calbria", 18, 'bold'))
    id_label.place(x=450, y=50)
    username_label = Label(screen1, bg='white', fg='#FF7F00', text='Username', font=('calibria', 12, 'bold'))
    username_label.place(x=500, y=90)
    password_label = Label(screen1, bg='white', fg='#FF7F00', text='Password', font=('calibria', 12, 'bold'))
    password_label.place(x=500, y=160)
    confrimpassword_label = Label(screen1, bg='white', fg='#FF7F00', text='Confirm Password', font=('calibria', 12, 'bold'))
    confrimpassword_label.place(x=500, y=230)
    global username
    global  password
    global username_entry
    global  password_entry
    global  password_entry2
    username = StringVar()
    password = StringVar()
    confirmpassword = StringVar()
    username_entry= Entry(screen1, textvariable=username, width='30', borderwidth='5')
    username_entry.place(x=500, y=120, height=30)
    password_entry = Entry(screen1, show="*", textvariable=password,width='30', borderwidth='5')
    password_entry.place(x=500, y=190, height=30)
    password_entry2 = Entry(screen1, show="*", textvariable= confirmpassword,width='30', borderwidth='5')
    password_entry2.place(x=500, y=260, height=30)
    register_btn=Button(screen1, text="Register", width=10, height=1, bg='dark orange', fg="white", font=("calbria", 13, 'bold'),command=register_user)
    register_btn.place(x=550, y=300)

    #image for register button
    global bg6
    bg6 = PhotoImage(file='C:/Users/gurun/Desktop/registermini.png')
    img1_label = Label(register_frame, image=bg6)
    register_btn=Button(screen1, image=bg6,bg='white', borderwidth=0, width=200, height=80,command=register_user)
    register_btn.place(x=500, y=300)
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("800x450")
    #image
    global bg3
    bg3 = PhotoImage(file="C:/Users/gurun/Desktop/bluu.png")
    img_label = Label(screen2, image=bg3)
    img_label.place(x=0, y=0, height=450, width=400)
    #login frame
    login_frame = Frame(screen2,bg='white')
    login_frame.place(x=400, y=0,height=450, width=480)
    label2 = Label(screen2, text="WELCOME BACK!", fg="#1874CD", bg='white', font=("calbria", 18, 'bold'))
    label2.place(x=450, y=70)
    user_label = Label(screen2, text="Username", fg='navy', bg='white', font=('calibria', 12, 'bold'))
    user_label.place(x=500, y=120)
    pass_label = Label(screen2, text="Password", fg='navy', bg='white', font=('calibria', 12, 'bold'))
    pass_label.place(x=500, y=200)
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    username_entry1 = Entry(screen2, textvariable= username_verify,width='30',borderwidth='5')
    username_entry1.place(x=500, y=150, height=30)
    password_entry1 = Entry(screen2, show="*", textvariable=password_verify, width='30', borderwidth='5')
    password_entry1.place(x=500, y=230, height=30,)
    global bg4
    bg4 = PhotoImage(file='C:/Users/gurun/Desktop/loginmini.png')
    img1_label = Label(login_frame, image=bg4)
    login_btn = Button(screen2, text="Login", bg='white', image=bg4, width=180, borderwidth=0, height=80,
                       command=login_verify)
    login_btn.place(x=500, y=260)
def main_screen():
    global screen
    screen = Tk()
    screen.geometry('1350x760')
    screen.resizable(False, False)
    screen.title('Login | Hospital Management System')
    #image
    global bg
    bg = PhotoImage(file="C:/Users/gurun/Desktop/hospi.png")
    label = Label(screen, image=bg)
    label.place(x=0, y=0)
    Title_frame = Frame(screen, padx=20,bg='white' ,relief=RIDGE)
    Title_frame.place(x=450, y=90, width=600, height=360)
    #image for login
    global bg1
    bg1 = PhotoImage(file="C:/Users/gurun/Desktop/LOGINB.png")
    label1 = Label(Title_frame, image=bg1)
    #image for register
    global bg2
    bg2 = PhotoImage(file="C:/Users/gurun/Desktop/REGISTERB.png")
    label2 = Label(Title_frame, image=bg2)
    # textboxes
    login_button = Button(Title_frame, image=bg1, height="80", bg='white', borderwidth=0, width="370", command=login)
    login_button.place(x=0, y=130)
    register_button = Button(Title_frame, image=bg2, height="80", bg='white', borderwidth=0, width="370", command=register)
    register_button.place(x=0, y=250)
    screen.mainloop()
main_screen()