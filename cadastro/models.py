from django.db import models

# Create your models here.

class Question(models.Model):
    questao = models.CharField(max_length=255)
    resposta = models.CharField(max_length=255)
    materia = models.CharField(max_length=100)
    erro = models.TextField(max_length=4000)


def __str__(self):
    return self.materia + " - " + self.questao


