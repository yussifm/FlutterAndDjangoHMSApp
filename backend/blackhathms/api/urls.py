from django.urls import path
from . import views


urlpatterns = [
    path("patience/", view=views.getpatience),
    path("patience/<str:pk>/", view=views.getpatience),
    path("doctor/", view=views.get_doctor),
    path("doctor/<str:pk>/", view=views.get_doctor)
]
