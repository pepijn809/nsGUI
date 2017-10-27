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
main_window.geometry("800x800+500+300")
main_window.title("NS")
main_window.configure(background='yellow')


# -------------------Alle funties-------------------------------#

def create_window():
    top = Toplevel(main_window)
    top.geometry("800x800+500+300")
    top.title('Vertrektijden')
    # Tweede scherm labels#
    second_window = Label(top, text=interfacePrinter('utrecht'), bg='yellow', fg='blue', width=100, height=2,
                          font=('Ariel', 24, 'bold')).pack()

    terug_knop = Button(top, text='Terug', command=top.destroy, width=10, height=1, font=('Ariel', 14, 'bold'),
                        bg='yellow', fg='blue').pack(side=BOTTOM)
    Potato = Scrollbar(top)
    Potato.pack(side=RIGHT, fill=Y)

    text = Text(top, wrap=WORD, yscrollcommand=Potato.set)
    text.pack()

    Potato.config(command=text.yview)



# ----------Alle main scherm labels-----------------------------#
main_label = Label(main_window, text='Welkom bij NS', foreground='blue', font=('Ariel', 24, 'bold')).pack()

station_label = Label(main_window, text='Typ uw station', foreground='blue', font=('Ariel', 16, 'bold')).pack()

entry = Entry(main_window).pack()

koop_label = Button(main_window, text='Kopen los kaartje', background='yellow', foreground='blue',
                    font=('Ariel', 14, 'bold')).pack(padx=5, pady=20, side=LEFT)

naar_buitenland_label = Button(main_window, text='Ik wil naar het buitenland', background='yellow', foreground='blue',
                               font=('Ariel', 14, 'bold')).pack(padx=5, pady=20, side=LEFT)

ov_label = Button(main_window, text='Koop OV-Chipkaart', background='yellow', foreground='blue',
                  font=('Ariel', 14, 'bold')).pack(padx=5, pady=20, side=LEFT)

vertrek_label = Button(main_window, command=create_window, text='Vertrektijden', background='yellow', foreground='blue',
                       font=('Ariel', 14, 'bold')).pack(padx=5, pady=10, side=LEFT)

# ------------NS logo downloader + weergeven-----------------


main_window.mainloop()