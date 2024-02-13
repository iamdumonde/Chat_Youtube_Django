# installation du framework django
pip install Django

# installation de mysqlclient
pip install mysqlclient

# pour créer un projet django
django-admin startproject nom_du_projet

# créer une application dans l'application projet, il faut entrer dans le projet d'abord
python manage.py startapp chat

# apès ajout des différentes tables qu'on aimerait avoir dans la base de donnée dans models.py 
python manage.py makemigrations //permet de voir les migrations ajoutées

# pour créer les différentes dans la base de donnée
python manage.py migrate

# creation de l'utilisateur admin
python manage.py createsuperuser

# pour démarrer mon application sur le serveur ou simplement dans le navigateur
python manage.py runserver





