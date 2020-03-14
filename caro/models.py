from django.db import models
# Create your models here.
class botInfo(models.Model):
    win = models.PositiveIntegerField()
    lose = models.PositiveIntegerField();
    draw = models.PositiveIntegerField();
    elo = models.PositiveSmallIntegerField();
class alertDt(models.Model):
    text = models.TextField()
    status = models.BooleanField()
