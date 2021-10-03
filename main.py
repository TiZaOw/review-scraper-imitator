import pymongo
import certifi
import json

#Verbindung und Set-Up mit dem MongoDB cluster
ca = certifi.where()
database_url = "mongodb+srv://admin:admin@review-cluster.y16gr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(database_url, tlsCAFile=ca)
mongo_db = client.db

#TODO Fake Reviews zu test Zwecken randomisiert generieren.
# Testumfang und Datenstrukturin in "vorlage_json" verdeutlicht

#TODO randomisierte Generierung soll anpasspare Bias-Parameter beinhalten, welche beliebig modifiziert werden können
vorlage_json = [ #es empfielt sich eine List of dicts in eine JSON File zu generieren.
    {
    'id': '0', #technisches Attribut. Insgesamt bis 5000 Reviews
    'restaurant_name': 'Pizza-Service', #Dieser eine Name bleibt fix
    'datum': '29.09.2021', #Hier macht ein Bias Sinn. Montag Tiefpunkt. Sonntag Höhepunkt
    'wochentag':'Mittwoch',#Extra Feld ermittelt aus dem Datum
    'Uhrzeit': '18:31', #nur zu üblichen Öffnungzeiten von 11:00-23:00Uhr
    'score_essen': '3', #1-5 Sterne. Durschnitt von ca. 4,5 Sternen anpeilen
    'score_lieferung': '3', #1-5 Sterne. Durschnitt von ca. 3 Sternen anpeilen
},
    {
    'id': '1', #technisches Attribut. Insgesamt bis 5000 Reviews
    'restaurant_name': 'Pizza-Service', #Dieser eine Name bleibt fix
    'datum': '26.09.2021', #Hier macht ein Bias Sinn. Montag Tiefpunkt. Sonntag Höhepunkt
    'wochentag':'Sonntag',#Extra Feld ermittelt aus dem Datum
    'Uhrzeit': '21:24', #nur zu üblichen Öffnungzeiten von 11:00-23:00Uhr
    'score_essen': '4', #1-5 Sterne. Durschnitt von ca. 4,5 Sternen anpeilen
    'score_lieferung': '2', #1-5 Sterne. Durschnitt von ca. 3 Sternen anpeilen
},
#{...},
]

with open('test.json') as file:
    json_file = json.load(file)

print(json_file)

#TODO Fake Reviews in die MongoDB uploaden

#TODO es handelt sich um einen kostenlosen MongoDB cluster mit begrenzten Kapazitäten
# bitte erst mit 100 Fake Reviews testen, bevor die gewünschten 5000 vollständig hochgeladen werden
mongo_db.lauches.insert_one(json_file)
print('file has been uploaded')