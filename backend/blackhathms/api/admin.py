from django.contrib import admin
from .models import Patients, Doctors, Appointment

# Register your models here.

admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Appointment)
