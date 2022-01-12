from django.db import models

class Song(models.Model):
    file = models.FileField()
