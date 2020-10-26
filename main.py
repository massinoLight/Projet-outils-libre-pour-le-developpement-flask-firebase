from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
#fonction pour l'authentification on utilise la methode post afin de récupérer le contenu du formulaire
#On affiche une erreur dans le cas ou l'utilisateur n'existe pas
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Utilisateur non trouvé,Merci de verifier votre login ou mdp.'
        else:
            #si l'utilisateur existe retourner sa page d'accueil
            return render_template('accueil.html')
    return render_template('index.html', error=error)



@app.route('/templates/signup', methods=["GET","POST"])
#fonction pour acceder a la page d'inscription a partir du lien sur la page html qui indique cette fonction
def signup():
    return render_template('signup.html')


