from tkinter import *


def lod():
    def nex_img(i):
        # delete previous image
        canvas.delete('image')
        # create next image
        canvas.create_image(20, 20, anchor=NW, image=listing[int(i)-1], tags='image')
    root = Toplevel()
    root.title(' DOCTORS AVAILABLE')
    #root.iconbitmap('C:/Users/RUPA/Downloads/iconn.ico')
    title_frame_label = Label(root, font=('Courier', 30, 'roman', 'bold'), fg="BLACK", text='OUR DOCTORS',
                              padx=20)
    title_frame_label.pack(side=TOP)
    image1 = PhotoImage(file='a.png')
    image2 = PhotoImage(file='b.png')
    image3 =PhotoImage(file='c.png')
    image4= PhotoImage(file='d.png')
    image5 = PhotoImage(file ='e.png')
    image6 = PhotoImage(file='f.png')
    image7 =PhotoImage(file='g.png')
    image8 = PhotoImage(file ='h.png')
    image9 = PhotoImage(file ='i.png')
    image10 = PhotoImage(file='j.png')
    image11 = PhotoImage(file='k.png')
    listing = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11]
    scale = Scale(master=root, orient=VERTICAL, from_=1, to=len(listing), resolution=1,
                  showvalue=False, command=nex_img)
    scale.pack(side=RIGHT, fill=X )
    canvas = Canvas(root, width=500, height=500 )
    canvas.pack()
    # show first image
    nex_img(1)
    root.mainloop()
