from tkinter import *
from tkinter import ttk

def imprimir():
    print(entry_text.get())

gui = Tk()
gui.geometry("200x200+50+50") 
gui.configure(background= "cyan4")

entry_text = StringVar() 
entry_widget = Entry(gui, width = 20, textvariable = entry_text, justify=CENTER).pack()

Button(gui, command= imprimir).pack()

gui.mainloop()