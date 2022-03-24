from django.db import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    client_since = models.DateTimeField('Client Since')
    userType = models.CharField(max_length=15) # Tipo do ator (Administrador,Cliente,Profissional)

class consultation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Scheduled consultation')
    results = models.CharField(max_length=200)




