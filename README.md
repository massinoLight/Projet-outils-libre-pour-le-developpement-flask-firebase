# Projet outils libre pour le developpement flask firebase

[![N|Solid](https://backendlessappcontent.com/652255C5-1DE3-9A8E-FF60-91C2EB139600/console/hkdjldwqrtjkmskrqbykfwbplqrcxyliqugk/files/view/images/Sans%20titre.png)](https://flask.palletsprojects.com/en/1.1.x/)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://firebase.google.com/docs/?gclid=CjwKCAjw0On8BRAgEiwAincsHMkeS9nN22V59FfSSS8tvCIfq0Cv61j1UZj72JB4NuoDngSou4rxZBoCZ7QQAvD_BwE)

Technologies utilisé dans ce projet.

  - Flask (Python)
  - Firebase (Google)
  - HTML CSS 

# systéme requirement!

  - Le projet a été développé dans un environnement Ubuntu 20.04 et macOS Catalina (version 10.15)
  - Mais il est censé tourner sous un systémes Windows  
  - L'IDE utilisé est pycharms


On doit au préalable :
  - Disposer de python3.x
  - Installer pip3 afin de faciliter l'installation d'autres modules
  - Disposer le clé google 

Étape 

> Créer un environnement python a la racine du répertoire ou est le projet sur la machine
> Installer Flask avec pip ou pip3 selon la version
> Installer les modules firebase avec pip ou pip3 selon la version ou directement via l'IDE pycharms
> Exporter l'application d'entrée flask ainsi que le mode développement
> Disposer d'un compte google avec lequel on va créer un projet et générer une clé account key






### Installation

Dillinger requires [Python](https://www.python.org/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ sudo apt-get update
$ sudo apt-get install python3 
$ sudo apt install python3-pip
```

pour installer flask...

```sh
$ cd /lechemin du projet 
$ python3 -m venv environnement
$ python3 -m venv environnement
$ source environnement/bin/activate
$ pip install Flask
$ pip install firebase-admin
```



### Déploiement (local)


```sh
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
$ flask run
```








Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://127.0.0.1:5000/
```





[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
