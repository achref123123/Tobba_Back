from authentification import serializers
from .models import Traitement
from rest_framework import serializers
from .models import Subscriber
from authentification.serializers import DoctorRegistrationSerializer

from rest_framework import serializers


class TraitementSerializer(serializers.ModelSerializer):
    # id_patient = serializers.CharField(read_only=True,default="2")
    # id_doctor = serializers.CharField(write_only=True,default="3")
    # patient_obj= serializers.SerializerMethodField('get_patient_object')
    # def get_patient_object(self):
    #     obj=Subscriber.objects.filter(pk=self.re)
    class Meta:
        model = Traitement
        # fields= "__all__"
        fields = ['pk',
                  'patient_id',
                  'traitement_content',
                  'traitement_title',
                  'traitement_type',
                  ]
        read_only_fields = ['patient_id']
