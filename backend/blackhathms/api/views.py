from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patients, Doctors
from .serializars import PatiensSerializer, DoctorsSerializer


# Create your views here.

@api_view(["GET"])
def getpatience(request):
    data = Patients.objects.all()
    serilizeData = PatiensSerializer(data, many=True)

    return Response(serilizeData.data)

@api_view(["GET"])
def get_doctor(request):
    data = Doctors.objects.all()
    serilizeData = DoctorsSerializer(data, many=True)

    return Response(serilizeData.data)
