from PIL import ImageTk, Image
def lod():
    def nex_img(i):   # takes the current scale position as an argument
        # delete previous image
        canvas.delete('image')
        # create next image
        canvas.create_image(20, 20, anchor=NW, image=listing[int(i)-1] ,tags = 'image') #Tagging something means that you have given that thing one or more strings that act as labels.
    root = Toplevel()
    root.title(' DOCTORS AVAILABLE')
    Title_frame_label = Label(root, font=('Courier', 30, 'roman','bold'),fg = "BLACK" , text='OUR DOCTORS',
                              padx=20)
    Title_frame_label.pack(side = TOP)
    image1 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/a.png'))
    image2 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/b.png'))
    image3 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/c.png'))
    image4= ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/d.png'))
    image5 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/e.png'))
    image6 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/f.png'))
    image7 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/g.png'))
    image8 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/h.png'))
    image9 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/i.png'))
    image10 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/j.png'))
    image11 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/k.png'))
    listing = [image1, image2 , image3 , image4 , image5 , image6 , image7 , image8 , image9 , image10 , image11]
    scale = Scale(master=root, orient=VERTICAL, from_=1, to=len(listing), resolution=1,
                  showvalue=False, command=nex_img)
    scale.pack(side=RIGHT, fill=X )
    canvas = Canvas(root, width=500, height=500 )
    canvas.pack()
    # show first image
    nex_img(1)
    root.mainloop()