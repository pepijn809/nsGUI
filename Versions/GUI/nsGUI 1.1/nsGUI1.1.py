from tkinter import *
from tkinter.messagebox import showinfo
import tkinter as tk

#GUI

def clicked():
    create_window()

def create_window():
    window = tk.Toplevel(root)
    window.attributes('-fullscreen', True)
    display = Label(window, text='De actuele vertrektijden:',
                    background='yellow',
                    foreground='blue',
                    height=15,
                    width=20,
                    font=('Ariel',24,'bold'))

    button = Button(window, text='Terug',
                    background='yellow',
                    foreground='blue')
    button.pack(side=BOTTOM)

    display.pack()


root = Tk()
root.attributes('-fullscreen', True)

label1 = Label(master=root,
              text='Welkom bij NS',
              background='yellow',
              foreground='blue',
              font=('Ariel', 24 , 'bold'),
              width=100,
              height=10)
label1.pack()

label2 = Label(master=root,
               text='Typ uw station?',
               background='yellow',
               foreground='blue',
               font=('Ariel', 16,'bold'),
               height=25,
               width=146)

label2.pack()

entry = Entry(master=root)
entry.pack(padx=15, pady=15)

button1 = Button(master=root, command=clicked,
                 text='Vertrektijden',
                 background='yellow',
                 foreground='blue',
                 font=('Ariel', 14, 'bold'))
button1.pack(pady=10)



root.mainloop()
