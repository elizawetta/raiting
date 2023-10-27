from django.db import models


class New(models.Model):
    id_user = models.IntegerField(primary_key=True)
    fio = models.TextField()
    raiting = models.IntegerField()
    liga = models.TextField()
    photo = models.TextField()

