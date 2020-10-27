from flask import Flask, render_template, request, url_for, redirect
from firebaseUtils import  get_collection,add_user

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
#fonction pour l'authentification on utilise la methode post afin de récupérer le contenu du formulaire
#On affiche une erreur dans le cas ou l'utilisateur n'existe pas
def login():
    error = None
    print("on est dans le login")
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Utilisateur non trouvé,Merci de verifier votre login ou mdp.'
        else:
            #si l'utilisateur existe retourner sa page d'accueil
            return render_template('accueil.html')
    return render_template('index.html', error=error)



@app.route('/templates', methods=["GET","POST"])
#fonction pour acceder a la page d'inscription a partir du lien sur la page html qui indique cette fonction
def formulaire():
    print("on est dans le formulaire")
    return render_template('signup.html')

@app.route('/templates/signup', methods=["GET","POST"])
#fonction
def signup():
    error = None
    print("on est dans le signup")

    if request.method == 'POST':
        print("on rentre dans le POST")
        if request.form['username'] == '' or request.form['password'] == '' or request.form['email'] == '':
            error = 'Merci de saisir tout les champs.'
        else:
            print("on est rentré ici")
            add_user(request.form['username'],request.form['email'],request.form['password'])
            return render_template('accueil.html')
    return render_template('index.html', error=error)





