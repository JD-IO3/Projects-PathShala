from tkinter import *
from tkinter import filedialog
from customtkinter import *
from PIL import Image, ImageTk
import os

set_appearance_mode('System')
set_default_color_theme('blue')

def showimg():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image', filetypes=(("JPG File", "*.JPG"), ("PNG file", "*.PNG"), ("All File", "how are you.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img

root = CTk()
root.title("Image Viewer")
root.geometry('400x450')

frame = CTkFrame(master=root)
frame.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = CTkButton(frame, text="Select Image", command=showimg)
btn.pack(side=LEFT)

exitbtn = CTkButton(frame, text="Exit", command=lambda: exit())
exitbtn.pack(side=LEFT, padx=12)

root.mainloop()