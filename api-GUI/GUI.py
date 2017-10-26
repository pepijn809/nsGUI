import random
import urllib.request
from tkinter import *
import tkinter as tk

def interfacePrinter(station):
    from ns_API import ns_API2Format
    ns_API2Format = ns_API2Format(str(station))
    # als de code zonder fouten runt wordt alles mooi onder elkaar geprint
    # als er een error voorkomt in de functie wordt de foutmelding gereturnt en geprint
    try:
        # kiezen uit
        # vertrektijd, eindbestemming, treinSoort, vertrekspoor, viaRoute, opmerking
        text = list()
        text += ['{:45}{:45}{:45}{}'.format('vertrektijd:', 'eindbestemming:', 'treinSoort:', 'vertrekspoor:')]
        for x in ns_API2Format:
            # opmaak voor de gui met een formule die grofweg omrekend hoe veel spaties er nodig zijn om de breedte van de letters om te rekenen.
            # dat is met deze formule dus wat makkeljker geregeld
            def opmaak(valueNaam, breedteAfstand):
                return (int((float(breedteAfstand) - len(ns_API2Format[x][str(valueNaam)])) * 1.8) * ' ')

            # makkelijke notatie voor makkelijk gebruik
            # inclusief de wat moeilijkere informatie in de variabelen wat niets anders is dan alles op de goede plaats krijgen met spaties
            vertrektijd = ns_API2Format[x]['vertrektijd']
            eindbestemming = ns_API2Format[x]['eindbestemming'] + opmaak('eindbestemming', 33)
            treinSoort = ns_API2Format[x]['treinSoort'] + opmaak('treinSoort', 33)
            vertrekspoor = ns_API2Format[x]['vertrekspoor']
            viaRoute = '{}via:  '.format(' ' * 41) + ns_API2Format[x]['viaRoute']
            opmerking = ns_API2Format[x]['opmerking']
            if opmerking != '':
                opmerking = '{}opmerking:  '.format(' ' * 41) + ns_API2Format[x]['opmerking']
            vertraging = ns_API2Format[x]['vertraging']
            if vertraging != '':
                vertraging = ns_API2Format[x]['vertraging'] + opmaak('vertrektijd', 21)
            else:
                vertraging = ns_API2Format[x]['vertraging'] + opmaak('vertrektijd', 27.5)


            #elke regel hier onder is een ook een nieuwe regel in de GUI
            text += ['{} {}{}{}{}'.format(vertrektijd, vertraging, eindbestemming, treinSoort, vertrekspoor)]
            text += ['{}'.format(viaRoute)]
            text += ['{}'.format(opmerking)] + ['']  #lege regel tussen de stations
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

# bij de GUI wordt er nieuwe data in het textvenster geplaatst door middel van deze functie
def on_change(e):
    text.delete(0, END)
    printt = (e.widget.get())
    for lines in interfacePrinter(printt):
        text.insert(END, lines)

# ----------Alle main scherm labels-----------------------------#
img = PhotoImage(file='nsPicture.jpg')
photo_label = Label(main_window, image=img, width=550, height=150).pack()
main_label = Label(main_window, text='Welkom bij NS', foreground='blue',bg='#ffc917', font=('Ariel', 24, 'bold')).pack()

station_label = Label(main_window,bg='#ffc917', text='Typ uw station', foreground='blue', font=('Ariel', 16, 'bold')).pack()


# gebruik maken van de onchange functie die gelinkt wordt aan de return toets op het toetsenbord
e = tk.Entry(main_window)
e.pack()
# Calling on_change when you press the return key
e.bind("<Return>", on_change)



koop_label = Button(main_window, text='Koop los kaartje', background='yellow', foreground='blue',
                    font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)

naar_buitenland_label = Button(main_window, text='Ik wil naar het buitenland', background='yellow', foreground='blue',
                               font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)

ov_label = Button(main_window, text='Koop OV-Chipkaart', background='yellow', foreground='blue',
                  font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)

vertrek_label = Button(main_window, text='Vertrektijden', background='yellow', foreground='blue',
                       font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=BOTTOM)

text = Listbox(main_window)
text.pack()
Listbox.pack(text,fill=BOTH)
Listbox.config(text,background='#ffc917', foreground='blue', font=('Ariel', 16), height=34,selectborderwidth=5)
#Potato.config(command=text.yview)
# ------------NS logo downloader + weergeven-----------------
# img = PhotoImage(file=download_img(
#     'https://i.imgur.com/FLXfxow.png'))
# photo_label = Label(main_window, image=img, width=300, height=150).pack(fill=BOTH, side=TOP,padx=50,pady=100)

main_window.mainloop()




