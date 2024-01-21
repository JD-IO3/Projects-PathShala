from tkinter import *
from customtkinter import *
import qrcode
from PIL import Image, ImageTk

set_appearance_mode('System')
set_default_color_theme('blue')

root = CTk()
root.title("QR Generator")
root.geometry('500x500')

showimg = None

def generateqr():
    global showimg
    
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)

    qr.add_data(inp.get())
    qr.make(fit=True)
    
    img = qr.make_image()
    img.save("Python/QR_Generator/qrcode.png")
    
    showimg = ImageTk.PhotoImage(Image.open('Python/QR_Generator/qrcode.png'))
    imglabel.configure(image=showimg)

inp = CTkEntry(master=root)
inp.place(relx=0.5, rely=0.1, anchor=CENTER)

imglabel = CTkLabel(master=root, text="")
imglabel.place(relx=0.5, rely=0.6, anchor = CENTER)

btn = CTkButton(master=root, text="Generate", command=generateqr, ) #*hex also works..
btn.place(relx=0.5, rely=0.2, anchor=CENTER)

root.mainloop()