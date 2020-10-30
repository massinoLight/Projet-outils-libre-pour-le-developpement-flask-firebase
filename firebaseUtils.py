import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from datetime import date
import datetime




###################################################
#                                                  #
# Des fonction pour accéder au cloud firbase       #
# et deux fonctions pour ajouter des données       #
# deux autres pour récupérer des données           #
#                                                  #
####################################################

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
#cette ligne est tres importante pour importer les clés google comme environement de variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./projetOutilsLibres-658591671fcb.json"




#Fonction qui permet d'ajouter un patient a la base de données si celui ci n'existe pas encore
def add_patient(NumeroSecuriteSocial,nom ,email,mdp,daten,genre,dateade):
    db = firestore.Client()
    doc_ref = db.collection('Patients').document(nom)
    doc = doc_ref.get()
    if doc.exists:
        return False
    else:
        doc_ref.set({
          'Numero Securite Social' : NumeroSecuriteSocial,
          'nom': nom,
          'email': email,
          'mot de passe': mdp,
          'date de naissance' : daten,
          'genre' : genre,
          'date d adésion' : dateade

         })
        return True

#Fonction qui permet d'ajouter un medecin a la base de données si celui ci n'existe toujours pas
def add_medecin(rpps,specialite,nom, email, mdp, dateade):
        db = firestore.Client()
        doc_ref = db.collection(u'Medecins').document(nom)
        doc = doc_ref.get()
        if doc.exists:
            return False
        else:
            doc_ref.set({
            'RPPS' :rpps,
            'Spécialité' : specialite,
            'nom': nom,
            'email': email,
            'mot de passe': mdp,
            'date d adésion': dateade

                })
            return True


#fonction qui permet de retourner toute une collection en indiquant son nom en paramétre
def get_collection(laCollection):
        db = firestore.Client()
        listeNom = []
        listeMdp = []

        users_ref = db.collection(laCollection)
        docs = users_ref.stream()

        for doc in docs:
            #print(f'{doc.id} => {doc.to_dict()}')
            print(f'{doc.id} => {doc.to_dict.first}')

#une fonction qui permet de retourner true si un medecin est dans la base de donnée document
def connection_medecin(nomDocument,login,motdepasserecu):
    db = firestore.Client()
    doc_ref = db.collection(u'Medecins').document(nomDocument)

    doc = doc_ref.get()
    medecin = doc.to_dict()

    if doc.exists:
        if (medecin['nom'] == login ) & (medecin['mot de passe'] == motdepasserecu ) :
          return True
    else:
        return False

#fonction qui permet de retourner true si un pation existe dans la base de données document
def connection_patient(nomDocument,login,motdepasserecu):
    db = firestore.Client()
    doc_ref = db.collection(u'Patients').document(nomDocument)

    doc = doc_ref.get()
    patient = doc.to_dict()

    if doc.exists:
        if (patient['nom'] == login ) & (patient['mot de passe'] == motdepasserecu ) :
          return True
    else:
        return False


"""if __name__ == '__main__':
    #get_collection('Utilisateurs')
    if add_medecin(1234,'Shaima','shaima@gmail.com','oui',datetime.datetime(1998, 2, 12),'Femme',
                datetime.datetime.now()) :
          print("Medecin bien ajouté")"""


