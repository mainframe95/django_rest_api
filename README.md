# django_rest_api
 * create virtual environemment => python3 -m venv env
 * activate virtual environemment => env\Scripts\activate 
 * deactivate virtual environemment => deactivate

 - create a project: django-admin startproject project
 - create an app: djangoadmin startapp posts

 - creation du fichier de migration pour la base de donne: python manage.py makemigrations
 - executer la migrations: python manage.py migrate
 - creation du superUser: python manage.py createsuperuser

 * creation des end-point
 - Le rest-framework prévoit donc une conversion entre le format Django et un format compatible JSON. Cette conversion utilise la classe Serializer.

 - ApiView (views.py)
Utiliser la classe ApiView est la technique la plus longue pour créer un API, mais elle permet une très grande personnalisation. Si vous avez des besoins particuliers, le ApiView est votre option de choix.

 - ViewSet (views.py)
Utiliser la classe ViewSet est la technique la plus rapide afin de créer un API basé sur un modèle Django lié à une base de donnée. La classe ViewSet va créer pour vous les 7 actions les plus souvent utilisées lorsque l'on crée un API: list, create, retreive, update, partial_update et destroy. C'est donc beaucoup plus rapide que créer chaque action manuellement comme avec les APIView. Par contre, si vous avez des besoins très particulier il ne sera pas possible de personnaliser votre API autant qu'avec les APIView

- Créer le chemin URL (urls.py )