from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('register/',views.register_patient,name='register_patient'),
    path('success/',views.patient_success,name='patient_success'),
    path('api/patients/',views.patient_list_api,name='patient_list_api'),
]

