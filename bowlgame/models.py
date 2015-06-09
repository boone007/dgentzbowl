from django.db import models

# Create your models here.
class BowlGame(models.Model):
    bowl = models.CharField(max_length=150)
    fav = models.CharField(max_length=150)
    dog = models.CharField(max_length=150)
    hilo = models.IntegerField()
    spread = models.IntegerField()

    def __unicode__(self):
        return self.bowl

class Player(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.username