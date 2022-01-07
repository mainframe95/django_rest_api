# Ajouter le modèle Post à l'admin panel
from django.contrib import admin
from posts import models

admin.site.register(models.Post)
