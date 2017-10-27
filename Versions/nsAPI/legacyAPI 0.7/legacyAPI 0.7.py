def ns_API2Format(inputStation):
    import requests
    import xmltodict

    loginID = "stsheefe@gmail.com"
    Password = "Ndtz9_SpgzP9AbNmsFP7_1km2_8B4r3LzBSkDqfW7u1m3t8bRQSYpw"
    API_URL = "https://webservices.ns.nl/ns-api-avt?station="
    XML_File = "stations.xml"

    while True:
        try:
            #api details voor inloggen:
            auth_details = (loginID, Password)
            api_url = "{}{}".format(API_URL, inputStation)

            # response van de web api naar lokaal bestand
            webResponse = requests.get(api_url, auth=auth_details)

            #openen van het bestand met de stations
            with open(XML_File, 'w') as infile:
                #het schrijven van de data op de web pagina naar een textbestand
                infile.write(webResponse.text)


            #functie xml naar dictionary
            def processXML(filename):
                with open(filename) as myXMLFile:
                    filecontentstring = myXMLFile.read()
                    xmldictionary = xmltodict.parse(filecontentstring)
                    return xmldictionary


            #convert xml to dictionary
            ViaRoute = ''
            stationsDict = processXML(XML_File)
            stations = stationsDict['ActueleVertrekTijden']['VertrekkendeTrein']
            for station in stations:
                try:
                    if station['RouteTekst'] != None:
                        ViaRoute = station['RouteTekst']
                    elif station['RouteTekst'] == None:
                        ViaRoute = '-'
                except KeyError:
                    ViaRoute = '-'
                #formaten van de tijd naar simpele uur:minuten
                vertrektijdString = ((((station['VertrekTijd']).split('T'))[1].split('+'))[0])[0:5]
                #het printen van de in volgorde: vertrektijd, eindbestemming, treinsoort(intercitty/sprinter), vertrekspoor
                print(vertrektijdString, station['EindBestemming'], station['TreinSoort'], station['VertrekSpoor']['#text'], sep=' - ')
                print(ViaRoute)
                #als er geen opmerkingen staan in het bestand dan doet het programma niks en anders
                try:
                    print(station['Opmerkingen']['Opmerking'])
                except KeyError:
                    print()
            break
        except KeyError:
            print('geen resultaten gevonden voor {}'.format(inputStation))
            inputStation = input('Op welk station wil je zoeken? ')
        except:
            print('Zorg voor stabiele internet connectie!')
            inputStation = input('Op welk station wil je zoeken? ')

inputStation = input('Op welk station wil je zoeken? ')

ns_API2Format(inputStation)
