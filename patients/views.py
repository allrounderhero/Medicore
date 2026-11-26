from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import PatientModelForm
from .models import Patient
from .serializers import PatientSerializer
from django.shortcuts import get_object_or_404
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

@api_view(["GET", "POST"])
def patient_list_api(request):
    if request.method == "GET":
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def patient_detail_api(request, pk):
    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        patient.delete()
        return Response(
            {"Message": "Patient deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )