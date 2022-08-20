from django.urls import path
from . import views


urlpatterns = [
    path("patience/", view=views.getpatience),
    path("patience/<str:pk>/", view=views.get_a_patience),
    path("doctor/", view=views.get_doctor),
    path("doctor/<str:pk>/", view=views.get_a_doctor),
    path("appointment/", view=views.getAppointments),
    path("appointment/<str:pk>/", view=views.get_an_Appointment),
    path("appointment/create/", view=views.Create_an_Appointment),
    path("appointment/update/<str:pk>/", view=views.update_an_Appointment),
    path("appointment/delete/<str:pk>/", view=views.delete_an_Appointment),
    
]
