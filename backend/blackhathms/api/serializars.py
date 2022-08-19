from rest_framework.serializers import ModelSerializer
from .models import Patients, Doctors, Appointment


class PatiensSerializer(ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'


class DoctorsSerializer(ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
