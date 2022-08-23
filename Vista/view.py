from struct import pack
from tkinter import *
from tkinter import ttk


ventana = Tk()
ventana.config(bd=50)
ventana.title("Aseo acuavalle")

buton1=ttk.Button(text="Aseo acuavalle")
buton1.pack()

menu=Menu(ventana)
filemenu = Menu(menu)
ventana.config(menu=menu)
menu.add_cascade(label="Archivo", menu=filemenu)







ventana.mainloop()