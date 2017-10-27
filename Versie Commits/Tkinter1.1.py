from tkinter import *
import tkinter as tk

def clicked(): create_window()

def destroy(self):
    top.destroy()

def create_window():
    top = Toplevel(root)
    top.attributes('-fullscreen',True)
    top.title('Vertrektijden')
    Display = Label(top, text='Actuele vertrektijden',
                    bg='yellow',
                    fg='blue',
                    width=100,
                    height=20,
                    font=('Ariel',24,'bold'))
    button = Button(top,
                    text='Terug',command=top.destroy,
                    width=15,
                    height=5,
                    font=("Ariel",14,'bold'),
                    bg='yellow',
                    fg='blue')
    button.pack(side=BOTTOM)
    Display.pack()


root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='yellow')
label1 = Label(master=root,
              text='Welkom bij NS',
              foreground='blue',
              font=('Ariel', 24 , 'bold'))
label1.pack()

label2 = Label(master=root,
               text='Typ uw station?',
               foreground='blue',
               font=('Ariel', 16,'bold'))
label2.pack()

entry = Entry(master=root)
entry.pack(padx=15, pady=15)

b1 = Button(master=root, command=clicked,
                 text='Vertrektijden',
                 background='yellow',
                 foreground='blue',
                 font=('Ariel', 14, 'bold'))
b1.pack(pady=5,padx=10)

root.mainloop()