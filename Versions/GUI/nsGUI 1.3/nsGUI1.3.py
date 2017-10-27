import random
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
        text = '{:14}{:20}{:12}{}'.format('vertrektijd:', 'eindbestemming:', 'treinSoort:', 'vertrekspoor:\n')
        for x in ns_API2Format:
            # makkelijke notatie voor makkelijk gebruik
            vertrektijd = ns_API2Format[x]['vertrektijd']
            eindbestemming = ns_API2Format[x]['eindbestemming']
            treinSoort = ns_API2Format[x]['treinSoort']
            vertrekspoor = ns_API2Format[x]['vertrekspoor']
            viaRoute = ns_API2Format[x]['viaRoute']
            opmerking = ns_API2Format[x]['opmerking']
            vertraging = ns_API2Format[x]['vertraging']

            # het printen van de data
            # print('{:6}{:8}{:20}{:12}{}'.format(vertrektijd, vertraging, eindbestemming, treinSoort, vertrekspoor))
            # print('{:14}{:20}'.format('',viaRoute))
            # print('{:14}{:20}\n'.format('',opmerking))

            text += ('{:6}{:8}{:20}{:12}{:5}\n'.format(vertrektijd, vertraging, eindbestemming, treinSoort, vertrekspoor) + '{:14}{:20}\n'.format('',viaRoute) + '{:14}{:20}\n\n'.format('',opmerking))
        return text


    except:
        return ns_API2Format

main_window = Tk()
main_window.attributes('-fullscreen',True)
main_window.title("NS")
main_window.configure(background='#ffc917')

width = main_window.winfo_screenwidth()
height = main_window.winfo_screenheight()

# -------------------Alle funties-------------------------------#
def download_img(url):
    name = random.randrange(1, 1000)
    ns = str(name) + '.jpg'
    urllib.request.urlretrieve(url, ns)
    return ns


#def create_window():
#    top = Toplevel(main_window)
#    top.geometry("800x800+500+300")
#    top.title('Vertrektijden')
#    # Tweede scherm labels#
#    second_window = Label(top, text=interfacePrinter('Utrecht'), bg='yellow', fg='blue', width=100, height=20,
#                          font=('Ariel', 24, 'bold')).pack()
#
#    terug_knop = Button(top, text='Terug', command=top.destroy, width=15, height=5, font=('Ariel', 14, 'bold'),
#                        bg='yellow', fg='blue').pack()


# ----------Alle main scherm labels-----------------------------#
img = PhotoImage(file=download_img(
    'https://i.imgur.com/FLXfxow.png'))
photo_label = Label(main_window, image=img, width=550, height=150).place(x=(width-640)/2, y=0)
main_label = Label(main_window, text='Welkom bij NS', foreground='blue',bg='#ffc917', font=('Ariel', 24, 'bold')).place(x=(width-250)/2,y=154)


station_label = Label(main_window,bg='#ffc917', text='Typ uw station', foreground='blue', font=('Ariel', 16, 'bold')).place(x=900,y=300)

entry = Entry(main_window).place()

Vertrektijd_Label = Label(main_window,text='Vertrektijd:', bg='#ffc917',fg='blue', font=('Ariel',12)).place()

koop_label = Button(main_window, text='Kopen los kaartje', background='yellow', foreground='blue',
                    font=('Ariel', 14, 'bold')).place(x=320,y=700)

naar_buitenland_label = Button(main_window, text='Ik wil naar het buitenland', background='yellow', foreground='blue',
                               font=('Ariel', 14, 'bold')).place(x=500,y=700)

ov_label = Button(main_window, text='Koop OV-Chipkaart', background='yellow', foreground='blue',
                  font=('Ariel', 14, 'bold')).place(x=1437, y=700)

vertrek_label = Button(main_window, text='Vertrektijden', background='yellow', foreground='blue',
                       font=('Ariel', 14, 'bold')).place(x=1300,y=700)



Potato = Scrollbar(main_window)
Potato.place(x=1083,y=700)

text = Listbox(main_window)
text.insert(END, str(interfacePrinter('Utrecht')))
text.place()
Listbox.place(text, x=900,y=600)
Listbox.config(text,background='#ffc917', foreground='blue',font=('Ariel',12))
Potato.config(command=text.yview)

main_window.mainloop()