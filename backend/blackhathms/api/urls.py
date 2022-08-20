from django.urls import path
from . import views


urlpatterns = [
    # -------Paths for the API-------
    path("patience/", view=views.getpatience),
    path("patience/<str:pk>/", view=views.get_a_patience),
    path("patience/create/", view=views.create_a_patience),
    path("patience/update/<str:pk>/", view=views.update_patience),
    path("patience/delete/<str:pk>/", view=views.delete_patience),
    # --------------------Doctor------------------------------
    path("doctor/", view=views.get_doctor),
    path("doctor/<str:pk>/", view=views.get_a_doctor),
    path("doctor/create/", view=views.create_doctor),
    path("doctor/update/<str:pk>/", view=views.update_doctor),
    path("doctor/delete/<str:pk>/", view=views.delete_doctor),
    
    # --------------------Appointment------------------------------
    path("appointment/", view=views.getAppointments),
    path("appointment/<str:pk>/", view=views.get_an_Appointment),
    path("appointment/create/", view=views.Create_an_Appointment),
    path("appointment/update/<str:pk>/", view=views.update_an_Appointment),
    path("appointment/delete/<str:pk>/", view=views.delete_an_Appointment),
    
]
