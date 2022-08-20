from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patients, Doctors, Appointment
from .serializars import PatiensSerializer, DoctorsSerializer, AppointmentSerializer


# Create your views here.
# ------------------------PATIENent -------------------------------------------------
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


@api_view(["POST"])
def create_a_patience(request):
    data = request.data
    # {'name': '', 'age': '', 'phone': '', 'address': '', 'email': '', 'blood_group': '', 'symtoms': '', 'assignDoctorId': ''}
    patiencedata = Patients(
        name=data['name'],
        age=data['age'],
        phone=data['phone'],
        address=data['address'],
        email=data['email'], 
        blood_group=data['blood_group'],
        symtoms=data['symtoms'], 
        assignDoctorId=data['assignDoctorId'])
    serilizeData = PatiensSerializer(patiencedata, many=False)

    return Response(serilizeData.data)

@api_view(["PUT"])
def update_patience(request,pk):
    patienc = Patients.objects.get(id=pk)
    serialzeData = PatiensSerializer(patienc, data=request.data)
    if(serialzeData.is_valid()):
        serialzeData.save()
        return Response(serialzeData.data)
    return Response(serialzeData.data)


@api_view(["DELETE"])
def delete_patience(request,pk):
    patienc = Patients.objects.get(id=pk)
    patienc.delete()
    return Response("Deleted")
# ---------------------------------------------END -----------------------------------------------------


# -----------------------------Doctor -----------------------------------------------------------------
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


@api_view(["POST"])
def create_doctor(request):
    data = request.data
    doctordata = Doctors.objects.create(
        name=data['name'],
        age=data['age'],
        phone=data['phone'],
        address=data['address'],
        email=data['email'],
        specialization=data['specialization'],
        experience=data['experience'],
        fee=data['fee'],
        assignPatientId=data['assignPatientId']
    )
    serilizeData = DoctorsSerializer(doctordata, many=False)

    return Response(serilizeData.data)


@api_view(["PUT"])
def update_doctor(request,pk):
    doctor = Doctors.objects.get(id=pk)
    serialzeDoc = DoctorsSerializer(doctor, data=request.data)
    if(serialzeDoc.is_valid()):
        serialzeDoc.save()
        return Response(serialzeDoc.data)
    
@api_view(["DELETE"])
def delete_doctor(request,pk):
    doctor = Doctors.objects.get(id=pk)
    doctor.delete()
    return Response("Doctor Deleted")
# ---------------------------------------------END -----------------------------------------------------


# ----------------------------AppointMent----------------------------------------------------------------
@api_view(["GET"])
def getAppointments(request):
    data = Appointment.objects.all()
    serializeData = AppointmentSerializer(data, many=True)
    return Response(serializeData.data)


@api_view(["GET"])
def get_an_Appointment(request, pk):
    data = Appointment.objects.get(id=pk)
    serializeData = AppointmentSerializer(data, many=False)
    return Response(serializeData.data)


@api_view(["POST"])
def Create_an_Appointment(request):
    data = request.data
    appointment = Appointment.objects.create(
        patientId=data["patientId"],
        doctorId=data["doctorId"],
        patientName=data["patientName"],
        doctorName=data["doctorName"],
        description=data["descripton"]

    )
    serializeAppoint = AppointmentSerializer(appointment, many=False)
    return Response(serializeAppoint.data)


@api_view(["PUT"])
def update_an_Appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    serializeAppoint = AppointmentSerializer(appointment, data=request.data)
    if (serializeAppoint.is_valid()):
        serializeAppoint.save()
        return Response(serializeAppoint.data)


@api_view(["DELETE"])
def delete_an_Appointment(request, pk):
    data = Appointment.objects.get(id=pk)
    data.delete()
    return Response("Delete Successfully")


# ---------------------------------------------END -----------------------------------------------------
