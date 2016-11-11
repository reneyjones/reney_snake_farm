from django.db import models
from django.utils import timezone


# Create your models here.


class Table(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    # joueurs

    player1_name = models.CharField(max_length=50)
    player1_score = models.IntegerField()

    player2_name = models.CharField(max_length=50)
    player2_score = models.IntegerField()

    player3_name = models.CharField(max_length=50)
    player3_score = models.IntegerField()

    player4_name = models.CharField(max_length=50)
    player4_score = models.IntegerField()


def reset(self):
    self.player1_score = 0
    self.player2_score = 0
    self.player3_score = 0
    self.player4_score = 0
    self.save()


def __str__(self):
        return self.title
