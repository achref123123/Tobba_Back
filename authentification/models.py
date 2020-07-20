from django.db import models
from django.contrib.auth.models import AbstractUser


SPEC_CHOICES = (
    ('Médecin générale', 'Médecin générale'),
    (' Chirurgien', 'Chirurgie'),
    (' Dermatologue', 'Dermatologue'),
    (' Pédiatre', 'Pédiatre'),
    (' Cardiologue', 'Cardilogue'),

)

class Subscriber(AbstractUser):
    edit_date = models.DateTimeField(auto_now=True)
    birth_date = models.DateField(auto_now=False)
    phonenumber = models.PositiveIntegerField(default=0)
    adresse_doctor = models.CharField(max_length=200, default="")
    spec_doctor = models.CharField(max_length=200,choices=SPEC_CHOICES)
    ROLE_CHOICES = (
        (1, 'Patient'),
        (2, 'Doctor'),
    )
    role_subscriber = models.IntegerField(choices=ROLE_CHOICES, default=1)



