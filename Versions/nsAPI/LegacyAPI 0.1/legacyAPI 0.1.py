import requests
import xmltodict

loginID = "stsheefe@gmail.com"
Password = "Ndtz9_SpgzP9AbNmsFP7_1km2_8B4r3LzBSkDqfW7u1m3t8bRQSYpw"

while True:
    #api details voor inloggen:
    auth_details = (loginID, Password)
    api_url = "http://webservices.ns.nl/ns-api-avt?station={}".format(input('Welk station? '))

    # response van de web api naar lokaal bestand
    webResponse = requests.get(api_url, auth=auth_details)

    #openen van het bestand met de stations
    with open('stations.xml', 'w') as infile:
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
    stationsDict = processXML('stations.xml')
    stations = stationsDict['ActueleVertrekTijden']['VertrekkendeTrein']
    for station in stations:
        try:
            with open('stations.xml', 'r') as checkRoute:
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


