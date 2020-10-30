# app/__init__.py
from flask import Flask, render_template, request, url_for, redirect
from firebaseUtils import  add_patient,add_medecin,connection_medecin,connection_patient
import datetime

date = datetime.datetime.now()

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

        print("on est dans le login")
        if request.method == 'POST':
            qui = request.form['username']
            if connection_medecin(request.form['username'],request.form['username'],request.form['password']) \
                    or connection_patient(request.form['username'],request.form['username'],request.form['password']):
                return render_template('accueil.html', username=qui)

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
                return render_template('accueil.html')
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
                return render_template('accueil.html')
        return render_template('index.html', error=error)

    return app