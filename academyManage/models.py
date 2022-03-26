from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50) # Isso precisa virar chave primária, não?
    password = models.CharField(max_length=32)


class Professional(User):
    salary = models.DecimalField(decimal_places=2, max_digits=7)  # util?
    payment_hist = []


class Professor(Professional):
    SPECIALTIES_CHOICES = [
        ('NAS', 'None'),
        ('SUPINO DE 20', 'Supino de 20'),
        ('CROSSFIT', 'Crossfit')
    ]

    # TODO: mudar para relacionamento N -> N

    specialties = models.CharField(choices=SPECIALTIES_CHOICES,
                                   max_length=32,
                                   default='NAS')
    offered_schedules = models.DateTimeField(verbose_name='Class Schedule')

class Doctor(Professional):
    offered_schedules = models.DateTimeField(verbose_name='Class Schedule')

class Client(User):
    client_since = models.DateTimeField('Client Since')
    membership_status = 'active'  # 'inactive' ou fazer booleano?
    payment_status = 'paid'  # 'not_paid'
    payment_hist = []  # datas?
    next_trains = []  # datas?
    next_consultations = []  # datas?


class consultation(models.Model):
    # client = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('Scheduled consultation')
    results = models.CharField(max_length=200)
