from django.db import models
from authentification.models import Subscriber
# Create your models here.
class Traitement(models.Model):

    patient_id = models.PositiveIntegerField()
    # doctor = models.ForeignKey(Subscriber, on_delete=models.CASCADE )
    creation_date= models.DateTimeField(auto_now=True)
    edit_date= models.DateTimeField(auto_now=True)
    traitement_content= models.TextField(null=True, blank=True)
    traitement_title = models.CharField(max_length=500,default="")

    TRAITEMENT_TYPE_CHOICES= (
        (1, 'ordonnance'),
        (2, 'kinésithérapie'),
        (3, 'analyses'),
    )
    traitement_type = models.IntegerField(choices=TRAITEMENT_TYPE_CHOICES , default=1)

