from rest_framework.serializers import ModelSerializer
from .models import Patients, Doctors

class PatiensSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'
        
class DoctorsSerializer(ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'