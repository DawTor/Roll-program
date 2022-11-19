import tkinter as tk
from tkinter import *
import random
from tkinter.messagebox import showinfo

list_of_elements = []

def add_button():
    element = entrybox.get()
    entrybox.delete(0, END)

    if element:
        with open("elementslist.txt", "a") as elf:
            elf.write(f'\n{element}')
        list_of_elements.append(element)
        listbox.insert(END, element)

        
def del_button():
    element = str(listbox.get(ANCHOR))
    if element in list_of_elements:
        list_of_elements.remove(element)
        with open("elementslist.txt", "w") as elf:
            for element in list_of_elements:
                elf.write(element+'\n')

        listbox.delete( ANCHOR)

        
def roll_button():
    choice = random.choice(list_of_elements)
    showinfo(title='Roll Winner!', message=f'{choice} WON!')

    
def listfile():
    try:
        with open("elementslist.txt", "r") as elf:
            elements = elf.readlines()

        for element in elements:
            if element !="\n":
                list_of_elements.append(element)
                listbox.insert(END ,element)

    except:
        file = open("elementslist.txt", "w")
        file.close()


#create a window
window = Tk()
window.title("Roller program")
window.geometry("400x220")
window.resizable(False, False)
window.config(bg="#252525")

frame = Frame(window, bg="#252525")
frame.place(x=48,y=20)

listbox = Listbox(frame, height=5, width=50,)
listbox.pack()

element = StringVar()
entrybox = Entry(frame)
entrybox.pack(padx=5,pady=10)
entrybox.focus()

listfile()

addbutton = Button(frame, text="Add", height=3, width=10, command=add_button).pack(side="left")
delbutton = Button(frame, text="Delete", height=3, width=10, command=del_button ).pack(side="left")
rollbutton = Button(frame, text="Roll", height=3, width=10, command=roll_button ).pack(side="right")


window.mainloop()
