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
def get_a_patience(request, pk):
    data = Patients.objects.get(id=pk)
    serilizeData = PatiensSerializer(data, many=False)

    return Response(serilizeData.data)

@api_view(["GET"])
def get_doctor(request):
    data = Doctors.objects.all()
    serilizeData = DoctorsSerializer(data, many=True)

    return Response(serilizeData.data)


@api_view(["GET"])
def get_a_doctor(request, pk):
    data = Doctors.objects.get(id=pk)
    serilizeData = DoctorsSerializer(data, many=False)

    return Response(serilizeData.data)