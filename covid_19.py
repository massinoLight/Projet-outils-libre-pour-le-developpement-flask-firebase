import json

data_dict=dict()

#recupérer les données a partir d'un fichier JSON
with open('JSONData/covidFrance.json') as json_data:
    data_dict = json.load(json_data)


liste = []
item = dict()
itemMort = dict()
itemCas = dict()

#on recupére les données dans une liste
for cle in data_dict:
    liste.append(cle)
#on extrait uniquement les données qui nous intérésse a savoir la date et le nombre de mort et le nombre de cas
def nbMort():
    for i in range(len(liste)):
       item=liste.__getitem__(i)
       date=item["dateRep"]
       mort=item["deaths"]

       itemMort[date]=mort
    return itemMort


def nbCas():
    for i in range(len(liste)):
       item=liste.__getitem__(i)
       date=item["dateRep"]
       cas=item["cases"]
       itemCas[date]=cas

    return itemCas
