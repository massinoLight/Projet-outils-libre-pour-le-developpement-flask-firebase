# Projet-outils-libre-pour-le-developpement-flask-firebase
#avant de lancer le projet il est nécessaire d'avoir ces modules configurés sur la machine (ou au moins sur l'environnement python)
#Le projet a était développé dans un environnement Ubuntu 20.04 et macOS Catalina (version 10.15) avec comme IDE PyCharm 2020.2.3 (community edition)

a-Disposer de python3.x
b-installer pip3 afin de faciliter l'installation d'autres modules 
 =====> sudo apt update
 =====> sudo apt-get install python3-pip

#################Étape 1########################################
créer un environnement python a la racine du répertoire ou est le projet sur la machine 
 ====> python3 -m venv environnement 
 ====> source environnement/bin/activate
installer Flask avec pip ou pip3 selon la version 
 ====> pip install flask
ne pas oublier d'exporter l'application d'entrée flask ainsi que le mode développement
 ===>export FLASK_APP=main
 ===>export FLASK_ENV=development



le contenu HTML et CSS des projets Flask doivent étre contenu réspéctivement dans 
les dossiers templates et static (le projet doit donc contenir ces dossier là)
 
exécuter la commande "flask run" pour lancer l'application sur le serveur local a l'adresse http://127.0.0.1:5000/
 
 
