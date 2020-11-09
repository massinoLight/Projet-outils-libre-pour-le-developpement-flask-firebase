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



#Fonction qui permet de récupérer les messages de la base de données documents qui concérne un topic
def get_message(topic):
        db = firestore.Client()



        listeSavoir = []
        docs=db.collection(u'Message')
        query = docs.where(
            u'topic', u'==', topic)

        #results = query.stream()
        #snapshot = docs.get()

        now = datetime.now()
        existing_posts = db.collection(u'Message').order_by(u'time').end_at({
    u'time': now}).get()
        for post in existing_posts:
            print(u'{} => {}'.format(post.id, post.to_dict()))




l=get_message('radiologie')
#print(l)



