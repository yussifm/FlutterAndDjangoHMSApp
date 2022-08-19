from django.urls import path
from . import views


urlpatterns = [
    path("patience/", view=views.getpatience),
    path("doctor/", view=views.get_doctor)
]