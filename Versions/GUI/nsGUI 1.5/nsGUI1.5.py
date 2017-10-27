import random
import tkinter as tk
import urllib.request
from tkinter import *


def interfacePrinter(station):
    from Project.ns_API import ns_API2Format
    ns_API2Format = ns_API2Format(str(station))
    # als de code zonder fouten runt wordt alles mooi onder elkaar geprint
    # als er een error voorkomt in de functie wordt de foutmelding gereturnt en geprint
    try:
        # kiezen uit
        # vertrektijd, eindbestemming, treinSoort, vertrekspoor, viaRoute, opmerking
        # print('{:14}{:20}{:12}{}'.format('vertrektijd:', 'eindbestemming:', 'treinSoort:', 'vertrekspoor:'))
        text = ['{:14}{:20}{:12}{}'.format('vertrektijd:', 'eindbestemming:', 'treinSoort:', 'vertrekspoor:')]
        for x in ns_API2Format:
            # makkelijke notatie voor makkelijk gebruik
            vertrektijd = ns_API2Format[x]['vertrektijd']
            eindbestemming = ns_API2Format[x]['eindbestemming']
            treinSoort = ns_API2Format[x]['treinSoort']
            vertrekspoor = ns_API2Format[x]['vertrekspoor']
            viaRoute = ns_API2Format[x]['viaRoute']
            opmerking = ns_API2Format[x]['opmerking']
            vertraging = ns_API2Format[x]['vertraging']

            #elke regel hier onder is een ook een nieuwe regel in de GUI
            text += ['{:6}{:12}{:20}{:12}{:5}'.format(vertrektijd, vertraging, eindbestemming, treinSoort, vertrekspoor)]
            text += ['{:18}{:20}'.format('',viaRoute)]
            text += ['{:18}{:20}'.format('',opmerking)] + ['']  #lege regel tussen de stations
        return text



    except:
        return ns_API2Format
main_window = tk.Tk()
main_window.attributes('-fullscreen',True)
main_window.title("NS")
main_window.configure(background='#ffc917')


# -------------------Alle funties-------------------------------#
def download_img(url):
    name = random.randrange(1, 1000)
    ns = str(name) + '.jpg'
    urllib.request.urlretrieve(url, ns)
    return ns

def create_window():
    top = Toplevel(main_window)
    top.attributes('-fullscreen',True)
    top.title('Vertrektijden')
    Display = Label(top, text='Actuele vertrektijden',
                    bg='',
                    fg='blue',
                    width=100,
                    height=20,
                    font=('Ariel',24,))
    button = Button(top,
                    text='Terug',command=top.destroy,
                    width=15,
                    height=5,
                    font=("Ariel",14,'bold'),
                    bg='#ffc917',
                    fg='blue')
    button.pack(side=BOTTOM)
    Display.pack()

def clicked():
    create_window()

def destroy(self):
    top.destroy()


#-------------------------functie naar window----------------------------#
def toListbox(stationNaam):
    for lines in interfacePrinter(stationNaam):
        text.insert(END, lines)

# ----------Alle main scherm labels-----------------------------#
img = PhotoImage(file=download_img(
    'https://i.imgur.com/FLXfxow.png'))
photo_label = Label(main_window, image=img, width=550, height=150).pack()
main_label = Label(main_window, text='Welkom bij NS', foreground='blue',bg='#ffc917', font=('Ariel', 24, 'bold')).pack()

station_label = Label(main_window,bg='#ffc917', text='Typ uw station', foreground='blue', font=('Ariel', 16, 'bold')).pack()



#e = tk.Entry(main_window)
#e.pack(padx=10, pady=10)
## Calling on_change when you press the return key
#e.bind("<Return>", on_change)

koop_label = Button(main_window, text='Koop los kaartje', background='yellow', foreground='blue',
                    font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)

naar_buitenland_label = Button(main_window, text='Ik wil naar het buitenland', background='yellow', foreground='blue',
                               font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)

ov_label = Button(main_window, text='Koop OV-Chipkaart', background='yellow', foreground='blue',
                  font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)

btn = tk.Button(main_window, text='Vertrektijden', command=clicked, background='yellow', foreground='blue',
                       font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)


text = Listbox(main_window)
#toListbox(on_change(e))
text.pack()
Listbox.pack(text, fill=BOTH)
Listbox.config(text,background='#ffc917', foreground='blue', font=('Ariel', 16), height=34,selectborderwidth=5)
#Potato.config(command=text.yview)

# ------------NS logo downloader + weergeven-----------------
# img = PhotoImage(file=download_img(
#     'https://i.imgur.com/FLXfxow.png'))
# photo_label = Label(main_window, image=img, width=300, height=150).pack(fill=BOTH, side=TOP,padx=50,pady=100)

main_window.mainloop()