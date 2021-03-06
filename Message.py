import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from datetime import datetime
import firebaseUtils







###################################################
#                                                  #
# Des fonction pour accéder au cloud firbase       #
# et des fonctions  pour ajouter des données       #
# notament des messages et de les récupérer        #
#                                                  #
####################################################




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

#Fonction qui permet de récupérer les messages tout les message d'un topic  de la base de données documents qui date de moins d'une journée
def get_all_topic_message(theme):
    db = firestore.Client()
    refMessages = []
    existing_posts = db.collection(u'Topic')
    query = existing_posts.where(u'theme', u'==', theme)
    results = query.stream()
    for post in results:
        message = post.to_dict()
        refMessages.append(message['message'])
    return refMessages

# Fonction qui permet de récupérer les messages tout les message d'un topic  de la base de données documents qui date de moins d'une journée
def get_all_topic():
    db = firestore.Client()
    docs = db.collection(u'Topic').stream()
    topic=[]

    for doc in docs:
        topic.append(doc.to_dict())
    return topic

#recupérer un message a paritir de sa reférence
def get_message_from_reference(ref):
    db = firestore.Client()
    doc_ref = db.collection(u'Message').document(ref)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()


#fonction qui permet de récupérer tout les message contenu dans un tompic en passant le théme de celui ci en paramétre
def get_all_message_from_reference(theme):

   listeMessage=[]
   l=get_all_topic_message(theme)
   for i in range(len(l)):

       t=l.__getitem__(i)
       for j in range(len(t)):
           listeMessage.append(get_message_from_reference(t[j].id))

   return listeMessage

#recupérer les détails d'un message
def get_message_details(message):
        details=[]
        details.append(message['emetteur'])
        details.append(message['time'])
        details.append(message['contenu'])
        return details



#Fonction qui permet d'ajouter un patient a la base de données si celui ci n'existe pas encore
def add_message(emetteur,time,contenu,topic):
    db = firestore.Client()
    mon_message = dict()
    mon_message={
        'emetteur': emetteur,
        'time': time,
        'contenu': contenu,
        'topic':topic

    }

    doc_ref = db.collection('Message').add(mon_message)


date = datetime.now()
add_message('Massino',date,'je cherche un cardiologue','cardiologie')