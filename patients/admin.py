from django.contrib import admin
from .models import * 

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "age",
        "gender",
        "phone",
        "email"
    )
    search_fields = ("name", "phone", "email")

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "specialization"
    )
    search_fields = ("name", "specialization")

@admin.register(Appoinment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "patient",
        "doctor",
        "appoinment_date",
        "reason"
    )
    search_fields = ("patient__name", "doctor__name", "reason")
    


