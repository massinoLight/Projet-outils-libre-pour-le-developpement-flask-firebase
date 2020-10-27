import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
###################################################
#                                                  #
# Des fonction pour accéder au cloud firbase       #
# et deux fonctions l'une pour ajouter des données #
# l'autre pour récupérer toute une colléction      #
#                                                  #
####################################################

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
#cette ligne est tres importante pour importer les clés google comme environement de variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./projetOutilsLibres-658591671fcb.json"


def add_user(nom ,email,mdp):
    db = firestore.Client()
    doc_ref = db.collection(u'Utilisateurs').document(nom)
    doc_ref.set({
        u'nom': nom,
        u'email': email,
        u'mot de passe': mdp

    })

def get_collection(laCollection):
        db = firestore.Client()

        users_ref = db.collection(laCollection)
        docs = users_ref.stream()

        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')


