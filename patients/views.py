from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {
        "hospital_name": "Medicore Hospital",
        "total_patients": 120,
    }
    return render(request, 'patients/Home.html', context)
def patient_list(request):
    return HttpResponse("Patient List Page")