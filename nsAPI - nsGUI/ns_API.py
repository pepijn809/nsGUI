# deze functie returnt de waardes in de volgende volgorde:
# vertrektijd, eindbestemming, treinSoort, vertrekspoor, viaRoute, opmerking, vertraging
# als er een error voordoet dan wordt alleen de error gereturnt
def ns_API2Format(inputStation):
    '''  deze functie zorgt er voor dat met de inloggegevens van de ns-api je kan inloggen op de website en de gereturnde waarde opslaat in en als het bestand stations.xml
      daarna wordt het bestand stations.xml uitgelezen door de functie processXML() en wordt daarna in een mooier format gezet die nuttiger is voor het bewerken en opmaken van de
      gereturnde waarde'''
    import requests
    import xmltodict

    # hardcoded variabelen die nodig zijn voor een goede werking van de functie:
    loginID = "stsheefe@gmail.com"
    Password = "Ndtz9_SpgzP9AbNmsFP7_1km2_8B4r3LzBSkDqfW7u1m3t8bRQSYpw"
    API_URL = "https://webservices.ns.nl/ns-api-avt?station="
    XML_File = "stations.xml"

    # goed overzicht wat er gereturnt gaat worden bij het gebruiken van de functie:
    vertrektijd = []
    eindbestemming = []
    treinSoort = []
    vertrekspoor = []
    viaRoute = []
    opmerking = []
    vertraging = []

    while True:
        try:
            #api details voor inloggen:
            auth_details = (loginID, Password)
            api_url = "{}{}".format(API_URL, inputStation)

            # response van de web api naar lokale variabele
            webResponse = requests.get(api_url, auth=auth_details)
            #openen van het bestand met of zonder de stations
            with open(XML_File, 'w') as infile:
                #het schrijven van de data op de web pagina naar een textbestand
                infile.write(webResponse.text)

            #functie xml naar dictionary en returnt dus een dictionary
            def processXML(filename):
                '''  het omzetten van de data in het xml bestand naar een dictionary '''
                with open(filename) as myXMLFile:
                    filecontentstring = myXMLFile.read()
                    xmldictionary = xmltodict.parse(filecontentstring)
                    return xmldictionary


            #convert xml to dictionary
            stationsDict = processXML(XML_File)
            stations = stationsDict['ActueleVertrekTijden']['VertrekkendeTrein']
            for station in stations:
                try:
                    if station['RouteTekst'] != None:
                        viaRoute += [station['RouteTekst']]
                    elif station['RouteTekst'] == None:
                        viaRoute += ['-']
                except KeyError:
                    viaRoute += ['-']
                #formaten van de tijd naar simpele uur:minuten
                vertrektijdString = ((((station['VertrekTijd']).split('T'))[1].split('+'))[0])[0:5]

                #toevoegen van data aan de variabelen
                vertrektijd += [vertrektijdString]
                eindbestemming += [station['EindBestemming']]
                treinSoort += [station['TreinSoort']]
                try:
                    vertrekspoor += [station['VertrekSpoor']['#text']]
                except KeyError:
                    vertrekspoor += ['']
                #als er geen opmerkingen staan in het xml bestand dan returnt het programma een lege string
                # en anders gaat het programma de opmerking returnen
                try:
                    opmerking += [station['Opmerkingen']['Opmerking']]
                except KeyError:
                    opmerking += ['']

                try:
                    vertraging += [station['VertrekVertragingTekst']]
                except KeyError:
                    vertraging += ['']
            break
        except KeyError:
            # errorMessage voor verschillende fouten die zich op kunnen doen
            return ['geen resultaten gevonden voor {}'.format(inputStation)]

        except Exception as error:
            print(error)
            return ['Zorg voor stabiele internet connectie!']

    dict = {}
    # er wordt een dict in dict gereturnt
    for x in range(len(eindbestemming)):
        # zet alle bestande in een dictionary (dubbele dictionary (dict in dict)) en returnt daarna de overzichtelijke dictionary,
        # die daarna verder bewerkt en opgemaakt kan worden door de andere functie
        dict[x] = {}
        dict[x]['vertrektijd'] = vertrektijd[x]
        dict[x]['eindbestemming'] = eindbestemming[x]
        dict[x]['treinSoort'] = treinSoort[x]
        dict[x]['vertrekspoor'] = vertrekspoor[x]
        dict[x]['viaRoute'] = viaRoute[x]
        dict[x]['opmerking'] = opmerking[x]
        dict[x]['vertraging'] = vertraging[x]
    return dict