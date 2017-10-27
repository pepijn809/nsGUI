def ns_API2Format(loginID, Password, inputStation, XML_File):
    import requests
    import xmltodict


    while True:
        #api details voor inloggen:
        auth_details = (loginID, Password)
        api_url = "http://webservices.ns.nl/ns-api-avt?station={}".format(inputStation)

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
        if 'error' in stationsDict: # Controle inhoud van XML - Indien 'Error' gevonden wordt, zal het programma opnieuw om input vragen
            inputStation = input('Van welk station wil je de vertrektijden zien? ') # Input question for application
        else: # Als er geen 'error' gevonden is in de XMLdict, stationsDict, ga dan door >
            stations = stationsDict['ActueleVertrekTijden']['VertrekkendeTrein']
            print('___________________________________________________________________')
            print('Onderstaand vind u de vertrektijden van station:', inputStation)
            print('')
            for station in stations:
                try:
                    with open(XML_File, 'r') as checkRoute:
                        if station['RouteTekst'] != None:
                                ViaRoute = station['RouteTekst']
                        elif station['RouteTekst'] == None:
                                ViaRoute = '-'
                except KeyError:
                    ViaRoute = ''
                except:
                    print('Sorry, een onbekende fout gevonden.')
                #formaten van de tijd naar simpele uur:minuten
                vertrektijdString = ((((station['VertrekTijd']).split('T'))[1].split('+'))[0])[0:5]
                #het printen van de in volgorde: vertrektijd, eindbestemming, treinsoort(intercitty/sprinter), vertrekspoor
                print(vertrektijdString, station['EindBestemming'], station['TreinSoort'], 'Spoor ' + station['VertrekSpoor']['#text'], sep=' - ')
                print('via ' + ViaRoute)
            break

# Authentication Information
loginID = "stsheefe@gmail.com" # Login ID for API
Password = "Ndtz9_SpgzP9AbNmsFP7_1km2_8B4r3LzBSkDqfW7u1m3t8bRQSYpw" # Login Password for API
inputStation = input('Van welk station wil je de vertrektijden zien? ') # Input question for application
XML_File = 'stations.xml' # XML file output

ns_API2Format(loginID, Password, inputStation, XML_File) # Execute NS_API2format Function
