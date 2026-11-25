from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import PatientModelForm
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.
def home(request):
    context = {
        "hospital_name": "Medicore Hospital",
        "total_patients": 120,
    }
    return render(request, 'patients/home.html', context)

def patient_list(request):
    return HttpResponse("Patient List Page")

def register_patient(request):
    if request.method == "POST":
        form = PatientModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_success")
    else:
        form = PatientModelForm()
    return render(
        request,
        "patients/register.html",
        {"form": form}
    ) 

def patient_success(request):
    return render(
        request,
        "patients/success.html"
    )

@api_view(["GET"])
def patient_list_api(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)