from flask import Flask, render_template, request
from firebaseUtils import  get_collection,add_user

login = Flask(__name__)

@login.route('/templates/signup', methods=["GET","POST"])
#fonction
def signup():
    error = None
    if request.method == 'POST':
        if request.form['username'] != '' or request.form['password'] != '' or request.form['email'] != '':
            error = 'Merci de saisir tout les champs.'
        else:
            print("on est rentré ici")
            add_user(request.form['username'],request.form['email'],request.form['password'])
            return render_template('accueil.html')
    return render_template('index.html', error=error)





