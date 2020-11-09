import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from datetime import datetime








###################################################
#                                                  #
# Des fonction pour accéder au cloud firbase       #
# et des fonctions  pour ajouter des données       #
# notament des messages et de les récupérer        #
#                                                  #
####################################################



cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
#cette ligne est tres importante pour importer les clés google comme environement de variables
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./projetOutilsLibres-658591671fcb.json"


#Fonction pour envoyer un message et le stoquer dans la base de données document
def send_message(nomUtilisateur ,topic,contenu,dateade):
    db = firestore.Client()
    doc_ref = db.collection('Message').document()
    doc = doc_ref.get()
    if doc.exists:
        return False
    else:
        doc_ref.set({
          'contenu' : contenu,
          'emetteur': nomUtilisateur,
          'topic' : topic,
          'time' : dateade

         })
        return True



#Fonction qui permet de récupérer les messages tout les message d'un topic  de la base de données documents qui date de moins d'une journée
def get_message(topic):
        db = firestore.Client()

        listeMessage = []
        now = datetime.now()


        existing_posts = db.collection(u'Message')
        query = existing_posts.where(u'topic', u'==', topic).order_by(u'time').end_at({
        u'time': now})
        results = query.stream()


        for post in results:
            message = post.to_dict()
            listeMessage.append(message['contenu'])
        return listeMessage





