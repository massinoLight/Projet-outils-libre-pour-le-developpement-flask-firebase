# app/__init__.py
from flask import Flask, render_template, request, url_for, redirect
from firebaseUtils import  add_patient,add_medecin,connection_medecin,connection_patient,get_collection
from covid_19 import nbCas,nbMort
import datetime
from datetime import datetime
import random
import Message
from Message import get_message_details,send_message,get_all_message_from_reference,get_all_topic,add_message


date = datetime.now()

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=["GET", "POST"])
    # fonction pour qui affiche la page d'acceuil
    def index():
        return render_template('index.html')

    @app.route('/login', methods=["GET", "POST"])
    # fonction pour l'authentification on utilise la methode post afin de récupérer le contenu du formulaire
    # On affiche une erreur dans le cas ou l'utilisateur n'existe pas
    def login():
        error = None
        nbcas=nbCas()
        nbmort=nbMort()
        nb_cas = []
        nb_mort = []
        savoir = []
        jour = []

        for cle, valeur in nbcas.items():
            jour.append(cle)
            nb_cas.append(valeur)
        jourdate = []
        for i in range(0,7):
            date_object = datetime.strptime(jour.__getitem__(i), '%d/%m/%Y').date()
            jourdate.append(date_object)

        for cle, valeur in nbmort.items():
            nb_mort.append(valeur)

        savoir=get_collection("bonASavoir")
        savoir_aleatoir=savoir.__getitem__(random.randint(0, len(savoir)-1))





        if request.method == 'POST':
            qui = request.form['username']
            if connection_medecin(request.form['username'],request.form['username'],request.form['password']) \
                    or connection_patient(request.form['username'],request.form['username'],request.form['password']):
                return render_template('index2.html',username=qui,cas=nb_cas,jour=jourdate,savoir=savoir_aleatoir)

            else:
                error = 'Utilisateur non trouvé,Merci de verifier votre login ou mdp.'
        return render_template('index.html', error=error)




    @app.route('/jeSuis', methods=["GET", "POST"])
    def jeSuis():
        return render_template('jeSuis.html')

    """"fonction qui pour renvoyer le formulaire pour un medecin
    """
    @app.route('/formulaireMedecin', methods=["GET", "POST"])
    # fonction pour acceder a la page d'inscription a partir du lien sur la page html qui indique cette fonction
    def formulaireMedecin():
            return render_template('signupMedecin.html')

    """"fonction qui pour renvoyer le formulaire pour un patient
        """
    @app.route('/formulairePatient', methods=["GET", "POST"])
    def formulairePatient():
            return render_template('signupPatient.html')

    """fonction pour ajouter un nouveau patient 
                 elle est enclencher par le formulaire a la page signupPatient   
                 """
    @app.route('/signupPatient', methods=["GET", "POST"])
    def signupPatient():
        error = None
        print("on est dans le signupPatient")

        if request.method == 'POST':
            print("on rentre dans le POST")
            if request.form['username'] == '' or request.form['password'] == '' or request.form['email'] == '' or request.form['numsecu'] == '':
                error = 'Merci de saisir tout les champs.'
            else:
                print("on est rentré ici")
                add_patient(request.form['numsecu'],request.form['username'],request.form['email'],request.form['password'],request.form['daten'],
                            request.form['gende'],datetime.datetime.now())
                return render_template('login.html')
        return render_template('index.html', error=error)

    """fonction pour ajouter un nouveau medecin 
                     elle est enclencher par le formulaire a la page signupMedecin   
                     """
    @app.route('/signupMedecin', methods=["GET", "POST"])
    def signupMedecin():
        error = None
        print("on est dans le signupMedecin")

        if request.method == 'POST':
            print("on rentre dans le POST")
            if request.form['username'] == '' or request.form['password'] == '' or request.form['email'] == '':
                error = 'Merci de saisir tout les champs.'
            else:
                print("on est rentré ici")
                add_medecin(request.form['rpps'], request.form['specialite'],request.form['username'], request.form['email'],
                            request.form['password'],datetime.datetime.now())
                return render_template('login.html')
        return render_template('index.html', error=error)

    @app.route('/topic', methods=["GET", "POST"])
    def topic():
        t = get_all_topic()
        lesTopic=[]
        for i in range(len(t)):
            lesTopic.append(t.__getitem__(i)['theme'])
        return render_template('topic.html',topic=lesTopic,len=len(lesTopic))


    @app.route('/chat/<string:theme>', methods=["GET", "POST"])
    def chat(theme):
        topic = theme
        detail = []
        contenu = []
        emetteur = []
        time = []
        listedesmessages = get_all_message_from_reference(topic)

        for i in range(len(listedesmessages)):
            detail.append(get_message_details(listedesmessages.__getitem__(i)))

        for j in range(len(detail)):
            d = detail.__getitem__(j)
            time.append(d[1])
            contenu.append(d[2])
            emetteur.append(d[0])
            for j in range(3, len(d)):
                if j % 2 == 0:
                    time.append(d[j])
                elif j % 3 == 0:
                    contenu.append(d[j])
                else:
                    emetteur.append(d[j])
        return render_template('chat.html',emetteur=emetteur,time=time,contenu=contenu,len=len(emetteur),topic=theme)

    @app.route('/ajouterMessage/<string:topic>', methods=["GET", "POST"])
    def ajouterMessage(user,topic):
        add_message('Massino',date,request.form['message'],topic)

    return app