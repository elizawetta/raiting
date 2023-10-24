from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class New(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fio = models.TextField()
    comp = models.TextField()
    raiting = models.IntegerField()
